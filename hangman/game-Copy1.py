# from .exceptions import *
import random
from pprint import pprint

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["Python"]


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    return list_of_words[random.randint(0, len(list_of_words)-1)]


def _mask_word(word):
    if not word:
        raise InvalidWordException()
    masked_word = ""
    if word:
        for i in word:
            masked_word+="*"
    return masked_word
    

def _uncover_word(answer_word, masked_word, character):
    character = character.lower()
    if len(answer_word) == 0:
        raise InvalidWordException("")
    if len(character)>1:
        raise InvalidGuessedLetterException()
    if len(masked_word) != len(answer_word):
        raise InvalidWordException()
        
        
    result=masked_word
    answer_word=answer_word.lower()
    indices = [i for i, x in enumerate(answer_word) if x == character]
    
    for letter in answer_word:
        if letter != character:
            continue
        if letter == character:
            result=list(result)
    
    for index in indices:
        result[index] = character       
    result = "".join(result)    
    return result
    



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
'''
    start_new_game(list_of_words="Python", number_of_guesses=5)
    
    ||
    ||
    \/
    
    game = {
    'answer_word': 'Python',
    'masked_word': '******',
    'previous_guesses': [],
    'remaining_misses': 5}
    
    '''
def guess_letter(game, letter):
    temp = game['remaining_misses']
    game['answer_word']=game['answer_word'].lower()
    letter=letter.lower()
    flag = False
    if letter and letter in game['answer_word']:
        game['masked_word'] =_uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter)
    
    if letter and letter not in game['answer_word']:
        game['previous_guesses'].append(letter)
        game['remaining_misses']-=1
        
    if game['answer_word'] == game['masked_word'] and game['remaining_misses'] == temp:
        game['previous_guesses'].append(letter)
        flag = True
        print ('GameWonException')
        
    if game['answer_word'] == game['masked_word'] and game['remaining_misses'] > 0:
        flag = True
        print ('GameFinishedException') 

    
    if game['answer_word'] != game['masked_word'] and game['remaining_misses'] == 0:
        flag = True
        print ('GameLostException') 
    
        
    if str(game['answer_word']) == str(game['masked_word']):
        flag = True
        print ('GameWonException')
    
    if game['remaining_misses'] == 0:
        flag = True
        print ('GameLostException')
        
    return flag
    


# print(_mask_word('word'))
# print(_uncover_word('Pythony', '*******', 'pythony'))
this_vals={
    'answer_word': 'Python', 
    'masked_word': '******', 
    'previous_guesses': [], 
    'remaining_misses': 5
    }
print("---------------")
print("---------------")
print("---------------")
pprint(start_new_game())
print(">--------------->")
pprint(guess_letter(this_vals, "n"))
print(">--------------->")

