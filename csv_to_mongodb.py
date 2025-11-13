#region asennusohjeet 
# # winget install --id-astral-sh.uv -e
# python -m pip install uv pymongo
# uv init
# uv add pymongo["srv"]

# dotenv-moduulu asennus
# uv add dotenv     tai     # python -m pip install dotenv
#endregion

from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv(override = True)

client = MongoClient(os.getenv("MONGO_URI"))

# Luetaan CSV-Tiedosto Pandasin Dataframeksi
df = pd.read_csv("worldcities.csv")

# Muutetaan Dataframe Pythonin
# Koska insert-many hyväksyy parametriksi diktionaryn (konvertoi  dict>json)
data_dict = df.to_dict(orient = "records")

#region orient esimerkit
# orient on oletuksena (jos sitä ei aseta) dict
# muita vaihtoehtoja list, series, spliot, records,
# esim,- dict:
    # {"name": {0:"Alice", 1:"Bob"},
    # "age": [25, 40]
    # }

# esim, list:
    # {"name": ["Alice", "Bob"],
    # "age": [25, 40]
    # }

# esim, series:
    # {"name": pad.series(["Alice", "Bob"], index = [0, 1]),
    # "age": pd.series([25, 40], index = [0, 1])
    # }

# esim. records: jokaisesta rivista tulee dictionary, tämä on hyvä mongon
  # insert lauseille koska ne hyväksyvät dictionaryn parametriksi
    # [
    # {"name": "Alice", "age": 25},
    # {"name: "Bob", , "age": 40}
    # ]
#endregion

# luodaan uusi tietokanta (käyttävä olemassa jos löytyy)
db = client["world_cities_DB"]

# luodaan collection (tai käytetään jos on olemassa)
#coll = db["cities_collection"]

# voidaan suoraan käytään myös:
db.cities_collection.insert_many(data_dict)


coll = db["anoher_cities_collection"]
# jos iso CSV, striimataan data paloina mongoon: (tosin hitaampi)
for chunk in pd.read_csv("world_cities.csv", chunksize = 1000):
    coll.insert_many(chunk.to_dict(orient = "records"))