import random

words = ['python', 'java', 'kotlin', 'javascript']
word = list(random.choice(words))
tries = 8
guesses = []
know = set()
word_set = set(word)
print('H A N G M A N')
while tries > 0:
    print()
    for letter in word:
        if letter in guesses:
            print(letter, end="")
            know.add(letter)
        else:
            print("-", end="")
    print("")
    if word_set == know:
        print("""You guessed the word!\nYou survived!\n""")
        break
    guess = input('Input a letter:')

    if (len(guess) > 1):
        print("You should input a single letter")
    # if guess.isalpha() == 0:

    elif not guess.islower() or (guess.isalpha() == 0):  # check if lowercase is true
        print("Please enter a lowercase English letter")

    elif guess in guesses:
        print("You've already guessed this letter")

    elif guess not in word:
        print("That letter doesn't appear in the word")
        tries -= 1

    guesses.append(guess)
    if word_set == know:
        print("""You guessed the word!\n
        You survived!\n""")
if tries == 0:
    print("You lost!")