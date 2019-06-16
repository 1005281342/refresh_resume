import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from utils.functools import new_operator
from utils.email_test import send_email

from core.sign_in import sing_in
from core.work import search_work


def do():
    send_email(content="简历刷新任务已激活")
    print("[start] The time is: %s" % datetime.now())
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
        print("[end] The time is: %s" % datetime.now())


if __name__ == '__main__':

    scheduler = BlockingScheduler()

    scheduler.add_job(do)
    scheduler.add_job(do, 'interval', seconds=60 * 60)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        pass
