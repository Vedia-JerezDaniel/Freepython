import pandas as pd

#def calculate_demographic_data(print_data = True):
  # Read data from file
    df = pd.read_csv('data/adults.csv')
    df.head()
    
  # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    print(race_count)
    
  # What is the average age of men?
    average_age_men = int(df.loc[df['sex'] == 'Male', 'age'].mean())
    print('Average men age is:' , average_age_men)

  # What is the percentage of people who have a Bachelors degree?
    percentage_bachelors = round(float(((df['education'] == 'Bachelors').sum()) / len(df))*100, 2)
    print('Bachelors percentage:' , percentage_bachelors)
    
  # What percentage of the people with AND without `education` equal to `Bachelors`, `Masters`, or `Doctorate` 
  # also have a `salary` of `>50K` (Note: Every row of data has salary of either '>50K' or '<=50K')?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    print('Higher education:' , higher_education.shape[0])
    print('Lower education:' , lower_education.shape[0])
    
  # percentage with salary >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 2)
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 2)
    print('High salary percentage:' , higher_education_rich)
    print('Low salary percentage:' , lower_education_rich)
    
  # What is the minumum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    print('Minimum work hours:', min_work_hours)
  
  # What percentage of the people who work the minumum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]

    rich_percentage = round((float(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]) 
                             / num_min_workers) * 100, 2)
    print('Rich people percentage', rich_percentage)
    
  # What country has the highest percentage of people that earn >50K?
    highest_earning_country = ""
    highest_earning_country_percentage = 0.0
    for (i), j in df.groupby(['native-country']):
      percentage = len(j[(j['salary'] == '>50K')])/ len(j)
    if highest_earning_country_percentage < percentage:
      highest_earning_country_percentage = round(percentage, 4)
      highest_earning_country = i
      highest_earning_country_percentage *= 100
  
    print('percentage of highest rich people', highest_earning_country_percentage)
    print('Richest country:', highest_earning_country)
    
  # Identify the most popular occupation for those who earn >50K in India. 
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().keys()[0]
    print('top occupation in India:', top_IN_occupation)
    
    
  # WARNING: DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Country with highest percentage of rich:", highest_earning_country)
    print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
    print("Top occupations in India:", top_IN_occupation)

  return {'race_count': race_count, 'average_age_men': average_age_men, 'percentage_bachelors': percentage_bachelors, 
          'higher_education_rich': higher_education_rich, 'lower_education_rich': lower_education_rich, 'min_work_hours': min_work_hours, 
          'rich_percentage': rich_percentage, 'top_IN_occupation': top_IN_occupation}