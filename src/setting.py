from configparser import ConfigParser
import os
import redis

config = ConfigParser()
config.read(os.getenv('ZZIZILY_PHASEWALK_CONFIG'))
redis_pool_common = redis.ConnectionPool(
    host=config.get('db','redis.host'),
    port=int(config.get('db','redis.port')),
    password=config.get('db','redis.password'),
    db=int(config.get('db','redis.db.common')),
)