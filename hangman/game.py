from .exceptions import *
from  random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['What', 'Python', 'Php', 'Computer', 'Pringle', 'Turner', 'Penguins']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException
    random_word = randint(0, len(list_of_words)-1)
    answer_word = list_of_words[random_word]

    return answer_word


def _mask_word(word):
    masked_word = ''
    if word == '':
        raise InvalidWordException
    for i in range(len(word)):
        masked_word += '*'
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if answer_word == '' or masked_word == '':
        raise InvalidWordException
    uncover_word = ''
    for i in answer_word:
        if i.lower() == character.lower():
            uncover_word += character.lower()
        elif i.lower() in masked_word:
            uncover_word += i.lower()
        else:
            uncover_word += '*'
    return uncover_word
        


def guess_letter(game, letter):##holding the value, im reassigning it each time. need to update the masked word each time?
    letter1 = letter.lower()
    
    if game['remaining_misses'] == 0:
        raise GameFinishedException

    if game['answer_word'].lower() == game['masked_word']:
        raise GameFinishedException
        
    if letter not in game['previous_guesses']:
        game['previous_guesses'].append(letter1)
    uncover_word = ''   
    for i in game['answer_word'].lower():
        if i not in game['masked_word']:
            if i.lower() == letter1:
                uncover_word += letter1
            else:
                uncover_word += "*"
        else:
            uncover_word += i
    game['masked_word'] = uncover_word
    miss_list = []
    for i in game['answer_word']:
        miss_list.append(i.lower())
    if letter1 not in miss_list:
        game['remaining_misses'] -= 1
    
    if game['answer_word'] == game['masked_word']:
        raise GameWonException
        
    if game['remaining_misses'] == 0:
        raise GameLostException
    
    
            
 


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
