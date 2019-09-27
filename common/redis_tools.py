import redis


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            cls_ = cls(*args, **kargs)
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
            cls_.r = redis.Redis(connection_pool=pool)

            _instance[cls] = cls_
        return _instance[cls]

    return _singleton


@Singleton
class RedisTools(object):
    r = None

    def __init__(self):
        pass

    def incr_counter(self, key_str):
        """
        通用计数
        :param id:
        :param key_str:
        :return:
        """
        return self.r.incr(key_str)

    def limit_speed(self, email_num):
        """
        通用限速（60秒）
        :param email_num:
        :return:
        """
        key = ""+email_num
        return self.r.set(key, 1, ex=60, nx=True)

