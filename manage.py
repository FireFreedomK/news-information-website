from flask import Flask
from config import Config

app=Flask(__name__)

#设置配置信息(基类配置信息)
class Config(object):
    DEBUG=True

#加载配置类
app.config.from_object(Config)

@app.route('/')
def index():
    return 'hello world'

if __name__=='__main__':
    app.run()