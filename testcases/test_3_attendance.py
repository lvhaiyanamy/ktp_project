"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
import time

import allure
import pytest
from selenium import webdriver

from common.conf_option import conf
from common.log_option import log
from page.loginPage import LoginPage
from page.indexPage import IndexPage
from datas.join_attendance_data import JoinAttendanceData


class TestAttendance:
    @allure.title('考勤成功')
    def test_attendance_success(self, teacher_login_fixture, stu_login_fixture):
        driver = teacher_login_fixture
        index_page = IndexPage(driver)
        index_page.create_attendance()
        attendance_code = index_page.get_attendance_code()
        attend_number = index_page.get_attendance_number()
        print('考勤前人数：', attend_number)

        driver2 = stu_login_fixture
        index_page2 = IndexPage(driver2)
        index_page2.join_attendance(attendance_code)
        time.sleep(3)
        l_attend_number = index_page.get_attendance_number()
        print('考勤后人数：', l_attend_number)
        # index_page.close_attendance()
        try:
            assert int(l_attend_number) - int(attend_number) == 1
        except AssertionError as e:
            log.error('【考勤成功的用例】------执行失败')
            log.exception(e)
            raise e
        else:
            log.info('【考勤成功的用例】------执行通过')

    @allure.title('考勤失败')
    @pytest.mark.parametrize('cases', JoinAttendanceData.error_case_data)
    def test_join_attendance_failure(self, cases, stu_login_fixture):
        driver = stu_login_fixture
        # 学生加入考勤
        index_page = IndexPage(driver)
        index_page.join_attendance(cases['attendance_code'])
        time.sleep(2)
        actual = index_page.get_join_attendance_error()
        assert actual == cases['expected']
