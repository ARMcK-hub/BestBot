from datetime import datetime
from time import time

runtime_log = "data/runtime_log.txt"

def clear_log():
    open(runtime_log, "w").close()


def write_log(scope, message = ""):
    time_stamp = datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')

    with open(runtime_log, "a") as file:

        if message == "":
            msg = f"{time_stamp}   :   {scope}"
        else:
            msg = f"{time_stamp}   :   {scope} - {message}"
        
        print(msg)
        file.writelines(msg + "\n")
