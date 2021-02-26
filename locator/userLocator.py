"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
from selenium.webdriver.common.by import By


class LoginLocator:
    mobile_loc = (By.XPATH, '//input[@placeholder="邮箱/账号/手机号"]')
    pwd_loc = (By.XPATH, '//input[@placeholder="密码"]')
    login_btn_loc = (By.XPATH, '(//a[text()="登录"])[2]')
    page_error_info_loc = (By.XPATH, '//p[@class="error-tips"]')
