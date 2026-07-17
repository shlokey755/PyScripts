import numpy as np
import pandas as pd
df = pd.read_csv("C:\\Users\\Keerti\\Downloads\\final_weather_data.csv")

'''
# Sorting by Temperature to get the highest value
df['Temperature (°C)'] = pd.to_numeric(df['Temperature (°C)'], errors='coerce')  # ensure numeric
highest_temp_record = df.loc[df['Temperature (°C)'].idxmax()]
print(highest_temp_record)

average_humidity = df['Humidity (%)'].mean()
print(f"Average Humidity: {average_humidity}%")

median_visibility = df['Visibility (km)'].median()
print(f"Median Visibility: {median_visibility} km")

most_frequent_wind = df['Wind_Direction (Compass)'].mode()[0]
print(f"Most Frequent Wind Direction: {most_frequent_wind}")

average_temp_by_condition = df.groupby('Weather_Condition')['Temperature (°C)'].mean()
print(average_temp_by_condition)

import pandas as pd

# Load the dataset (Replace this with the actual data loading process)
# df = pd.read_csv('your_dataset.csv')

# Convert 'Temperature (°C)' to numeric (if it's not already)
df['Temperature (°C)'] = pd.to_numeric(df['Temperature (°C)'], errors='coerce')

# Group by Weather_Condition and calculate the mean temperature
average_temp_by_condition = df.groupby('Weather_Condition')['Temperature (°C)'].mean()

# Find the weather condition with the highest average temperature
highest_temp_condition = average_temp_by_condition.idxmax()
highest_temp_value = average_temp_by_condition.max()

print(f"The weather condition with the highest average temperature is {highest_temp_condition} with an average temperature of {highest_temp_value}°C.")

import numpy as np

# New record data
new_record = np.array([13, 60, 1018, 20, 1])  # Dew Point, Humidity, Pressure, Temperature, Visibility

# Existing records (numerical columns only)
existing_records = df[['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']].values

# Calculate Euclidean distances
distances = np.linalg.norm(existing_records - new_record, axis=1)

# Sort distances and find the indices of the 3 nearest neighbors
nearest_neighbors = np.argsort(distances)[:3]
print(f"Indices of 3 nearest neighbors: {nearest_neighbors}")

# Check the rain presence for the 3 nearest neighbors
rain_presence_neighbors = df.iloc[nearest_neighbors]['Rain_Presence']
print(f"Rain Presence for nearest neighbors: {rain_presence_neighbors}")'''

# Cluster centers (using 01-Jan-2015 and 02-Jan-2015)
cluster_1_center = np.array(df.iloc[0][['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']].values)
cluster_2_center = np.array(df.iloc[1][['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']].values)

# 12-Jan-2016 data
record_12_jan_2016 = np.array(df[df['Date'] == '12-Jan-2016'][['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']].values[0])

# Calculate distance between record_12_jan_2016 and cluster_1_center
distance_cluster_1 = np.linalg.norm(record_12_jan_2016 - cluster_1_center)
print(f"Distance between 12-Jan-2016 and Cluster 1: {distance_cluster_1}")
# 04-Jan-2015 data
record_04_jan_2015 = np.array(df[df['Date'] == '04-Jan-2015'][['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']].values[0])

# Calculate distance from both clusters
distance_from_cluster_1 = np.linalg.norm(record_04_jan_2015 - cluster_1_center)
distance_from_cluster_2 = np.linalg.norm(record_04_jan_2015 - cluster_2_center)

# Assign to the closest cluster
assigned_cluster = 1 if distance_from_cluster_1 < distance_from_cluster_2 else 2
print(f"Assigned Cluster for 04-Jan-2015: Cluster {assigned_cluster}")

# Example for re-calculating new cluster centers (after assignment)
# For simplicity, assume the dataset is split into two clusters based on distance from cluster centers
'''
# Example: Compute new centers after assignment (simple average)
new_cluster_1_center = df[df['Assigned_Cluster'] == 1][['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']].mean().values
new_cluster_2_center = df[df['Assigned_Cluster'] == 2][['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']].mean().values

print(f"New Cluster 1 Center: {new_cluster_1_center}")
print(f"New Cluster 2 Center: {new_cluster_2_center}")'''
'''
import pandas as pd

# Load the dataset (Replace this with the actual data loading process)
# df = pd.read_csv('your_dataset.csv')

# Convert 'Temperature (°C)' to numeric (if it's not already)
df['Temperature (°C)'] = pd.to_numeric(df['Temperature (°C)'], errors='coerce')

# Group by Weather_Condition and calculate the mean temperature
average_temp_by_condition = df.groupby('Weather_Condition')['Temperature (°C)'].mean()

# Find the weather condition with the highest average temperature
highest_temp_condition = average_temp_by_condition.idxmax()
highest_temp_value = average_temp_by_condition.max()

print(f"The weather condition with the highest average temperature is {highest_temp_condition} with an average temperature of {highest_temp_value}°C.")

'''
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load the CSV dataset
# Replace with your CSV file path
file_path = "path_to_your_dataset.csv"
df = pd.read_csv(file_path)

# Step 2: Select relevant columns for clustering (ignoring categorical features like Weather_Condition and Wind_Direction)
features = ['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']
df_clean = df[features]

# Optional: Normalize the data (recommended for K-means)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_clean)

# Step 3: Apply K-Means Clustering (with K=2 as an example)
kmeans = KMeans(n_clusters=2, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# Step 4: Assign clusters and calculate new cluster centers
cluster_centers = kmeans.cluster_centers_

# Step 5: Calculate new cluster centers (after assignment step)
# Get the points assigned to each cluster and calculate the mea

