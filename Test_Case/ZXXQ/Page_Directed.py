import unittest, time, re
from Test_Case.Shared_Models import Login
from Config import Pictures_Config
import os


class PageDirected(unittest.TestCase):
    """最新学情"""
    def setUp(self):
        self.driver = Login.test_login()

    def test_page_directed(self):
        """点击学情追踪，页面跳转正确"""
        driver = self.driver
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector(".enli_1").click()
        time.sleep(3)
        #调用图片存放文件路径
        file = Pictures_Config.PicturesConfig()
        nowtime = time.strftime("%Y%m%d.%H.%M.%S")
        driver.get_screenshot_as_file(file+"PageDirected_%s.png" % nowtime)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()