import json
import datetime
from functools import wraps

import threading
import requests
from selenium import webdriver

from utils.constant import CookieFile, IPProxyURL


def new_operator():
    # return webdriver.PhantomJS()
    opt = webdriver.ChromeOptions()
    # opt.add_argument('--proxy-server=http://' + get_proxy().decode())
    opt.set_headless()
    return webdriver.Chrome(chrome_options=opt)


def get_cookie(file_name=CookieFile):
    cs = e = None
    try:
        with open(file_name, 'r') as f:
            cs = json.loads(f.read())
    except Exception as ee:
        e = ee
    return cs, e


def write_cookie(operator, file_name=CookieFile):
    cookies = operator.get_cookies()
    with open(file_name, 'w') as f:
        f.write(json.dumps(cookies))
    print("写入成功")


def get_proxy():
    r = requests.get(IPProxyURL + "/get/").content
    print("获取到的代理IP为", r)
    return r


def delete_proxy(proxy):
    requests.get(IPProxyURL + "/delete/?proxy={}".format(proxy))


# def set_proxy(operator):
#     ip, port = get_proxy().decode().split(':')
#     script = "phantom.setProxy('{ip}',{port})".format(ip=ip, port=port)
#     operator.execute('EXECUTE_PHANTOM_SCRIPT', {'script': script, 'args': []})
#     return operator


def time_click(func):
    """

    :param func: 需要定时执行的 任务函数
    :return:
    """
    func()
    time_r = threading.Timer(10, time_click)
    time_r.start()


def timer_func(func, start_time="20:30:00"):
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day

    start_time = " " + start_time

    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + start_time,
                                           "%Y-%m-%d %H:%M:%S")
    timer_start_time = (next_time - now_time).total_seconds()
    print(timer_start_time)

    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    timer = threading.Timer(60, func)
    timer.start()


def test_timer():
    with open('test.txt', 'a') as f:
        f.write("1\n")


def log(label):
    def decorate(func):
        @wraps(func)
        def _wrap(*args, **kwargs):
            try:
                func(*args, **kwargs)
                print("name", func.__name__)
            except Exception as e:
                print(e.args)

        return _wrap

    return decorate


@log("info")
def foo(a, b, c):
    print(a + b + c)
    print("in foo")


# decorate=decorate(foo)

if __name__ == '__main__':
    foo(1, 2, 3)
    # decorate()
