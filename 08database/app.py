from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:111111@localhost:3306/demo'
# 配置多个数据库绑定
# app.config['SQLALCHEMY_BINDS'] = {
#     'users': 'sqlite:///:memory:',
#     'main': 'mysql+pymysql://root:111111@localhost:3306/demo'
# }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # 数据库对象
# db = SQLAlchemy()
# 延迟绑定
# db.init(app)
migrate = Migrate(app, db)


# 数据模型定义
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # status = db.Column(db.SmallInteger, primary_key=True, nullable=True)
#     username = db.Column(db.String(80), unique=True)  # 必须指明长度
#     email = db.Column(db.String(120), unique=True)

# xuanke = db.Table(
#     'xuanke',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
#     )
class Xuanke(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), primary_key=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # subjects = db.relationship(
    #     'Subject', secondary=xuanke,
    #     backref=db.backref('users'), lazy='dynamic'
    # )
    subjects = db.relationship('Xuanke', backref='student')


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subjects = db.relationship('Xuanke', backref='subject')


class Project(db.Model):
    # __tablename__ = 'project_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # modules = db.relationship('Module', backref='module_project')  # 和数据库的表是没有关系的
    modules = db.relationship('Module', back_populates='module_project')  # 另一种
    # 当查询到一个project的时候，---> project.modules
    # module = Module.query.get(1) module.module_project
    # 多对一关系 backref back_populates
    # 一对一关系 relationship(userlist=False)


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    module_project = db.relationship('Project', back_populates='modules')


@app.route('/insert')
def insert():
    # 添加数据
    # new_user = User(username='apple', email='demo')
    # db.session.add(new_user)  # 保存到会话
    # db.session.commit()  # 事务
    # try:
    #     db.session.commit()
    # except ValueError:
    #     db.session.rollback()
    user1 = User(name='apple')
    user2 = User(name='python')
    user3 = User(name='orange')
    subject1 = Subject(name='自动化')
    subject2 = Subject(name='测试开发')
    subject3 = Subject(name='前端')
    user1.subjects.append(subject1)
    user2.subjects.append(subject2)

    db.session.add_all([user1, user2, user3, subject1, subject2, subject3])
    db.session.commit()
    return 'success'


@app.route('/select')
def select():
    user = User.query.get(1)
    a = user.subjects
    for xuanke in a:
        print(xuanke.subject)
    print(a)
    return 'select true'


@app.route('/')
def index():
    # 查询数据
    # users = User.query.all()  # 查询所有的
    # users = User.query.filter_by(username='apple').all()
    # users = User.query.filter(User.username=='apple').order_by(User.id.desc()).all()
    # User.query.get()  # 获取主键
    # User.query.filter_by()
    users = db.session.execute("SELECT * FROM user")  # <sqlalchemy.engine.result.ResultProxy object at 0x7fc0d6344b50>
    users = users.fetchall()  # [(1, 'python', '123445556@qq.com')]
    print(users)
    return 'hello'


@app.route('/update')
def update():
    user = User.query.get(1)
    user.username = 'python'
    user.email = '123445556@qq.com'
    db.session.add(user)
    db.session.commit()
    print(user)
    return 'update'


if __name__ == '__main__':
    app.run(debug=True)


'''
ORM
将PySql和SQL语句封装成对象
好处：避免SQL注入；各个不同的数据需要写不同的查询语句，这个不同
坏处：每一个的具体语法是不一样的，而SQL语句却是大体相同的
数据库创建步骤：
0. 安装sqlalchemy
1. 配置数据库
2. 定义表结构，设计表
3. 创建表

创建数据库
1. 在command创建：
set FLASK_APP=app.py
flask shell 进入python shell
from app import db
db.create_all()
2. 代码创建
def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app
    # 推入上下文更好
    with app.app_context as ctx:
        db.create_all()
3. 通过migrate创建：迁移的时候方便；动态修改数据库结构
set FLASK_APP=app.py
flask db init
flask db migrate 生成脚本
flask db upgrade 更新到数据库
flask db downgrade 退回
'''




