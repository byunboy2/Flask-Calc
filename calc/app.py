from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def add():
    """Return the sum"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return add(integer1,integer2)

@app.get("/sub")
def sub():
    """Return the difference"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return sub(integer1,integer2)

@app.get("/mult")
def mult():
    """Return the difference"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return mult(integer1,integer2)

@app.get("/div")
def div():
    """Return the difference"""
    integer1 = request.args["a"]
    integer2 = request.args["b"]
    return div(integer1,integer2)