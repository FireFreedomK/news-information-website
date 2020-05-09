from flask import Flask
from redis import StrictRedis

from config import config_dict


# 定义redis_store变量
redis_store = None
redis_store=StrictRedis()

#定义工厂方法
def create_app(config_name):
    app = Flask(__name__)

    #根据传入的配置类名称,取出对应的配置类
    config = config_dict.get(config_name)

    #加载配置类
    app.config.from_object(config)

    # 创建redis对象
    global redis_store  # global将局部变量声明为一个全局的
    redis_store = StrictRedis(host=config.REDIS_HOST,
                              port=config.REDIS_PORT,
                              decode_responses=True)

    # 将首页蓝图index_bp,注册到app中
    from info.modules.index import index_bp
    app.register_blueprint(index_bp)

    return app