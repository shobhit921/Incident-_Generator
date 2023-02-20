import csv
import random
import datetime

# Define the fields for the CSV file
fields = ['Incident Number', 'Status', 'DateTime', 'Priority', 'Weight', 'Owner']

# Define the datetime range for the incidents
start_date = datetime.datetime(2022, 12, 1)
end_date = datetime.datetime(2023, 2, 28)

# Create a function to generate random datetime within the range
def random_datetime(start, end):
    delta = end - start
    random_second = random.randint(0, delta.total_seconds())
    return start + datetime.timedelta(seconds=random_second)

# Create a list to store the incident data
incidents = []

# Generate the incidents
for i in range(2500, 3501):
    priority = random.randint(1, 5)
    weight = [8, 5, 3, 2, 1][priority - 1]
    owner = 'DT'
    datetime_str = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
    incidents.append([i, 'New', datetime_str, priority, weight, owner])
    
    # Create a subset for 98% of the incidents
    if random.random() < 0.98:
        datetime_str_subset = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
        incidents.append([i, 'In-progress', datetime_str_subset, priority, weight, owner])
        
        # Add entries with owner as ACN
        datetime_str_acn = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
        incidents.append([i, 'In-progress', datetime_str_acn, priority, weight, 'ACN'])
        
        # Add entries with status as resolved
        num_resolved = random.randint(1, 20)
        for j in range(num_resolved):
            datetime_str_resolved = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
            incidents.append([i, 'Resolved', datetime_str_resolved, priority, weight, 'ACN'])
            
            # Mark 50% of the resolved incidents as closed
            if j == num_resolved - 1 and random.random() < 0.5:
                datetime_str_closed = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
                incidents.append([i, 'Closed', datetime_str_closed, priority, weight, 'ACN'])

# Write the incident data to the CSV file
with open('03_incidents.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(incidents)
