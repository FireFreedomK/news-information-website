from flask import Blueprint

#1.创建蓝图对象
passport_bp=Blueprint("passport",__name__,url_prefix="/passport")

# 2.导入views装饰图函数
from . import views