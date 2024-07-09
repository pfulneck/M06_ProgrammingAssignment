import time
from datetime import datetime

#13.1
currentDate = datetime.now().strftime('%Y-%m-%d')
with open('today.txt', 'w') as file:
    file.write(currentDate)

#13.2
with open('today.txt', 'r') as file:
    today_string = file.read()

#13.3
fmt = '%Y-%m-%d'
parsed_date = datetime.strptime(today_string, fmt)

print('Current Date: ', currentDate)
print('Today String: ', today_string)
print('Parsed Date: ', parsed_date)