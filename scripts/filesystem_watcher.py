import os
import time
import shutil

INBOX = r"D:\Digital_FTE_Project\AI_Employee_Vault\Inbox"
NEEDS_ACTION = r"D:\Digital_FTE_Project\AI_Employee_Vault\Needs_Action"
LOG_PATH = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log"

print("Checking paths...")

print(os.path.exists(INBOX))
print(os.path.exists(NEEDS_ACTION))

print("Watcher Running...")

while True:

    files = os.listdir(INBOX)

    for file in files:

        source = INBOX + "\\" + file
        destination = NEEDS_ACTION + "\\" + file

        if os.path.isfile(source):

            shutil.move(source,destination)

            print("Moved:",file)

            with open(LOG_PATH,"a") as log:
                log.write("Task detected: "+file+"\n")

    time.sleep(5)