"""
============================
Author:蓝色水汀
Time: 
E-mail:826926575@qq.com
Company:陕西伟业医药有限公司
============================
"""
from common.path_option import Report_Path
import pytest

pytest.main(['-s', '-v', '--alluredir={}'.format(Report_Path)])
