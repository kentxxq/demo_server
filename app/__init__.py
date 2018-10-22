# coding:utf-8

import os
from flask import Flask, send_file, request, render_template, redirect, url_for
from flask_cors import CORS
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer

# 实例化jsonrpc对象
jsonrpc = JSONRPC()
db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.tss = TimedJSONWebSignatureSerializer(
        app.config['SECRET_KEY'], expires_in=3600)

    # 初始化app
    jsonrpc.init_app(app)
    db.init_app(app)
    CORS(app)

    # 把对应的模块挂载到相应的路径
    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    @app.before_request
    def check_token():
        print(request.cookies)
        # 如果post请求api目录
        if request.path == '/api' and request.method == 'POST':
            # api请求如果不能json化或者token验证有问题就返回index.html
            try:
                # 如果是登陆就放行
                if request.json['method'] == 'App.login':
                    return None
                # cookie中含有token和username
                if request.cookies.get('token') and request.cookies.get('username'):
                    token = request.cookies.get('token')
                    username = request.cookies.get('username')
                    # 验证token
                    if app.tss.loads(token)['username'] == username:
                        return None
                    return 'token error'
                else:
                    return 'token error'
            except Exception:
                return 'token error'
        # 默认放行
        return None

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/test')
    def test():
        return render_template('test.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('index.html'), 404

    return app
