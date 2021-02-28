"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
import os
import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.path_option import Error_Image_Path
from common.log_option import log

"""
BasePage:封装一个所有页面的父类，在父类中封装一些页面常用的操作方法。
1、查找元素
2、点击元素
3、输入内容
4、清空输入框
5、获取元素文本
6、获取元素的属性
7、等待元素可见
8、等待元素可点击
9、等待元素存在
10、iframe切换
11、错误截图
12、窗口切换
13、打开新窗口
14、执行js代码
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, desc=None):
        """
        查找元素
        :param loc: 元素定位器
        :param desc: 元素描述
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            log.error('查找元素--【{}】--失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('查找元素--【{}】--成功'.format(desc))
        return ele

    def find_elements(self, loc, desc=None):
        """
        查找元素
        :param loc: 元素定位器
        :param desc: 元素描述
        :return:
        """
        try:
            eles = self.driver.find_elements(*loc)
        except Exception as e:
            log.error('查找元素--【{}】--失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('查找元素--【{}】--成功'.format(desc))
        return eles

    def click_element(self, loc, desc=None):
        """
        点击元素
        :param loc: 元素定位器
        :param desc: 元素描述
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            log.error('点击元素--【{}】--失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('点击元素--【{}】--成功'.format(desc))

    def input_send_keys(self, loc, value, desc=None):
        """
        输入框，输入
        :param loc: 输入框的定位器
        :param value: 输入的内容
        :param desc: 元素描述
        :return:
        """
        try:
            self.driver.find_element(*loc).send_keys(value)
        except Exception as e:
            log.error('往输入框--【{}】--输入值失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('往输入框--【{}】--输入值成功'.format(desc))

    def clear_input(self, loc, desc=None):
        """
        清空输入框
        :param loc: 输入框的定位器
        :param desc: 元素描述
        :return:
        """
        try:
            self.driver.find_element(*loc).clear()
        except Exception as e:
            log.error('清空输入框--【{}】--失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('清空输入框--【{}】--成功'.format(desc))

    def get_element_text(self, loc, desc=None):
        """
        获取元素的文本
        :param loc: 输入框的定位器
        :param desc: 元素描述
        :return:
        """
        try:
            text = self.driver.find_element(*loc).text
        except Exception as e:
            log.error('获取元素--【{}】--文本失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('获取元素--【{}】--文本成功'.format(desc))
        return text

    def get_element_attribute(self, loc, attr, desc=None):
        """
        获取元素的属性值
        :param loc: 元素定位器
        :param attr: 属性名
        :param desc: 元素的描述
        :return:
        """
        try:
            res = self.driver.find_element(*loc).get_attribute(attr)
        except Exception as e:
            log.error('获取元素--【{}】--属性值失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('获取元素--【{}】--属性值成功'.format(desc))
        return res

    def wait_element_visibility(self, loc, desc=None, timeout=15):
        """
        等待元素可见
        :param loc: 元素定位器
        :param desc: 元素的描述
        :param timeout: 超时时间
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout, 0.5).until(
                expected_conditions.visibility_of_element_located(loc)
            )
        except Exception as e:
            log.error('等待--【{}】--元素可见失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('等待--【{}】--元素可见成功'.format(desc))
        return ele

    def wait_element_clickable(self, loc, desc=None, timeout=20):
        """
        等待元素可点击
        :param loc: 元素定位器
        :param desc: 元素的描述
        :param timeout: 超时时间
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout, 0.5).until(
                expected_conditions.element_to_be_clickable(loc)
            )
        except Exception as e:
            log.error('等待--【{}】--元素可点击失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('等待--【{}】--元素可点击成功'.format(desc))
        return ele

    def wait_element_exis(self, loc, desc=None, timeout=10):
        """
        等待元素存在
        :param loc: 元素定位器
        :param desc: 元素的描述
        :param timeout: 超时时间
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout, 0.5).until(
                expected_conditions.presence_of_element_located(loc)
            )
        except Exception as e:
            log.error('等待--【{}】--元素存在失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('等待--【{}】--元素存在成功'.format(desc))
        return ele

    def switch_to_iframe_loc(self, loc, desc=None):
        """
        通过frame标签的定位表达式进行iframe的切换
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            WebDriverWait(self.driver, 0.5).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(loc)
            )
        except Exception as e:
            log.error('等待iframe可见并进行切换--【{}】--失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('等待iframe可见并进行切换--【{}】--成功'.format(desc))

    def switch_to_iframe_name(self, name, desc=None):
        """
        通过frame标签的name属性进行iframe的切换
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        """
        try:
            self.driver.switch_to.frame(name)
        except Exception as e:
            log.error('切换iframe--【{}】--失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('切换iframe--【{}】--成功'.format(desc))

    def open_new_window(self, desc=None):
        """
        打开新窗口
        :param desc: 元素的描述
        :return:
        """
        wins = self.driver.window_handles
        try:
            WebDriverWait(self.driver, 15, 0.5).until(
                expected_conditions.new_window_is_opened(wins)
            )
            win = self.driver.window_handles
            self.driver.switch_to.window(win[-1])
        except Exception as e:
            log.error('新窗口--【{}】--打开失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('新窗口--【{}】--打卡成功'.format(desc))

    def execute_script(self, js, desc=None):
        """
        执行js代码
        :param js: js代码
        :param desc: 元素的描述
        :return:
        """
        try:
            self.driver.execute_script(js)
        except Exception as e:
            log.error('执行js--【{}】--失败'.format(desc))
            log.exception(e)
            self.error_save_screenshot(desc)
            raise e
        else:
            log.info('执行js--【{}】--成功'.format(desc))

    def error_save_screenshot(self, desc):
        """
        错误截图
        :param desc: 图片的描述信息
        :return:
        """
        date = time.strftime("%Y-%m-%d_%H_%M_%S_")
        filename = date + desc + '.png'
        file_path = os.path.join(Error_Image_Path, filename)
        try:
            self.driver.save_screenshot(file_path)
        except Exception as e:
            log.error('对-【{}】--操作进行截图--失败'.format(desc))
            log.exception(e)
            raise e
        else:
            with open(file_path,'rb')as f:
                content=f.read()
            allure.attach(content,'失败截图',allure.attachment_type.PNG)
            log.info('对-【{}】--操作进行截图--成功'.format(desc))
            log.info('图片名为{}'.format(file_path))
