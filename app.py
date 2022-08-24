from configparser import ConfigParser
import configparser
from distutils.command.config import config

configFile = 'config.ini'
config = ConfigParser()
config.read(configFile)

print(config.sections())
print(list(config['preferences']))

nameInput = input("What is your first name?: ")

config.set('preferences', 'name', nameInput)
with open(configFile, 'w') as configWrite:
    config.write(configWrite)

print((config['preferences']['name']) + " " + config['preferences']['location'])