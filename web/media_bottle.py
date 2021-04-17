#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Exemple d'usage de Bottle avec quelques cas.

Commectez-vous en :8080/ ou :8080/tpl/

"""

from bottle import Bottle, run, template, request

app = Bottle()

our_heroes = ['Luke', 'Yoda', 'Han', 'Leia']


@app.route('/')
def index():
    return '<b>Great, Python Works !</b>!'


@app.route('/tpl/')
def indextpl():
    return template('hello_world', names=our_heroes)


@app.route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@app.post('/add/')
def add_hero():
    our_heroes.append(request.forms.get('new_hero'))
    return "<a href='/tpl/'>Go back<a>"


if __name__ == "__main__":
    run(app, host='localhost', port=8080)
