deep.py：运行deep.py后，可在同目录下/saver/model.ckpt处存储model文件,即通过deep_mnist算法得到的mnist模型

apply.py: 运行apply.py后（需要以save_filepath作为输入,即待识别图片路径），可在同目录下./image/transfer.png将其转化成单通道28*28像素图片，接着predict（save_filepath）函数会通过上述算法识别提交图片所代表的数字，并将结果输出

main.py: 需要在终端输入:

set FLASK_RUN=main.py 

然后再根目录下输入

flask run

运行flask，接着打开网页，输入127.0.0.1:8000/mnist 即可显示提交图片的页面，选中图片点击“提交”后，即可输出预测的结果

image：保存测试图像的文件夹

receive：接受被转化为28*28像素图片的文件夹

MNIST_data: 下载下来的测试数据集，训练deep.py中模型时需要用到

saver：保存model.ckpt文件夹

注意：上述三个文件夹请一定要保证其在与程序运行相同的目录中