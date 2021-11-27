import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic("matplotlib", " inline")


sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])


sales.head()


# your code goes here



sales['Customer_Age'].mean()


# your code goes here



sales['Customer_Age'].plot(kind='kde', figsize=(14,6))


sales['Customer_Age'].plot(kind='box', vert=False, figsize=(14,6))


# your code goes here



sales['Order_Quantity'].mean()


# your code goes here



sales['Order_Quantity'].plot(kind='hist', bins=30, figsize=(14,6))


sales['Order_Quantity'].plot(kind='box', vert=False, figsize=(14,6))


# your code goes here



sales['Year'].value_counts()


# your code goes here



sales['Year'].value_counts().plot(kind='pie', figsize=(6,6))


# your code goes here



sales['Month'].value_counts()


# your code goes here



sales['Month'].value_counts().plot(kind='bar', figsize=(14,6))


# your code goes here



sales['Country'].value_counts().head(1)


sales['Country'].value_counts()


# your code goes here



sales['Country'].value_counts().plot(kind='bar', figsize=(14,6))


# your code goes here



#sales.loc[:, 'Product'].unique()

sales['Product'].unique()


# your code goes here



sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(14,6))


# your code goes here



sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6,6))


# your code goes here



sales.plot(kind='scatter', x='Order_Quantity', y='Profit', figsize=(6,6))


# your code goes here



sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10,6))


# your code goes here



sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10,6))


# your code goes here



sales['Calculated_Date'] = sales[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)

sales['Calculated_Date'].head()


# your code goes here



sales['Calculated_Date'] = pd.to_datetime(sales['Calculated_Date'])

sales['Calculated_Date'].head()


# your code goes here



sales['Calculated_Date'].value_counts().plot(kind='line', figsize=(14,6))


# your code goes here



#sales['Revenue'] = sales['Revenue'] + 50

sales['Revenue'] += 50


# your code goes here



sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0]


# your code goes here



sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0]


# your code goes here



france_states = sales.loc[sales['Country'] == 'France', 'State'].value_counts()

france_states


# your code goes here



france_states.plot(kind='bar', figsize=(14,6))


# your code goes here



sales['Product_Category'].value_counts()


# your code goes here



sales['Product_Category'].value_counts().plot(kind='pie', figsize=(6,6))


# your code goes here



accessories = sales.loc[sales['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()

accessories


# your code goes here



accessories.plot(kind='bar', figsize=(14,6))


# your code goes here



bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()

bikes


# your code goes here



bikes.plot(kind='pie', figsize=(6,6))


# your code goes here



sales['Customer_Gender'].value_counts()


sales['Customer_Gender'].value_counts().plot(kind='bar')


# your code goes here



sales.loc[(sales['Customer_Gender'] == 'M') & (sales['Revenue'] == 500)].shape[0]


# your code goes here



sales.sort_values(['Revenue'], ascending=False).head(5)


# your code goes here



#sales.sort_values(['Revenue'], ascending=False).head(1)

cond = sales['Revenue'] == sales['Revenue'].max()

sales.loc[cond]


# your code goes here



cond = sales['Revenue'] > 10_000

sales.loc[cond, 'Order_Quantity'].mean()


# your code goes here



cond = sales['Revenue'] < 10_000

sales.loc[cond, 'Order_Quantity'].mean()


# your code goes here



cond = (sales['Year'] == 2016) & (sales['Month'] == 'May')

sales.loc[cond].shape[0]


# your code goes here



cond = (sales['Year'] == 2016) & (sales['Month'].isin(['May', 'June', 'July']))

sales.loc[cond].shape[0]


# your code goes here



profit_2016 = sales.loc[sales['Year'] == 2016, ['Profit', 'Month']]

profit_2016.boxplot(by='Month', figsize=(14,6))


# your code goes here



#sales.loc[sales['Country'] == 'United States', 'Unit_Price'] = sales.loc[sales['Country'] == 'United States', 'Unit_Price'] * 1.072

sales.loc[sales['Country'] == 'United States', 'Unit_Price'] *= 1.072
