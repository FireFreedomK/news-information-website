import logging
from flask import render_template,current_app

from . import index_bp


@index_bp.route('/')
def show_index():
    return render_template('news/index.html')

#处理网站logo
@index_bp.route('/favicon.ico')
def get_web_log():

    return current_app.send_static_file('news/favicon.ico')
