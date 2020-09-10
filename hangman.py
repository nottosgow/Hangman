import random
import time

print("\nWelcome to Hangman: The Best Game for kids with Dead People!!\n")
name = input("Enter your name: ")
print(f"Hello {name}! Good Luck!\n")
time.sleep(2)

words_to_guess = ["Coherence", "Good Time", "What We Do in the Shadows",
            "Memento", "Us", "The Lighthouse", "Primer", "Donnie Darko",
            "OldBoy", "Sicario", "Taxi Driver"]

def newDisp(word, disp, guess):
	for i in range(len(word)):
		if word[i].lower() == guess.lower():
			disp[i] = guess
	return disp

def show(disp):
    for i in disp:
        print(i, end='')

def assign(word):
    disp = []
    for i in word.lower():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == ' ': 
        	disp.append(i)
        else: disp.append('-')
    return disp

def main():

    global count
    global disp
    global word
    global already_guessed
    global length
    global play_game
    
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    disp = []
    disp = assign(word)
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want to play? (y/n)\n")
    while play_game not in ["n", "N", 'y', "Y"]:
        play_game = input("Enter correctly please")
    if play_game == 'y':
        main()
        hangman()
    elif play_game == 'n':
        print("Thanks for playing! Please come back sometime!\n")
        exit()

def hangman():
    global count
    global disp
    global word 
    global already_guessed
    global play_game

    limit = 5
    print(f"This is your Hangman Word, {name}: ", end='');
    show(disp)
    guess = input("\n\nEnter your guess:\n")
    guess = guess.strip()
    guess = guess.lower()
    time.sleep(1)

    for i in disp:
    	if i.isalpha():
    		already_guessed.append(i)

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in already_guessed:
        print("You already guessed this, dummy. Try another\n")

    elif guess in word.lower():
        print("Correct Guess!!!\n")
        already_guessed.extend([guess])
        disp = newDisp(word, disp, guess)
        #show(disp)
        print()

    else:
        already_guessed.extend([guess])
        count += 1

        if count == 1:
            print("    ------  \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  " __|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining")

        elif count == 2:
            print("    ------  \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |        \n"
                  "   |        \n"
                  "   |        \n"
                  " __|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")

        elif count == 3:
            print("    ------  \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      O \n"
                  "   |        \n"
                  "   |        \n"
                  " __|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")
        
        elif count == 4:
            print("    ------  \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      O \n"
                  "   |     /|\\\n"
                  "   |        \n"
                  " __|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")

        elif count == 5:
            print("    ------  \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      | \n"
                  "   |      O \n"
                  "   |     /|\\\n"
                  "   |     / \\\n"
                  " __|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining.\n")

    if disp.count('-') == 0: 
        print("Congrats! You have won and saved this poor, innocent man!\n\n\n")
        play_loop()
    elif count != limit:
        hangman()
    elif count == limit:
        print(f"Aww shucks, {name}! You're just a Loser.. :((\n\n")
        play_loop()


main()

hangman()
