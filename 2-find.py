# python -m pip install colorma
import mongo_connection
from colorama import Fore, Style, init

from pprint import pprint       # uv add pprint     # pretty print

conn = mongo_connection.connect()


db = conn["sample_mflix"]

    # valitaaan tietokantaan collection
coll = db["movies"]


### ===== find vastaa SQL.n SELECT.iä ===== ###
# haetaan kaikki data movies-collection:ista

documents =  coll.find()    # hakee kaikki, palautta cursorin         # SELECT * FROM movies

for doc in documents:       # huo: kursorin sisältö tyhjenee tässä täysin
   print(doc)
#   pass


# haetaan kaikki, jossa year on 1985

documents = coll.find( {"year":1916} )

for doc in documents:
    pprint(doc)

    #haetaan ensimmäinen dokumentti, jossa vusoi on 1986


documents = coll.find_one( {"year":1986} )
pprint(documents["title"])  # tulosta vain titlen
pprint(documents["writers"])


documents = coll.find_one()
pprint(documents)


    # halutaan tietää, montako dokumenttia kannassa on
count = coll.count_documents({})    # parametriksi objekti, eli {} täytty aina laittaa
print(Fore.GREEN + f"Löytyi {count} dokumenttia\n"+ Style.RESET_ALL)


    # halutaan titää kuinka monta dokumnettia on, jossa yea on 1986
count = coll.count_documents({"year":1986})    # parametriksi objekti, eli {} täytty aina laittaa
print(Fore.RED + f"Löytyi {count} määrä dokumenttia vuodelta 1986\n"+ Style.RESET_ALL)


    # halutaan titää kuinka monta dokumnettia on, jossa yea on 1986 ja runtim > 60
count = coll.count_documents(
                            {"year":1986,
                            "runtime": {"$gt":60}}
                            )

print(Fore.BLUE + f"vuodelta 1986 Löytyi {count} määrä dokumenttia jotka ovat yli tunnin pituisia\n"+ Style.RESET_ALL)



# Harjoitus 1: hae dokumenttien määrä, jossa genereä on ainakin "Comdey"
# toisinsanoeo, montako elokuvaa, jotka ovat luokiettlu komediksi

count = coll.count_documents({"genres":
                            "Comedy"} )
print(Fore.GREEN + f"Löytyi {count} dokumenttia\n"+ Style.RESET_ALL)


count = coll.count_documents({"genres": "Comedy"})
