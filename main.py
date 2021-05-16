from flask import Flask
app  = Flask(__name__)
import config
app.config.from_object(config)
@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/devops_one/<int:devops_id>')
def xiaolige_one_detail(devops_id):
    return "你的运维id是: %s" % devops_id


@app.route('/devops_two/<path:devopsId>')
def devops_two_detail(devopsId):
    return "你的运维id是: %s" % devopsId


@app.route('/devops_force/<uuid:uuidId>')
def devops_force_detail(uuidId):
    return "你的运维id是: %s" % uuidId


@app.route('/<any(user,group,resource):url_path>/<id>')
def any_detail(url_path,id):
    if url_path == "user":
       return "用户详情：%s" % id
    elif url_path == "group":
       return '用户组的详情: %s' % id
    else:
       return "用户资源详情: %s" % id



if __name__ == '__main__':
   app.run(
   host="192.168.1.200"
   )

