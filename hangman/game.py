from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["Arsenal","Piano","Wushu","Kendo","Dvorak","Monet","Thierry","Jazz","RMOTR"]


def _get_random_word(list_of_words):
    if list_of_words:
        word_to_guess=random.choice(list_of_words)
        return word_to_guess
    raise InvalidListOfWordsException
    

def _mask_word(word):
    if word:
        masked_word =''
        for char in word:
            masked_word += "*"
        return masked_word
    raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    if len(masked_word) > len(answer_word):
        raise InvalidWordException()
    if not answer_word or not masked_word:
        raise InvalidWordException()
    
    success_guess=[]
    
    for char in masked_word:
        
        if char !='*':
            success_guess.append(char.lower())        
        
        if character.lower() in answer_word.lower():
            success_guess.append(character.lower())
            new_masked_word = "".join(c if c in success_guess else '*' for c in answer_word.lower())
        else:
            new_masked_word=masked_word  
    
    return new_masked_word
    


def guess_letter(game, letter):
    if letter.lower() in game["answer_word"].lower():
        game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'],letter)
        game['previous_guesses'].append(letter.lower())
        if game['masked_word'] == game['answer_word']:
            raise GameWonException()
        elif game['remaining_misses'] == 0:
            raise GameFinishedException()

    else:
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            raise GameLostException()
        elif game['masked_word'] == game['answer_word']:
            raise GameFinishedException()
            
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
