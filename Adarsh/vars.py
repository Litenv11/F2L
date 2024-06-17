# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv("API_ID", 29256711))
    API_HASH = str(getenv('API_HASH', "e1e7f435524bc0c756783949cad78fcd"))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "6875581535:AAFIQnFPm2KnHVwsO1_-ebb4iPInTZfqE0c"))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1001750626831"))
    PORT = int(getenv('PORT', ))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "2010387571").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME' "mrx235"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', "file2lk-22f759a7eff4"))
   
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "http://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://leechbot:Jod7421@leechbot.23hzrrg.mongodb.net/?retryWrites=true&w=majority&appName=leechbot"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "Drxupdates"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
