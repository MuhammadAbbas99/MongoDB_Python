# python > JSON
# -----------
# dict  > Object (Javascript objekt)
# list > Array
# tuple > Array
# str > String
# int >  Number
# float > Number
# True > true   # HUOM
# None > null   # HUOM

import json
# DUMPS (dump python object to JSON string)
d = {       # python dictionary
    "name": "Donald Duck",
    "is_cartoon": True,
    "age": 120
    }

# konvertoidaan diktionary json:iksi
d_as_json = json.dumps(d, indent = 4, sort_keys = True)
        # Separators =
print(type(d))  # tulee python dict
print(type(d_as_json))  # tulee (json) string
print(d_as_json)

#----------------------
# tallennetaan json string json-tiedosotoon perinteeisesti file.write:illa

with open("aku.json", "w", encoding = "utf-8") as file:
    file.write(d_as_json)

# DUMP - voidaan tallentaa suoraan jso-tiedostoon-muodosta json:iksi tiedostoon
with open("aku2.json", "w", encoding = "utf-8") as file:
    json.dump(d, file, indent = 4)


