from setuptools import setup, find_packages

setup(
    name='dragon_app',
    version='1.0.0',
    description='RESTful API based on Flask-RESTPlus',
    url='https://github.com/',
    author='Dan Xie',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: ',
        'Topic :: Data Sharing Platform',
        'License :: Noe',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Aystronomy, simulation',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1', 'pymysql==2.1.0'],
)
