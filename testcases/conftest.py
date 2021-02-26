"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
import pytest
from selenium import webdriver

from common.conf_option import conf
from page.loginPage import LoginPage


@pytest.fixture(scope='function')
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def teacher_login_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    url = eval(conf.get('url', 'url'))
    driver.get(url)
    login=LoginPage(driver)
    mobile=conf.get('test_data', 'mobile_tea')
    pwd = conf.get('test_data', 'pwd_tea')
    login.login(mobile,pwd)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def stu_login_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    url = eval(conf.get('url', 'url'))
    driver.get(url)
    login=LoginPage(driver)
    mobile=conf.get('test_data', 'mobile_stu')
    pwd = conf.get('test_data', 'pwd_stu')
    login.login(mobile,pwd)
    yield driver
    driver.quit()





