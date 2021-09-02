import json
from difflib import get_close_matches, SequenceMatcher

data = json.load(open("data.json"))
keys = data.keys()


def display(lst):
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]}")


def translate(the_key):
    if the_key.lower() in data:
        return display(data[the_key.lower()])
    elif len(get_close_matches(the_key.lower(), keys, n=1, cutoff=0.8)) > 0:
        # Todo: Other Solution:
        #  matched = SequenceMatcher(None, the_key,  m[0]).ratio()
        #  t = m[0]
        #  for i in m[1:]:
        #      if SequenceMatcher(None, the_key, i).ratio() > matched:
        #          t = i
        asw = input(f"Did you mean: {get_close_matches(the_key.lower(), keys, n=1, cutoff=0.8)[0]}? If yes Enter Y if "
                    f"no enter N: ")
        if asw.lower() == 'y':
            return display(data[get_close_matches(the_key.lower(), keys, n=1, cutoff=0.8)[0]])
        elif asw.lower() == 'n':
            w = input("Then Please double check it: ")
            print(translate(w))
        else:
            return "We didn't understand your entry."
    else:
        w = input("The word doesn't exist. Please double check it: ")
        print(translate(w))


word = input("Enter word: ")
translate(word)

