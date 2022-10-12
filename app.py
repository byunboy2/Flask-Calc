from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def adds():
    """Return the sum"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return str(add(int(integer1),int(integer2)))

@app.get("/sub")
def subs():
    """Return the difference"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return str(sub(int(integer1),int(integer2)))

@app.get("/mult")
def mults():
    """Return the difference"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return str(mult(int(integer1),int(integer2)))

@app.get("/div")
def divs():
    """Return the difference"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return str(div(int(integer1),int(integer2)))