import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

#for (index, row) in alphabet.iterrows():
#    alphabet_dict.update({row.letter: row.code})
cont = True
while cont:
    txt = input("Insert Your word: ").upper()
    #Hello
    #['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
    try:
        word_list = [alphabet_dict[character] for character in txt]
    except KeyError:
        print("Sorry, only english letters in the alphabet please")
    else:
        cont = False






print(word_list)
