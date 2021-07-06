from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['python', 'computer', 'program', 'logic', 'test', 'keyboard']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    
    if len(list_of_words) == 1:
        return list_of_words[0]
    else:
        rnd = random.randint(0,len(list_of_words)-1)
        return list_of_words[rnd]


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException()
    
    return "*" * len(word)


def _uncover_word(answer_word, masked_word, character):
    if answer_word == "" or masked_word == "":
        raise InvalidWordException()
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    
    word = ""
    if character.lower() in answer_word.lower():
        for i in range(len(answer_word)):
            if answer_word[i].lower() == character.lower():
                word += character.lower()
            else:
                word += masked_word[i].lower()
    else: 
        word = masked_word
                
    return word
    
    


def guess_letter(game, letter):
    
    if game["answer_word"] == game["masked_word"]:
        raise GameFinishedException()
    
    if game["remaining_misses"] == 0:
        raise GameFinishedException()
        
    temp = game["masked_word"]
    
    game["masked_word"] = _uncover_word(game["answer_word"], game["masked_word"], letter)
    
    if temp == game["masked_word"]:
        game["remaining_misses"] -= 1
    
    letter = letter.lower()
    game["previous_guesses"].append(letter)
        
    if game["masked_word"] == game["answer_word"]:
        raise GameWonException()
        
    if game["remaining_misses"] == 0:
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
