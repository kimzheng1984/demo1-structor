import unittest, time, re
from Test_Case.Shared_Models import Login
from Test_Case.Shared_Models import Is_Element_Exist
from Config import Pictures_Config


class TestHome(unittest.TestCase):
    """教师展示正确"""
    def setUp(self):
        # 调用登录
        self.driver = Login.test_login()

    def test_home(self):
        """进入首页，页面展示正确"""
        #获得driver
        driver = self.driver

        # 判断学情追踪是否存在
        if driver.find_element_by_css_selector(".enli_1"):
            print("Is_Element_Exist.is_element_exist:",Is_Element_Exist.is_element_exist(self,".enli_1"))

        #调用判断元素是否存在方法
        if Is_Element_Exist.is_element_exist(self,".enli_1"):
            msg1 = "学情追踪存在"
            print(msg1)

        # 判断题库出卷是否存在
        if Is_Element_Exist.is_element_exist(self,".enli_3"):
            msg2 = "题库出卷存在"
            print(msg2)

        # 判断我的学生是否存在
        if Is_Element_Exist.is_element_exist(self,".enli_4"):
            print("我的学生存在")

        # 判断报表中心是否存在
        if Is_Element_Exist.is_element_exist(self,".enli_5"):
            print("报表中心存在")

        # 判断使用情况是否存在
        if Is_Element_Exist.is_element_exist(self,".enli_6"):
            print("使用情况存在")

        # 判断在线批改是否存在
        if Is_Element_Exist.is_element_exist(self,".enli_7"):
            print("在线批改存在")

        # 判断学情追踪是否存在
        if driver.find_element_by_css_selector(".enli_1") and Is_Element_Exist.is_element_exist(self,".enli_3") and \
                Is_Element_Exist.is_element_exist(self,".enli_4") and Is_Element_Exist.is_element_exist(self,".enli_5") \
                and Is_Element_Exist.is_element_exist(self,".enli_6") \
                and Is_Element_Exist.is_element_exist(self,".enli_7"):
            print("首页显示正常:学情追踪存在，题库出卷存在，我的学生存在，报表中心存在，使用情况存在，在线批改存在")

        #调用图片存放文件路径
        file = Pictures_Config.PicturesConfig()
        nowtime = time.strftime("%Y%m%d.%H.%M.%S")
        # 截图
        driver.get_screenshot_as_file(file+"Home_%s.png" % nowtime)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
            unittest.main()
