import os
import time
import shutil

NEEDS_ACTION = r"D:\Digital_FTE_Project\AI_Employee_Vault\Needs_Action"
PLANS = r"D:\Digital_FTE_Project\AI_Employee_Vault\Plans"
PENDING = r"D:\Digital_FTE_Project\AI_Employee_Vault\Pending_Approval"

print("Agent Brain Running...")

while True:

    try:
        tasks = os.listdir(NEEDS_ACTION)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
        continue

    for task in tasks:

        task_path = NEEDS_ACTION + "\\" + task

        if os.path.isfile(task_path):

            plan_name = "PLAN_" + task

            plan_path = PLANS + "\\" + plan_name

            with open(plan_path,"w") as file:

                file.write("PLAN FOR TASK\n")
                file.write(task + "\n")
                file.write("\nSteps:\n")
                file.write("1 Analyze request\n")
                file.write("2 Prepare response\n")
                file.write("3 Send for approval\n")

            approval_file = PENDING + "\\APPROVAL_" + task

            with open(approval_file,"w") as file:

                file.write("APPROVAL NEEDED FOR:\n")
                file.write(task)

            shutil.move(task_path,PLANS+"\\"+task)

            print("Plan created for:",task)

log_path = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log"

with open(log_path,"a") as log:

    log.write("Plan created for: "+task+"\n")

    time.sleep(8)