import os


# 截屏文件夹相对路径
def PicturesConfig():
    #获取当前运行文件路径
    currentPathName = os.path.abspath(os.getcwd())
    # 拼接目录test\\Pictures
    file_dir = os.path.join(currentPathName,"Pictures")
    # 判断文件是否存在，存在则不创建
    if os.path.isdir(file_dir):
        pass
    else:
        os.makedirs(file_dir)

    # 文件最后加上路径分隔符，方便截屏文件拼接
    return_dir = file_dir+"\\"

    return return_dir
