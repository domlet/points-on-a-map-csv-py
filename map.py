import pandas as pd
import folium

# Load the CSV file
df = pd.read_csv('data.csv')

# Create a map centered around the mean latitude and longitude
m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)

# Add points to the map
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name']
    ).add_to(m)

# Save the map to an HTML file
m.save('youMadeThisMap.html')
