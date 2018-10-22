# coding:utf-8

from flask import Blueprint
from app import jsonrpc

api = Blueprint('api', __name__)

from . import login
