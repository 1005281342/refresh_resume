from random import randint
from time import sleep

from utils.constant import WorkList, WorkErrEmailContext, WorkOverEmailContext, WorkTitle
from utils.email_test import send_email


def search(operator):
    sleep(1 + randint(1, 10))

    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input').clear()
    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input').send_keys(
        WorkList[randint(0, len(WorkList)-1)])

    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/button').click()


def search_work(operator):
    sleep(20)
    operator.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[1]/a').click()
    operator.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/form/div[2]/p/input').send_keys(
        WorkList[randint(0, len(WorkList)-1)])

    # 提交
    operator.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/form/button').click()
    e_c = 0
    count = 0
    while True:
        e_msg = ''
        count += 1
        try:
            search(operator)
        except Exception as e:
            e_c += 1
            print(e)
            e_msg = e
        if e_c > 5 or count > 300:
            if count > 300:
                send_email(content=WorkOverEmailContext, title=WorkTitle)
            else:
                send_email(content=WorkErrEmailContext+e_msg, title=WorkTitle)
            break
