from random import randint
from time import sleep

from utils.constant import WorkList, WorkErrEmailContext, WorkOverEmailContext, WorkTitle
from utils.email_test import send_email


def search(operator):
    sleep(1 + randint(1, 7))

    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input').clear()
    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input').send_keys(
        WorkList[randint(0, len(WorkList)-1)])

    operator.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/button').click()


def search_work(operator):
    # sleep(20)
    # operator.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[1]/a').click()
    # operator.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/form/div[2]/p/input').send_keys(
    #     WorkList[randint(0, len(WorkList)-1)])
    #
    # # 提交
    # operator.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/div[1]/form/button').click()
    e_c = 0
    count = 0
    while True:
        count += 1
        try:
            search(operator)
        except Exception as e:
            e_c += 1
            print(e)
        if e_c > 5 or count > 120:
            if count > 120:
                send_email(content=WorkOverEmailContext, title=WorkTitle)
            else:
                send_email(content=WorkErrEmailContext, title=WorkTitle)
            break
