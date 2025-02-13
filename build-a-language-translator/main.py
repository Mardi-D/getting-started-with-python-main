translations = {
  "hello":        "hola",
  "thank you":    "gracias",
  "sorry":        "lo siento",
  "I'm hungry":   "yo tengo hambre",
  "I love you":   "te amo mucho"
}

done = False

print('Type "done" at any time to exit')

while not done:
    word = input('Please type an English word to translate to Spanish: ').lower()

    if word == 'done':
        done = True
    elif word in translations:
        print(translations[word])
    else: 
        print(f'{word} is not in the translations dictionary. Please try a different word.')
        


