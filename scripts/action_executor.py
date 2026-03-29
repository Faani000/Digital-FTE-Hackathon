import os
import time

DONE = r"D:\Digital_FTE_Project\AI_Employee_Vault\Done"
LOG_PATH = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log"

print("Action Executor Running...")

while True:

    tasks = os.listdir(DONE)

    for task in tasks:

        if task.endswith(".txt"):

            print("Executing task:",task)

            with open(LOG_PATH,"a") as log:
                log.write("Executed task: "+task+"\n")

    time.sleep(10)