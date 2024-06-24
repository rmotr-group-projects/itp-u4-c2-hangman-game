from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    if list_of_words:
        return random.choice(list_of_words)
    else:
        raise InvalidListOfWordsException('You need some words')


def _mask_word(word):
    if word:
        return word.replace(word, str(len(word) * '*'))
    else:
        raise InvalidWordException('Invalid word')


def _uncover_word(answer_word, masked_word, character):
    if len(character) > 1:
        raise InvalidGuessedLetterException('Only 1 character plz')
    if len(masked_word) > len(answer_word):
        raise InvalidWordException('Masked word length too long')
    if answer_word:
        lowercased_answer = answer_word.lower()
        lowercased_character = character.lower()
        if lowercased_character in lowercased_answer:
            cleaned_word = ''
            for letter in lowercased_answer:
                if letter == lowercased_character:
                    cleaned_word += letter
                elif letter in masked_word:
                    cleaned_word += letter
                else:
                    cleaned_word += '*'
            return cleaned_word
        else:
            return masked_word
    else:
        raise InvalidWordException('Your words must have value')


def _is_game_won(game):
    return game['answer_word'].lower() == game['masked_word'].lower()


def _is_game_lost(game):
    return game['remaining_misses'] <= 0


def _is_game_finished(game):
    return _is_game_lost(game) or _is_game_won(game)


def guess_letter(game, letter):  # game is a dict
    letter = letter.lower()
    
    if _is_game_finished(game):
        raise GameFinishedException('The game is already finished')
        
    game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
    if letter not in game['answer_word'].lower():
        game['remaining_misses'] -= 1
    game['previous_guesses'].append(letter)
    
    if game['answer_word'].lower() == game['masked_word'].lower():
        raise GameWonException('You win first try!')
    
    if game['remaining_misses'] == 0:
        raise GameLostException('Game over!')
        
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
