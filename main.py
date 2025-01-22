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

def filter_and_plot_from_file(filepath, min_days=None, max_days=None):
    '''opens a csv-file and plots the duration of the incarceration period and saves the generated graph as a jpeg file
    Parameters:
    filepath = the path to the csv-file
    min_days = the minimum duration of the incarceration period - int/optional
    max_days = the maximum duration of the incarceration period - int/optional
    '''

    # Todo 1: open the csv-file as a dataframe

    # Todo 2: Convert date columns to datetime format

    # Todo 3: Calculate the incarceration period in days

    # Todo 4: Filter the dataframe based on the min_days and max_days parameters

    # Todo 5: Generate the filename to save the file to

    # Todo 6: Create the bar chart

    # Todo 7: Add labels and title

    # Todo 8: Rotate x-axis labels for readability

    # Todo 9: save the figure as a jpeg file

    # Todo 10: Display the bar chart


    pass




