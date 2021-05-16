# op-devops-flask
1.主要记录Python flas框架学习笔记

***1.falsk 配置文件方式***
```
配置文件：
Flask项目的配置，都是通过app.config对象来进行配置的。比如要配置一个项目处于DEBUG模式下，那么可以使用app.config['DEBUG] = True来进行设置，那么Flask项目将以DEBUG模式运行。在Flask项目中，有四种方式进行项目的配置：

直接硬编码：

app = Flask(__name__)
app.config['DEBUG'] = True
因为app.config是flask.config.Config的实例，而Config类是继承自dict，因此可以通过update方法：

app.config.update(
   DEBUG=True,
   SECRET_KEY='...'
)
如果你的配置项特别多，你可以把所有的配置项都放在一个模块中，然后通过加载模块的方式进行配置，假设有一个settings.py模块，专门用来存储配置项的，此时你可以通过app.config.from_object()方法进行加载，并且该方法既可以接收模块的的字符串名称，也可以模块对象：

# 1. 通过模块字符串
app.config.from_object('settings')
# 2. 通过模块对象
import settings
app.config.from_object(settings)
也可以通过另外一个方法加载，该方法就是app.config.from_pyfile()，该方法传入一个文件名，通常是以.py结尾的文件，但也不限于只使用.py后缀的文件：

app.config.from_pyfile('settings.py',silent=True)
# silent=True表示如果配置文件不存在的时候不抛出异常，默认是为False，会抛出异常。

#配置文件1示例代码:
from flask import Flask
app  = Flask(__name__)
import config
app.config.from_object(config)
@app.route('/')
def hello_world():
    return "Hello world"

if __name__ == '__main__':
   app.run(
   host="192.168.1.200"
   )


#配置文件2示例代码:
from flask import Flask
app  = Flask(__name__)
app.config.from_pyfile("config.ini",silent=True) #silent=True表示如果配置文件不存在的时候不抛出异常，默认是为False，会抛出异常
@app.route('/')
def hello_world():
    return "Hello world"

if __name__ == '__main__':
   app.run(
   host="192.168.1.200"
   )
```


***2.URl和函数映射***
```
#URL与函数的映射：
一个URL要与执行函数进行映射，使用的是@app.route装饰器。@app.route装饰器中，可以指定URL的规则来进行更加详细的映射，比如现在要映射一个文章详情的URL，文章详情的URL是/article/id/，id有可能为1、2、3...,那么可以通过以下方式：

   @app.route('/article/<id>/')
   def article(id):
       return '%s article detail' % id

#示例函数代码
from flask import Flask
app  = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/devops/<devops_id>') 
def xiaolige_detail(devops_id):
    return "你的运维id是: %s" % devops_id

支持多个数据类型: 
string: 默认的数据类型，接受没有任何斜杠/的字符串。
int: 整形
float: 浮点型。
path： 和string类似，但是可以传递斜杠/。
uuid： uuid类型的字符串。
any：可以指定多种路径，这个通过一个例子来进行说明:

参考Int用法: @app.route('/devops/<int:devops_id>') 
def xiaolige_detail(devops_id):
    return "你的运维id是: %s" % devops_id

参考path用法:@app.route('/devops/<path:devopsId>')
def devops_detail(devopsId):
    return "你的运维id是: %s" % devopsId



if __name__ == '__main__':
   app.run(
   host="192.168.1.200"
   )
```