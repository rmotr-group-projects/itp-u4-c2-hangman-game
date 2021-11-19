from .exceptions import *
from random import randrange

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

#chemistry, radians, rainbows, trees, smiles, joy, walking, green, puppy, airplane, dinasour, orchid, mario, lake, mountains, fishing, swimming, ligands, fission

def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    return list_of_words[
        randrange(0, len(list_of_words), 1)
    ]


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    return len(word) * '*'


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

    if character.lower() not in answer_word.lower():
        return masked_word
    
    masked_word_as_list = list(masked_word)
    for indx, letter in enumerate(answer_word):
        if letter.lower() == character.lower():
            masked_word_as_list[indx] = letter.lower()
    return ''.join(masked_word_as_list)

    
def guess_letter(game, letter):
    letter = letter.lower()
    
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()
    if game['remaining_misses'] == 0 or game['answer_word'].lower() == game['masked_word'].lower():
        raise GameFinishedException()
    
    starting_masked_word = game['masked_word']
    new_masked_word = _uncover_word(game['answer_word'], starting_masked_word, letter)
    
    if starting_masked_word == new_masked_word:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_masked_word
    
    game['previous_guesses'].append(letter)
    
    if game['remaining_misses'] == 0:
            raise GameLostException()
    if game['answer_word'].lower() == game['masked_word'].lower():
            raise GameWonException()
    
    
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