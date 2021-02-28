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
from selenium.webdriver import ChromeOptions
from common.conf_option import conf
from page.loginPage import LoginPage

# --------------------以下是无头浏览器设置方式-----------------------------


def create_driver(is_headers=True):
    """
    启动driver：默认启动浏览器窗口，当is_headers为false时则无头模式运行
    :param is_headers: True 或者 False
    :return:
    """
    if is_headers:
        driver=webdriver.Chrome()
    else:
        # 设置无头浏览器方式，创建对象
        options=ChromeOptions()
        # 无头模式
        options.add_argument('--headless')
        # 设置窗口大小（无头模式下maximize_window()无法将窗口最大化，需要通过下面的启动参数去设置窗口大小）
        options.add_argument('--window-size=1920,1080')
        # 禁用GPU（可选）
        options.add_argument('--disable-gpu')
        # 非沙箱环境（可选）
        options.add_argument('--no-sandbox')
        driver=webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def open_browser():
    driver = create_driver(is_headers=True)
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def teacher_login_fixture():
    driver = create_driver(is_headers=True)
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
    driver = create_driver(is_headers=True)
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

# ----------------以下是正常的启动浏览器的设置方式---------------
# @pytest.fixture(scope='function')
# def open_browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(15)
#     yield driver
#     driver.quit()

# @pytest.fixture(scope='function')
# def teacher_login_fixture():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(15)
#     url = eval(conf.get('url', 'url'))
#     driver.get(url)
#     login=LoginPage(driver)
#     mobile=conf.get('test_data', 'mobile_tea')
#     pwd = conf.get('test_data', 'pwd_tea')
#     login.login(mobile,pwd)
#     yield driver
#     driver.quit()

# @pytest.fixture(scope='function')
# def stu_login_fixture():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(15)
#     url = eval(conf.get('url', 'url'))
#     driver.get(url)
#     login=LoginPage(driver)
#     mobile=conf.get('test_data', 'mobile_stu')
#     pwd = conf.get('test_data', 'pwd_stu')
#     login.login(mobile,pwd)
#     yield driver
#     driver.quit()





