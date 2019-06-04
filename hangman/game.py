from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['python', 'hello', 'goodbye']


def _get_random_word(list_of_words):
    if list_of_words == []:
      raise InvalidListOfWordsException
    return random.choice(list_of_words) # returned a random word form list


def _mask_word(word):
    masked_word = ""
    for char in word:
      masked_word += "*"
    if word == "":
      raise InvalidWordException
    return masked_word

      
def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
      raise InvalidWordException
      
    if len(character) > 1:
      raise InvalidGuessedLetterException
      
    if len(answer_word) != len(masked_word):
      raise InvalidWordException
      
        
    results=''
    
    for index, letter in enumerate(answer_word):
        if character.lower() ==letter.lower():
            results+=answer_word[index].lower()
        else:
            results+=masked_word[index].lower()        
    return results
  
  


def guess_letter(game, letter):
    if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
      raise GameFinishedException()
    
    
    if letter.lower() in game['answer_word'].lower():
      game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'], letter)
      game['previous_guesses'].append(letter.lower())
      
    else:
      game['previous_guesses'].append(letter.lower())
      game['remaining_misses'] -= 1   
    
    
    if game['answer_word'] == game['masked_word']:
      raise GameWonException()

    if game['remaining_misses'] == 0:
        raise GameLostException()


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
