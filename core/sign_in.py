from time import sleep

from utils.constant import Msg, URL
from utils.functools import get_cookie, write_cookie


def sing_in(operator):
    not_sign_in = True
    cs, e = get_cookie()
    operator.get(URL)
    operator.maximize_window()

    # if e:
    #     print(e)
    #     return None
    print("获取cookie异常", e)
    try:
        for c in cs:
            # print(c)
            operator.add_cookie(c)
        operator.refresh()
    except Exception as sie:
        print("无法正常设置cookie", sie)

        while not_sign_in:
            try:
                operator.find_element_by_xpath('//*[@id="header"]/div/div[3]/ul/li[5]/a/span')
                write_cookie(operator)
            finally:
                sleep(60)
                not_sign_in = False

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
