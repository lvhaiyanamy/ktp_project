"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
from selenium.webdriver.common.by import By


class IndexLocator:
    # 用户头像定位表达式
    user_loc=(By.ID,'user')
    # 老师：创建/加入课程按钮
    create_course_loc=(By.XPATH,'//span[text()="+ 创建/加入课程"]')
    # 老师：创建课程
    create_course_a_loc=(By.XPATH,'//a[text()="创建课程"]')
    # 老师：创建课程名字
    create_course_name_loc=(By.XPATH,'//input[@placeholder="请输入课程名称"]')
    # 老师：创建按钮
    create_course_btn_loc=(By.XPATH,'//a[text()="创建"]')
    # 学生：加入课程按钮
    join_course_loc=(By.XPATH,'//div[text()="+ 加入课程"]')
    # 学生：输入加课码
    join_course_code_loc=(By.XPATH,'//input[@placeholder="请输入课程加课验证码"]')
    # 学生：确定加课
    join_course_btn_loc=(By.XPATH,'//a[text()="加入"]')
    # 学生：错误加课码提示
    join_course_error_loc=(By.XPATH,'//div[@id="error-tip"]//span')
    # 老师：课程定位
    course_loc = (By.XPATH, '//a[@title="Renee Brooks"]')
    # 切换iframe
    attend_iframe_loc = (By.XPATH, '//iframe[contains(@id,"layui-layer-content")]')
    # 切换iframe
    pop_iframe_loc=(By.XPATH,'//iframe[@id="layui-layer-content1"]')
    # 老师：考勤定位
    attendance_loc = (By.XPATH, '//i[@class="iconfont iconkaoqin"]/..')
    # 老师：放弃考勤
    cancel_attendance_loc=(By.XPATH,'//div[@id="number-attend"]//a[text()="结束"]')
    # 老师：确认放弃考勤
    cancel_confirm_loc=(By.XPATH,'//*[@id="end-attend"]/div/a[2]')
    # 老师：关闭弹窗
    close_win=(By.XPATH,'//div[@id="layui-layer1"]//div[@class="icon"]')
    # 老师：新建考勤
    create_loc = (By.XPATH, '//a[@class="btn-createattend"]')
    # 老师：选择数字考勤
    num_loc = (By.XPATH, '//div[@class="iconarea digit"]')
    # 老师：开始考勤
    begin_loc = (By.XPATH, '//div[@id="new-perform"]//a[text()="开始考勤"]')
    # 老师：考勤码
    attendance_code_loc=(By.XPATH,'//div[@class="number-box"]')
    # 老师：考勤人数
    attendance_num_loc=(By.XPATH,'//div[@id="number-attend"]//i[@class="ing"]')
    # 学生：立即签到
    sign_btn_loc = (By.XPATH, '//a[text()="立即签到"]')
    # 学生：输入考勤码
    sign_input_loc = (By.XPATH, '//input[@id="phoneVer_modalAuthInput"]')
    # 学生：错误考勤码提示
    join_attendance_error_loc = (By.XPATH, '//div[@id="number-attend"]//p')
