import csv
import random
from datetime import datetime, timedelta

# Set up the field names and file name
fields = ['Incident Number', 'Status', 'DateTime', 'Priority', 'Weight', 'Owner']
filename = 'incidents.csv'

# Set up the date range
start_date = datetime(2022, 12, 1)
end_date = datetime(2023, 2, 28)

# Generate 1000 incidents with random data
incidents = []
for i in range(1000):
    incident_number = random.randint(2500, 3500)
    status = random.choice(['New', 'In-progress', 'Resolved', 'Closed'])
    date_time = start_date + (end_date - start_date) * random.random()
    date_time = date_time.strftime('%d/%m/%Y %H:%M:%S')
    priority = random.randint(1, 5)
    weight = random.randint(1, 5)
    owner = 'DT'
    incidents.append([incident_number, status, date_time, priority, weight, owner])

# Modify the incidents with "New" status
new_incidents = []
for incident in incidents:
    if incident[1] == 'New':
        incident[1] = 'In-progress'
        date_time = datetime.strptime(incident[2], '%d/%m/%Y %H:%M:%S')
        date_time += timedelta(hours=random.randint(2, 5))
        incident[2] = date_time.strftime('%d/%m/%Y %H:%M:%S')
        incident[5] = 'ACN'
        new_incidents.append(incident)

# Add the modified incidents to the original list
incidents.extend(new_incidents)

# Write the incidents to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(incidents)
