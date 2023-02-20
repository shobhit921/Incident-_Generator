import csv
import random
import datetime


fields = ['Incident Number', 'Status', 'DateTime', 'Priority', 'Weight', 'Owner']


start_date = datetime.datetime(2022, 12, 1)
end_date = datetime.datetime(2023, 2, 28)


def random_datetime(start, end):
    delta = end - start
    random_second = random.randint(0, delta.total_seconds())
    return start + datetime.timedelta(seconds=random_second)


incidents = []

for i in range(2500, 3501):
    priority = random.randint(1, 5)
    weight = [8, 5, 3, 2, 1][priority - 1]
    owner = 'DTH'
    datetime_str = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
    incidents.append([i, 'New', datetime_str, priority, weight, owner])
    
    
    if random.random() < 0.98:
        datetime_str_subset = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
        incidents.append([i, 'In-progress', datetime_str_subset, priority, weight, owner])
        
        
        datetime_str_acn = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
        incidents.append([i, 'In-progress', datetime_str_acn, priority, weight, 'ABC'])
        
        
        num_resolved = random.randint(1, 20)
        for j in range(num_resolved):
            datetime_str_resolved = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
            incidents.append([i, 'Resolved', datetime_str_resolved, priority, weight, 'ABC'])
            
            
            if j == num_resolved - 1 and random.random() < 0.5:
                datetime_str_closed = random_datetime(start_date, end_date).strftime('%d/%m/%Y %H:%M:%S')
                incidents.append([i, 'Closed', datetime_str_closed, priority, weight, 'ABC'])


with open('03_incidents.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(incidents)
