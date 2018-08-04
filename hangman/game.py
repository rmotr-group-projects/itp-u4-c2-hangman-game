from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException("The list of words in empty")
    return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException("no input work")
    return "*" * len(word)

def _uncover_word(answer_word, masked_word, character):
    if not answer_word and not masked_word:
        raise InvalidWordException("please input a word to start")
    
    if len(masked_word) != len(answer_word):
        raise InvalidWordException("Length isn't right in terms of word input")

    if character and character.isalpha() and len(character) > 1:
        raise InvalidGuessedLetterException("Guess not accepted: just one character per guess please")

    letter = character.lower()
    answer_word = answer_word.lower()
    updated_masked = ''
   
    if letter in answer_word:
        for i, char in enumerate(answer_word):
            if letter == char:
                updated_masked += letter
            else:
                updated_masked += masked_word[i]
        return updated_masked
    return masked_word
    
def guess_letter(game, letter):
    if game["answer_word"] == game["masked_word"] or game["remaining_misses"] == 0:
        raise GameFinishedException("the game is over")
        
    letter = letter.lower()
    secret_word = game.get('answer_word').lower()
    guess_result = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if letter in game["previous_guesses"]:
        raise InvalidGuessedLetterException("you already tried to used this letter")
    game["previous_guesses"].append(letter)
    
    if letter not in secret_word:
        game["remaining_misses"] -= 1
    game["masked_word"] = guess_result
    
    if guess_result == secret_word:
        raise GameWonException("You Win!")
    
    if guess_result != secret_word and game["remaining_misses"] < 1:
        raise GameLostException("You didn't get the word and no guesses left sorry")
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
