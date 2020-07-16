from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        return 'success, url'


if __name__ == '__main__':
    app.run(debug=True)
