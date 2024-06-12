from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['jamie','lauren']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()

    num = randint(0, len(list_of_words)-1)
    return list_of_words[num]


def _mask_word(word):
    if not word:
        raise InvalidWordException

    result = ''

    for char in word:
        result += '*'

    return result


def _uncover_word(answer_word, masked_word, character):
    answer_word = answer_word.lower()
    character = character.lower()

    if not answer_word or not masked_word:
        raise InvalidWordException

    if len(character) > 1:
        raise InvalidGuessedLetterException

    if len(answer_word) != len(masked_word):
        raise InvalidWordException

    try:
        i = 0

        while True:
            i = answer_word.find(character, i)

            if i == -1:
                break

            masked_word = masked_word[:i] + character + masked_word[i + 1:]
            
            i += 1


    except ValueError:
        return masked_word
        raise InvalidGuessedLetterException

    return masked_word



def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word']:
        raise GameFinishedException()

    if game['remaining_misses'] == 0:
        raise GameFinishedException()


    game['previous_guesses'].append(letter.lower())

    if letter.lower() in game['answer_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    else:
        game['remaining_misses'] -= 1

    if game['masked_word'] == game['answer_word']:
        raise GameWonException()

    if game['remaining_misses'] == 0:
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

if __name__ == "__main__":

    print('test'.find('t', 4))
    # start_new_game()






    