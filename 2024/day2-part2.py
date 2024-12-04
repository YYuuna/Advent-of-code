#read input from txt file
file = open("2024/day2-input.txt", "r")
lines = file.readlines()
file.close()
reports=[[int(level) for level in report.split()] for report in lines]
#initialize the sum
sum = 0
def checkSafety(report):
    safe = True
    if report[0] < report[1]:
        for i in range(0,len(report)-1):
            safe = (report[i+1]-report[i]>=1) and (report[i+1]-report[i]<=3)
            if not safe:
                break
    elif report[0] > report[1]:
        for i in range(0,len(report)-1):
            safe = (report[i]-report[i+1]>=1) and (report[i]-report[i+1]<=3)
            if not safe:
                break
    else:
        safe=False
    return safe
for report in reports:
    if not checkSafety(report):
        safe=False
        for level in report:
            dampenedReport=report.copy()
            dampenedReport.remove(level)
            if checkSafety(dampenedReport):
                safe=True
                break
    else:
        safe=True    
    if safe:
        sum+=1
print(sum)
    

