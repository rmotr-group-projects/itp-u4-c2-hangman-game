from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = ["pelican", "rabbit", "rhino", "vulture"]


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException
    word = random.choice(list_of_words)
    return word


def _mask_word(word):
    if word == '':
        raise InvalidWordException
    maskedword = ''
    for i in word:
        maskedword = maskedword + '*'
    return maskedword
        


def _uncover_word(answer_word, masked_word, character):
    character = character.lower()
    answer_word = answer_word.lower()
    if character == '' or len(character) > 1:
        raise InvalidGuessedLetterException
    if answer_word == '':
        raise InvalidWordException
    if masked_word == '':
        raise InvalidWordException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    guessedcharacters = []
    newmaskedword = ''
    for i in masked_word:
        if i in answer_word:
            guessedcharacters.append(i)
    guessedcharacters.append(character)
    for i in answer_word:
        if i in guessedcharacters:
            newmaskedword = newmaskedword + i
        else:
            newmaskedword = newmaskedword + '*'
    return newmaskedword 
            
    
    
            


def guess_letter(game, letter):
    letter = letter.lower()
    game['answer_word'] = game['answer_word'].lower()
    if game['remaining_misses'] == 0:
        raise GameFinishedException
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException
        
    if letter in game['answer_word']:
        game['previous_guesses'].append(letter)
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    else:
        game['previous_guesses'].append(letter)
        game['remaining_misses'] = game['remaining_misses'] - 1
    if game['answer_word'] == game['masked_word']:
        raise GameWonException
    if game['remaining_misses'] == 0:
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
