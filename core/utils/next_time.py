from time import time, sleep

def next_time(wait_sec):
    while True:
        now = int(time())
        sleep(1)
        if now % wait_sec == 0:
            break

