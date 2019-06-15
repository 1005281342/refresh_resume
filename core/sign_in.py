from utils.constant import Msg, URL
from utils.functools import get_cookie


def sing_in(operator):
    cs, e = get_cookie()
    operator.get(URL)
    operator.maximize_window()
    for c in cs:
        # print(c)
        operator.add_cookie(c)
    operator.refresh()
    # state = False
    # c = 0
    # while not state:
    #     c += 1
    #     if c > 60:
    #         return None
    #     cs, e = get_cookie()
    #     print(e)
    #     if (not cs) or e:
    #         state = False
    #     else:
    #
    #         operator.get(URL)
    #         operator.maximize_window()
    #         for c in cs:
    #             print(c)
    #             operator.add_cookie(c)
    #         operator.refresh()
    #         try:
    #             state = True
    #         except Exception as e:
    #             _ = e
    #             state = False
    return Msg['SignIn']
