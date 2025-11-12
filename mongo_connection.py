# winget install --id-astral-sh.uv -e
# python -m pip install uv pymongo
# uv init
# uv add pymongo["srv"]

# dotenv-moduulu asennus
# uv add dotenv     tai     # python -m pip install dotenv

from pymongo import MongoClient
from dotenv import load_dotenv   
import os

mongo_url = "mongodb+srv://jouluupuukki:7991949Hash@cluster0.rkzrote.mongodb.net/?appName=Cluster0"

        # hakee ympäristömmuuttujista jos ei asetettu  (tai override = False)
load_dotenv (override = True)    # oletuksesena False jos ei aseta
        # pakotetaan hakemaan .env -tiedostosta

print(os.name +"\n")
      
def connect():
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        client.admin.command("ping")
        print("Connected to MongoDB\n")
        return client
    except:
        raise ConnectionError("it cannot connect whatseover")
    
if __name__ == "__main__":
    connect()