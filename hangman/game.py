from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = [ 'Python', 'Javascript', 'Ruby', 'Java' ]

def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException('List cannot be empty')
    num_range = len(list_of_words) - 1 
    i = randint(0, num_range)
    chosen_word = list_of_words[i]
    
    return chosen_word

def _mask_word(word):
    num_of_asterix = len(word)
    if not word:
	    raise InvalidWordException('Invalid word')
    
    return '*' * num_of_asterix

def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException('Invalid word')

    if len(character) > 1:
        raise InvalidGuessedLetterException('Invalid guess')

    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Incorrect info')

    answer = answer_word.lower()
    if character.lower() not in answer:
        return masked_word

    new_word = ''

    for answer_char, masked_char in zip(answer, masked_word):
        if character.lower() == answer_char:
            new_word += answer_char
        else:
            new_word += masked_char

    return new_word

def game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()


def game_lost(game):
    return game['remaining_misses'] <= 0


def game_finished(game):
    return game_lost(game) or game_won(game)

def guess_letter(game, letter):
    letter = letter.lower()
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException('Invalid Guessed Letter')

    if game_finished(game): 
        raise GameFinishedException('Game Finished')

    previous_masked = game['masked_word']
    new_masked = _uncover_word(game['answer_word'], previous_masked, letter)

    if previous_masked == new_masked:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_masked

    game['previous_guesses'].append(letter)

    if game_won(game):
        raise GameWonException('Game Won')

    if game_lost(game):
        raise GameLostException('Game Lost')

    return new_masked

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
