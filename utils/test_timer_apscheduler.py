from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    with open('timer_test.log', 'a') as f:
        f.write('Tick! The time is: %s' % datetime.now() + '\n')


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # 每天 15:12 定时执行
    scheduler.add_job(tick, 'cron', hour=15, minute=50)
    scheduler.add_job(tick, 'cron', hour=15, minute=49)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
