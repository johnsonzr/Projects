import pandas as pd
import seaborn as sns

men = pd.read_csv('datacamp_projects/hypothesis_testing_soccer_project/data/men_results.csv')
women = pd.read_csv('datacamp_projects/hypothesis_testing_soccer_project/data/women_results.csv')
# print(men.head())
# print(men.date.min)

# Preparing the df
men['gender'] = 'mens'
women['gender'] = 'womens'

soccer = pd.concat([men, women])
soccer = soccer[soccer['date'] >= '2002-01-01'] 
soccer = soccer[soccer['tournament'] == 'FIFA World Cup']
soccer['total_goals'] = soccer['home_score'] + soccer['away_score']
# print(soccer.columns)

# Understaning the data
import pingouin

# sns.histplot(data = soccer, x = 'total_goals')
# result = anderson(x = soccer['total_goals'], dist = 'norm')
# print(result)

#sns.displot(data = soccer, x = 'total_goals', kind = 'kde')

# Running the test
goals_vs_gender = soccer[['total_goals', 'gender']]
pivot = goals_vs_gender.pivot(columns = 'gender', values = 'total_goals')

test = pingouin.mwu(x = pivot['womens'], y = pivot['mens'], alternative='greater')
print(test['p-val'])

result_dict = {"p_val": 0.005107, "result": "reject"}
print(result_dict)