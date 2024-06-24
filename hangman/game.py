from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

def _get_random_word(list_of_words):
    
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException('Invalid List of Words!')
    else:
        rand_idx = randint(0, len(list_of_words)-1)
        word = list_of_words[rand_idx]
        if type(word) != str:
            raise InvalidWordException('Invalid word!')
        else:
            return word

def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException('Invalid Word!')
        
    res = ''
    res += ('*' * len(word))
    return res


def _uncover_word(answer_word, masked_word, character):
    if character in masked_word or character.lower() in masked_word:
        raise InvalidGuessedLetterException('That letter has already been guessed!')
    
    elif len(character) != 1:
        raise InvalidGuessedLetterException('Invalid guess!')
    
    elif len(answer_word) < 1 or len(masked_word) < 1:
        raise InvalidWordException('Invalid word!')
    
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException('Invalid word!')
    else:
        idxs = [pos for pos, char in enumerate(answer_word) if char.lower() == character.lower()]
        for i in idxs:
            masked_word = masked_word[:i] + character + masked_word[i+1:]
        
        return masked_word.lower()


def guess_letter(game, letter):
    #game is already over
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException('This game has already finished!')
        
    #guessed letter is invalid
    elif not letter.isalpha():
        raise InvalidGuessedLetterException('Guessesed letter is invalid!')
    
    #game is not over    
    else:
        letter = letter.lower()
        game['answer_word'] = game['answer_word'].lower()
        new_uncover = ''
        new_uncover = _uncover_word(game['answer_word'], game['masked_word'], letter)
        
        #guess is a match
        if new_uncover != game['masked_word']:
            game['masked_word'] = new_uncover
            game['previous_guesses'] += letter
            if game['answer_word'] == game['masked_word']:
                raise GameWonException('You won the game!')
        
        #guess is a miss
        else:
            game['previous_guesses'] += letter
            game['remaining_misses'] -= 1
            if game['remaining_misses'] < 1:
                raise GameLostException('You lost the game!')
        

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
