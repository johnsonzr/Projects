import pandas as pd

ds_jobs = pd.read_csv("datacamp_projects/preparing_data_for_modeling_with_customer_analytics_project/data/customer_train.csv")
dtype_dict = {'student_id' : 'int32', 'city_development_index' : 'float16', 'training_hours' : 'int32', 'job_change' : 'int32', 'city' : 'category', 'gender' : 'category', 'relevant_experience' : 'category', 'enrolled_university' : 'category', 'education_level' : 'category', 'major_discipline' : 'category', 'experience' : 'category', 'company_size' : 'category', 'company_type' : 'category', 'last_new_job' : 'category'}
ds_jobs_clean = ds_jobs.astype(dtype_dict)
# print(ds_jobs_clean.info())

# print(ds_jobs_clean['last_new_job'].unique())

ds_jobs_clean['relevant_experience'] = ds_jobs_clean['relevant_experience'].cat.reorder_categories(new_categories = ['No relevant experience', 'Has relevant experience'], ordered = True)

ds_jobs_clean['education_level'] = ds_jobs_clean['education_level'].cat.reorder_categories(new_categories = ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'], ordered = True)

ds_jobs_clean['experience'] = ds_jobs_clean['experience'].cat.reorder_categories(new_categories = ['<1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '>20'], ordered = True)

ds_jobs_clean['company_size'] = ds_jobs_clean['company_size'].cat.reorder_categories(new_categories = ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'], ordered = True)

ds_jobs_clean['enrolled_university'] = ds_jobs_clean['enrolled_university'].cat.reorder_categories(new_categories = ['no_enrollment', 'Part time course', 'Full time course'], ordered = True)

ds_jobs_clean['last_new_job'] = ds_jobs_clean['last_new_job'].cat.reorder_categories(new_categories = ['never', '1', '2', '3', '4', '>4'], ordered = True)


ds_jobs = ds_jobs_clean[(ds_jobs_clean['experience'] >= '10') & (ds_jobs_clean['company_size'] >= '1000-4999')]
# print(ds_jobs.size)


# Copy the DataFrame for cleaning
ds_jobs_clean = ds_jobs.copy()

# Create a dictionary of columns containing ordered categorical data
ordered_cats = {
    'relevant_experience': ['No relevant experience', 'Has relevant experience'],
    'enrolled_university': ['no_enrollment', 'Part time course', 'Full time course'],
    'education_level': ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'],
    'experience': ['<1'] + list(map(str, range(1, 21))) + ['>20'],
    'company_size': ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'],
    'last_new_job': ['never', '1', '2', '3', '4', '>4']
}

# Loop through DataFrame columns to efficiently change data types
for col in ds_jobs_clean:
    
    # Convert integer columns to int32
    if ds_jobs_clean[col].dtype == 'int':
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('int32')
    
    # Convert float columns to float16
    elif ds_jobs_clean[col].dtype == 'float':
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('float16')
    
    # Convert columns containing ordered categorical data to ordered categories using dict
    elif col in ordered_cats.keys():
        category = pd.CategoricalDtype(ordered_cats[col], ordered=True)
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('category')
    
    # Convert remaining columns to standard categories
    else:
        ds_jobs_clean[col] = ds_jobs_clean[col].astype('category')
        
# Filter students with 10 or more years experience at companies with at least 1000 employees
ds_jobs_clean = ds_jobs_clean[(ds_jobs_clean['experience'] >= '10') & (ds_jobs_clean['company_size'] >= '1000-4999')]
print(ds_jobs_clean.size)