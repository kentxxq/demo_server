# coding:utf-8

from app import create_app, db
from config import config
import os
import click
from app.model import User

env = os.getenv('FLASK_ENV', 'development')
app = create_app(config[env])


@app.cli.command()
def init():
    db.drop_all()
    db.create_all()
    user = User(username='admin', password='admin')
    db.session.add(user)
    db.session.commit()
    print('完成一系列的初始化！')


if __name__ == '__main__':
    app.run()
