from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Pineapple', 'coconut', 'chocolate', 'vAnilla', 'strawberry', 'mint']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    return random.choice(list_of_words)

def _mask_word(word):
    masked = ""
    if not word:
        raise InvalidWordException()

    for eachchar in word:
        masked += "*"
    return masked
    
def _uncover_word(answer_word, masked_word, character):
    if not answer_word or len(answer_word) != len(masked_word):
        raise InvalidWordException()
    elif len(character) != 1:
        raise InvalidGuessedLetterException()
    else:
        masked_list = list(masked_word)

    for index, eachchar in enumerate(answer_word.lower()):
        if eachchar == character.lower():
            masked_list[index] = eachchar
    revealed = ''.join(masked_list)
    return revealed

def guess_letter(game, letter):
    chosen_word = game['answer_word']    #string will not change throughout
    masked_word = game['masked_word']    #string

    # check if the game has already been completed
    if chosen_word == masked_word or game['remaining_misses'] < 1:
        # word is completely revealed or user out of guesses
        raise GameFinishedException()

    letter = letter.lower()
    
    # if letter is reused
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException()
    else:
        game['previous_guesses'].append(letter)

    word_inprogress = _uncover_word(chosen_word, masked_word, letter)

    # if letter has not been revealed
    if letter not in word_inprogress:
        game['remaining_misses'] -= 1
    else:
        # if new letter has been revealed
        game['masked_word'] = word_inprogress

    # check game status
    if "*" not in game['masked_word']:
        raise GameWonException()
    elif game['remaining_misses'] < 1:
        raise GameLostException()

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
