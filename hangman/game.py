from .exceptions import *
from random import choice
import string
# Complete with your own, just for fun :)
LIST_OF_WORDS = ["hurry","and","give","my","jac","back","so","wryn","has","someone","fun","to","smack"]


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException("You've supplied an empty word list.")
    return choice(list_of_words)


def _mask_word(word):
    if word == '':
        raise InvalidWordException("You haven't entered a word.")
    return "*" * len(word)


def _uncover_word(answer_word, masked_word, character):
    if answer_word == '' or masked_word == '':
        raise InvalidWordException("Please supply a word.")
    if character.lower() not in string.ascii_lowercase:
        return InvalidWordException("Please supply a letter between A and Z.")
    if len(character) > 1:
        raise InvalidGuessedLetterException("Please only guess one letter at a time.")
    if len(answer_word) != len(masked_word):
        raise InvalidWordException("Answer word and Masked word lengths not matching.")
    answer_word = answer_word.lower()
    character = character.lower()
    if character not in answer_word:
        return masked_word
    else:
        new_masked_word = ""

        for index in range(0, len(masked_word)):
            if masked_word[index] != "*":
                new_masked_word += masked_word[index]
            elif answer_word[index] == character:
                new_masked_word += character
            else:
                new_masked_word += "*"

        return new_masked_word


def guess_letter(game, letter):
    if game["remaining_misses"] <= 0 or game["answer_word"] == game["masked_word"]:
        raise GameFinishedException()

    new_masked_word = _uncover_word(game["answer_word"], game["masked_word"], letter)
    game["previous_guesses"].append(letter.lower())
    if new_masked_word == game["masked_word"]:
        game["remaining_misses"] -= 1
        if game["remaining_misses"] <= 0:
            raise GameLostException()

    elif new_masked_word == game["answer_word"]:
        game["masked_word"] = new_masked_word
        raise GameWonException()

    else:
        game["masked_word"] = new_masked_word






def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses

    }

    return game
