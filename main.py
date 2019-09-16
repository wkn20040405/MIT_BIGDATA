import os
from apply import predict
from flask import Flask, request
from datetime import datetime
from werkzeug.utils import secure_filename
from os import path

app = Flask(__name__)
UPLOAD_FOLDER = 'receive'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'jpg', 'png'}  #允许文件上传的格式


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/mnist', methods=['GET','POST'])
def mnist():
    """
    when users submit pictures to '0.0.0.0:8000/mnist',
    the program returns users predictions and records them on Cassandra
    """
    req_time = datetime.now()

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            # get the upload time, the filename, the filepath and the prediction
            upload_filename = secure_filename(file.filename)
            save_filename = str(req_time).rsplit('.', 1)[0] + ' ' + upload_filename
            save_filepath = path.join(app.config['UPLOAD_FOLDER'], 'after_recognize.png')
            file.save(save_filepath)
            mnist_result = str(predict(save_filepath))

            insert_filename = '\'' + upload_filename + '\''
            insert_time = '\'' + str(req_time).rsplit('.', 1)[0] + '\''

            # insert data to the Cassandra
            # insertData(insert_filename, insert_time, mnist_result)

            # return the user with the information
            return ("%s%s%s%s%s%s%s%s%s" % ("Upload File Name ", upload_filename, "\n",
                                        "Upload Time: ", req_time, "\n",
                                        "Prediction: ", mnist_result, "\n"))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
