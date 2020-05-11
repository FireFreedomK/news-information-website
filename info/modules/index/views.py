import logging
from flask import render_template

from . import index_bp


@index_bp.route('/')
def show_index():
    from info import redis_store
    # 测试redis
    #参数1：key ，参数2：value
    #redis_store.set('name', 'laoli')

    # 使用日志记录方法loggin进行输出可控
    # logging.debug("输入调试信息")
    # logging.info("输入详细信息")
    # logging.warning("输入警告信息")
    # logging.error("输入错误信息")

    return render_template('news/index.html')

