import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic("matplotlib", " inline")


get_ipython().getoutput("head data/sales_data.csv")


sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])


sales.head()


sales.shape


sales.info()


sales.describe()


sales['Unit_Cost'].describe()


sales['Unit_Cost'].mean()


sales['Unit_Cost'].median()


sales['Unit_Cost'].plot(kind='box', vert=True, figsize=(3,6))


sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde


ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')


ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6), bins=10)
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')


sales.head(6)


sales['Age_Group'].value_counts()


sales['Customer_Gender'].value_counts()


sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))


ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Sales')


ax = sales['Customer_Gender'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Sales')


corr = sales.corr()

corr


fig = plt.figure(figsize=(8,8))

plt.matshow(corr, cmap='RdBu', fignum = fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);


sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))


sales.plot(kind='scatter', x='Order_Quantity', y='Revenue', figsize=(6,6))


ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(8,6))
ax.set_ylabel('Profit')


ax = sales[['Profit', 'Customer_Gender']].boxplot(by='Customer_Gender', figsize=(4,6))
ax.set_ylabel('Profit')


boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit', 'Revenue']

sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,4), figsize=(14,8))


sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

sales['Revenue_per_Age'].head(10)


sales['Revenue_per_Age'].plot(kind='density', figsize=(14,6))


sales['Revenue_per_Age'].plot(kind='hist', figsize=(14,6))


sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']

sales['Calculated_Cost'].head(10)


(sales['Calculated_Cost'] get_ipython().getoutput("= sales['Cost']).sum()")


sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))


sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']

sales['Calculated_Revenue'].head(10)


(sales['Calculated_Revenue'] get_ipython().getoutput("= sales['Revenue']).sum()")


sales.head()


sales['Revenue'].plot(kind='hist', bins=30, figsize=(14,6))


sales['Unit_Price'].head(8)


#sales['Unit_Price'] = sales['Unit_Price'] * 1.03

sales['Unit_Price'] *= 1.03


sales['Unit_Price'].head()


sales.loc[sales['State'] == 'Kentucky']


sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()


sales.loc[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]


sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 
          'Revenue'].mean()


sales.loc[sales['Country'] == 'France', 'Revenue'].head()


#sales.loc[sales['Country'] == 'France', 'Revenue'] = sales.loc[sales['Country'] == 'France', 'Revenue'] * 1.1

sales.loc[sales['Country'] == 'France', 'Revenue'] *= 1.1


sales.loc[sales['Country'] == 'France', 'Revenue'].head()
