meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            }

for i in range(5):
  klucz = input("Podaj słowo").upper()
  znaczenie = input("Podaj znaczenie słowa")
  meme_dict[klucz] = znaczenie

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Brak słowa")
