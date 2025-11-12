import mongo_connection
'''
def main():
    # pass
    # print("Hello world from Mongo Python!")
    conn = mongo_connection.connect()
    
if __name__ == "__main__": 
    main()
    '''
conn = mongo_connection.connect()
    
    # tulostetaan kaikki tietokantojen nimet
# print(conn.list_database_names())

    # valitaan tietokanta, johon halutaan yhteys ja asetetaan se muuttujaan
db = conn["python-data-DB"]

   # tulostetaan kaikki databasen collectionit
print(db.list_collection_names())
