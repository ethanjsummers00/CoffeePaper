from configparser import ConfigParser
import configparser
from distutils.command.config import config

configFile = 'config.ini'
config = ConfigParser()
config.read(configFile)

print(config.sections())
print(list(config['preferences']))

nameConfig = config['preferences']

if ((nameConfig['name']) == "null"):
    nameInput = input("What is your first name?: ")
    
    config.set('preferences', 'name', nameInput)
    with open(configFile, 'w') as configWrite:
        config.write(configWrite)
else:
    print("Hello " + (config['preferences']['name']))

locInput = input("What city are you in?: ")

config.set('preferences', 'location', locInput)
with open(configFile, 'w') as configWrite:
    config.write(configWrite)
    
locConfig = config['preferences']

urlWeather = "https://www.google.com/search?q=" + "weather" + (locConfig['location'])

print(urlWeather)