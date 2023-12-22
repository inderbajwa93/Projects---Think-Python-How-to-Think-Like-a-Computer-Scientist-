import random
import string

fin = open('words.txt')
words = fin.readlines()
i = random.randint(0,len(words))
rand_word = words[i].strip().upper()
print(rand_word)

def hangman():
  word_letters = set(rand_word) #letters in randomly generated word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() #what the user has guessed

  #getting user input
  while len(word_letters) > 0:
    #letters used
    # ' '.join(['a','b','cd']) --> 'a,b,cd'
    print('You have used the following letters: ', ' '.join(used_letters))

    #what the current word is (ie W-RD)
    word_list = [letter if letter in used_letters else '-' for letter in rand_word]
    print('Current word: ', ' '.join(word_list))

    
    user_letter =  input('Guess a letter: | ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
  
    elif user_letter in used_letters:
      print('You have already used that character. Please try again')
  
    else:
      print('Invalid character')
  #gets here when len(word_letters) == 0
  print(f'Good job! your guessed the word {rand_word} correct!')

hangman()
    
