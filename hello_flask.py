from flask import Flask, request, render_template, url_for


print(f'__name__ : {__name__}')

app=Flask(__name__)


@app.route('/')
def index():
    return "안녕"

# @app.route('/trans1')
@app.get('/trans')
def trans_get():
    return "<p>안녕1</p>"

@app.post('/trans')
def trans_post():
    return "<p>안녕2</p>"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Christmas')
    return f"<p>안녕 {name}</p>"

# @app.route 데코레이터의 Rule에 변수를 지정할 수 있다. 변수는 <변수명>
@app.route('/hello2/<height>')
def hello2(height):
    height=int(height)+7
    return f"<p>안녕 {height}</p>"





@app.route('/tomorrow/<menu>')
def tomorrow(menu):
    return render_template('index.html', m=menu)
