from exceptions import *
import random
from random import randrange
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException('No Words in List!')
    else:
        random_idx = randrange(0,len(list_of_words))
    return list_of_words[random_idx]


def _mask_word(word):
    masked_word = ''
    if word.isalpha() == False:
       raise InvalidWordException('Word is invalid!')
    else:
        for letter in word:
           masked_word += '*'
    return masked_word

def _uncover_word(answer_word, masked_word, character):
    count = 0
    newword = list(masked_word.lower())
    uncovered_word = masked_word.lower()
    if answer_word == '' or masked_word == '':
        raise InvalidWordException
    elif len(character) > 1:
        raise InvalidGuessedLetterException
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException
        
    for letter in answer_word.lower():
        if letter == character.lower() and newword[count] == '*':
            newword[count] = character.lower()
            count+=1
        else:
            count +=1
        word = ''
        for i in newword:
            word +=i
    return word
    
    
        
        

def game_lost(test):
    print(test)
    if test == True: 
        raise GameFinishedException
def guess_letter(game, letter):
    gamelost = False
    if letter.lower() in game['answer_word'].lower():
        test = _uncover_word(game['answer_word'], game['masked_word'], letter.lower())
        game['masked_word']=test
        game['previous_guesses']=game['previous_guesses'] + [letter.lower()]
        if '*' not in game['masked_word']:
            raise GameWonException
            raise GameFinishedException
    else:
        temp = game['remaining_misses'] -1
        game['remaining_misses'] = temp
        game['previous_guesses']=game['previous_guesses'] + [letter.lower()]
        if game['remaining_misses'] == 0:
            raise GameLostException and game_lost(True)
                
            
def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess.lower(),
        'masked_word': masked_word.lower(),
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
