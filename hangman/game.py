from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["Secret", "Purple", "Cheetos"]


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException("Error: No words were provided for the game.")
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException("Error: A word must be provided in order to hide its characters.")
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if not answer_word and not masked_word:
        raise InvalidWordException("Error: A word must be provided in order to reveal correct guesses.")
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException("Error: Masked word must equal the length of the word generated to start guessing.")
        
    if character and character.isalpha() and len(character) > 1:
        raise InvalidGuessedLetterException("Guess not accepted: ({chars}). Only 1 character per guess allowed.".format(chars=character))

    letter = character.lower()
    answer_word = answer_word.lower()
    updated_masked = ''
    
    if letter in answer_word:
        for i, char in enumerate(answer_word):
            if letter == char:
                updated_masked += letter
            else:
                updated_masked += masked_word[i]
            
        return updated_masked
    return masked_word

def guess_letter(game, letter):
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException("Game over.")
    
    letter = letter.lower()
    game_word = game.get('answer_word').lower()
    guessed_result = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException("That letter has already been guessed. Pick another letter.")
    game['previous_guesses'].append(letter)
    
    if letter not in game_word:
        game['remaining_misses'] -= 1
    game['masked_word'] = guessed_result
    
    if guessed_result == game_word:
        raise GameWonException("Great! You figured out the word!")
    
    if guessed_result != game_word and game['remaining_misses'] < 1:
        raise GameLostException("You ran out of guesses. The word remains a mystery!")
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
