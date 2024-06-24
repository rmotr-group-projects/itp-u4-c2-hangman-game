from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    # Exception check
    if not list_of_words:
        raise InvalidListOfWordsException()

    # Using a random integer as an indexer to select a word
    rand_indexer = random.randint(0, (len(list_of_words) - 1))
    return list_of_words[rand_indexer]


def _mask_word(word):
    # Exception check
    if not word:
        raise InvalidWordException()

    # Returning a string of "*" equal to the length of the word
    masked_word = "*" * len(word)
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    # Exception checks.
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

    if not answer_word or not masked_word:
        raise InvalidWordException()

    if len(character) != 1:
        raise InvalidGuessedLetterException()

    # Blank string for the unmasked word
    unmasked_word = ""

    """
    Using .index() to hold the spot of the iterated character
    and then using a for loop and if statements to 
    either unmask it or replace it with "*" to keep the rest masked. 
    """

    for char in answer_word:
        indexer = answer_word.index(char)

        if char.lower() == character.lower():
            unmasked_word += char.lower()
            continue
        if masked_word[indexer] != "*":
            unmasked_word += masked_word[indexer]
            continue

        unmasked_word += "*"

    return unmasked_word


def guess_letter(game, letter):
    # Conditions/checks for the state of the game overall.
    finished = False

    if finished:
        raise GameFinishedException()

    # Setting up for masked word vs. answer word and appending
    # the previous guesses
    game["masked_word"] = _uncover_word(game["answer_word"], game["masked_word"], letter)
    game["previous_guesses"].append(letter.lower())

    # Conditions to win the game
    if game["masked_word"] == game["answer_word"]:
        if letter not in game["answer_word"]:
            raise GameFinishedException()
        raise GameWonException()

    # Decrementing for incorrect guesses
    if letter.lower() not in game["answer_word"].lower():
        game["remaining_misses"] -= 1

    # Conditionals for the remaining guesses reaching 0.
    if game["remaining_misses"] == 0:
        if letter in game["answer_word"]:
            raise GameFinishedException()
        raise GameLostException()

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
