import os

from flask import Flask, request, render_template, send_from_directory
from flask.views import View, MethodView
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(request.json)
        print(request.content_type)  # application/json
        print(request.environ)
        # X - Requested - With: XMLHttpRequest
        # print(request.form)  # ImmutableMultiDict([])
        return '成功'


def allowed_format(filename):
    format_list = ['jpg', 'png']
    format_file = filename.split('.')[1]
    if format_file in format_list:
        return True
    return False


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files.get('pic')
    if file is None:
        return render_template('index.html')
    if allowed_format(file.filename):
        # TODO 处理文件名中间有空格 secure_filename
        file.save(secure_filename(file.filename))
        return 'save success'
    return 'error'


@app.route('/upload/<filename>')
def get_upload(filename):
    return send_from_directory(os.getcwd(), filename)


app.run(debug=True)







