import os
import time
import shutil

MESSAGES = r"D:\Digital_FTE_Project\AI_Employee_Vault\Social_Media"
INBOX = r"D:\Digital_FTE_Project\AI_Employee_Vault\Inbox"

print("Message Watcher Running...")

while True:

    files = os.listdir(MESSAGES)

    for file in files:

        source = MESSAGES + "\\" + file
        dest = INBOX + "\\" + file

        if os.path.isfile(source):

            shutil.move(source,dest)

            print("Message moved to Inbox:",file)

    time.sleep(6)