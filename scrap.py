from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import re

import warnings
warnings.filterwarnings('ignore')

#To make Car Price Prediction model we need to use Regression model. And a Regression model needs the data. That's why, firstly, we have to scrap our data. I will do it from turbo.az 

def get_car_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find('div', class_='product-properties-container')
    info_rows = info.find_all('li')
    
    car_info={}
    for index, row in enumerate(info_rows):
        try:
            content_key = row.find('label').get_text()
            content_value = row.find('div', class_ ='product-properties-value' ).get_text()
            car_info[content_key] = content_value
        except:
            continue
    return car_info
    

#This function get the url adress of the car and get all important information about the car that had been set

#In the code below we get link adress of cars from page 1 to 20

base_path = 'https://turbo.az/'
car_info_list = []
lst = []
link_list = []

for j in range(1,20):
    url = 'https://turbo.az/autos?page={}'.format(j)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cars = soup.select('.products a')
    for i in cars:
        lst.append(i['href'])


for i in lst:
    if i.startswith('/autos')==True and i.endswith('bookmarks')==False:
        link_list.append(base_path+i)
    

#After getting link adresses of cars now we can use our function to scrap the data

for i in link_list:
    try:
        car_info_list.append(get_car_info(i))
    except:
        continue

import json

def save_data(title,data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
        
def load_data(title):
    with open(title, encoding='utf-8') as f:
        return json.load(f)

#"save_data" function helps us to save our data in a json file and "load_data" helps us to load data into jupyter notebook

save_data('cars.json', car_info_list)

cars = load_data('cars.json')

car_data = pd.DataFrame(cars)

car_data.head()
