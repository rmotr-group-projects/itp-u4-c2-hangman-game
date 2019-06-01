from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["Dog", "Cat", "Fish", "Mouse"]

def _get_random_word(list_of_words):
    if list_of_words:
        return(random.choice(list_of_words))
    else:
        raise InvalidListOfWordsException()

def _mask_word(word):
    if word:
        return str("*" * len(word))
    else:
        raise InvalidWordException()

def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException()
    if len(character) > 1:
        raise InvalidGuessedLetterException()

    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    character = character.lower()
    
    locations_of_character = []
    for index, letter in enumerate(answer_word):
        if letter == character:
            locations_of_character.append(index)
    for location in locations_of_character:
        masked_word = masked_word[:location] + character + masked_word[location + 1:]
    return masked_word

def guess_letter(game, letter):
    answer_word = game['answer_word'].lower()
    masked_word = game['masked_word'].lower()
    letter = letter.lower()
    
    if "*" not in game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
    
    new_masked_word = _uncover_word(answer_word, masked_word, letter)
    
    # Decrement remaining_misses if guess was wrong
    if masked_word == new_masked_word:
        game['remaining_misses'] = game['remaining_misses'] -1
    else:
        game['masked_word'] = new_masked_word #if word changed, update value in game
    
    # Append guessed letter to game previous guesses list
    game['previous_guesses'].append(letter)
    
    if game['answer_word'] == game['masked_word']:
        raise GameWonException
    
    if game['remaining_misses'] <= 0:
        raise GameLostException

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
