"""
============================
Author:蓝色水汀
Time:
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator.IndexLocator import IndexLocator
from common.base_page import BasePage


class IndexPage(BasePage):

    def is_login_success(self):
        try:
            self.find_element(IndexLocator.user_loc, '首页_获取用户头像')
        except:
            res = "登录失败"
        else:
            res = "登录成功"
        return res

    def create_course(self, course_name):
        """
        老师：创建课程
        :param course_name: 课程名称
        :return:
        """
        self.click_element(IndexLocator.create_course_loc, '首页_老师点击创建课程')
        self.click_element(IndexLocator.create_course_a_loc, '首页_老师点击创建')
        self.input_send_keys(IndexLocator.create_course_name_loc, course_name, '首页_老师输入课程名称')
        self.click_element(IndexLocator.create_course_btn_loc, '首页_老师点击创建课程按钮')

    def save_course_code(self, course_name):
        """
        老师：提取课程加课码和课程id
        :param course_name: 课程名称
        :return:
        """
        course_code_loc = '//a[@title="{}"]//..//..//div[@class="down-menu"]//span'.format(course_name)
        course_id_loc = '//a[text()="{}"]'.format(course_name)
        course_code = self.get_element_attribute((By.XPATH, course_code_loc), 'data-code', '首页_获取课程加课码')
        course_id = self.get_element_attribute((By.XPATH, course_id_loc), 'data-id', '首页_获取课程id')
        return course_code, course_id

    def join_course(self, course_code):
        """
        学生：加入课程
        :param course_code: 加课码
        :return:
        """
        self.click_element(IndexLocator.join_course_loc, '首页_学生加入课程')
        self.input_send_keys(IndexLocator.join_course_code_loc, course_code, '首页_学生输入加课码')
        self.click_element(IndexLocator.join_course_btn_loc, '首页_加入按钮')

    def is_join_course_success(self, course_id):
        """
        学生是否加课成功
        :param course_id: 课程id
        :return:
        """
        course_loc = '//dl[@data-id="{}"]'.format(course_id)
        try:
            self.find_element((By.XPATH, course_loc), '首页_查找课程')
        except:
            expected = '加课失败'
        else:
            expected = '加课成功'
        return expected

    def get_join_course_error(self):
        ele = self.wait_element_visibility(IndexLocator.join_course_error_loc, '首页_加课失败的错误提示')
        return ele.text

    def course_name(self):
        self.click_element(IndexLocator.course_loc, '首页_老师点击课程名称')

    def attend_attence(self):
        self.click_element(IndexLocator.attendance_loc, '课程页面_老师点击考勤')
        self.switch_to_iframe_loc(IndexLocator.attend_iframe_loc, '课程页面_考勤iframe')

    def create_attendance(self):
        """
        老师：创建考勤码并保存
        :return:
        """
        self.course_name()
        self.attend_attence()
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath('//iframe[@src="/Attence/indexpop/courseid/MDAwMDAwMDAwMLWGvZWHz82y"]'))
        time.sleep(2)
        try:
            self.click_element(IndexLocator.create_loc, '考勤页面_点击新建考勤按钮')
        except:
            self.close_attendance()
            self.driver.refresh()
            self.attend_attence()
            time.sleep(3)
            self.click_element(IndexLocator.create_loc, '考勤页面_点击新建考勤按钮')
        self.click_element(IndexLocator.num_loc, '考勤页面_选择数字考勤')
        self.click_element(IndexLocator.begin_loc, '考勤页面_点击开始考勤')

    def get_attendance_code(self):
        self.wait_element_visibility(IndexLocator.attendance_code_loc,'考勤页面_考勤数字')
        eles=self.find_elements(IndexLocator.attendance_code_loc,'考勤页面_考勤数字')
        attendance_code=''
        for ele in eles:
            attendance_code+=ele.text
        print('考勤码为：',attendance_code)
        return attendance_code

    def get_attendance_number(self):
        self.wait_element_visibility(IndexLocator.attendance_num_loc, '课程页面_已考勤人数')
        number = self.get_element_text(IndexLocator.attendance_num_loc, '课程页面_已考勤人数')
        return number

    def close_attendance(self):
        self.click_element(IndexLocator.cancel_attendance_loc, '课程页面_结束考勤')
        # self.switch_to_iframe_loc(IndexLocator.pop_iframe_loc,'考勤页面_确认弹窗')
        self.click_element(IndexLocator.cancel_confirm_loc, '课程页面_弹框结束考勤')
        self.wait_element_visibility(IndexLocator.close_win,'考勤页面_关闭弹窗')
        self.click_element(IndexLocator.close_win, '考勤页面_关闭弹窗')

    def join_attendance(self, attendance_code):
        """
        学生：加入考勤
        :param attendance_code: 考勤码
        :return:
        """
        self.click_element(IndexLocator.course_loc, '首页_学生点击课程名称')
        self.wait_element_visibility(IndexLocator.sign_btn_loc, '课程页面_学生点击立即签到')
        self.click_element(IndexLocator.sign_btn_loc, '课程页面_学生点击立即签到')
        time.sleep(3)
        self.input_send_keys(IndexLocator.sign_input_loc, attendance_code, '签到页面_学生输入考勤码')

    def get_join_attendance_error(self):
        ele = self.wait_element_visibility(IndexLocator.join_attendance_error_loc, '签到页面_学生输入错误考勤码提示信息')
        # ele=WebDriverWait(self.driver,15,0.5).until(
        #     expected_conditions.visibility_of_element_located(IndexLocator.join_attendance_error_loc)
        # )
        return ele.text
