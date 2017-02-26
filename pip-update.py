"""
python package update 및 requirements.txt 만들기
"""
import traceback
from subprocess import call

import pip

for dist in pip.get_installed_distributions():
    try:
        call('pip install --upgrade {app}'.format(app=dist.project_name))
    except Exception:
        print(traceback.format_exc())

call('pip-update.cmd')
