#coding:utf-8
#Blueprint for route

from flask import Blueprint

main= Blueprint('main',__name__)

#路由和错误处理
from . import views,errors
