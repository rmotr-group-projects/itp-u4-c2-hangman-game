from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['evaporate', 'combustion', 'elusive', 'loop']


def _get_random_word(list_of_words):
    if len(list_of_words) == 0:
        raise InvalidListOfWordsException()
    else:
    
        return random.choice(list_of_words)


def _mask_word(word):
    if word == "":
        raise InvalidWordException()
    else:
        w = len(word)
        egun = '*' * w
        return egun


def _uncover_word(answer_word, masked_word, character):
    masqurade = ""
    if not answer_word and not masked_word  :
        raise InvalidWordException("Empty words")
    elif len(character)> 1:
        raise InvalidGuessedLetterException("Can only guess a character at a time")
    elif len(masked_word) != len(answer_word):
        raise InvalidWordException('haba! 2 different words snucked in')
    elif character.lower() in answer_word.lower():
        for lttr in answer_word.lower():
            if lttr == character.lower():
                masqurade += lttr
            elif lttr in masked_word:
                masqurade += lttr
            else:
                masqurade += '*'
                
        return masqurade
    elif character.lower() not in answer_word.lower():
        return masked_word
            


def guess_letter(game, letter):
    # help from dylancruse
    
    answer = game['answer_word'].lower()
    masked = game['masked_word']
    guess = letter.lower()
    guesses_left = game['remaining_misses']
     #check if masked word already equals the answer
    if answer == masked:
        raise GameFinishedException()
     #check if there are guesses left
    if guesses_left <= 0:
        raise GameFinishedException()
     #update the masked word and assign it to game dict
    updated_masked = _uncover_word(answer, masked, guess)
    game['masked_word'] = updated_masked
     #add the guess to previous guesses
    game['previous_guesses'].append(guess)
     #check if the guess caused them to win
    if answer == game['masked_word']:
        raise GameWonException()
     #if a missed guess, decrement remaining guesses
    if guess not in answer:
        game['remaining_misses'] -= 1
     #check if they ran out of guesses
    if game['remaining_misses'] <= 0:
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
