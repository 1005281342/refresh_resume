import os
from datetime import datetime
import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from utils.functools import new_operator

from core.sign_in import sing_in
from core.work import search_work

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log_1.txt',
                    filemode='a')


def do():
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
        print("[end] The time is: %s" % datetime.now())
        operator.close()


if __name__ == '__main__':

    scheduler = BlockingScheduler()

    scheduler.add_job(do)
    scheduler.add_job(do, 'interval', seconds=2 * 30 * 60)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        pass
