import logging
from flask import render_template,current_app, session,jsonify

from . import index_bp
from info.models import User,News,Category
from info.utils.response_code import RET


@index_bp.route('/')
def show_index():

    #1.获取用户的登陆信息
    user_id = session.get("user_id")

    #2.通过user_id取出用户对象
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    # 3.查询热门新闻,根据点击量,查询前十条新闻
    try:
        news = News.query.order_by(News.clicks.desc()).limit(10).all()
        print(news)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取新闻失败")

    # 4.将新闻对象列表转成,字典列表
    news_list = []
    for item in news:
        news_list.append(item.to_dict())

    # 5.查询所有的分类数据
    try:
        categories = Category.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取分类失败")

    # 6.将分类的对象列表转成,字典列表
    category_list = []
    for category in categories:
        category_list.append(category.to_dict())

    #7.拼接用户数据,渲染页面
    data = {
        #如果user有值返回左边的内容, 否则返回右边的值
        "user_info":user.to_dict() if user else "",
        "news_list": news_list,
        "category_list": category_list,
    }
    #渲染页面
    return render_template("news/index.html",data=data)

#处理网站logo
@index_bp.route('/favicon.ico')
def get_web_log():

    return current_app.send_static_file('news/favicon.ico')
