from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Python', 'Television', 'Carriage', 'Golf Course', 'Driver', 'Previous']


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException ("Empty list of words")
    
    return random.choice(list_of_words)


def _mask_word(word):
    if word == '':
        raise InvalidWordException ("No word entered")
    
    masked_word = ""
    
    for char in word:
        if char == ' ':
            masked_word += " "
        masked_word += "*"
    
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if answer_word == '' or masked_word == '':
        raise InvalidWordException ("Need to enter a word")
    elif len(character) > 1:
        raise InvalidGuessedLetterException ("Guess must be one character")
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException ("Error with masked word and answer word lengths")
    
    
    new_masked_word = ""
    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    character = character.lower()
    
    for index, char in enumerate(answer_word):
        if char == character:
            new_masked_word+=char
        else:
            new_masked_word+=masked_word[index]
    
    return new_masked_word


def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] < 1:
        raise GameFinishedException ("Game has finished")
    
    letter = letter.lower()
    
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter)
    
    if letter not in game['masked_word']:
        game['remaining_misses']-=1
    
    if game['masked_word'] == game['answer_word']:
        raise GameWonException("You won!")
    
    if game['remaining_misses'] == 0:
        raise GameLostException("You lost!")

    
def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None or list_of_words == []:
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
