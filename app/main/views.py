#coding:utf-8
from datetime import datetime
from flask import Flask, jsonify,render_template,session, redirect, url_for,flash

from . import main #在app/main/__init__.py中
from .forms import NameForm
from .. import db #在app/__init__.py中
from ..models import User

#@blueprint.route,这里蓝图的字就是main
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        # 注意url_for的命名空间
        return redirect(url_for('.index'))
    return render_template('index.html',
                            form=form, name=session.get('name'),
                            known=session.get('known', False),
                            current_time=datetime.utcnow())


@main.route('/user/<name>')
def user(name):
        #return '<h1>hello,%s!</h1>' %name
        return render_template('user.html', name=name)
