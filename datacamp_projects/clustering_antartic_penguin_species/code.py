# Import Required Packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Loading and examining the dataset
penguins_df = pd.read_csv("datacamp_projects/clustering_antartic_penguin_species/data/penguins.csv")
penguins_df.head()

df = pd.get_dummies(penguins_df)
print(df.head())

scaler = StandardScaler()
scaled_df = scaler.fit_transform(df)

iner = []
for x in range(1, 11):
    model = KMeans(n_clusters=x)
    model.fit(scaled_df)
    iner.append(model.inertia_)
    
plt.plot(range(1, 11), iner)
plt.show()

model = KMeans(n_clusters=6)
model.fit(scaled_df)
df['group'] = model.predict(scaled_df)

stat_penguins = df.groupby('group')[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']].mean()
print(stat_penguins)