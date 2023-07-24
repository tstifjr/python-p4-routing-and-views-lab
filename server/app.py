#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    my_print = ''
    param_int = int(parameter)
    for i in range(0,param_int):
        my_print += f'{i}\n'
    return my_print

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    my_calc = {
        '+': num1 + num2, 
        '-' : num1 - num2, 
        '*' : num1 * num2, 
        'div': num1 / num2, 
        '%' : num1 % num2}
    return str(my_calc[operation])

if __name__ == '__main__':
    app.run(port=5555, debug=True)
