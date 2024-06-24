from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['starbucks', 'latte','book', 'sandwhich','chocolate', 'carmel','ginger']


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException('Cmon bruh')
    else:
        return random.choice(list_of_words)


def _mask_word(word):
    if word == '':
        raise InvalidWordException('Cmon bruh')
    else:
        return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException('Cmon bruh')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Cmon bruh')
    if len(character) > 1:
        raise InvalidGuessedLetterException('Cmon bruh')
        
    answer = answer_word.lower()
    char = character.lower()
    result = ''
    if char in answer:
        for i in range(len(answer)):
            if answer[i] == char:
                result += char
            else:
                result += masked_word[i]
    else:
        result = masked_word
    
    return result


def guess_letter(game, letter):
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException()
    if game['remaining_misses'] == 0:
        raise GameFinishedException()
    
    word = game['masked_word']
    
    game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'],letter)
    
    if word == game['masked_word']:
        game['remaining_misses'] -= 1
        
    letter = letter.lower()
    game['previous_guesses'].append(letter)
    
    if game['masked_word'] == game['answer_word']:
        raise GameWonException()
        
    if game['remaining_misses'] == 0:
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
