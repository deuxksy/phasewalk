import os

from cryptography.fernet import Fernet

crypto = Fernet(os.getenv('ZZIZILY_PHASEWALK_CRYPTO'))
package_name = 'phasewalk'
project_home = os.getenv('ZZIZILY_PHASEWALK_HOME')