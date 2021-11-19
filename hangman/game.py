from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if len(list_of_words) > 0:
        num = random.uniform(0,len(list_of_words))
        letter = list_of_words[int(num)]
        return letter
    else:
        raise InvalidListOfWordsException


def _mask_word(word):
    if len(word) > 0:
        word_masked =""
        for letter in word:
            word_masked += "*"
    else:
        raise InvalidWordException
    return  word_masked


def _uncover_word(answer_word, masked_word, character):
    answer_word_l = answer_word.lower()
    character_l = character.lower()
    if len(answer_word_l) == 0 or len(answer_word_l) != len(masked_word):
        raise InvalidWordException
    if len(character_l) != 1:
        raise InvalidGuessedLetterException
    masked_word_ = ""
    if character_l not in answer_word_l:
        return masked_word
    else:
        for pos in range(0,len(answer_word_l)):
            if character_l == answer_word_l[pos] :
                masked_word_ += character_l
            else:
                masked_word_ += masked_word[pos]
    return masked_word_
    

def guess_letter(game, letter):
    if game["remaining_misses"]== 0 or game["answer_word"] == game["masked_word"]:
        raise GameFinishedException
    if letter in game["previous_guesses"]:
        return game
    masked_word_ = _uncover_word(game["answer_word"], game["masked_word"], letter)
    game["masked_word"] = masked_word_
    if game["answer_word"].lower() == masked_word_:
        raise GameWonException  
    if letter.lower() not in game["answer_word"].lower():
        game["remaining_misses"] -= 1
        if game["remaining_misses"]== 0:
            raise GameLostException
    game["previous_guesses"].append(letter.lower())
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
