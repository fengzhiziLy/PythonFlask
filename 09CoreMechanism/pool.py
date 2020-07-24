class Pool:
    # 上下文协议
    def __enter__(self):
        print('我不走要游泳')
        print('泳池已经备好')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('游泳池已经搬走')


def swim():
    print('looking, I am Swimming')


# 没有上下文
swim()

# 有了上下文环境
with Pool() as pool:
    # 上下文管理器
    print(pool)  # <__main__.Pool object at 0x7f9bd77d6810>
    swim()

params = {
    'username': '111',
    'pwd': '222'
}


def add():
    return params.get('username') + params.get('pwd')


