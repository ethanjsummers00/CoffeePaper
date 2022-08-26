from configparser import ConfigParser
import configparser
from distutils.command.config import config
import requests
from bs4 import BeautifulSoup
import pandas
import secrets
import pyfiglet

configFile = 'config.ini'
config = ConfigParser()
config.read(configFile)

# print(config.sections())
# print(list(config['preferences']))

ASCII_art_1 = pyfiglet.figlet_format("CoffeePaper")
print(ASCII_art_1)

pullConfig = config['preferences']

if ((pullConfig['name']) == "null"):
    nameInput = input("What is your first name?: ")
    
    config.set('preferences', 'name', nameInput)
    with open(configFile, 'w') as configWrite:
        config.write(configWrite)
    
    print("Hello " + (config['preferences']['name']))
else:
    print("Hello " + (config['preferences']['name']))

urlWeather = "https://www.google.com/search?q=" + "weather" + (pullConfig['location'])

if ((pullConfig['location']) == "null"):
    locInput = input("What city are you in?: ")
    
    config.set('preferences', 'location', locInput)
    with open(configFile, 'w') as configWrite:
        config.write(configWrite)
    
    urlWeather = "https://www.google.com/search?q=" + "weather" + (pullConfig['location'])    
    
    print('\n')
else:
    print("------------")

html = requests.get(urlWeather).content
soup = BeautifulSoup(html, 'html.parser')

temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

data = str.split('\n')
time = data[0]
sky = data[1]

# list having all div tags having particular clas sname
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# particular list with required data
strd = listdiv[5].text

# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]

print("Time: ", time)
print("Temperature is", temp)
print("Sky Description: ", sky)

data = pandas.read_csv("funFacts.csv", header=0)
col_a = list(data.Facts)

print("------------")
print("Fun fact of the day: " + (secrets.choice(col_a)))
print('\n')