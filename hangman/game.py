from .exceptions import *
from random import choice

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['notebooks',
                 'python',
                 'london',
                 'Thames',
                 'wine',
                 'olives',
                 'yellow',
                 'apple',
                 'pillow',
                 'sofa',
                 'yawn',
                 'colors',
                 'river',
                 'Big Ben',
                 'church'
                ]


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException()
    return choice(list_of_words)


def _mask_word(word):
    if word == '':
        raise InvalidWordException()
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if answer_word == '' and masked_word == '':
        raise InvalidWordException()
    elif len(character) > 1:
        raise  InvalidGuessedLetterException()
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException()
    small_character = character.lower()
    temp_answer_word_list = list(answer_word.lower())
    temp_masked_word_list = list(masked_word)

    for idx, letter in enumerate(answer_word.lower()):
        if letter == small_character:
            temp_masked_word_list[idx] = small_character
    new_masked_word = "".join(temp_masked_word_list)
    
    return new_masked_word


def guess_letter(game, letter):
    small_letter = letter.lower()
    small_answer_word = game['answer_word'].lower()
    if game['remaining_misses'] == 0 or '*' not in game['masked_word']:
        raise GameFinishedException()
        return "Doesn't matter"
    game['previous_guesses'].append(small_letter)
    if small_letter not in small_answer_word:
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            game_over = True
            raise GameLostException()
        return 'Miss!'    
    game['masked_word'] = _uncover_word(small_answer_word, game['masked_word'], small_letter)
    
    if '*' not in game['masked_word']:
        game_over = True
        raise GameWonException()
    
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