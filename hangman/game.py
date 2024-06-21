from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException('List is empty!!')
    word = random.choice(list_of_words)
    return word


def _mask_word(word):
    if type(word) is not str or word == '':
        raise InvalidWordException('Invalid Word!')
    
    masked = '*' * len(word)
    
    return masked
        
    
def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException("""Words are empty""")
    if len(character) > 1:
        raise InvalidGuessedLetterException("""Character to guess has len() > 1""")
    if len(answer_word) != len(masked_word):
        raise InvalidWordException("""Length of words is different""")
        
    if character.lower() in answer_word.lower():
        answer_word_lower = answer_word.lower()
        character_lower = character.lower()
        letter_index = 0
        masked_list = list(masked_word)
        for letter in answer_word_lower:
            if letter == character_lower:
                masked_list[letter_index] = letter
            letter_index += 1
                
        masked_word = ''.join(masked_list)
        
    return masked_word


def guess_letter(game, letter):
    
    if '*' not in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException('The Game Has Already Ended!!!!!!!')
    
    if letter.lower() in game['answer_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'],letter)
        
    else:
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            game['masked_word'] = _mask_word(game['answer_word'])
                     
    game['previous_guesses'] += letter.lower()
    
    if game['remaining_misses'] == 0:
        raise GameLostException('You Lost') 
        
    if '*' not in game['masked_word']:
        raise GameWonException('You Won The Game!!!')
    
    return game


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess, #word
        'masked_word': masked_word, # *****
        'previous_guesses': [],
        'remaining_misses': number_of_guesses, # 5
    }

    return game
