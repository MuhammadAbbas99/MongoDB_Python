import json
from colorama import Fore, Style

class Character:
    def __init__(self, name, isCartoon, age):
        self.name = name
        self.isCartoon = isCartoon
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")

    def __repr__(self):
        return f"Person (name = {self.name}, age= {self.age})"
    
aku = Character("Donald", True, 120)
aku.walk()
iines = Character("Daisy", True, 25)

print(Fore.BLUE + str(aku) + Style.RESET_ALL)
print(Fore.MAGENTA + str(iines) + Style.RESET_ALL)  
print(Fore.LIGHTMAGENTA_EX + "Daisy's age is " + str(iines.age) + Style.RESET_ALL)  
print(Fore.YELLOW + "Donald's current age is " + str(aku.age) + Style.RESET_ALL)

aku.age = 150
print(Fore.RED + "Donald's updated age is " + str(aku.age) + Style.RESET_ALL)

json_string = '{"name": "Aku", "isCartoon": true, "age": 120}'

d = json.loads(json_string)
    # konvertoidaanjson stringi pythoniksi

# luodaan Character luokasta olio, käyttäen 'dictionary unpacking'
aku = Character(**d)
