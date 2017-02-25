from setuptools import setup
from setuptools import find_packages
from src.settings import __version__

try:
    license = open('LICENSE').read()
except:
    license = None

try:
    readme = open('README.md').read()
except:
    readme = None

setup(
    name='phasewalk',
    version=".".join(str(x) for x in __version__),
    package_dir={'kiki': 'src'},
    packages=['phasewalk', 'phasewalk.proxy'],
    description='ZZiZiLY phasewalk Project',
    long_description=readme,
    author='crom',
    author_email='crom@zzizily.com',
    url='https://github.com/deuxksy/kiki',
    install_requires=[
    ],
    license=license,
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Korean',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='zzizily phasewalk api'
)
