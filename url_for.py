from flask import Flask,url_for
app  = Flask(__name__)
@app.route('/')
# def hello_world():
#     return url_for('my_list',page=100,count=100)

# @app.route('/list/<page>/')
# def my_list(page):
#     return "My list"


@app.route('/')
def devops():
    return url_for('login',next='/')

@app.route('/login/')
def login():
    return login



if __name__ == '__main__':
   app.run(
   host="192.168.1.200"
   )

