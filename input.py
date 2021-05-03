import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['DEFAULT']['token']
COMPETITION_NAME = config['DEFAULT']['competition_name']
COUNTRY = config['DEFAULT']['country']
TEAM = config['DEFAULT']['team']

HEADER = {'X-Auth-Token': TOKEN}