from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Cats', 'Swimming', 'Music', 'Reddit', 'Zelda']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException("List cannot be empty")
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException("Word to guess cannot be empty")
    masked_word = '*' * len(word)
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException("Invalid word provided")
    if len(character) > 1:
        raise InvalidGuessedLetterException("Only one character can be given")
    if len(answer_word) != len(masked_word):
        raise InvalidWordException("Invalid word provided")

    updated_masked_word = ''
    for idx, letter in enumerate(answer_word):
        if letter.lower() == character.lower():
            updated_masked_word += character.lower()
        elif letter.lower() == masked_word[idx].lower():
            updated_masked_word += masked_word[idx].lower()
        else:
            updated_masked_word += '*'

    return updated_masked_word



def guess_letter(game, letter):
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
