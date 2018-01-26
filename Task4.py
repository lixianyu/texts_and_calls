"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

fcall = open('calls.csv', 'r')
reader_call = csv.reader(fcall)
calls = list(reader_call)

fsms = open('texts.csv', 'r')
reader_sms = csv.reader(fsms)
texts = list(reader_sms)

def in_sms(phone_number):
    """
    判断一个电话是否在短信中出现

    若出现则返回True，否则返回False
    """
    for sms in texts:
        if sms[0] == phone_number:
            return True
        if sms[1] == phone_number:
            return True
    return False

def is_called(phone_number):
    """
    判断一个电话是否在被叫列表中出现

    若出现则返回True，否则返回False
    """
    for call in calls:
        if phone_number == call[1]:
            return True
    return False


noSmsList = []
for call in calls:
    #找到所有不发短信、不收短信的号码
    if in_sms(call[0]):
        continue
    else:
        if call[0] not in noSmsList:
            noSmsList.append(call[0])
telemarketersList = []
for phone_number in noSmsList:
    if not is_called(phone_number):
        telemarketersList.append(phone_number)

sList = sorted(telemarketersList)
print("These numbers could be telemarketers: ")
for num in sList:
    print(num)

fcall.close()
fsms.close()

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
