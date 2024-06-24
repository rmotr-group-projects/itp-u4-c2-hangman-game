from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if len(list_of_words) > 0:
        return random.choice(list_of_words)
    else:
        raise InvalidListOfWordsException


def _mask_word(word):
    if len(word) > 0:
        return '*' * len(word)
    else:
        raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) > 0 and len(masked_word) > 0 and len(answer_word) == len(masked_word):
        if len(character) == 1:
            masked_word_as_list = list(masked_word)
            new_state_masked_word = ''
            if character.lower() in answer_word.lower():
                char_positions = []
                for index, char in enumerate(answer_word):
                    if char.lower() == character.lower():
                        char_positions.append(index)
                for pos in char_positions:
                    masked_word_as_list[pos] = character.lower()
                new_state_masked_word = ''.join(masked_word_as_list)
                return new_state_masked_word
            else:
                return masked_word
        else:
            raise InvalidGuessedLetterException
    else:
        raise InvalidWordException


def guess_letter(game, letter):
    if game["remaining_misses"] == 0 or game["answer_word"] == game["masked_word"]:
        raise GameFinishedException
    guess = _uncover_word(game['answer_word'], game['masked_word'], letter)
    if guess == game['masked_word']:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = guess
    game['previous_guesses'].append(letter.lower())
    if guess == game['answer_word']:
        raise GameWonException
    if game['remaining_misses'] == 0:
        raise GameLostException
    return guess
    

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
