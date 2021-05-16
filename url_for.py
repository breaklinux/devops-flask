from flask import Flask,url_for
app  = Flask(__name__)
@app.route('/')
def hello_world():
    return url_for('my_list',page=1,count=1)

@app.route('/list/<page>/')
def my_list(page):
    return "My list"





if __name__ == '__main__':
   app.run(
   host="192.168.1.200"
   )

