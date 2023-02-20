import csv
import random
from datetime import datetime, timedelta

# Set up the field names and file name
fields = ['Incident Number', 'Status', 'DateTime', 'Priority', 'Weight', 'Owner']
filename = 'incidents3.csv'

# Set up the date range
start_date = datetime(2022, 12, 1)
end_date = datetime(2023, 2, 28)

# Generate incidents with random data
incidents = []
for i in range(100):
    incident_number = random.randint(2500, 3500)
    status = 'New'
    date_time = start_date + (end_date - start_date) * random.random()
    date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
    priority = random.randint(1, 5)
    weight = random.randint(1, 5)
    owner = 'DT'
    incidents.append([incident_number, status, date_time, priority, weight, owner])

# Add new incidents with status "In-progress" for 95% of the incidents
for i in range(len(incidents)):
    if random.random() < 0.95:
        incident = incidents[i]
        incident_number = incident[0]
        status = 'In-progress'
        date_time = datetime.strptime(incident[2], '%d/%m/%Y %H:%M:%S')
        date_time += timedelta(hours=random.randint(2, 5))
        date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
        priority = incident[3]
        weight = incident[4]
        owner = 'DT'
        incidents.append([incident_number, status, date_time, priority, weight, owner])

# Add new incidents with status "Resolved" for random incidents with owner as "ACN"
for incident in incidents:
    if incident[5] == 'ACN' and random.random() < 0.2:
        incident_number = incident[0]
        status = 'Resolved'
        date_time = datetime.strptime(incident[2], '%d/%m/%Y %H:%M:%S')
        date_time += timedelta(hours=random.randint(2, 48))
        date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
        priority = incident[3]
        weight = incident[4]
        owner = 'ACN'
        incidents.append([incident_number, status, date_time, priority, weight, owner])

# Add new incidents with owner as "ACN" for the subset with status "In-progress"
for incident in incidents:
    if incident[1] == 'In-progress':
        incident_number = incident[0]
        status = incident[1]
        date_time = datetime.strptime(incident[2], '%d/%m/%Y %H:%M:%S')
        date_time += timedelta(hours=random.randint(2, 5))
        date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
        priority = incident[3]
        weight = incident[4]
        owner = 'ACN'
        incidents.append([incident_number, status, date_time, priority, weight, owner])

# Write the incidents to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(incidents)
