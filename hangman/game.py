from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['carbonero', 'manya']

import random
def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException
        
    word = random.choice(list_of_words)
    return word


def _mask_word(word):
    masked = []
    if word == '':
        raise InvalidWordException
    for char in word:
        masked.append('*')
    return(''.join(masked))


def _uncover_word(answer_word, masked_word, character):
    #character = input('Enter a character: ')
    guessed_pos = []
    if answer_word == "":
        raise InvalidWordException
    if len(character) != 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    for pos, char in enumerate(answer_word):
        
        if char.lower() == character.lower():
            guessed_pos.append(pos)
            masked_word = masked_word[:pos] + character.lower() + masked_word[pos + 1:]
    return masked_word



def guess_letter(game, letter):
    letter = letter.lower()
     
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
    
    try:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter)
        if letter.lower() not in game['answer_word'].lower():
            game['remaining_misses'] -= 1
    except Exception as e:
        raise e
    if game['answer_word'] == game['masked_word']:
        raise GameWonException
    if game['remaining_misses']  == 0:
        raise GameLostException
        
    
    
    
        
        
    
        

  


  #  while number_of_guesses > 1:
  #      if letter != word:
  #          number_of_guesses -= 1
  #      elif letter == word:
  #          return('the game is won')
  #      else:
  #          return('the game is lost')

    






def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
