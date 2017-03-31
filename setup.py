# from distutils.core import setup
from setuptools import setup

setup(
    name='telegram',
    version='0.1.1',
    packages=['telegram'],
    url='',
    license='',
    author='azalio',
    author_email='azalio@azalio.net',
    description='',
    requires=['telepot', 'magic'],
    entry_points={
        'console_scripts': ['send_to_telegram = telegram.telegram:run']
    }
)
