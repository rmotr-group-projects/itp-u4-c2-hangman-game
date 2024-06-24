from .exceptions import *
from random import choice
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    random_word = choice(list_of_words)
    return random_word


def _mask_word(word):
    masked_word = ""
    if not word:
        raise InvalidWordException
    for char in word:
        masked_word += "*"
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
    character = character.lower()
    answer_word = answer_word.lower()
    
    idx_list = []
    final_word = ""
    for idx, char in enumerate(answer_word):
        if char == character:
            idx_list.append(idx)
    
    if character not in answer_word:
        return masked_word
    else:
        for idx2, char2, in enumerate(masked_word):
            if char2 != "*":
                final_word += char2
            elif idx2 in idx_list:
                final_word += character
            else:
                final_word += "*"
        return final_word
        

def guess_letter(game, letter):
    letter = letter.lower()
    if "*" not in game["masked_word"] or game["remaining_misses"] == 0:
        raise GameFinishedException
    if letter in game["answer_word"].lower():
        game["masked_word"] = _uncover_word(game["answer_word"], game["masked_word"], letter)
        game["previous_guesses"].append(letter)
        if "*" not in game["masked_word"]:
            raise GameWonException
    else:
        game["previous_guesses"].append(letter)
        game["remaining_misses"] -= 1
        if game["remaining_misses"] == 0:
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
