import whois
import re
import dateutil
import datetime

w = whois.whois('')
date = re.findall('Expiration Date:*(.+)', w.text)
final_date = dateutil.parser.parse(date[0])
current_time = datetime.datetime.now()
result_time = final_date.date() - current_time.date()
print result_time

date = re.findall('Creation Date:*(.+)', w.text)
date.append(re.findall('Created On:*(.+)', w.text))
try:
    final_date = dateutil.parser.parse(date[0])
    current_time = datetime.datetime.now()
    result_time = current_time.date() - final_date.date()
except TypeError:
    final_date = dateutil.parser.parse(date[0][0])
    current_time = datetime.datetime.now()
    result_time = current_time.date() - final_date.date()
print result_time
