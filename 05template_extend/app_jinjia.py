from flask import Flask, make_response, jsonify, render_template, flash, session, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)


