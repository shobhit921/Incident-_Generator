import pandas as pd
from datetime import datetime, timedelta
import random


descriptions = ["-reset password", "Forgot Password", "unable to log in", "Login Failed", "Crazy Stupid Computers"]



incident_num_range = range(2500, 3701)


status = "New"


df = pd.DataFrame(columns=["Incident Number", "Priority", "DateTime", "Short Description", "Status", "Weight"])


start_date = datetime(2022, 12, 1)
end_date = datetime(2023, 2, 28)


for incident_num in incident_num_range:

    
    priority = random.randint(1, 5)
    datetime_str = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    short_desc = random.choice(descriptions)
    weight = random.randint(1, 5)
    
    
    if status == "New" or status == "Closed":
        status = "In-progress"
    elif status == "In-progress":
        
        if random.random() < 0.5:
            status = "Resolved"
        else:
            status = "In-progress"
    elif status == "Resolved":
        
        if random.random() < 0.5:
            status = "In-progress"
            
            priority = random.randint(1, 5)
            datetime_str = datetime_str + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
            short_desc = random.choice(descriptions)
            weight = random.randint(1, 5)
            new_row = {"Incident Number": incident_num, "Priority": priority, "DateTime": datetime_str.strftime("%d/%m/%Y %H:%M:%S"), "Short Description": short_desc, "Status": status, "Weight": weight}
            df = df.append(new_row, ignore_index=True)
            incident_num += 1
        else:
            status = "In-progress"
    
    
    new_row = {"Incident Number": incident_num, "Priority": priority, "DateTime": datetime_str.strftime("%d/%m/%Y %H:%M:%S"), "Short Description": short_desc, "Status": status, "Weight": weight}
    
    
    df = df.append(new_row, ignore_index=True)


df.to_excel("incidents5.xlsx", index=False)
