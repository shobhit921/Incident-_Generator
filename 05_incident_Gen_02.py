import csv
import random
from datetime import datetime, timedelta


fields = ['Incident Number', 'Status', 'DateTime', 'Priority', 'Weight', 'Owner']
filename = '01_incidents.csv'


start_date = datetime(2022, 12, 1)
end_date = datetime(2023, 2, 28)


incidents = []
for i in range(1000):
    incident_number = random.randint(2500, 3500)
    status = 'New'
    date_time = start_date + (end_date - start_date) * random.random()
    date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
    priority = random.randint(1, 5)
    weight = random.randint(1, 5)
    owner = 'DTH'
    incidents.append([incident_number, status, date_time, priority, weight, owner])

   
    if random.random() < 0.95:
        date_time = datetime.strptime(date_time, '%d/%m/%Y %H:%M:%S')
        date_time += timedelta(hours=random.randint(2, 5))
        date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
        incidents.append([incident_number, 'In-progress', date_time, priority, weight, owner])


for i in range(len(incidents)):
    if incidents[i][5] == 'ABC' and random.random() < 0.2:
        date_time = datetime.strptime(incidents[i][2], '%d/%m/%Y %H:%M:%S')
        date_time += timedelta(hours=random.randint(1, 4))
        date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
        incidents.append([incidents[i][0], 'Resolved', date_time, incidents[i][3], incidents[i][4], 'ABC'])


for i in range(len(incidents)):
    if incidents[i][1] == 'In-progress':
        date_time = datetime.strptime(incidents[i][2], '%d/%m/%Y %H:%M:%S')
        date_time += timedelta(hours=random.randint(2, 5))
        date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
        incidents.append([incidents[i][0], incidents[i][1], date_time, incidents[i][3], incidents[i][4], 'ABC'])


with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(incidents)
    print('File Created!') 