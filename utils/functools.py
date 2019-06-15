import json

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


def get_proxy():
    return requests.get(IPProxyURL + "/get/").content


def delete_proxy(proxy):
    requests.get(IPProxyURL + "/delete/?proxy={}".format(proxy))


# def set_proxy(operator):
#     ip, port = get_proxy().decode().split(':')
#     script = "phantom.setProxy('{ip}',{port})".format(ip=ip, port=port)
#     operator.execute('EXECUTE_PHANTOM_SCRIPT', {'script': script, 'args': []})
#     return operator

if __name__ == '__main__':
    res = get_proxy().decode()
    print(res)
