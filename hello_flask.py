from flask import Flask, request


print(f'__name__ : {__name__}')

app=Flask(__name__)

@app.route('/')
def index():
    return "안녕"

@app.route('/trans')
def trans():
    return "안녕"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Christmas')
    return f"<p>안녕 {name}</p>"