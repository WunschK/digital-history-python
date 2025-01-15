# Eine Funktion schreiben
def digital_history(n, m):
    while(n < m):
        n = n + 1
        if(n % 3 == 0 and n % 5 == 0):
            print("digital history")
        else:
            print(n)

# Die erstellte Funktion ausführen
#digital_history(n=7, m=20)


# import einer Bibliothek
import csv
from pprint import pprint

def open_csv(filename):
    with open(f'{filename}') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pprint(row['Einlieferung'])


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

df = pd.read_csv('gefangenenbuecher_heidelberg.csv')


df['Einlieferung'] = pd.to_datetime(df['Einlieferung'],format='%d.%m.%y')
df['Entlassung'] = pd.to_datetime(df['Entlassung'],format='%d.%m.%y')

df['duration (days)'] = (df['Entlassung'] - df['Einlieferung']).dt.days




# Create the bar chart
# plt.bar(df['Zuname'], df['duration (days)'], color='skyblue')
#
# # Add labels and title
# plt.title('Haftdauer', fontsize=16)
# plt.xlabel('Name', fontsize=14)
# plt.ylabel('Dauer', fontsize=14)
#
# # Rotate x-axis labels for readability
# plt.xticks(rotation=90)
#
# # Display the bar chart
# plt.tight_layout()
# plt.show()


# # Replace missing values with "no value"
# df['falls überstellt, wohin? (reguläre Haftanstalt oder Kislau/Ankenbuk'] = df[
#     'falls überstellt, wohin? (reguläre Haftanstalt oder Kislau/Ankenbuk'].fillna('Entlassung oder keine Information')
#
# # Clean the column by removing leading/trailing spaces
# df['falls überstellt, wohin? (reguläre Haftanstalt oder Kislau/Ankenbuk'] = df[
#     'falls überstellt, wohin? (reguläre Haftanstalt oder Kislau/Ankenbuk'].str.strip()
#
# # Calculate the frequency of each unique value in the specified column
# value_counts = df['falls überstellt, wohin? (reguläre Haftanstalt oder Kislau/Ankenbuk'].value_counts()
#
# # Create a pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90,
#         colors=['skyblue', 'lightcoral', 'lightgreen', 'gold', 'purple'])
#
# # Add a title
# plt.title('Distribution of Transfers to Different Institutions', fontsize=16)
#
# # Display the pie chart
# plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
# plt.show()




# Convert the dates to datetime format
df['Einlieferung'] = pd.to_datetime(df['Einlieferung'], format='%d.%m.%y', errors='coerce')
df['Entlassung'] = pd.to_datetime(df['Entlassung'], format='%d.%m.%y', errors='coerce')


# Drop rows with missing or invalid dates
df = df.dropna(subset=['Einlieferung', 'Entlassung'])

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))

# Plot the bars with the 'Einlieferung' date as the start and 'Entlassung' as the end
for idx, row in df.iterrows():
    plt.barh(row['Zuname'], (row['Entlassung'] - row['Einlieferung']).days, left=row['Einlieferung'], color='skyblue')

# Add labels and title
plt.title('Duration of Stay from Einlieferung to Entlassung', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Name', fontsize=14)

# Set the x-ticks to show only the unique 'Einlieferung' and 'Entlassung' dates
all_dates = pd.concat([df['Einlieferung'], df['Entlassung']]).unique()
plt.xticks(all_dates, rotation=45)

# Display the chart
plt.tight_layout()
plt.show()
