import os

# 测试报告相对路径
def report_config():
    # 获取当前运行文件路径
    currentPath = os.path.abspath(os.getcwd())
    # 目录test\\Pictures
    file_dir = os.path.join(currentPath,"Report")
    # 判断文件是否存在，存在则不创建
    if os.path.isdir(file_dir):
        pass
    else:
        os.makedirs(file_dir)
    # 文件最后加上路径分隔符，方便截屏文件拼接
    ReportConfig = file_dir+"\\"

    return ReportConfig


# 测试报告存放路径（绝对路径）
# def report_config():
#     ReportConfig = "D:\\python\\projects\\test\\Report\\"
#     return ReportConfig




