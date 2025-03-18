import os
import random
from words import *

# --- Function definitions

# --- displays the available and used letters
def display_letters():
	print("Available Letters:")
	print("------------------")
	letters.sort()
	print(" ".join(letters))
	print()
	print("Used Letters:")
	print("------------------")
	used_letters.sort()
	print(" ".join(used_letters))
	print()

# --- displays the hangman
def display_hangman(wrong):
	if wrong == 1:
		show_head = "|  ( )"
		show_neck = blank
		show_arms = blank
		show_legs = blank
	elif	wrong == 2:
		show_head = "|  ( )"
		show_neck = "|  - -"
		show_arms = blank
		show_legs = blank
	elif wrong == 3:
		show_head = "|  ( )"
		show_neck = "|  - -"
		show_arms = "|   |"
		show_legs = blank
	elif wrong == 4:
		show_head = "|  ( )"
		show_neck = "|  - -"
		show_arms = "|   |"
		show_legs = "|  /  "
	elif wrong == 5:
		show_head = "|  ( )"
		show_neck = "|  - -"
		show_arms = "|   |"
		show_legs = "|  / \\"
		eog = True
	else:
		show_head = blank
		show_neck = blank
		show_arms = blank
		show_legs = blank

	if wrong < 5:
		print("+---+")
		print(show_head)
		print(show_neck)
		print(show_arms)
		print(show_legs)
		print("|")
		print("+-------+")
		print("|Hangman|")
		print("+-------+")
	
# --- displays the hung man when user loses
def display_lost():
	print("+---+")
	print("|   |")
	print("|  ( )")
	print("|  - -")
	print("|   |")
	print("|  / \\")
	print("+-     -+")
	print("|H\\   /n|")
	print("+-------+")
	print()
	
# --- displays the escaped man when user wins		
def display_escaped():
	print("+---+")
	print("|   |")
	print("|")
	print("|")
	print("|")
	print("|           ( )")
	print("+-------+   - -")
	print("|Hangman|    |")
	print("+-------+   / \\")
	print()

# --- gets the word and displays the number of letters
def get_word(word):
	for x in word:
		word_2_guess.append(x)
		word_2_display.append("-")
		
# --- updates the displayed word with the correctly guessed letter 	
def check_word(letter):
	y = 0
	for x in word_2_guess:
		if letter == x:
			word_2_display[y] = letter
		else:
			if word_2_display[y] != "-":
				t = 0
			else:
				word_2_display[y] = "-"
		y += 1
	return word_2_display

# --- Initiates variables
wrong = 0
eog = False
win = 0
blank = "|"
show_arms = blank
show_neck = blank
show_arms = blank
show_legs = blank

# --- Sets up the lists of letters to choose and used
used_letters = []
word_2_guess = []
word_2_display = []

# --- Asks who is playing
os.system('cls' if os.name=='nt' else 'clear')
print("Let's play a game of Hangman. Who will be playing?")
print()
player = int(input("Enter - 1 - for Ellianna. Enter - 2 - for Ethan.  "))
# --- Gets the word to choose
if player == 1:
	word = random.choice(ellianna_words)
else:
	word = random.choice(ethan_words)
word_display = get_word(word)

# --- Displays the available and used letters 
while eog != True and wrong < 5:
	os.system('cls' if os.name=='nt' else 'clear')
	display_letters()
	display_hangman(wrong)
	print()	
	print("Your word is ...")
	print()
	print(" ".join(word_2_display))
	print()
		
# --- Asks the user for a letter and will move that letter from Available letters to Used letters
	guess = input("Please select one of the available letters:  ")
	cap_guess = guess.capitalize()
	while cap_guess in used_letters:
		guess = input("Sorry, that letter has already been guessed. Please guess another letter:  ")
		cap_guess = guess.capitalize()
	used_letters.append(cap_guess)
	letters.remove(cap_guess)
	if cap_guess not in word_2_guess:
		wrong += 1
	else:
		word_2_display = check_word(cap_guess)
	if word_2_guess == word_2_display and wrong < 5:
		eog = True
		win = True
		os.system('cls' if os.name=='nt' else 'clear')		
		display_escaped()
		print("Congratulations!! You guessed the word ", word, "in time! He has been saved!")
	else:
		eog = False

if win == False:
	os.system('cls' if os.name=='nt' else 'clear')
	display_lost()
	print("Sorry! You didn't get it in time and he died!")
	print("The word was... ", word)