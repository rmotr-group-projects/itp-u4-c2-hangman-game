from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

def _get_random_word(list_of_words):
    if(len(list_of_words)<1):
       raise InvalidListOfWordsException("Not valid list")
    return random.choice(list_of_words)


def _mask_word(word):
    vres = ""
    if(len(word)<1):
        raise InvalidWordException("No valido")
    
    for vcount in range(len(word)):
        vres=vres+'*'
    return vres


def _uncover_word(answer_word, masked_word, character):
    vres_str=""
    vpos = 0
    
    if(len(answer_word)<1):
        raise InvalidWordException("String is empty")
    if(len(character)>1):
        raise InvalidGuessedLetterException("Character is not valid")
    if(len(answer_word)!=len(masked_word)):
        raise InvalidWordException("Strings don't have same lenght")
    for vcar in answer_word:      
        if(masked_word[vpos]=='*'):
            if(vcar.lower() == character.lower()):           
                vres_str= vres_str+vcar.lower()
            else:
                vres_str=vres_str+masked_word[vpos]
        else:
            vres_str=vres_str+masked_word[vpos]
        vpos= vpos+1
    return vres_str
        
def guess_letter(game, letter):       
    vnum_let1 = 0
  
    for vlet in game['masked_word']:
        if(vlet=='*'):
             vnum_let1 = vnum_let1+1
    if(vnum_let1<1):
        raise GameFinishedException("Game Finished")
    
    if(game['remaining_misses']==0):
        raise GameFinishedException("Game Finished")
     
    vtmp_str=_uncover_word(game['answer_word'], game['masked_word'],letter)
    print(vtmp_str)
    game['masked_word']=vtmp_str  
    vnum_let2 = 0
    for i in vtmp_str:
        if(i=='*'):
            vnum_let2 = vnum_let2+1
                  
    if(vnum_let2==0):
        raise GameWonException("Game won")
        
    if(vnum_let1<=vnum_let2):
        game['remaining_misses']=game['remaining_misses']-1
    
    if(game['remaining_misses']==0):
        raise GameLostException("Game lost")
    
    
    game['previous_guesses'].append(letter.lower())
    
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
