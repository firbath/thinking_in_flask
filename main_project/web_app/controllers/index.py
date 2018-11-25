# -*- coding:utf-8 -*-
from os import path
from flask import Blueprint, render_template

index_blueprint = Blueprint(
    'index',
    __name__,
    static_folder=path.join(path.pardir, 'static', 'index'),
    template_folder=path.join(path.pardir, 'templates', 'index'),
    url_prefix='/index'
)


@index_blueprint.route('/')
def home():
    return render_template('hello.html')
