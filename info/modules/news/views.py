from flask import render_template, session, current_app, g

from . import news_bp
from info.models import User
from info.utils.commons import user_login_data


# 请求路径: /news/<int:news_id>
# 请求方式: GET
# 请求参数:news_id
# 返回值: detail.html页面, 用户data字典数据
@news_bp.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):

    data = {
        "user_info": g.user.to_dict() if g.user else "",
    }
    return render_template("news/detail.html",data=data)