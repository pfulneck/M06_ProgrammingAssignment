#15.1

import multiprocessing
import random
import time
from datetime import datetime

def processTask():
    waitTime = random.uniform(0,1)
    time.sleep(waitTime)
    print(f'The current time is now: {datetime.now()}')

if __name__ == '__main__':
    processes = []

    for _ in range(3):
        p = multiprocessing.Process(target=processTask)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()