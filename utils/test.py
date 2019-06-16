import os
import sys

currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
# print(parentUrl)
sys.path.append(parentUrl)

if __name__ == '__main__':
    from utils.functools import timer_func, time_click, test_timer

    new_time_click = time_click(func=test_timer)
    timer_func(func=new_time_click, start_time="13:27:00")