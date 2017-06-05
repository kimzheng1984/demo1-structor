import unittest, time, re
import Config.Base_Url
import Config.Excel_Config
from Test_Case.Shared_Models import ReadExcel
import Config.Browser_Config
from selenium.webdriver.common.action_chains import ActionChains


class UpdatePassword(unittest.TestCase):
    """修改密码功能验证"""
    # 修改的密码必须为字母数字组合，不适合调用login方法
    def setUp(self):
        """修改密码功能验证"""
        # 获取excel的配置文件
        self.excel_file = Config.Excel_Config.excel_config()
        # 调用浏览器驱动
        self.driver = Config.Browser_Config.browser_config()
        # Base_Url中配置浏览器登录地址
        base_url = Config.Base_Url.base_url()
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//div[@class='login']/div[@class='title']/span[2]").click()

    def test_update1_password(self):
        """修改密码"""
        #登录
        driver = self.driver
        # 获取excel返回的用户名数据
        user_name = ReadExcel.readcolumn(self.excel_file, "login_account", 0)
        driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
        driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys(user_name)

        # 读取excel中的密码
        password = int(ReadExcel.readcolumn(self.excel_file, "login_account", 1))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_css_selector("button.login_btn.ng-binding").click()
        driver.implicitly_wait(30)
        time.sleep(5)

        #修改密码
        # 更改密码,鼠标悬停在右上角欢迎您按钮上
        above = driver.find_element_by_xpath("//span[@class='name ng-binding']")
        ActionChains(driver).move_to_element(above).perform()
        # 点击帐号管理
        driver.find_element_by_xpath("//div[@class='logout']/ul/li[@ng-click='gotoSetting();']").click()
        # 点击左侧修改密码菜单
        driver.find_element_by_css_selector("li.change_word").click()
        # 调用excel，读取excel中的用户名
        excel_file = self.excel_file
        # 获取excel中的旧密码
        old_password1 = int(ReadExcel.readcolumn(excel_file, "update_password", 0))
        print(old_password1)
        # 获取excel中的新密码
        new_password1 = str(ReadExcel.readcolumn(excel_file, "update_password", 1))
        print(new_password1)

        # 输入现在的密码
        driver.find_element_by_id("oldPassword").clear()
        driver.find_element_by_id("oldPassword").send_keys(old_password1)
        # 输入新密码
        driver.find_element_by_id("newPasswordOne").clear()
        driver.find_element_by_id("newPasswordOne").send_keys(new_password1)
        # 输入确认密码
        driver.find_element_by_id("newPasswordTwo").clear()
        driver.find_element_by_id("newPasswordTwo").send_keys(new_password1)
        # 点击确定按钮
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("button.complete").click()
        print("修改密码完成")
        time.sleep(3)
        driver.close()

    def test_update2_password_check(self):
        """用原密码重新登录，验证是否修改成功"""
        driver = self.driver
        # 获取excel返回的用户名数据
        user_name2 = ReadExcel.readcolumn(self.excel_file, "login_account", 0)
        driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
        driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys(user_name2)

        # 读取excel中的密码
        password2 = int(ReadExcel.readcolumn(self.excel_file, "login_account", 1))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password2)
        driver.find_element_by_css_selector("button.login_btn.ng-binding").click()
        driver.implicitly_wait(30)
        time.sleep(5)
        msg2 = str(driver.find_element_by_xpath("//div[@class='wrong_tip']/span[@class='ng-binding']").text)[0:12]
        driver.implicitly_wait(30)
        print("原用户名密码登录页面提示：", msg2)
        self.assertEqual(msg2, '您输入的密码与账号不匹配')
        driver.close()

    def test_update3_password_back(self):
        """密码改回原密码123456"""
        driver = self.driver
        # 获取excel返回的用户名数据
        user_name3 = ReadExcel.readcolumn(self.excel_file, "update_password", 2)
        driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
        driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys(user_name3)

        # 读取excel中的密码
        password3 = str(ReadExcel.readcolumn(self.excel_file, "update_password", 1))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password3)
        driver.find_element_by_css_selector("button.login_btn.ng-binding").click()
        driver.implicitly_wait(30)
        time.sleep(10)
        #修改密码
        # 更改密码,鼠标悬停在右上角欢迎您按钮上
        above = driver.find_element_by_xpath("//span[@class='name ng-binding']")
        ActionChains(driver).move_to_element(above).perform()
        # 点击帐号管理
        driver.find_element_by_xpath("//div[@class='logout']/ul/li[@ng-click='gotoSetting();']").click()
        # 点击左侧修改密码菜单
        driver.find_element_by_css_selector("li.change_word").click()

        # 调用excel，读取excel中的用户名
        excel_file = Config.Excel_Config.excel_config()
        # 获取excel中的旧密码
        old_password = str(ReadExcel.readcolumn(excel_file, "update_password", 1))
        print(old_password)
        # 获取excel中的新密码
        new_password = int(ReadExcel.readcolumn(excel_file, "update_password", 0))
        print(new_password)

        # 输入现在的密码
        driver.find_element_by_id("oldPassword").clear()
        driver.find_element_by_id("oldPassword").send_keys(old_password)
        # 输入新密码
        driver.find_element_by_id("newPasswordOne").clear()
        driver.find_element_by_id("newPasswordOne").send_keys(new_password)
        # 输入确认密码
        driver.find_element_by_id("newPasswordTwo").clear()
        driver.find_element_by_id("newPasswordTwo").send_keys(new_password)
        # 点击确定按钮
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("button.complete").click()
        print("修改回原密码完成")
        time.sleep(3)
        driver.close()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

