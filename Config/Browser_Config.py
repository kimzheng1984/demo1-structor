# 定义浏览器驱动模式
# -*- coding: utf-8 -*-
from selenium import webdriver

def browser_config():
    
    # driver默认调用谷歌浏览器默认的配置，而不是调用本地谷歌浏览器的配置
    option = webdriver.ChromeOptions()
    # 设置成用户自己的数据目录（谷歌浏览器配置）
    # option.add_argument('--user-data-dir=C:\\Users\\x2w\\AppData\\Local\\Google\\Chrome\\User Data')
    # 公司电脑谷歌配置
    option.add_argument('--user-data-dir=C:\\Users\\JIke\\AppData\\Local\\Google\\Chrome\\User Data')
    browser = webdriver.Chrome(chrome_options= option)
    # browser = webdriver.Chrome()
    return browser

'''
#IE和Chrome浏览器，下载这两个浏览器的驱动程序，将解压得到的exe文件放到python环境变量所设置的目录下（D:\Python36）
#使用IE浏览器
def browser_config(self):
    browser = webdriver.Ie()
    return browser

#使用火狐浏览器
def browser_config(self):
    browser = webdriver.Firefox()
    return browser
'''