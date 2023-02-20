import pandas as pd
from datetime import datetime, timedelta
import random


descriptions = ["reset password", "Forgot Password", "unable to log in", "Login Failed", "Crazy Stupid Computers"]


incident_num = 1
status = "New"


df = pd.DataFrame(columns=["Incident Number", "Priority", "DateTime", "Short Description", "Status", "Weight"])


start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now()


while incident_num <= 100:

    
    priority = random.randint(1, 5)
    datetime_str = start_date + timedelta(days=random.randint(0, 30))
    short_desc = random.choice(descriptions)
    weight = random.randint(1, 5)
    
    
    if status == "New" or status == "Closed":
        status = "In-progress"
    elif status == "In-progress":
        status = "Resolved"
    
    
    if status == "Resolved":
        
        priority = random.randint(1, 5)
        datetime_str = datetime_str + timedelta(days=random.randint(0, 1))
        short_desc = random.choice(descriptions)
        weight = random.randint(1, 5)
        status = "New"
        incident_num += 1
    else:
        incident_num += 1
    
    
    new_row = {"Incident Number": incident_num, "Priority": priority, "DateTime": datetime_str.strftime("%d/%m/%Y %H:%M:%S"), "Short Description": short_desc, "Status": status, "Weight": weight}
    
    
    df = df.append(new_row, ignore_index=True)


df.to_excel("incidents4.xlsx", index=False)
