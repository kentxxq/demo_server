# coding:utf-8

from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        return '不能直接获取密码'

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_token(self, expiration=60*60*24):
        return current_app.tss.dumps({'username': self.username}).decode('ascii')

    def check_login(self, password):
        return check_password_hash(self.password_hash, password)
