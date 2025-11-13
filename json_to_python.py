import json
from colorama import Fore, Style, init


# LOADS
json_string = '{"name": "Donald Duck",' \
'               "is_cartoon" : true}'
# LOAD parsii json-stingi (konvertoi pythoniksi)
d = json.loads(json_string)
print(Fore.GREEN + str(type(d)) + Style.RESET_ALL)
print(Fore.BLUE + str(d) + Style.RESET_ALL)


# LOAD (avataan json tyyppinen tiedosto ja konvertoidaan suoraan pythoniksi)
with open("aku.json", "r", encoding = "utf-8") as file:
    aku_dict = json.load(file)
    print(Fore.YELLOW + str(type(aku_dict)) + Style.RESET_ALL)
    print(Fore.RED + str(aku_dict) + Style.RESET_ALL)