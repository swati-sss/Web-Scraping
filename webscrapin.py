import pandas as pd
import requests 
from bs4 import BeautifulSoup
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2455#.XyFbdJ4zaM8')
Soup = BeautifulSoup(page.content, 'html.parser')
week = Soup.find(id = 'seven-day-forecast-body')
items = week.find_all(class_ = 'tombstone-container')
print(items[0])
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
period_names =[item.find(class_ = 'period-name').get_text() for item in items]
print(period_names)
Short_description =[item.find(class_ = 'short-desc').get_text() for item in items]
print(Short_description)
Temperature =[item.find(class_ = 'temp').get_text() for item in items]
print(Temperature)
weather_stuff = pd.DataFrame({'period':period_names,'Short description':Short_description,'Temperature':Temperature,})
print(weather_stuff)
weather_stuff.to_csv('weather.csv')