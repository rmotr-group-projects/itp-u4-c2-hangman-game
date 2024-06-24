from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = [
    'dog',
    'fish',
    'python',
    'rmotr',
    'happy',
    'great'
]


def _get_random_word(list_of_words):
    try:
        return random.choice(list_of_words)
    except:
        raise InvalidListOfWordsException('Try again')


def _mask_word(word):
    i = len(word)
    if i > 0:
        mask = '*' * i
        return mask
    else:
        raise InvalidWordException('Invalid word')


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) != len(masked_word) or not answer_word or not masked_word:
        raise InvalidWordException('Those are invalid words')
        
    if len(character) > 1:
        raise InvalidGuessedLetterException('Wrong Character..Try again') 
    
    for idx, char in enumerate(answer_word):
        if char.lower() == character.lower():
            masked_word = list(masked_word)
            masked_word[idx] = character.lower()
            masked_word = ''.join(masked_word)
    return masked_word


def guess_letter(game, letter):
    if game['remaining_misses'] == 0 or game['answer_word'] == game['masked_word']:
        raise GameFinishedException()
        
    mask = '*'
    letter = letter.lower()
    a_word = game['answer_word'].lower()
    m_word = game['masked_word']
    game['previous_guesses'].append(letter)
    game['masked_word'] = _uncover_word(a_word, m_word, letter)
       
    if letter not in a_word:
        game['remaining_misses'] -= 1

        
    if game['answer_word'] == game['masked_word']:
        raise GameWonException('You are the winner')
    
    if game['remaining_misses'] == 0:
        raise GameLostException('Sorry you Lost') 


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
