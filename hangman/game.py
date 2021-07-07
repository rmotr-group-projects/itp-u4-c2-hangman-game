from hangman.exceptions import *
import random
import string

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['funky']


def _get_random_word(list_of_words):
    if len(list_of_words)>0:
        return random.choice(list_of_words)
    raise InvalidListOfWordsException('Invalid List')


def _mask_word(word):
    length = len(word)
    if length != 0:
        maskedWord = ''
        for _ in range(length):
            maskedWord += '*'
        return maskedWord
    else:
        raise InvalidWordException('Invalid word')

def _uncover_word(correctWord, maskedWord, letter):

    matches = []
    maskedWordList = list(maskedWord)
    
    if len(letter)!=1:
        raise InvalidGuessedLetterException('Too many letters')
    
    elif len(maskedWord)==0 or len(correctWord)==0 or len(maskedWord) != len(correctWord):
        raise InvalidWordException(Exception)
        
    else:
        for pos,let in enumerate(correctWord):
            if let.lower() == letter.lower():
                matches.append(pos)
        for pos,let in enumerate(maskedWord):
            if pos in matches:
                maskedWordList[pos]=letter.lower()
    return ''.join(maskedWordList)


def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word']:
        raise GameFinishedException('Game is already done - You won')
    elif game['remaining_misses'] == 0:
        raise GameFinishedException('Game is already done - You lost')
    elif game['masked_word'] == _uncover_word(game['answer_word'], game['masked_word'], letter):
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses']-=1
        if game['remaining_misses']==0:
            print('You Lost!')
            raise GameLostException('Ran out of moves')
        print('not in the word')
    else: 
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
        print('correct guess')
        print(game['masked_word'])
        if game['masked_word'] == game['answer_word']:
            raise GameWonException('You Win')

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
