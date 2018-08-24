import re
import collections
import sys
import pandas as pd


#defining the regular expressions
regexp = re.compile(
    r'(?P<date>\d{4}-\d{2}-\d{2})' +
    '(?P<timestamp>\d{2}:\d{2}:\d{2},\d{3})' +
    '(?P<errorcode>[A-Z]{4,6})'
    
)
## can just make this dynamic with an argv[1] line
LC = open('server.log').read().split('\n')

csv = []


#looping through array with regex
for index, val in enumerate(LC):
    logList = LC[index]
    date = re.findall(r'\d{4}-\d{2}-\d{2}',logList)
    if date:
        date = [date[0]]
    timestamp = re.findall(r'\d{2}:\d{2}:\d{2},\d{3}',logList)
    if timestamp:
       timestamp = [timestamp[0]]
    errorcode = re.findall(r'INFO|ERROR|WARN',logList)
    if errorcode:
       errorcode = [errorcode[0]]
#    address = re.findall(r'\[\w+\.\w+\.\w+\.\w+\.\w+\.\w+\]',logList)
    address = re.findall(r'\[\w.+\]',logList)
    defaultTask = re.findall(r'(default task-\d{1,3})',logList)
    if address:
        address = [address[0][1:-1]]
#        print address
    printout = date + timestamp + errorcode + address + defaultTask
    csv.append(printout)


csv = pd.DataFrame(data=csv)


print csv

csv.to_csv('testlogstructure.csv', encoding='utf-8', index=False)



#for line in LC:
#    m = re.findall(regexp)

#print LC[0]

'''
for line in LC:
    m= regexp.match(line)
    if not m:
        continue

    print 'date/timestamp: %s %s, errorcode: %s' % (
            m.group('date'),
            m.group('timestamp'),
            m.group('errorcode')
    )                             
'''

