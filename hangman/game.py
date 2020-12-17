from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "angel","dog","shotgun","tiger", "phantom", "cat", "lemon", "cabel", "mirror", "hat","car","python"]


def _get_random_word(list_of_words):
    if list_of_words != []:
        return random.choice(list_of_words)
    else:
        raise InvalidListOfWordsException()


def _mask_word(word):
    if word != "":
        masked_word = "".join(["*" for letter in word])
        return masked_word
    else:
        raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    elif answer_word == "" or masked_word == "":
        raise InvalidWordException()
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException()
    hidden_word = "".join(answer_word[idx].lower() if character.lower() == answer_word[idx].lower() != -1 else masked_word[idx] for idx,letter in enumerate(answer_word))
    return hidden_word

def guess_letter(game, letter):
    if game["masked_word"] == game["answer_word"]:
            raise GameFinishedException()
    elif game["remaining_misses"] == 0:
            raise GameFinishedException()
    elif letter.lower() in game["answer_word"].lower():
        game["previous_guesses"].append(letter.lower())
        game["masked_word"] = _uncover_word(game["answer_word"],game["masked_word"],letter)
        if game["masked_word"] == game["answer_word"]:
            raise GameWonException()
    else:
        game["previous_guesses"].append(letter.lower())
        game["remaining_misses"] -= 1
        if game["remaining_misses"] == 0:
            raise GameLostException()


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
