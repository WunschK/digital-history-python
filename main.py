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

print(df.head())


# Create the bar chart
plt.bar(df['Zuname'], df['duration (days)'], color='skyblue')

# Add labels and title
plt.title('Haftdauer', fontsize=16)
plt.xlabel('Name', fontsize=14)
plt.ylabel('Dauer', fontsize=14)

# Rotate x-axis labels for readability
plt.xticks(rotation=90)

# Display the bar chart
plt.tight_layout()
plt.show()



