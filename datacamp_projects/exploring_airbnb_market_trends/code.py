# Import necessary packages
import pandas as pd
import numpy as np

# Begin coding here ...
df_csv = pd.read_csv('datacamp_projects/exploring_airbnb_market_trends/data/airbnb_price.csv')

df_xlsx = pd.read_excel('datacamp_projects/exploring_airbnb_market_trends/data/airbnb_room_type.xlsx')

df_tsv = pd.read_csv('datacamp_projects/exploring_airbnb_market_trends/data/airbnb_last_review.tsv', sep='\t')

# Earliest and most recent views
df_tsv.last_review = pd.to_datetime(df_tsv.last_review)

earliest = df_tsv.last_review.min()
latest = df_tsv.last_review.max()

# Number of private room listings
df_xlsx.room_type = df_xlsx.room_type.str.lower()
private_rooms = df_xlsx[df_xlsx['room_type'] == 'private room'].count()[0]
print(private_rooms)

# Average listing price
df_csv.price = df_csv.price.str.replace(r' dollars','')
df_csv.price = df_csv.price.astype('int')

avg_price = df_csv.price.mean().round(2)

# Creating review dates
review_dates = pd.DataFrame(data = [[earliest, latest, private_rooms, avg_price]], columns = ['first_reviewed', 'last_reviewed', 'nb_private_rooms', 'avg_price'])

print(review_dates)