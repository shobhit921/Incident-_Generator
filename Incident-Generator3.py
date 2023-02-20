import pandas as pd
from datetime import datetime, timedelta
import random

# Define incident descriptions
descriptions = ["-reset password", "Forgot Password", "unable to log in", "Login Failed", "Crazy Stupid Computers"]

# Define incident numbers range
incident_num_range = range(2500, 3701)

# Define initial incident status
status = "New"

# Create empty dataframe
df = pd.DataFrame(columns=["Incident Number", "Priority", "DateTime", "Short Description", "Status", "Weight"])

# Set start and end date for incidents
start_date = datetime(2022, 12, 1)
end_date = datetime(2023, 2, 28)

# Loop to generate incidents
for incident_num in incident_num_range:

    # Generate random values for incident fields
    priority = random.randint(1, 5)
    datetime_str = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    short_desc = random.choice(descriptions)
    weight = random.randint(1, 5)
    
    # Check if incident is new or closed
    if status == "New" or status == "Closed":
        status = "In-progress"
    elif status == "In-progress":
        # Randomly decide if incident should be resolved or remain in-progress
        if random.random() < 0.5:
            status = "Resolved"
        else:
            status = "In-progress"
    elif status == "Resolved":
        # Randomly decide if incident should be in-progress or generate a new entry with the same incident number
        if random.random() < 0.5:
            status = "In-progress"
            # Create new row with the same incident number but new status
            priority = random.randint(1, 5)
            datetime_str = datetime_str + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
            short_desc = random.choice(descriptions)
            weight = random.randint(1, 5)
            new_row = {"Incident Number": incident_num, "Priority": priority, "DateTime": datetime_str.strftime("%d/%m/%Y %H:%M:%S"), "Short Description": short_desc, "Status": status, "Weight": weight}
            df = df.append(new_row, ignore_index=True)
            incident_num += 1
        else:
            status = "In-progress"
    
    # Create new row for incident
    new_row = {"Incident Number": incident_num, "Priority": priority, "DateTime": datetime_str.strftime("%d/%m/%Y %H:%M:%S"), "Short Description": short_desc, "Status": status, "Weight": weight}
    
    # Add row to dataframe
    df = df.append(new_row, ignore_index=True)

# Export dataframe to excel file
df.to_excel("incidents5.xlsx", index=False)
