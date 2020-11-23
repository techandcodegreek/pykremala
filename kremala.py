import random

with open('words.txt', encoding='utf-8') as f:
    word = random.choice(f.readlines()).rstrip()

tries = 6
letters = []

def hide():
    hidden = ''
    for letter in word:
        if letter in letters:
            hidden += letter
        else:
            hidden += '-'
    return hidden

# print(word)

while tries > 0:
    hidden_word = hide()
    print(hidden_word)
    if hidden_word == word:
        print("Συγχαρηρήρια κερδίσατε!")
        exit()
    
    letter = input("Γράμμα: ").upper()
    if letter == 'Q':
        print("Ευχαριστώ που παίξατε!")
        exit()
    if letter == 'H':
        print("""
              Αυτό ειναι ένα παιχνίδι κρεμάλας.
              """)
        continue
    
    if letter in letters:
        print("Έχετε ήδη δοκιμάσει αυτό το γράμμα")
        continue
        
    letters.append(letter)
    if letter in word:
        print("Το γράμμα υπάρχει!")
    else:
        print("Το γράμμα δεν υπάρχει.")
        tries -= 1
    print(f"Απομένουν {tries} προσπάθειες")
    
print("Χάσατε!")
print(f"Η λέξη ήταν: {word}")

## This is an example change