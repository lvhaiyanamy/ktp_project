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
import random

from common.log_option import log
from page.indexPage import IndexPage
from datas.join_course_data import JoinCourseData


class TestJoinCourse:
    @staticmethod
    def random_course_name():
        course_name = '测试课程' + str(random.randint(0, 10000))
        return course_name

    @allure.title('加课成功')
    def test_join_course_success(self, teacher_login_fixture, stu_login_fixture):
        driver = teacher_login_fixture
        # 老师添加课程
        index_page = IndexPage(driver)
        course_name = self.random_course_name()
        index_page.create_course(course_name)
        # 课程的加课码和id
        course_code, course_id = index_page.save_course_code(course_name)

        driver2 = stu_login_fixture
        # 学生加入课程
        index_page2 = IndexPage(driver2)
        index_page2.join_course(course_code)
        # 断言是否加课成功
        actual = index_page2.is_join_course_success(course_id)
        assert actual == '加课成功'

    @allure.title('加课失败')
    @pytest.mark.parametrize('cases', JoinCourseData.error_case_data)
    def test_join_course_failure(self, cases, stu_login_fixture):
        driver = stu_login_fixture
        # 学生加入课程
        index_page = IndexPage(driver)
        index_page.join_course(cases['course_code'])
        actual = index_page.get_join_course_error()
        try:
            assert actual == cases['expected']
        except AssertionError as e:
            index_page.error_save_screenshot("加课用例断言失败")
            log.error("————>执行失败")
            log.exception(e)
            raise e
        else:
            log.info("————>执行通过")
