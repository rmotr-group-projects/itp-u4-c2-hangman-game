from hangman.exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['apples', 'potatos', 'carrots', 'controller', 'paper', 'pens', 'toilet', 'pencil', 'fireworks', 'cans', 'cats', 'dogs', 'dove', 'dang', 'spank', 'man', 'berry', 'carry', 'span', 'plan']


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException('We need some words!')
    word = random.randint(0,len(list_of_words)-1)
    return list_of_words[word]

def _mask_word(word):
    if len(word) < 1:
        raise InvalidWordException('We a random word!')
    return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word)==0 or len(masked_word)==0:
        raise InvalidWordException('Those words are invalid!')
    if len(character)>1:
        raise InvalidGuessedLetterException('Only one letter per guess')
    if len(answer_word) != len(masked_word):
        raise InvalidWordException('answer_word and masked_word not same length')
    
    count = 0
    mask = list(masked_word.lower())
    for char in answer_word:
        if char.lower() == character.lower():
            mask[count] = character.lower()
        count += 1
    mask = ''.join(mask)
    return mask

print(_uncover_word('return', '******', 't'))
        

def guess_letter(game, letter):
    if game['masked_word']==game['answer_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException('we are done here')
    answer = game['answer_word'].lower()
    letter = letter.lower()
    masked_word = game['masked_word']
    game['previous_guesses'].append(letter)

    
    if letter in answer:
        game['masked_word'] = _uncover_word(answer, masked_word, letter)
        if '*' not in game['masked_word']:
            raise GameWonException('WINNER!')
    else:
        game['remaining_misses'] -= 1
        if game['remaining_misses'] == 0:
            raise GameLostException('LOSER!')
            


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
