from random import randint
from time import sleep

from utils.constant import WorkList
from utils.functools import new_operator

operator = new_operator()


def search():
    sleep(1 + randint(1, 10))

    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input').clear().send_keys(
        WorkList[randint(0, len(WorkList))])

    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/button').click()


def search_work():
    operator.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[1]/a').click()
    operator.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/form/div[2]/p/input').send_keys(
        WorkList[randint(0, len(WorkList))])

    # 提交
    operator.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/form/button').click()

    while True:
        try:
            search()
        except Exception as e:
            operator.close()
            return e
