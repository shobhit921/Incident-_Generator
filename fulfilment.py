import csv
import random
from datetime import date, timedelta


start_date = date(2023, 1, 1)
end_date = date(2023, 3, 31)


dates = []
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 5:
        dates.append(current_date)
    current_date += timedelta(days=1)


with open('data2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Requirements', 'Fulfilment', 'startDate', 'endDate'])

    for i in range(len(dates)):
       
        requirements = ' '.join(random.choices(['Lorem', 'ipsum', 'dolor', 'sit', 'amet'], k=10))
        if i < len(dates) * 0.9:
            end_date = dates[i] + timedelta(days=random.randint(1, 3))
            fulfilment = 'Yes'
        else:
            end_date = dates[i] + timedelta(days=random.randint(5, 7))
            fulfilment = 'No'

        
        writer.writerow([requirements, fulfilment, dates[i].strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')])
