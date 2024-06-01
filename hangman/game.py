from .exceptions import *
import random as rand

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["apple", "orange", "apex", "bitcoin", "monero", "litecoin", "augur", "zcash", "binance", "shapeshift", "coinbase", "circle"]


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException('That is an invalid list of words')
    else:
        return rand.choice(list_of_words)


def _mask_word(word):
    if word == '':
        raise InvalidWordException('Not a word, b!')
    else:
        x = len(word)
        return "*"*x


def _uncover_word(answer_word, masked_word, character):
    #Exceptions!
    if answer_word.lower() == '':
        raise InvalidWordException('Not a word')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('Not a valid character')
    if character.lower() in answer_word.lower() and character.lower() in masked_word.lower():
        raise InvalidGuessedLetterException('Already guessed!')
    if character.lower() not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] or len(character) > 1:
        raise InvalidGuessedLetterException('not a letter!')
    
    #Guess is valid but not in asnwer word
    if character.lower() not in answer_word.lower() and character.lower() not in masked_word.lower():
        return masked_word
    
    #Code to run if the user correctly plays the game
    if character.lower() in answer_word.lower() and character.lower() not in masked_word.lower():
        for all in range(len(answer_word)):
            if answer_word[all].lower() == character.lower():
                masked_word = list(masked_word)
                masked_word[all] = character
                masked_word = "".join(masked_word)
        return masked_word.lower()

def guess_letter(game, letter):
    if game['answer_word'] == game['masked_word']:
        raise GameFinishedException()
    if game['remaining_misses'] == 0:
        raise GameFinishedException()
    
    x = _uncover_word(game['answer_word'], game['masked_word'], letter)
    if game['masked_word'] == x:
        game['remaining_misses'] -= 1
        game['previous_guesses'].append(letter.lower())
    else:
        game['masked_word'] = x
        game['previous_guesses'].append(letter.lower())
    
    if game['answer_word'] == game['masked_word']:
        raise GameWonException()
    if game['remaining_misses'] == 0:
        raise GameLostException()
    return x
    
    
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


# game = start_new_game(['Python'], number_of_guesses=3)

# guess_letter(game, 'x')  # Miss!
# print(game)
# guess_letter(game, 'z')  # Miss!
# print(game)
# # guess_letter(game, 'p')
# # print(game)
# guess_letter(game, 'a')  # Miss!
# print(game)