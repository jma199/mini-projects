import random
import string
from words import words

# skip words with spaces or dashes

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # track letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # keep track of letters guessed
        print(f"\nYou have {lives} lives left.\n"
        "You have used these letters: ", ' '.join(used_letters))

        # print correct letters guessed in target word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # get user input
        guessed_letter = input("\nGuess a letter: ").upper()
       
        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                #print('')
            
            else:
                lives = lives - 1 # take away a life
                print('\nYour letter is not in the word.')

        elif guessed_letter in used_letters:
            print('\nYou have already used that letter. Guess again.')

        else:
            print('\nInvalid letter. Guess again.')
    
    # when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("\nSorry, you've run out of lives, sorry. The word was", word)
    else:
        print("\nHooray! You figured out the word", word, "!!")

if __name__ == '__main__':
    hangman()