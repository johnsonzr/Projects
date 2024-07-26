# Import required modules
import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

# Start coding!
df = pd.read_csv('datacamp_projects/modeling_car_insurance_claim_outcomes/data/car_insurance.csv')

# print(df.columns)
#print(df.info())
#df = df.fillna(df.mean())

df_model = df.drop(columns = ['id', 'outcome'])

models = []

for x in list(df_model):
    model = logit('outcome ~ {}'.format(x), data = df).fit()
    models.append(model)
#print(models)

# Testing accuracy
accuracy = []
for model in models:
    conf_matrix = model.pred_table()
    TN, FP, FN, TP = conf_matrix.ravel()
    #print(TN, FP, FN, TP)
    accuracy.append((TN + TP) / (TN + FP + FN + TP))
result = pd.DataFrame({'Feature': df_model.columns,
                        'Accuracy': accuracy})

best_feature = result[result.Accuracy == result.Accuracy.max()]

best_feature_df = pd.DataFrame({'best_feature' : best_feature.Feature,
             'best_accuracy' : best_feature.Accuracy})
print(best_feature_df)
