# Import libraries that we will use

# for reading the csv file
import pandas as pd

# for plotting
import matplotlib.pyplot as plt

weather_data = pd.read_csv("weather_data.csv")

print(weather_data)
date = weather['Date']
temp = weather['High_Temp_degF']
plt.plot(date,temp)

Create a scatter plot figure for plotting weather_data data
fig, ax = plt.subplots(figsize=(10,10)) # Create a figure for plotting data
ax.scatter(date,temp)
fontsize = 14
ax.set_xlabel('date (day)', fontsize=fontsize)
ax.set_ylabel('temp (degF)', fontsize=fontsize)
ax.tick_params(axis='x', labelsize=fontsize)
ax.tick_params(axis='y', labelsize=fontsize)