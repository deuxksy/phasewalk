from configparser import ConfigParser
from cryptography.fernet import Fernet
import os
import redis

__version__ = (0, 0, 1)

crypto = Fernet(os.getenv('ZZIZILY_PHASEWALK_CRYPTO'))

config = ConfigParser()
config.read(os.getenv('ZZIZILY_PHASEWALK_CONFIG'))

redis_pool_common = redis.ConnectionPool(
    host=crypto.decrypt(config.get('db', 'redis.host').encode()).decode(),
    port=int(crypto.decrypt(config.get('db', 'redis.port').encode()).decode()),
    password=crypto.decrypt(config.get('db', 'redis.password').encode()).decode(),
    db=int(config.get('db', 'redis.db.common')),
)
