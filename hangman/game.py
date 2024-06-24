from .exceptions import *

from random import randint


# Complete with your own, just for fun :)
# list_of_words = [ "house", "phone", "brush", "chair", "carpet", "watch", "desk", "boot", "robe", "fridge", "box", "shoe", "suit", "helmet", "bag"]


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException
    list_length = len(list_of_words)
    random_number = randint(1,list_length)
    word = list_of_words[random_number - 1]
    print(word)
    return word

def _mask_word(word):
    if word == "":
        raise InvalidWordException
    word_length = len(word)
    masked_word = "*" * word_length
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    if answer_word == "" or masked_word == "":
        raise InvalidWordException
    if character.lower() in answer_word.lower():
        new_masked_word = ""
        counter = 0
        for letter in list(answer_word.lower()):
            if masked_word[counter] != "*":
                new_masked_word += masked_word[counter]
            elif letter == character.lower():
                new_masked_word += character.lower()
#             if masked_word[counter] != "*":
#                 new_masked_word += masked_word[counter]
#           
# elif letters is not "*":
#                 new_masked_word += letters
            else:
                new_masked_word += "*"
            counter += 1
#         masked_word = new_masked_word
        return new_masked_word
        
    else:
#         raise InvalidGuessedLetterException()
        return masked_word
        


def guess_letter(game, letter):
    if game["answer_word"] == game["masked_word"] or game["remaining_misses"] == 0:
        raise GameFinishedException
    new_masked_word_from_function = _uncover_word(game["answer_word"], game["masked_word"], letter)
    game["masked_word"] = new_masked_word_from_function
    game["previous_guesses"] = game["previous_guesses"] +[letter.lower()]
    if letter.lower() not in game["answer_word"].lower():
        game["remaining_misses"] -= 1
    if game["remaining_misses"] == 0:
        raise GameLostException
    if game["answer_word"] == game["masked_word"]:
        raise GameWonException
    
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
