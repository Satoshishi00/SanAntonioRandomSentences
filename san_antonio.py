import random
import json


def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)

# Return a random item in a list
def get_random_item_in(my_list):
    rand_nb = random.randint(0, len(my_list)-1)
    item = my_list[rand_nb] # get a quote from a list
    return item # return the item

# Return a random value from a json file
def read_value_from_json(fileName, key):
    new_characters = []
    # Get data in file
    with open(fileName, "r") as file:
        characters_dico = json.load(file)
    # Add data in a list
    for item in characters_dico:
        new_characters.append(item[key])

    return new_characters

def get_random_character():
    all_characters = read_value_from_json("characters.json", "character")
    rand_character = get_random_item_in(all_characters)
    return rand_character

def get_random_quote():
    all_quotes = read_value_from_json("quotes.json", "quote")
    rand_quote = get_random_item_in(all_quotes)
    return rand_quote

# PROGRAM START
user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(get_random_character(), get_random_quote()))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')