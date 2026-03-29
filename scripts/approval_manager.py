import os
import time
import shutil

DONE = r"D:\Digital_FTE_Project\AI_Employee_Vault\Done"
PENDING = r"D:\Digital_FTE_Project\AI_Employee_Vault\Pending_Approval"
APPROVED = r"D:\Digital_FTE_Project\AI_Employee_Vault\Approved"
REJECTED = r"D:\Digital_FTE_Project\AI_Employee_Vault\Rejected"
log_path = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log"

print("Approval Manager Running...")

while True:
    # Get the list of files inside the pending directory
    files = os.listdir(PENDING)

    for file in files:
        file_path = PENDING + "\\" + file

        # Check for Approved files
        if file.startswith("APPROVED_"):
            shutil.move(file_path, DONE + "\\" + file)
            print("Task Approved:", file)
            
            with open(log_path, "a") as log:
                log.write("Approved: " + file + "\n")

        # Check for Rejected files
        if file.startswith("REJECTED_"):
            shutil.move(file_path, REJECTED + "\\" + file)
            print("Task Rejected:", file)
            
            with open(log_path, "a") as log:
                log.write("Rejected: " + file + "\n")

    # Wait for 6 seconds before checking the folder again
    time.sleep(6)