import json, random
adjectives = json.load(open('adjectives.json'))

def AdjectiveAcrostic(string):
    choices = []
    for letter in string.upper():
        if letter.isalpha():
            for word in adjectives:
                if word.startswith(letter): choices.append(word)
            print(f"{letter.upper()} - {(random.choice(choices))}")
            choices.clear()
        else: print()
    
while True:
    string = input("Enter word: ")
    for x in range(50):print('-',end="")
    print()
    AdjectiveAcrostic(string)
    for x in range(50):print('-',end="")
    print()
