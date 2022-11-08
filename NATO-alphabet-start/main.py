import pandas as pd
#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
charecter = { row.letter:row.code for(index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
string = input("Enter a word: ").upper()
result = [charecter[char] for char in string]
print(result)