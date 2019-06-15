from utils.constant import Msg, URL
from utils.functools import new_operator, get_cookie

operator_g = new_operator()


def sing_in(operator=operator_g):
    state = False
    c = 0
    while not state:
        c += 1
        if c > 60:
            return None
        cs, e = get_cookie()
        if (not cs) or e:
            state = False
        else:

            operator.get(URL)
            operator.maximize_window()
            for c in cs:
                operator.add_cookie(c)
            operator.refresh()
            try:
                state = True
            except Exception as e:
                _ = e
                state = False
    return Msg['SignIn']
