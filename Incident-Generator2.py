import pandas as pd
from datetime import datetime, timedelta
import random

# Define incident descriptions
descriptions = ["reset password", "Forgot Password", "unable to log in", "Login Failed", "Crazy Stupid Computers"]

# Define initial incident numbers and status
incident_num = 1
status = "New"

# Create empty dataframe
df = pd.DataFrame(columns=["Incident Number", "Priority", "DateTime", "Short Description", "Status", "Weight"])

# Set start and end date for incidents
start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now()

# Loop to generate incidents
while incident_num <= 100:

    # Generate random values for incident fields
    priority = random.randint(1, 5)
    datetime_str = start_date + timedelta(days=random.randint(0, 30))
    short_desc = random.choice(descriptions)
    weight = random.randint(1, 5)
    
    # Check if incident is new or closed
    if status == "New" or status == "Closed":
        status = "In-progress"
    elif status == "In-progress":
        status = "Resolved"
    
    # Check if incident is resolved and add a new entry
    if status == "Resolved":
        # Generate new entry with same incident number but new status
        priority = random.randint(1, 5)
        datetime_str = datetime_str + timedelta(days=random.randint(0, 1))
        short_desc = random.choice(descriptions)
        weight = random.randint(1, 5)
        status = "New"
        incident_num += 1
    else:
        incident_num += 1
    
    # Create new row for incident
    new_row = {"Incident Number": incident_num, "Priority": priority, "DateTime": datetime_str.strftime("%d/%m/%Y %H:%M:%S"), "Short Description": short_desc, "Status": status, "Weight": weight}
    
    # Add row to dataframe
    df = df.append(new_row, ignore_index=True)

# Export dataframe to excel file
df.to_excel("incidents4.xlsx", index=False)
