from time import time

def next_time(wait_sec):
    while True:
        now = int(time())
        if now % wait_sec == 0:
            break

