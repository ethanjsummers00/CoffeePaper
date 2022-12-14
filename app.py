#!/usr/bin/env python3
# app.py

from configparser import ConfigParser
from distutils.command.config import config
from logging.config import listen
from operator import contains
import requests
from bs4 import BeautifulSoup
import pandas
import secrets
import pyfiglet
from colorama import Fore, Back, Style

configFile = 'config.ini'
config = ConfigParser()
config.read(configFile)
pullConfig = config['preferences']

ASCII_art_1 = pyfiglet.figlet_format("CoffeePaper")
print(Fore.YELLOW + ASCII_art_1 + Style.RESET_ALL)

# modifies name in config
if ((pullConfig['name']) == "null"):
    nameInput = input("What is your first name?: ")
    
    config.set('preferences', 'name', nameInput)
    with open(configFile, 'w') as configWrite:
        config.write(configWrite)
    
    print("Hello " + (config['preferences']['name']))
else:
    print("Hello " + (config['preferences']['name']))

urlWeather = "https://www.google.com/search?q=" + "weather" + (pullConfig['location'])

# modifies location in config
if ((pullConfig['location']) == "null"):
    locInput = input("What city are you in?: ")
    
    config.set('preferences', 'location', locInput)
    with open(configFile, 'w') as configWrite:
        config.write(configWrite)
    
    #searches google weather for location set in config
    urlWeather = "https://www.google.com/search?q=" + "weather" + (pullConfig['location'])    
    
    print('\n')
else:
    print("------------")

html = requests.get(urlWeather).content
soup = BeautifulSoup(html, 'html.parser')

# pulls weather data from the loaded page
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

editList = ["National", "Weather", "Service" , "Enviornment"]
for word in editList:
    temp = temp.replace(word, "------------")

tempEdit = temp[:61] + '\n' + "Temperature: " + temp[62:]
# print(tempEdit)

data = str.split('\n')
time = data[0]
sky = data[1]

# list having all div tags with a specific class
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# particular list with required data
strd = listdiv[5].text

print("Time:", time)
# looking for an alert or warning in the temperature class
if 'arning' in temp or 'ert' in temp:
    print(Fore.RED + "!!Alert!!"+ Style.RESET_ALL, tempEdit)
else:
    print("Temperature:", temp)
print("Sky Description:", sky)

#ASCII weather output
if 'unny' in sky:
    print(Fore.YELLOW + "\n   \ | / \n    .-.\n-- (   ) --\n    `-'\n   / | \ \n" + Style.RESET_ALL)
elif 'ain' in sky:
    print(Fore.BLUE + "\n\ \ \ \n \  \ \n \ \ \ \n" + Style.RESET_ALL)
elif 'oudy' in sky:
    print(Fore.WHITE + "     _\n   _( )_\n _(     )_\n(_________)\n" + Style.RESET_ALL)
elif 'lear' in sky:
    print("    _...\n  .::'   \n :::       \n :::       \n `::.     \n   `::..-'\n")
elif 'now' in sky:
    print("Snow")
data = pandas.read_csv("funFacts.csv", header=0)
col_a = list(data.Facts)

print("------------")
print("Fun fact of the day: " + (secrets.choice(col_a)))
print('\n')

newsInput = input("Would you like to see today's headlines? (y or n): ")
if(newsInput == "y"):
    print("Okay!")
elif(newsInput == "n"):
    print("Boo!")
else:
    newsInput = input("(y or n): ")