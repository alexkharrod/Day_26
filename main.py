import pandas as pd
alphabet_name = []
df = pd.read_csv('nato_phonetic_alphabet.csv')

new_dict = {row.letter:row.code for (index, row) in df.iterrows()}


name = input("Enter a name: ").upper()
word = [new_dict[letter] for letter  in name]



print(word)
