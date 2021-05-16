from flask import Flask
app  = Flask(__name__)
import config
app.config.from_object(config)
@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/devops/<int:devops_id>')
def xiaolige_detail(devops_id):
    return "你的运维id是: %s" % devops_id


@app.route('/devops/<path:devopsId>')
def devops_detail(devopsId):
    return "你的运维id是: %s" % devopsId

if __name__ == '__main__':
   app.run(
   host="192.168.1.200"
   )

