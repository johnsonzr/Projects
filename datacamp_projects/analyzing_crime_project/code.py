# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("datacamp_projects/analyzing_crime_project/data/crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
# print(crimes.head())

hour = pd.to_datetime(crimes['TIME OCC'], format = '%H%M')
# crimes['TIME OCC'] = hour.dt.strftime('%I:%M %p')
crimes['hour'] = hour.dt.strftime('%I %p')
# print(crimes['hour'].head())
# print(crimes.value_counts('hour'))
peak_crime_hour = 12
print(peak_crime_hour)

crimes['TIME OCC'] = crimes['TIME OCC'].astype(int)
crimes['day_time'] = np.where((crimes['TIME OCC'] < 400) | (crimes['TIME OCC'] > 2200 ), 'night', 'day')
# print(crimes.groupby('AREA NAME')['day_time'].agg('count').sort_values(ascending = False))
# print(crimes.value_counts(['AREA NAME', 'day_time']))

sns.set_context('paper', font_scale = .95)
night_crimes = crimes[crimes['day_time'] == 'night']
areas = list(crimes['AREA NAME'].unique())

values1 = areas[:4]
values2 = areas[4:8]
values3 = areas[8:12]
values4 = areas[12:16]
values5 = areas[16:20]
values6 = areas[20:24]


areas1 = crimes[crimes['AREA NAME'].isin(values1)]
areas2 = crimes[crimes['AREA NAME'].isin(values2)]
areas3 = crimes[crimes['AREA NAME'].isin(values3)]
areas4 = crimes[crimes['AREA NAME'].isin(values4)]
areas5 = crimes[crimes['AREA NAME'].isin(values5)]
areas6 = crimes[crimes['AREA NAME'].isin(values6)]
    

fig, axes = plt.subplots(2, 3, figsize = (12, 10))
sns.countplot(data = areas1, x = areas1['AREA NAME'], hue =  areas1['day_time'], ax = axes[0, 0])
sns.countplot(data = areas2, x = 'AREA NAME', hue =  'day_time', ax = axes[0, 1])
sns.countplot(data = areas3, x = 'AREA NAME', hue =  'day_time', ax = axes[0, 2])
sns.countplot(data = areas4, x = 'AREA NAME', hue =  'day_time', ax = axes[1, 0])
sns.countplot(data = areas5, x = 'AREA NAME', hue =  'day_time', ax = axes[1, 1])
sns.countplot(data = areas6, x = 'AREA NAME', hue =  'day_time', ax = axes[1, 2])

plt.show()

peak_night_crime_location = 'Central'
print(peak_night_crime_location)

# Finding victim age group crime counts

bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
labels = ['0-17', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']
crimes['Age Bracket'] = pd.cut(crimes['Vict Age'], bins = bins, labels = labels)
victim_ages = crimes['Age Bracket'].value_counts()
# print(crimes[crimes['Vict Age'] == 26]['Age Bracket'])
print(victim_ages)

