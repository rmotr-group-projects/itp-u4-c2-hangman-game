from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["car", "bus"]


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    else:
        new_list = random.choice(list_of_words)
        return new_list


def _mask_word(word):
    if word == "":
        raise InvalidWordException()
    return len(word)*"*"


def _uncover_word(answer_word, masked_word, character):
    
    answer_word = answer_word.lower()
    character = character.lower()
    new_word = "" 
    if len(answer_word) == 0 or len(masked_word) == 0:
        raise InvalidWordException(Exception)
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    if character in answer_word:
        index_lst = []
        for index,char in enumerate(answer_word):
            
            if char == character:
                new_word += char
            else:
                new_word += masked_word[index]
            
        return new_word
    else: 
        return masked_word

def gameWon(game):
    return game['answer_word'].lower() == game['masked_word'].lower()

def gameLost(game):
    return game['remaining_misses'] <= 0

def gameOver(game):
    return gameLost(game) or gameWon(game)       


def guess_letter(game, letter):
    letter = letter.lower()
    # letter doesn't exist in list of previous guesses
    if gameOver(game):
        raise GameFinishedException()
    if letter in  game['previous_guesses']:
        raise InvalidGuessedLetterException()

    # word masked by * symbol
    old_masked_word = game['masked_word']
    new_masked_word = _uncover_word(game["answer_word"], old_masked_word, letter)

    if old_masked_word == new_masked_word:
        game['remaining_misses'] -= 1
    else:
        game['masked_word'] = new_masked_word
    
    game['previous_guesses'].append(letter)
    
    if gameWon(game):
        raise GameWonException()    
    
    if gameLost(game):
        raise GameLostException()    

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
