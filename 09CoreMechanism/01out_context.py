from flask import Flask, request, current_app, g, session

app = Flask(__name__)


@app.route('/')
def index():
    # print(request)
    # print(current_app)
    # print(g)
    # print(session)
    return 'hello'
# 四大变量脱离请求环境，是无法访问的，经典错误：outside context

# print(request)  # RuntimeError: Working outside of request context.


# if __name__ == '__main__':
#     app.run(debug=True)
app.app_context().push()
print(current_app)
