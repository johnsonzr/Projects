import pandas as pd
import seaborn as sns
import numpy as np

# Data
nobel = pd.read_csv('datacamp_projects/nobel_prize_winners_project/data/nobel.csv')
df = nobel
# print(df.columns)
# print(df[df.year == 1939])

# Most common gender and birth country
# print(df.sex.value_counts(), df.birth_country.value_counts())
genders = df.sex.value_counts()
top_gender = 'Male'
countries = df.birth_country.value_counts()
top_country = 'United States of America'

# Decade loop
my_dict = {}
data = df
x = 1910
while len(data) != 0:
    my_dict[x - 10] = data[data.year < x] 
    data = data[data.year >= x]
    x += 10
    

# Getting decade with highest proportion of US born winners

x = 1910
country_pro = {}
while x < 2023: 
        countries = my_dict[x]['birth_country'].value_counts()
        us_pro = (countries['United States of America'] / (countries.sum() - countries['United States of America'])) * 100
        country_pro[x] = us_pro 
        x += 10
        
# print(country_pro)
max_decade_usa = 2000
print(max_decade_usa)

x = 1910
ratios = {}
while x < df.year.max():
    my_data = pd.DataFrame.from_dict(my_dict[x])
    my_data = my_data[['sex', 'category']]

    counts = my_data.groupby(['sex', 'category']).size()

    sex_counts = my_data['category'].value_counts()

    ratios[x] = (counts.div(sex_counts, level='category')).round(2) 
    x += 10

# print(ratios)
max_female_dict = {2020 : 'Literature'}
print(max_female_dict)

female_df = df[df.sex == 'Female']
first_woman = female_df[['full_name', 'category']].head(1)
print(first_woman)

first_woman_name = 'Marie Curie, née Sklodowska'
first_woman_category = 'Physics'

from collections import Counter
multi_win = Counter(df.full_name)
repeat_list = [var for var, multi_win in multi_win.items() if multi_win > 1]