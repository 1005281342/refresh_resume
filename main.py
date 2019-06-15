from utils.functools import new_operator, set_proxy
from core.sign_in import sing_in
from core.work import search_work


def do():
    operator = new_operator()
    if not sing_in(operator=operator):
        raise Exception("登录失败")

    search_work()
    do()


if __name__ == '__main__':

    do()
