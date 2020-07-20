from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['geek', 'nerd', 'Super', 'Marvel']


def _get_random_word(list_of_words):
    # if there is no list an exception is raised.
    if not list_of_words:
        raise InvalidListOfWordsException()
    # if there is a list a random word is chosen and returned.    
    return random.choice(list_of_words)


def _mask_word(word):
    # if there is no word an exception is raised.
    if not word:
        raise InvalidWordException('The word is invalid')
    # A string with asterisks the length of the word is returned
    return len(word)* "*"


def _uncover_word(answer_word, masked_word, character):
    # If there is nothing in answer_word or masked_word an exception is raised
    if not answer_word or not masked_word:
        raise InvalidWordException('The word is invalid')
    # If the length of the character guessed is greater than 1 an exception is
    # raised
    elif len(character) > 1:
        raise InvalidGuessedLetterException('Too many characters guessed')
    # If the length of the answer_word and the masked_word aren't the same, an 
    # exception is raised.
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException('The word is not the same length')

    new_masked_word = ""
    
    # Cycle through the characters in answer_word and providing the character 
    # and index.
    for index, char in enumerate(answer_word):
        # If the lowercase character in answer_word is the same as the lowercase 
        # character guessed add the character new_masked_word otherwise add a 
        # characther from the same index in masked_word
        if char.lower() == character.lower():
            new_masked_word += character.lower()
        else:
            new_masked_word += masked_word[index].lower()
    return new_masked_word
    


def guess_letter(game, letter):
    # If answer_word and masked_word are the same or if there are no more misses 
    # the an exception is raised and the game finishes
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameFinishedException()
    elif game['remaining_misses'] == 0:
        raise GameFinishedException()
    
    # Assign the previous masked_word to a temp varialbe    
    old_mask = game['masked_word']
    
    # Add the guessed character to the previous_guess list in game
    game['previous_guesses'].append(letter.lower())
    
    # Assign the new uncovered_word after the letter guessed to a temp variable
    new_masked_word = _uncover_word(game['answer_word'], old_mask, letter)
    
    # Replace game['masked_word'] current value with the new_masked_word
    game['masked_word'] = new_masked_word
    
    # If the new masked word is the same as the old masked word nothing has
    # changed and remaining misses is decreaced
    if new_masked_word == old_mask:
        game['remaining_misses'] -= 1
    # If the new masked word is the same as answer word you win the game and an
    # exception is raised
    if new_masked_word.lower() == game['answer_word'].lower():
        raise GameWonException
    # If there are no more guesses remaining you lose the game
    if game['remaining_misses'] == 0:
        raise GameLostException


def start_new_game(list_of_words=None, number_of_guesses=5):
    # If a list of words isn't passed through then use the default list word
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS
        
    # Calls get random word function and assigns a random word from the list to
    # the variable word_to_guess
    word_to_guess = _get_random_word(list_of_words)
    # Calls the masked_word function and assigns a masked string of word_to_guess
    # to the variable masked_word
    masked_word = _mask_word(word_to_guess)
    # Game is a dictionary that keeps track of the status of the game
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
