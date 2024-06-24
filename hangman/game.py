from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["less", "let", "letter",
"level", "lie", "life", "light", "like", "likely", "line", "list", "listen",
"little", "live", "local", "long", "look", "lose", "loss", "lot", "love", "low",
"machine", "magazine", "main", "maintain", "major", "majority", "make", "man",
"manage"]


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException("Gotta have words")
    else:
        return random.choice(list_of_words)


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException
    else:
        return "*" * len(word)

def find_positions(answer_word, character):
    answer_word = answer_word.lower()
    character = character.lower()
    return [p for p, char in enumerate(answer_word) if char == character]

def replace_char(masked_word, positions, character):
    character = character.lower()
    for i in positions:
        masked_word = masked_word[:i] + character + masked_word[(i + 1):]
    return masked_word

def _uncover_word(answer_word, masked_word, character):
    if (len(character) > 1) or (type(character) != str):
        raise InvalidGuessedLetterException("Please guess a single letter")
    elif (len(answer_word) != len(masked_word)) or (len(answer_word) == 0) or (len(masked_word) == 0):
        raise InvalidWordException("Something's not write with the words")
    else:
        pos = find_positions(answer_word, character)
        new_masked_word = replace_char(masked_word, pos, character)
        return new_masked_word



def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException("Game Over")

    ll = letter.lower()
    lanswer = game['answer_word'].lower()

    if letter not in game['previous_guesses']:
        game['previous_guesses'].append(ll)
    if ll in lanswer:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], ll)
    else:
        game['remaining_misses'] -= 1

    if game['answer_word'] == game['masked_word']:
        raise GameWonException("Game Won")

    if game['remaining_misses'] == 0:
        raise GameLostException("Game Lost")


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
