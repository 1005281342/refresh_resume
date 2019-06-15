from utils.functools import new_operator
from core.sign_in import sing_in
from core.work import search_work


def do():
    operator = new_operator()
    try:
        if not sing_in(operator=operator):
            raise Exception("登录失败")

        search_work(operator)
    # do()
    except Exception as e:
        print(e)
    finally:
        operator.close()


if __name__ == '__main__':
    do()
