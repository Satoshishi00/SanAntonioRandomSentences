import random
import json

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)


def get_random_item_in(my_list):
    rand_nb = random.randint(0, len(my_list)-1)
    item = my_list[rand_nb] # get a quote from a list
    return item # return the item

def read_value_from_json(fileName, key):
    new_characters = []

    with open(fileName, "r") as file:
        characters_dico = json.load(file)

    for item in characters_dico:
        new_characters.append(item[key])

    return new_characters

def get_random_character():
    all_characters = characters + read_value_from_json("characters.json", "character")
    rand_character = get_random_item_in(all_characters)
    return rand_character

def get_random_quote():
    all_quotes = quotes + read_value_from_json("quotes.json", "quote")
    rand_quote = get_random_item_in(all_quotes)
    return rand_quote

# Programm
user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(get_random_character(), get_random_quote()))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')