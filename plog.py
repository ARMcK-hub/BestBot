runtime_log = "logs/runtime_log.log"

with open(runtime_log, "r") as file:
    for line in file:
        print(line) 