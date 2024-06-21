from .exceptions import *
from random import randint 

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    
    word =''

    if len(list_of_words) == 1:
        return list_of_words[0]
            
    if len(list_of_words) > 1:
        size_l=len(list_of_words)-1
        word=list_of_words[randint(0,size_l)]
        return word
    raise InvalidListOfWordsException()



def _mask_word(word):
    
    if word =='':
        raise InvalidWordException()
    else:
        word_res =''
        for i in range(0,len(word)):
            word_res +='*'
        return word_res

    
 #help function to get a position of the char in case if there is more than one
def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char.lower():
            pos.append(n)
        elif string[n] == char.upper():
            pos.append(n)
            
    return pos


def _uncover_word(answer_word, masked_word, character):
    
    if answer_word=='' or masked_word=='':
        raise InvalidWordException()
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    
    if len(character) > 1:
        raise InvalidGuessedLetterException()
        
    list_pos = charposition(answer_word,character)
    list_masked_word = list(masked_word) # convert to list because string is not mutable 

    for i in range(0,len(list_pos)):
        list_masked_word[list_pos[i]]=character

        masked_word = ''.join(list_masked_word) # reconvert to string again after modification
    return masked_word.lower()

    
    
    
    
def guess_letter(game, letter):
    
    # test_game_already_won_raises_game_finished():
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException
    
    

    
    game['masked_word']= _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['previous_guesses'].append(letter.lower())
    
    if letter.lower() not in game['answer_word'].lower():
        game['remaining_misses'] -=1
    
    
    if game['masked_word']==game['answer_word']:
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
