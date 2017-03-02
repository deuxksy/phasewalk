import os

from cryptography.fernet import Fernet

crypto = Fernet(os.getenv('ZZIZILY_PHASEWALK_CRYPTO'))
project_name = 'phasewalk'
project_home = os.getenv('ZZIZILY_PHASEWALK_HOME')