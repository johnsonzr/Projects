import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the dataset
df = pd.read_csv("datacamp_projects/predictive_modeling_for_agriculture/data/soil_measures.csv")

# Train test split
x_df = df.drop(columns = 'crop')
y_df = df.crop

x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size = .2)

model = LogisticRegression()
model.fit(x_train, y_train)

coefficients = pd.DataFrame({
    'Feature': x_df.columns,
    'Coefficient': model.coef_[0]
})

best_predictive_feature = {'K' : float(coefficients.Coefficient.max())}
print(best_predictive_feature)