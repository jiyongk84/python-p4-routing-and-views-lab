#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_route():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_route(text):
    print(text)

    return text

@app.route('/count/<int:num>')
def count_route(num):
    # Generate the count as a list of strings from 0 to num
    count_list = [str(i) for i in range(num)]

    # Join the list with newline characters to create the response
    count_response = '\n'.join(count_list) + '\n'  # Add an extra newline character at the end

    return count_response

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_route(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Error: Modulo by zero"
        result = num1 % num2
    else:
        return "Error: Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)