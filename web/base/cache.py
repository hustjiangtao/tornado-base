# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""
Redis service
"""


import redis


pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)

# r_cache = redis.Redis(connection_pool=pool)  # 旧版本，命令少许不同
r_cache = redis.StrictRedis(connection_pool=pool)  # 官方推荐，命令与官方保持一致
