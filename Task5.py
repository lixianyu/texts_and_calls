'''
Task5是Task4的改进
'''
import csv

fcall = open('calls.csv', 'r')
reader_call = csv.reader(fcall)
calls = list(reader_call)

fsms = open('texts.csv', 'r')
reader_sms = csv.reader(fsms)
texts = list(reader_sms)

def just_incoming_telephone(calls):
    """
    找出参数列表(calls)中,只拨打电话的号码
    """
    incomings = set()
    answerings = set()
    for record in calls:
        incomings.add(record[0])
        answerings.add(record[1])
    for phone in answerings:
        if phone in incomings:
            incomings.remove(phone)
    return incomings

def get_no_text_contact_telephones(telephones):
    """
    找出参数集合(telephones)中,没有发送或收到过短信的号码
    """
    for record in texts:
        if record[0] in telephones:
            telephones.remove(record[0])
        if record[1] in telephones:
            telephones.remove(record[1])
    return telephones

#1.找出calls中只拨号的电话号码,2.然后从中找出没有收发过短信的电话号码,3.转换为列表,以便排序
result_list = list(get_no_text_contact_telephones(just_incoming_telephone(calls)))
print("These numbers could be telemarketers: \n" + "\n".join(sorted(result_list)))

fcall.close()
fsms.close()
