# coding:utf-8

from app import jsonrpc
from app.model import User
from flask import request, jsonify


@jsonrpc.method('App.index')
def index():
    return 'app.index oooo23'


@jsonrpc.method('App.login')
def login(username, password):
    data = {}
    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_login(password):
        data['loginname'] = user.username
        data['token'] = user.get_token()
        return jsonify(data)
    return jsonify('login error')
