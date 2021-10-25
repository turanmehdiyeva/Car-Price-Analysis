### Exploratory data analysis

car_data.dtypes

#### Sale trends in different regions of Azerbaijan:

import seaborn as sns
import matplotlib.pyplot as plt
 
sns.barplot(x = 'Şəhər',
            y = 'Price',
            data = car_data)

plt.xticks(rotation=90)
plt.show()

count_df = car_data.groupby('Şəhər').count()[['Marka']]
count_df
values = list(count_df['Marka'])
labels = list(count_df.index)
plt.title(label='Number of cars by region', fontsize=15)
sns.barplot(labels,values)
plt.xticks(rotation=90)
plt.show()

average_df = car_data.groupby('Şəhər').mean()[['Price']]
average_df

values = list(average_df['Price'])
labels = list(average_df.index)
plt.title(label='Average price by region', fontsize=15)
sns.barplot(labels,values)
plt.xticks(rotation=90)
plt.show()

#### Market Share of different car manufacturers:

marka_count_df = car_data.groupby('Marka').agg({'Model':'count'})
marka_count_df

f, ax = plt.subplots(figsize=(15,5)) 
sns.barplot(x = marka_count_df.index,
            y = 'Model',
            data = marka_count_df)

plt.ylabel('count')
plt.xticks(rotation=90)
plt.show()

marka_mean_df = car_data.groupby('Marka').mean()[['Price']]
marka_mean_df

f, ax = plt.subplots(figsize=(15,5)) 
sns.barplot(x = marka_mean_df.index,
            y = 'Price',
            data = marka_mean_df)

plt.ylabel('Average Price')
plt.xticks(rotation=90)
plt.show()

#### Types of vehicle and the Fuel they use :

fuel_df = car_data.groupby('Yanacaq növü').count()[['Marka']]
fuel_df

values = list(fuel_df['Marka'])
labels = list(fuel_df.index)
plt.title(label='Number of cars by fuel type', fontsize=15)
sns.barplot(labels,values)
plt.xticks(rotation=90)
plt.show()

#### Trend of number of cars for sale according to the year they were manufactured in :

sns.kdeplot(data=car_data, x="Buraxılış ili", shade=True, color="r")
plt.show()

year_df = car_data.groupby('Buraxılış ili').count()[['Marka']]

f, ax = plt.subplots(figsize=(15,5)) 
sns.barplot(x = year_df.index,
            y = 'Marka',
            data = year_df)
plt.ylabel('Number of cars by Years')
plt.xticks(rotation=90)
plt.show()

#### Relation of price other variables of a car:

ax = sns.boxplot(x="Yanacaq növü", y="Price", data=car_data)

ax = sns.boxplot(x="Sürətlər qutusu", y="Price", data=car_data)
plt.xticks(rotation=90)
plt.show()

f, ax = plt.subplots(figsize=(10,5))
ax = sns.boxplot(x="Rəng", y="Price", data=car_data)
plt.xticks(rotation=90)
plt.show()

ax = sns.boxplot(x="Ötürücü", y="Price", data=car_data)
plt.xticks(rotation=90)
plt.show()

ax = sns.boxplot(x="Ban növü", y="Price", data=car_data)
plt.xticks(rotation=90)
plt.show()

ax = sns.boxplot(x="Yeni", y="Price", data=car_data)
plt.xticks(rotation=90)
plt.show()
