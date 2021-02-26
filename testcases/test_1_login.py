"""
============================
Author:蓝色水汀
Time:
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
import allure
import pytest

from common.log_option import log
from datas.login_data import LoginData
from common.conf_option import conf
from page.indexPage import IndexPage
from page.loginPage import LoginPage


class TestLogin:
    @allure.title('登录成功')
    @pytest.mark.parametrize('cases', LoginData.success_case_data)
    def test_login_pass(self, cases, open_browser):
        expect = cases['expected']
        driver = open_browser
        url=eval(conf.get('url','url'))
        driver.get(url)
        login_page = LoginPage(driver)
        login_page.login(cases['mobile'], cases['pwd'])
        index_page = IndexPage(driver)
        res = index_page.is_login_success()
        try:
            assert res == expect
        except AssertionError as e:
            log.error('【登录成功的用例】————>执行失败')
            log.exception(e)
            raise e
        else:
            log.info('【登录成功的用例】————>执行通过')

    @allure.title('登录失败')
    @pytest.mark.parametrize('cases', LoginData.error_case_data)
    def test_login_error(self, cases, open_browser):
        driver = open_browser
        url = eval(conf.get('url', 'url'))
        driver.get(url)
        l_page = LoginPage(driver)
        l_page.login(cases['mobile'], cases['pwd'])
        actual = l_page.get_error_text()
        assert cases['expected'] in actual

