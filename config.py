from os import path, getenv

class config:
    API_ID = int(getenv("", ""))
    API_HASH = getenv(":", "")
    BOT_TOKEN = getenv("8889285131:", "")
    IP_API =getenv("","")
    
con = config()
