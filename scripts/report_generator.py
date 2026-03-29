import os

LOG_PATH = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log"
REPORT_PATH = r"D:\Digital_FTE_Project\AI_Employee_Vault\Reports\weekly_report"

print("Generating Report...")

with open(LOG_PATH,"r") as log:
    data = log.readlines()

report = open(REPORT_PATH,"w")

report.write("WEEKLY CEO REPORT\n\n")
report.write("Total activities:\n")
report.write(str(len(data))+"\n\n")

report.write("Recent Logs:\n")

for line in data[-10:]:
    report.write(line)

report.close()

print("Report Generated.")