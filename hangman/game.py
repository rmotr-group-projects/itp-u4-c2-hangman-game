from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['book','view','quill','interrupt','macabre','marked','snakes','zephyr','behave','drum','blood','plucky']


def _get_random_word(list):
    if len(list) ==0:
        raise InvalidListOfWordsException('Cannot choose from an empty sequence')
    else:
        return random.choice(list) 


def _mask_word(word):
    if len(word)==0:
        raise InvalidWordException('Invalid word')
    else:
        rword = _get_random_word(word)
        masked_word = "".join(['*' for char in range(len(word))])
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word)  ==0 or len(masked_word)==0:
        raise InvalidWordException('Those words are invalid!')
    if len(answer_word) is not len(masked_word):
        raise InvalidWordException('Those words are invalid!')
    if len(character) > 1:
        raise InvalidGuessedLetterException('also wrong')
    answer_list = list(answer_word.lower())
    masked_list = list(masked_word)
    character_l = character.lower()
    for char in range(len(answer_list)):
        if answer_list[char] == character_l:
            masked_list[char] = character_l
        masked_answer = "".join(masked_list)
    return masked_answer


def guess_letter(game, letter):
    letter = letter.lower()
    if game['remaining_misses'] == 0 or game['masked_word'] == game['answer_word']:
        raise GameFinishedException("You LOSE!")
    updated_word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['masked_word'] = updated_word
    game['previous_guesses'].append(letter)
    if letter not in game['masked_word']:
        game['remaining_misses'] -=1
    if game['masked_word'] == game['answer_word']:
        raise GameWonException("You won!")
    if game['remaining_misses'] == 0:
        raise GameLostException("You LOSE!")
    return game

    



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
