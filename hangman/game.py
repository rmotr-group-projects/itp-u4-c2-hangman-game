from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Python', 'Boston', 'Singapore', 'Minneapolis']


def _get_random_word(list_of_words):
    #Get a word for the game from the input list
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException
    word = random.randint(0, len(list_of_words) -1)
    return list_of_words[word]


def _mask_word(word):
    #Create a mask of the game word using *
    if len(word) == 0:
        raise InvalidWordException
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    #Look for empty inputs in function parameters
    if not answer_word or not masked_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if len(character) > 1:
        raise InvalidGuessedLetterException
        
    #Convert answer and character to lower to prevent case sensitive game
    answer = answer_word.lower()
    letter = character.lower()
    result = ''
    
    #Check the answer word for the character and return * if not found
    for i in range(len(answer)):
        if letter != answer[i] or masked_word[i] != '*':
            result += masked_word[i]
            continue
        result += letter

    return result
    

def guess_letter(game, letter):
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter.lower())
    
    #Check if game is finished and raise Finished exception if true
    if game['answer_word'] == game['masked_word']:
        if letter not in game['masked_word']:
            raise GameFinishedException('The game is already finished')
    
    #Check if game is won and raise Won exception if true
    if '*' not in game['masked_word']:
        raise GameWonException('You have won the game')

    #Decrease remaining_misses if an incorrect letter is entered
    if letter.lower() not in game['answer_word'].lower():
        game['remaining_misses'] -= 1
    
    #Raise Finished exception if no more remaining_misses and correct guess
    #Raise Lost exception if no more remaining_misses and incorrect guess
    if game['remaining_misses'] == 0:
        if letter in game['answer_word']:
            raise GameFinishedException('The game is already finished')
        raise GameLostException('You have lost')
    
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
