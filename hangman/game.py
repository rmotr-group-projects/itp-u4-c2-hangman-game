from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    raise InvalidListOfWordsException()

def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException()
    else:
        word= '*'*len(word)
        return word
        

def _uncover_word(answer_word, masked_word, character):
    
    if len(answer_word) == 0 or len(masked_word)==0:
        raise InvalidWordException()
    if len(character)>1:
        raise InvalidGuessedLetterException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    new_word = masked_word
    
    if character.lower() in answer_word.lower():
        
        for idx, char in enumerate(answer_word.lower()):
            idxs = []
            if char.lower() == character.lower():
                idxs.append(idx)
            for idx in idxs:
                new_word = masked_word[:idx].lower() + char.lower() + masked_word[idx+1:]
                masked_word = new_word
        masked_word = new_word.lower()
    return masked_word
    

def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException()
    if letter.lower() in game['answer_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
        if game['masked_word'] == game['answer_word']:
            raise GameWonException()
        return game
    else:
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses'] -= 1
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