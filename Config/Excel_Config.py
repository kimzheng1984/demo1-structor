import os


# excel存放路径（相对路径）
def excel_config():
    currentPath = os.path.abspath(os.getcwd())
    excel_dir = os.path.join(currentPath,"Data","config.xlsx")

    return excel_dir


# # EXCEL存放路径（绝对路径）
# def excel_config():
#     excel_config = "D:\\python\\projects\\test\\Data\\config.xlsx"
#     return excel_config

