# -*- coding: utf-8 -*-
import Test_Case.Shared_Models.ReadExcel
import Config.Excel_Config
import Config.Base_Url
import Config.Browser_Config
import Config.Excel_Config
import Test_Case.Shared_Models.ReadExcel


def test_login(self,name_sheet="login_account", name_index=0, password_sheet="login_account", password_index=1):
    # 用户名所在的sheet名，用户名在sheet中第几列，密码所在的sheet名，密码在sheet中第几列作为登录的参数
    driver = self.driver
    # driver.find_element_by_xpath("//div[@class='login']/div[@class='title']/span[2]").click()
    # 获取excel的配置文件
    excel_file = Config.Excel_Config.excel_config()
    # 获取excel返回的用户名数据
    user_name = Test_Case.Shared_Models.ReadExcel.readcolumn(excel_file, name_sheet, name_index)
    driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
    driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys(user_name)

    # 读取excel中的密码
    password = int(Test_Case.Shared_Models.ReadExcel.readcolumn(excel_file, password_sheet, password_index))
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector("button.login_btn.ng-binding").click()


