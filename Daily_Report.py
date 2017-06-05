# -*-coding:utf-8-*-
import HTMLTestRunner, unittest, os, time, sys, doctest
import os
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Config import *
from Test_Case.Home import *
from Test_Case.ZXXQ import *


# 定义发送邮件
def send_mail(file_new):
    mail_info = Mail_Config.mail_config()
    # 这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])
    f = open(file_new, 'rb')
    try:
        html = f.read()
    finally:
        f.close()

    html_part = MIMEText(html, _subtype='html', _charset='utf-8')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg['Date'] = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    msg['From'] = mail_info["from"]
    msg['To'] = mail_info["to"]
    msg.attach(html_part)

    # 邮件附件
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="AutomationTestResult.html"'
    msg.attach(att)
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    smtp.quit()

# 寻找最新报告
def send_report():
    # 报告存放目录
    result_dir = Report_Config.report_config()
    # 获得报告文件目录夹下的所有文件
    lists = os.listdir(str(result_dir))
    # 重新按时间对目录下的文件进行排序
    # os.path.getmtime返回在报告文件目录下最后一次修改的时间，os.path.isdir(path)判断路径是否为目录
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if os.path.isdir(result_dir + "\\" + fn) else 0)
    # os.path.join(path1[, path2[, ...]])把目录和文件名合成一个路径,把报告目录和最新报告文件名合成一个路径
    file_new = os.path.join(result_dir, lists[-1])
    # file_new2 = os.path.join(result_dir, lists[-2])
    # 调用发送邮件方法，把最新测试报告作为邮件附件发送
    send_mail(file_new)

if __name__ == '__main__':
    # 定义测试用例容器
    suite = unittest.TestSuite()
    test_cases = [Login.TestLogin,
                  Update_Password.UpdatePassword,
                  Home.TestHome,
                  Page_Directed.PageDirected
                  ]
    # 将用例加入用例容器
    for test_case in test_cases:
        suite.addTest(unittest.makeSuite(test_case))

    time.sleep(10)
    # 测试报告以当前时间+Report.html命名文件名
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    # report_file =  Config.Report_Config.report_config() + now + 'Report.html'
    report_file = Report_Config.report_config() + now + 'Report.html'
    # 打开测试报告并生成测试报告
    fp = open(report_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='极客教师WEB自动化测试报告', description='教师WEB自动化测试')
    runner.run(suite)
    #关闭文件否则无法生成报告
    fp.close()
    send_report()
    print("测试用例执行完成！")



