import csv
import random
from datetime import datetime


fields = ['Incident Number', 'Status', 'DateTime', 'Priority', 'Weight', 'Owner']
filename = 'incidents.csv'


start_date = datetime(2022, 12, 1)
end_date = datetime(2023, 2, 28)


incidents = []
for i in range(1000):
    incident_number = random.randint(2500, 3500)
    status = random.choice(['New', 'In-progress', 'Resolved', 'Closed'])
    date_time = start_date + (end_date - start_date) * random.random()
    date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
    priority = random.randint(1, 5)
    weight = random.randint(1, 5)
    owner = 'DTH'
    incidents.append([incident_number, status, date_time, priority, weight, owner])


with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(incidents)
