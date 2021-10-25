#### Data Cleaning

We see that some columns don't have correct types. We have to do data cleaning.

car_data['Buraxılış ili'] = car_data['Buraxılış ili'].astype(int)

In our price column, some prices is showed in Azerbaijan manat and others in US dollars. We are going to convert all of them into AZN, and change its dtype to float.

car_data['Qiymət'] = car_data['Qiymət'].str.replace(' ','').astype(str)
x = car_data[car_data['Qiymət'].str.contains('AZN')==False]['Qiymət'].str[:-1].astype(int)*1.70
y = car_data[car_data['Qiymət'].str.contains('AZN')]['Qiymət'].str[:-3].astype(int)
car_data['Price'] = pd.concat([x,y])
car_data.drop('Qiymət', axis=1, inplace=True)

If we substract produced date of the car from today's date, we can find car's age 

car_data['Age'] = pd.datetime.today().year - car_data['Buraxılış ili']

car_data['Mühərrikin gücü'] = car_data['Mühərrikin gücü'].str.replace('a.g.','').str.strip().astype(int)

car_data['Mühərrik'] = car_data['Mühərrik'].str.replace('L','').str.strip().astype(float)

car_data['Yürüş'] = car_data['Yürüş'].str.replace('km','').str.replace(' ','').astype(int)

car_data.head()
