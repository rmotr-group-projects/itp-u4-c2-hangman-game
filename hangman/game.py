from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException()
    else:
        return random.choice(list_of_words)


def _mask_word(word):
    num_char = len(word)
    if num_char > 0:
        mask_word = '*' * num_char
        return mask_word
    else:
        raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) < 1 or len(masked_word) < 1:
        raise InvalidWordException()

    if len(character) != 1:
        raise InvalidGuessedLetterException()

    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

    if answer_word == masked_word:
        raise GameFinishedException()

    word = ''
    answer_case = answer_word.lower()
    character_case = character.lower()

    if character_case not in answer_case:
        return masked_word

    for index in range(len(answer_word)):
        if character_case == answer_case[index]:
            word += answer_case[index]
        else:
            word += masked_word[index]
    return word


def guess_letter(game, letter):
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameFinishedException()

    if game['remaining_misses'] < 1:
        raise GameFinishedException()

    if letter.lower() in game['previous_guesses']:
        raise InvalidGuessedLetterException()

    m_word = game['masked_word']

    word = _uncover_word(game['answer_word'], m_word, letter)

    if m_word == word:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = word

    game['previous_guesses'].append(letter.lower())

    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameWonException()

    if game['remaining_misses'] < 1:
        raise GameLostException()

    return word

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
