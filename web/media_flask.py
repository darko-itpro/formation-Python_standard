#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

our_heroes = ['Luke', 'Yoda', 'Han', 'Leia']


@app.route('/')
def index():
    return '<b>Great, Python Works !</b>'


@app.route('/tpl/')
def indextpl():
    return render_template('hello_world.html', names=our_heroes)


@app.route('/hello/<name>')
def hello(name):
    return '<b>Hello {}</b>'.format(name)


@app.route('/add/', methods=['POST'])
def add_hero():
    our_heroes.append(request.form.get('new_hero'))
    return "<a href='/tpl/'>Go back<a>"

@app.route('/training/')
def json_demo():
    response_body = {"title": "Python", "duration": 5, "seats": 12}

    return make_response((jsonify(response_body)), 200)

if __name__ == '__main__':
    app.run()
