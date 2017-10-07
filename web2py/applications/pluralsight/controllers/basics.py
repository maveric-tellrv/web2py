# -*- coding: utf-8 -*-
# try something like

def sum_val(a,b):
    return a+b

def request_args():
    arg1 = float(request.args(0))
    arg2 = float(request.args(1))
    total = sum_val(arg1,arg2)
    #total = arg1+arg2
    return locals()


def request_vars1():
    num1 = 0
    num2 = 0
    total = 0
    if request.post_vars:
        num1 = float(request.post_vars.num1)
        num2 = float(request.post_vars.num2)
#         total = num1 + num2
        total = sum_val(num1,num2)
    else:
        msg = "No value found in this page"
    return locals()

def request_vars():
    num1 = 0
    num2 = 0
    total = 0
    if request.post_vars:
        num1 = float(request.post_vars.num1)
        num2 = float(request.post_vars.num2)
        total = sum_val(num1,num2)
        msg = "hello"
        return locals()

def request_object():
    app = request.application
    cntr = request.controller
    fx = request.function
    now = request.now
    client = request.client
    return locals()

def helloworld():
    msg = "hello  from the controller"
    return locals()

def index():
    return dict(message="hello from basics.py")
