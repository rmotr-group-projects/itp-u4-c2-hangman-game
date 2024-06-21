from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return list_of_words[randint(0,len(list_of_words)-1)]


def _mask_word(word):
    if not word:
        raise InvalidWordException
    masked_word = '*'*len(word)
    return masked_word
        

def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) != 1:
        raise InvalidGuessedLetterException
    masked_list = list(masked_word)
    for i in range(len(answer_word)):
        if answer_word[i].lower() == character.lower():
            masked_list[i] = character.lower()
    return ''.join(masked_list)
            


def guess_letter(game, letter):    
    ans = game['answer_word']
    m_ans = game['masked_word']
    if ans.lower() == game['masked_word'].lower() or game['remaining_misses'] == 0:
        raise GameFinishedException
    if letter.lower() in ans.lower():
        game['masked_word'] = _uncover_word(ans,m_ans,letter)    
    else:
        game['remaining_misses'] -= 1
    
    game['previous_guesses'].append(letter.lower())
    if ans.lower() == game['masked_word'].lower():
        raise GameWonException
    elif game['remaining_misses'] == 0:
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
