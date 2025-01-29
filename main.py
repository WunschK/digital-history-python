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
#
df = pd.read_csv('gefangenenbuecher_heidelberg.csv')
#
#
df['Einlieferung'] = pd.to_datetime(df['Einlieferung'],format='%d.%m.%y')
df['Entlassung'] = pd.to_datetime(df['Entlassung'],format='%d.%m.%y')
#
df['duration (days)'] = (df['Entlassung'] - df['Einlieferung']).dt.days
#
print(df.head())
#
#
# # Create the bar chart
plt.bar(df['Zuname'], df['duration (days)'], color='skyblue')
#
# # Add labels and title
plt.title('Haftdauer', fontsize=16)
plt.xlabel('Name', fontsize=14)
plt.ylabel('Dauer', fontsize=14)
#
# # Rotate x-axis labels for readability
plt.xticks(rotation=90)
# # Display the bar chart
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
    df = pd.read_csv(filepath)




    # Todo 2: Convert date columns to datetime format
    df['Einlieferung'] = pd.to_datetime(df['Einlieferung'], format='%d.%m.%y')
    df['Entlassung'] = pd.to_datetime(df['Entlassung'], format='%d.%m.%y')



    # Todo 3: Calculate the incarceration period in days
    df['duration (days)'] = (df['Entlassung'] - df['Einlieferung']).dt.days


    # Ende 23.01.
    # Todo 4: Filter the dataframe based on the min_days and max_days parameters
    filtered_df = df.copy()
    if min_days is not None:
        filtered_df = filtered_df[filtered_df['duration (days)'] >= min_days]
    if max_days is not None:
        filtered_df = filtered_df[filtered_df['duration (days)'] <= max_days]





    # Todo 5: Generate the filename to save the file to
    filename = f"{min_days if min_days is not None else 'min'}_{max_days if max_days is not None else 'max'}.jpg"





    # Todo 6: Create the bar chart
    plt.figure(figsize=(25,15))
    plt.bar(filtered_df['Zuname'], filtered_df['duration (days)'], color='skyblue')
    # Todo 6.5 min/max/average
    max_value = filtered_df['duration (days)'].max()
    min_value = filtered_df['duration (days)'].min()
    avg_value = filtered_df['duration (days)'].mean()
    plt.axhline(max_value, color='red', linestyle='--', linewidth=2, label=f'Biggest: {max_value} days')
    plt.axhline(min_value, color='green', linestyle='--', linewidth=2, label=f'Lowest: {min_value} days')
    plt.axhline(avg_value, color='yellow', linestyle='--', linewidth=2, label=f'Average: {avg_value:.2f} days')
    # Todo 7: Add labels and title
    plt.title(f'Duration from {min_days} to {max_days} days', fontsize=16)
    plt.xlabel('Name', fontsize=14)
    plt.ylabel('Duration (days)', fontsize=14)
    # Todo 8: Rotate x-axis labels for readability
    plt.xticks(rotation=90)
    # Todo 8.5: every 2nd day on y-axis
    min_value = 0
    max_value = int(filtered_df['duration (days)'].max())
    plt.yticks(range(min_value, max_value, 2))
    # Todo 9: save the figure as a jpeg file
    plt.tight_layout()
    plt.savefig(filename, format='jpg', dpi=300)
    plt.close()  # Close the figure to free up memory
    # Todo 10: Display the bar chart
    print(f"Figure saved as: {filename}")
    return filtered_df



# filter_and_plot_from_file('gefangenenbuecher_heidelberg.csv', min_days=10, max_days=13)