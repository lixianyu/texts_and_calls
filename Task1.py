"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

def getSmsPhoneNumbers():
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        #print(type(reader))
        texts = list(reader)
        #print(type(texts))
        allPhoneNUM = []
        for sms in texts:
            if sms[0] not in allPhoneNUM:
                allPhoneNUM.append(sms[0])
            if sms[1] not in allPhoneNUM:
                allPhoneNUM.append(sms[1])
        return (allPhoneNUM)

def getCallPhoneNumbers():
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        allCallNUM = []
        for call in calls:
            if call[0] not in allCallNUM:
                allCallNUM.append(call[0])
            if call[1] not in allCallNUM:
                allCallNUM.append(call[1])
        return (allCallNUM)

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
smsCountList = getSmsPhoneNumbers()
# print(smsCount)
callCountList = getCallPhoneNumbers()
# print(callCount)
allList = smsCountList + callCountList
# print(allList)
allSet = set(allList)
print("There are {} different telephone numbers in the records.".format(len(allSet)))
