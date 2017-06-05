#判断元素是否存在共用方法（通过css_selector，也可以通过其他方法）
def is_element_exist(self,css):
    driver = self.driver
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print("元素未找到:%s")%css
        return False
    elif len(s) == 1:
        return True
    else:
        print("找到%s个元素：%s"%(len(s),css))
        return False