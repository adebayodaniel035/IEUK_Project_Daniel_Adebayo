#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Telemetry Data Processing File
#Author: Daniel Adebayo
#Purpose: Read telemetry_data.csv, calculate average temperature per turbine and check for anomalous results and output list
#Import data to Python from csv files and defines known functions
import pandas as pd
#Define telemetry data and read into a DataFrame
telemetry_data = pd.read_csv("telemetry_data(in).csv")
#Define variable names from data into code
temperature = telemetry_data["temperature_c"]
vibrations= telemetry_data["vibration_mm_s"]
rotation_per_minute = telemetry_data["rpm"]
turbine_number = telemetry_data["turbine_id"]
#Group data by turbine
grouped_data = telemetry_data.groupby("turbine_id")
#Define average temperature and vibration spikes, then calculate mean and maximum
average_temperature = grouped_data["temperature_c"].mean()
max_vibrations = grouped_data["vibration_mm_s"].max()
#Create a list to store anomalous values and create a loop to see which fail the test
turbines_failed = []
for turbine in grouped_data.groups.keys():
    if average_temperature[turbine] > 85 or max_vibrations[turbine] > 15:
        turbines_failed.append(turbine)
    else:
        pass
#Output results        
print("Failed Turbines:", turbines_failed)


# In[ ]:





# In[ ]:





# In[ ]:




