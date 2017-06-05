import unittest, time, re
import Test_Case.Shared_Models.Login_Part
import Test_Case.Shared_Models.ReadExcel
import Config.Excel_Config
import Config.Base_Url
import Config.Browser_Config
from Config import Pictures_Config
from selenium.webdriver import ActionChains


class TestLogin(unittest.TestCase):
    """登录功能验证"""
    def setUp(self):
        """登录功能验证"""
        # 获取excel的配置文件
        self.excel_file = Config.Excel_Config.excel_config()
        # 调用日志，显示所有请求
        # logging.basicConfig(level=logging.DEBUG)

        # 调用浏览器驱动
        self.driver = Config.Browser_Config.browser_config()
        # Base_Url中配置浏览器登录地址
        base_url = Config.Base_Url.base_url()
        self.driver.get(base_url + "/login/main.html#/login")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//div[@class='login']/div[@class='title']/span[2]").click()

    def test_case1(self):
        """用户名密码为空"""
        driver = self.driver
        driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
        driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys("")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("")
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("button.login_btn.ng-binding").click()
        msg1 = str(driver.find_element_by_xpath("//div[@class='wrong_tip']").text)
        driver.implicitly_wait(30)

        #调用图片存放文件路径
        file = Pictures_Config.PicturesConfig()
        nowtime = time.strftime("%Y%m%d.%H.%M.%S")
        # 截图
        driver.get_screenshot_as_file(file+"LoginCase1_%s.png" % nowtime)

        if msg1 == "请输入账号与密码":
            print("页面提示:" + msg1)
            print("case1用户名密码为空,验证成功！")
        else:
            print("case1用户名密码为空，验证失败！")
            print("页面提示:"+msg1)
        self.assertEqual("请输入账号与密码", msg1)

        driver.close()

    def test_case2(self):
        """用户名正确，密码错误"""
        driver = self.driver
        # 获取excel返回的用户名数据
        user_name = Test_Case.Shared_Models.ReadExcel.readcolumn(self.excel_file, "login_account", 0)
        driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
        driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys(user_name)

        # 读取excel中的密码
        password = int(Test_Case.Shared_Models.ReadExcel.readcolumn(self.excel_file, "test_login",1 ))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_css_selector("button.login_btn.ng-binding").click()
        driver.implicitly_wait(30)
        time.sleep(5)
        msg2 = str(driver.find_element_by_xpath("//div[@class='wrong_tip']/span[@class='ng-binding']").text)[0:12]
        driver.implicitly_wait(30)

        #调用图片存放文件路径
        file = Pictures_Config.PicturesConfig()
        nowtime = time.strftime("%Y%m%d.%H.%M.%S")
        driver.get_screenshot_as_file(file+"LoginCase2_%s.png" % nowtime)

        if msg2 =="您输入的密码与账号不匹配":

            print("case2用户名正确密码错误，验证成功")
            print("页面提示:" + msg2)
        else:
            print("case2用户名正确密码错误，验证失败")
            print("页面提示:" + msg2)
        self.assertEqual(msg2, '您输入的密码与账号不匹配')
        driver.close()

    def test_case3(self):
        """用户名错误，密码正确"""
        driver = self.driver
        # 获取excel返回的用户名数据
        user_name = Test_Case.Shared_Models.ReadExcel.readcolumn(self.excel_file, "test_login", 0)
        driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
        driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys(user_name)

        # 读取excel中的密码
        password = int(Test_Case.Shared_Models.ReadExcel.readcolumn(self.excel_file, "login_account",1 ))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("button.login_btn.ng-binding").click()
        driver.implicitly_wait(30)
        time.sleep(5)
        msg3 = str(driver.find_element_by_xpath("//div[@class='account_box']/div[@class='wrong_tip']/span[@class='ng-binding']").text)
        print(msg3)
        driver.implicitly_wait(30)

        # 调用图片存放文件路径
        file = Pictures_Config.PicturesConfig()
        nowtime = time.strftime("%Y%m%d.%H.%M.%S")
        driver.get_screenshot_as_file(file + "LoginCase3_%s.png" % nowtime)

        if msg3 == "账号不存在":
            print("页面提示:"+msg3)
            print("case3用户名错误密码正确，验证成功")
        else:
            print("页面提示:"+msg3)
            print("case3用户名错误密码正确，验证失败")
        self.assertEqual("账号不存在", msg3)
        driver.close()

    def test_case4(self):
        """用户名正确，密码正确"""
        driver = self.driver
        # 获取excel返回的用户名数据
        user_name = Test_Case.Shared_Models.ReadExcel.readcolumn(self.excel_file, "login_account", 0)
        driver.find_element_by_xpath("//input[@ng-model='userName']").clear()
        driver.find_element_by_xpath("//input[@ng-model='userName']").send_keys(user_name)

        # 读取excel中的密码
        password = int(Test_Case.Shared_Models.ReadExcel.readcolumn(self.excel_file, "login_account",1 ))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        print(password)
        driver.implicitly_wait(30)
        time.sleep(5)
        driver.find_element_by_css_selector("button.login_btn.ng-binding").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        # 鼠标悬停在右上角欢迎您按钮上
        above = driver.find_element_by_xpath("//span[@class='name ng-binding']")
        # ActionChains(driver).move_to_element(above).perform()
        # 截取欢迎你字符串
        msg4 = str(above.text)[0:3]

        # 调用图片存放文件路径
        file = Pictures_Config.PicturesConfig()
        nowtime = time.strftime("%Y%m%d.%H.%M.%S")
        driver.get_screenshot_as_file(file + "LoginCase4_%s.png" % nowtime)

        # 判断是否登录成功
        if msg4 == "欢迎您":
            print("页面提示:" + msg4)
            print("case4:正确用户名正确密码，登录成功！")
        else:
            print("页面提示:"+msg4)
            print("case4:正确用户名正确密码，登录失败！")
        self.assertEqual("欢迎您", msg4)
        driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
     unittest.main()





