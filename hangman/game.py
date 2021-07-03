import random
from .exceptions import *


# Complete with your own, just for fun :)
LIST_OF_WORDS = ["REI", "adams", "glacier", "ice", "cold", "snow", "crampons"]

#passing
def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException
    last_index = len(list_of_words) - 1
    index = random.randint(0, last_index)
    return list_of_words[index]


#passing
def _mask_word(word):
    if word == "":
        raise InvalidWordException
    multiple = len(word)
    masked_word = "*" * multiple
    return masked_word

#passing
def _uncover_word(answer_word, masked_word, character):
    result = ""
    if answer_word == "" and masked_word == "":
        raise InvalidWordException
    elif len(character) > 1:
        raise InvalidGuessedLetterException
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException
    for idx,letter in enumerate(answer_word):
        if masked_word[idx].lower() == "*":
            if letter.lower() == character.lower():
                result += letter.lower()
            else:
                result += "*"
        else:
            result += masked_word[idx].lower()
    return result
        

def guess_letter(game, letter):
    found_letter = False
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException
    elif game['remaining_misses'] == 0:
        raise GameFinishedException
    elif letter in game['previous_guesses']:
        return game
    else:
        game['previous_guesses'] += letter.lower()

    for character in game['answer_word']:
        if letter.lower() == character.lower():
            found_letter = True
            masked_word = _uncover_word(game['answer_word'],game['masked_word'], letter)
            game['masked_word'] = masked_word
            if game['answer_word'] == game['masked_word']:
                raise GameWonException
    if found_letter == False:
    
        game['remaining_misses'] += -1
        if game['remaining_misses'] == 0:
                raise GameLostException
    return game

#passing
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
