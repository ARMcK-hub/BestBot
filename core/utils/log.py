from datetime import datetime
from time import time

runtime_log = "data/runtime_log.txt"

def clear_log():
    open(runtime_log, "w").close()


def write_log(scope, message = ""):
    time_stamp = datetime.utcfromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')

    with open(runtime_log, "a") as file:

        if scope == "oos":
            file.writelines(f"{time_stamp}   :   OOS - {message}\n")
        elif scope == "wait":
            file.writelines(f"{time_stamp}   :   Wait Initiated\n")
        elif scope == "loop":
            file.writelines(f"{time_stamp}   :   Started Loop\n")
        elif scope == "stock":
            file.writelines(f"{time_stamp}   :   IN STOCK! - {message}\n")
        elif scope == "contact":
            file.writelines(f"{time_stamp}   :   Notification Sent - {message}\n")
        elif scope == "terminate":
            file.writelines(f"{time_stamp}   :   Terminating Script\n")
        elif scope == "init":
            file.writelines(f"{time_stamp}   :   Script Initiated\n")
        elif scope == "set_contacts":
            file.writelines(f"{time_stamp}   :   Contacts Set - {message}\n")
        elif scope == "set_products":
            file.writelines(f"{time_stamp}   :   Products Set - {message}\n")
        else:
            file.writelines(f"{time_stamp}   :   UNKNOWN WRITE - {message}\n")
