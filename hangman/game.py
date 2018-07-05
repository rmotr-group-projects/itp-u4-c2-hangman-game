from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException('Incorrect list of words')
    return random.choice(list_of_words)


def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException('The word provided is invalid')
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) < 1 or len(masked_word) < 1:
        raise InvalidWordException('The masked word or answer word is empty')
    if len(character) > 1:
        raise InvalidGuessedLetterException('The character has lenght more than 1')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('The lenths of masked word and answer word is not same')
    
    answer_lower = answer_word.lower()
    if character.lower() not in answer_lower:
        return masked_word
    
    
    new_answer =''
    for answer_char, masked_char in zip(answer_lower,masked_word):
        if character.lower() == answer_char:
            new_answer += answer_char
        else:
            new_answer += masked_char
    return new_answer

def gameWon(game):
    return game['answer_word'].lower() == game['masked_word'].lower()

def gameLost(game):
    return game['remaining_misses'] <= 0

def gameOver(game):
    return gameLost(game) or gameWon(game)

def guess_letter(game, letter):
    letter = letter.lower()
    
    if gameOver(game):
        raise GameFinishedException('The game is over')
    
    if letter in game['previous_guesses']:
        raise InvalidGuessedLetterException('You have used this letter already')
        
    mask_word = game['masked_word']
    new_mask_word = _uncover_word(game['answer_word'], mask_word, letter)
    
    if mask_word == new_mask_word:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_mask_word
    
    game['previous_guesses'].append(letter)
    
    if gameWon(game):
        raise GameWonException('You won the game')
    
    if gameLost(game):
        raise GameLostException('You lost the game')
    
    
    #return mask_word


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
