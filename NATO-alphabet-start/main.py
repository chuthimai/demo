import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
charecter = {row.letter: row.code for(index, row) in data.iterrows()}


def process():
    string = input("Enter a word: ").upper()
    try:
        result = [charecter[char] for char in string]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        process()
    else:
        print(result)


process()
