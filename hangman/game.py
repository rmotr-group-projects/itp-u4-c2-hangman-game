from .exceptions import *
from random import choice

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    word=choice(list_of_words)
    return word


def _mask_word(word):
    if not word:
        raise InvalidWordException
    l=len(word)
    return l*"*"


def _uncover_word(answer_word, masked_word, character):
    if not answer_word:
        raise InvalidWordException
    if not masked_word:
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    char1=character.lower()
    answer_word1=answer_word.lower()
    if char1 not in answer_word1:
        return masked_word 
    count1=answer_word1.count(char1)
    answer_list=list(answer_word1)
    masked_list=list(masked_word)
    for i in range(len(answer_list)):
        itr=0
        if answer_list[i] == char1 and itr < count1:
            masked_list[i] = char1
        itr+=1
    masked_answer="".join(masked_list)
    return masked_answer
     


def guess_letter(game, letter):
    if game['remaining_misses'] == 0 or '*' not in game['masked_word']:
        raise GameFinishedException
    masked_answer=_uncover_word(game['answer_word'], game['masked_word'], letter)
    if masked_answer == game['masked_word']:
        game['remaining_misses']-=1
        if game['remaining_misses'] == 0:
            raise GameLostException
    game['previous_guesses'].append(letter.lower())
    game['masked_word'] = masked_answer
    if game['masked_word'] == game['answer_word']:
        raise GameWonException

        


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
