import mongo_connection
import pandas as pd
import csv      # csv.QUOTE_ALL, QUOTE-NONE jne.

conn = mongo_connection.connect()
db = conn["world_cities_DB"]
# coll = db["cities_collections"]

# haetaan kaikki collectiontietueet
all_records = db["cities_collection"].find()

# luodaan pandas DataFrame suoraan kursorista
df = pd.DataFrame(all_records)

# poistetaan _id-kenta
df.pop("_id")   # huom. df.pop palauttaa arvon, eli sen voi sijoittaa muuttujaan

# kirjoitetaann Dataframen sisältö
df.to_csv("kaupungit_mongosta.csv", ",", index = False, quoting = csv.QUOTE_ALL)
