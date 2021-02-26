"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator.userLocator import LoginLocator
from common.base_page import BasePage


class LoginPage(BasePage):
    def login(self, mobile, pwd):
        self.input_send_keys(LoginLocator.mobile_loc,mobile,'登录页面_账号输入')
        self.input_send_keys(LoginLocator.pwd_loc,pwd,'登录页面_密码输入')
        self.click_element(LoginLocator.login_btn_loc,'登录页面_登录按钮')

    def get_error_text(self):
        res = self.get_element_text(LoginLocator.page_error_info_loc,'登录页面_登录的错误提示')
        return res
