import random

print("H A N G M A N")
decision = input('Type "play" to play the game, "exit"  to quit: ')
possible_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(possible_words)
hidden = "-" * len(word)
hidden = list(hidden)
lives = 8
used_letters = list()

while True:
    if decision == "play":
        while lives:
            print(f"\n{''.join(hidden)}")
            if not '-' in hidden:
                print("You guessed the word!")
                print("You survived!")
                break
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif not guess.isalpha():
                print("Please enter a lowercase English letter")
            elif guess in used_letters:
                print("You've already guessed this letter")
            elif not guess.islower():
                print("Please enter a lowercase English letter")
            elif guess in word:
                for j in range(len(word)):
                    if hidden[j] == '-':
                        if word[j] == guess:
                            hidden[j] = guess
            else:
                lives -= 1
                print("That letter doesn't appear in the word")
            used_letters.append(guess)
            if lives <= 0:
                print("You lost!")
        break
    elif decision == ("quit"):
        quit()
    else:
        print("")
        print('Type "play" to play the game, "exit"  to quit: ')