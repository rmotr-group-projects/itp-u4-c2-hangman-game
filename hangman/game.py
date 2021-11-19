from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['chicken', 'horse', 'donkey', 'monkey', 'lion']


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    if word == '':
        raise InvalidWordException
    secret_word = ''
    for letter in word:
        secret_word += '*'
    return secret_word


def _uncover_word(answer_word, masked_word, character):
    answer_word = answer_word.lower()
    masked_word = masked_word.lower()
    character = character.lower()
    if len(answer_word) == 0:
        raise InvalidWordException
    elif len(character) > 1:
        raise InvalidGuessedLetterException
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    new_masked_word = ''
    for order, letter in enumerate(answer_word):
        if letter == character:
            new_masked_word += letter
        else:
            new_masked_word += "*"
#     return new_masked_word
    masked_word_list = list(masked_word)
    new_masked_word_list = list(new_masked_word)
    count = 0
    final_word = ''
    for letter in masked_word_list:
        if letter == '*' and new_masked_word_list[count] == '*':
            final_word += '*'
            count += 1
            
        elif letter == '*' and new_masked_word_list[count] != '*':
            final_word += new_masked_word_list[count]
            count += 1
            
        elif letter != '*' and new_masked_word_list[count] == '*':
            final_word += letter
            count += 1
    return final_word
        
            
        

def guess_letter(game, letter):
    
    letter = letter.lower()
    game_finished = False
    initial_game_word = game['masked_word']
    word = _uncover_word(game['answer_word'].lower(), game['masked_word'], letter)
    game['masked_word'] = word
    game['previous_guesses'].append(letter)
    try:
        if game['already_won'] or game['already_lost']:
            game_finished = True
    except:
        game['already_won'] = False
        game['already_lost'] = False
        
    if game_finished:
        raise GameFinishedException

    elif game['answer_word'] == word:
        game['already_won'] = True
        raise GameWonException

    elif game['remaining_misses'] == 1 and initial_game_word == word:
        game['already_lost'] = True
        raise GameLostException

    elif initial_game_word == word:
        game['remaining_misses'] -= 1

    else:
        game['remaining_misses'] -= 0
    
    return word


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses}
#         'already_won': False,
#         'already_lost': False}

    return game
