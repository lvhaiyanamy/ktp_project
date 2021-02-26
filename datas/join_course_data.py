"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""


class JoinCourseData:
    error_case_data = [
        {'course_code': "0", "expected": "加课验证码必须是6位字符"},
        {'course_code': "123456", "expected": "该加课码不存在或者已经失效"},
        {'course_code': "123456789", "expected": "该加课码不存在或者已经失效"}
    ]
