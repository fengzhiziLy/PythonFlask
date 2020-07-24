## 上下文管理

### 上下文例子

- 文件操作首先要打开，操作完要关闭
- 数据库操作首先要链接，操作完要断掉

### 外部环境依赖解决

- 变成内部环境，函数可以把外部变量作为参数传递到函数内部
- 但是每次多了一个函数，而且参数一多，管理起来很麻烦
- 要在视图函数里获取请求参数，最直接的办法是通过传递参数
- 第二种：通过全局变量
- 第三种：上下文

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
```

1. 最小原型里面的app是一个函数，而flask是对象，对象被调用是执行`__call__`方法
2. `app.__call__`里面的函数： `wsgi_app()`
3. `wsgi_app()`源码：会通过环境变量数据实例化一个`RequestContext(environ)`，并执行`ctx.push()`方法将这个请求上下文推入一个栈中
4. `request_ctx.push()`先判断是否有一个`appContext`，没有的话推入一个
5. `_request_ctx_stack.top`就是现在的请求对象
6. `_app_ctx_stack.top`就是现在的app对象
7. `_request_ctx_stack.top`就是`current_app`
8. `app_ctx_stack.top`就是`request`

```python
@app.route('/')
def index():
    a = app_ctx_stack.top
    b = request_ctx_stack.top
    return 'year'
```



