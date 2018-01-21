import json
import random

random.seed()
with open('json/cards.json', 'r') as f:
    cards = json.load(f)

dict_names = {}
list_name_lengths = []
dict_descriptions = {}
list_description_lengths = []
card_count = len(cards)
first_words = []
first_letters = []

# building corpus out of json
for _, card in cards.items():
    for k, v in card.items():
        if k == "NAME":

            list_name_lengths.append(len(v.split()))
            first_letters.append((v[0], v[1]))

            for i, c1 in enumerate(v[:-2]):
                c2 = v[i+1]
                t = v[i+2]
                if (c1, c2) in dict_names:
                    dict_names[(c1, c2)].append(t)
                else:
                    dict_names[(c1, c2)] = [t]

        elif k == "DESCRIPTION":

            list_description_lengths.append(len(v.split()))
            if len(v.split()) > 1:
                first_words.append((v.split()[0], v.split()[1]))

            for i, word1 in enumerate(v.split()[:-2]):
                word2 = v.split()[i+1]
                target = v.split()[i+2]
                if (word1, word2) in dict_descriptions:
                    dict_descriptions[(word1, word2)].append(target)
                else:
                    dict_descriptions[(word1, word2)] = [target]

# use corpus to generate card
descriptions = []
names = []
for _ in range(100):

    key = random.choice(first_words)
    new_card = [key[0], key[1]]
    while True:

        w = random.choice(list(dict_descriptions[key]))
        new_card.append(w)
        key = (key[1], w)
        if key not in dict_descriptions or (w[-1][-1]=="." and random.randint(0,100) < 75):
            break

    description = " ".join(new_card)
    descriptions.append(description)

    key_letter = random.choice(first_letters)
    new_card_name = [key_letter[0], key_letter[1]]
    while True:

        l = random.choice(list(dict_names[key_letter]))
        new_card_name.append(l)
        key_letter = (key_letter[1], l)
        if key_letter not in dict_names or len("".join(new_card_name).split()) > random.randint(0, 5):
            break

    name = "".join(new_card_name)
    names.append(name)
    print(name+"\n", description.replace(" NL ", "\n"))
    print()

input("Press Enter to close")

