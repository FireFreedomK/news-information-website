from flask import Flask
from config import config_dict


#定义工厂方法
def create_app(config_name):
    app = Flask(__name__)

    #根据传入的配置类名称,取出对应的配置类
    config = config_dict.get(config_name)

    #加载配置类
    app.config.from_object(config)

    return app