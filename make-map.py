import pandas as pd
import folium
# from screeninfo import get_monitors

# Load the CSV file
df = pd.read_csv('data.csv')

# m = get_monitors()
# m_width = m[0].width
# m_height = m[0].height

# print(m_width)
# print(m_height)

# Create a map centered around the mean latitude and longitude
m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12, width = '100%', height = '100%')

# Add points to the map
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name']
    ).add_to(m)

# Save the map to an HTML file
m.save('youMadeThisMap.html')
