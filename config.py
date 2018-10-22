# coding:utf-8

import os

base_path = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(BaseConfig):
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + base_path + '/data_dev.db'


class ServerConfig(BaseConfig):
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(16)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


config = {
    'base': BaseConfig,
    'development': DevConfig,
    'production': ServerConfig
}
