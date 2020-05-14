from flask import render_template, \
    session, current_app, g,abort,jsonify

from . import news_bp
from info.models import User
from info.utils.commons import user_login_data
from info.utils.response_code import RET
from info.models import News


# 请求路径: /news/<int:news_id>
# 请求方式: GET
# 请求参数:news_id
# 返回值: detail.html页面, 用户data字典数据
@news_bp.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    # 1.根据新闻编号,查询新闻对象
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取新闻失败")

    # 2.如果新闻对象不存在直接抛出异常
    if not news:
        abort(404)

    data = {
        "news_info": news.to_dict(),
        "user_info": g.user.to_dict() if g.user else "",
    }
    return render_template("news/detail.html",data=data)