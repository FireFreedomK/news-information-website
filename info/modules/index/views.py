from . import index_bp


@index_bp.route('/')
def index():
    from info import redis_store
    # 测试redis
    #参数1：key ，参数2：value
    redis_store.set('name', 'laoli')
    return 'index'