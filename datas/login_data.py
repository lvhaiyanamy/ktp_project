"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""


class LoginData:
    success_case_data = [
        {'mobile': "1303845892@qq.com", "pwd": "nmb_python", "expected": "登录成功"},
    ]
    # 异常的用例数据：错误提示在页面上
    error_case_data = [
        {'mobile': "", "pwd": "nmb_python", "expected": "账号不能为空"},
        {'mobile': "1303845892@qq", "pwd": "nmb_python", "expected": "用户不存在"},
        {'mobile': "1303845892@qq.com", "pwd": "", "expected": "密码不能为空"},
        {'mobile': "1303845892@qq.com", "pwd": "nmb_pytho", "expected": "密码错误"}
    ]

