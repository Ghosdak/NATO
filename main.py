import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

df_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(df_dict)
def generate_phonetic():
    
    word = input("Enter a word: ").upper()
    try:
        result = [df_dict[n] for n in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)
        
generate_phonetic()