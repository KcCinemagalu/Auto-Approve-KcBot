from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "14356452"))
    API_HASH = getenv("API_HASH", "cac21249a0c6373a1b742afb8dbc9cb7")
    BOT_TOKEN = getenv("BOT_TOKEN", "6704921667:AAGKp6AJSmEcGUKiX4Jhg_2xlPO3YBHqGMc")
    FSUB = getenv("FSUB", "KC_Moviez")
    CHID = int(getenv("CHID", "-1002045732976"))
    SUDO = list(map(int, getenv("SUDO", "5720092781").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Nandesha:alabal18@cluster0.6qjsxnq.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
