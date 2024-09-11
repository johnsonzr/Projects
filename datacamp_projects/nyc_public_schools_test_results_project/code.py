import pandas as pd

# Read in the data
schools = pd.read_csv("datacamp_projects/nyc_public_schools_test_results_project/data/schools.csv")

# Preview the data

# print(schools.head())

best_math_schools = schools[schools.average_math > (.8 * 800)]
best_math_schools = best_math_schools.drop(columns = ['borough', 'building_code', 'average_reading', 
                                                     'average_writing', 'percent_tested'])
best_math_schools = best_math_schools.sort_values('average_math', ascending = False)
# print(best_math_schools)

# Getting top 10 schools dataframe 
SAT_scores = schools.average_math + schools.average_reading + schools.average_writing
scores = {'school_name' : schools.school_name,
          'total_SAT' : SAT_scores}
top_10_schools = pd.DataFrame(scores)
top_10_schools = top_10_schools.sort_values('total_SAT', ascending = False)
top_10_schools = top_10_schools.head(10)
print(top_10_schools)

# Getting the borough with the largest std in SAT scores
schools['total_SAT'] = SAT_scores

borough_stats = schools.groupby(['borough']).agg({'total_SAT': ['std', 'mean']})
# borough_stats = borough_std.rename(columns = {"('total_SAT', 'std')" : 'SAT_std',
#                                            "('total_SAT', 'mean')": 'SAT_mean'})

borough_num = schools.borough.value_counts()

borough_dict = {'borough' : schools.borough.unique(),
                'num_schools' : borough_num,
                'average_SAT' : borough_stats.iloc[:, 1],
                'std_SAT' : borough_stats.iloc[:, 0]}

borough_df = pd.DataFrame(borough_dict).round(2)
borough_df = borough_df.sort_values('std_SAT', ascending = False)
largest_std_dev = borough_df[borough_df['borough'] == 'Bronx']
print(largest_std_dev)