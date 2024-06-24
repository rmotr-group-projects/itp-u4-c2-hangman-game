from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["pineapple", "baseball", "computers"]


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException("The List of words is empty")
        
    rand = randint(0, len(list_of_words)-1)
    return list_of_words[rand]


def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException("Your word does not exist")
    
    masked = len(word) * "*"
    return masked


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0 or len(masked_word) == 0 or len(masked_word) != len(answer_word):
        raise InvalidWordException("Your words do not exist or are not the same")
        
    if len(character) != 1:
        raise InvalidGuessedLetterException("Guess with a single character")
    
    index_list = [i for i, ltr in enumerate(answer_word) if ltr.lower() == character.lower()]
    for i in index_list:
        masked_word = masked_word[:i] + character + masked_word[i+1:]
    return masked_word.lower()
        


def guess_letter(game, letter):
    if game["masked_word"] == game["answer_word"] or game["remaining_misses"] == 0:
        raise GameFinishedException("The Game is Already Over!")
    
    
    if letter.lower() in game["answer_word"] or letter.upper() in game["answer_word"]:
        game["masked_word"] = _uncover_word(game["answer_word"], game["masked_word"], letter)
        
        if game["masked_word"] == game["answer_word"]:
            raise GameWonException("You Won!")
    else:
        game["remaining_misses"] -= 1
        if game["remaining_misses"] == 0:
            raise GameLostException("You Lost :(")
    game["previous_guesses"].append(letter.lower())
        


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
