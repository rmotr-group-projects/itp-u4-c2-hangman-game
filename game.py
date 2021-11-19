from exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['kitten']


def _get_random_word(list_of_words):
    
    if len(list_of_words) > 0:
        pick = random.choice(list_of_words)
        return pick
    else:
        raise InvalidListOfWordsException()


# word = _get_random_word(LIST_OF_WORDS)
# print(word)
# print(len(word))

def _mask_word(word):
    pick = ""
    
    if len(word) == 0:
        raise InvalidWordException('Words are empty')
    
    for i in range(len(word)):
        pick += '*'
    return pick
        
    

# masked = _mask_word(word)
# print(masked)


def _uncover_word(answer_word, masked_word, character):
    guesses = ""
    answer_list = []
    mask_list = []
    

    
#     if len(character) > 1:
#         raise InvalidGuessedLetterException("Character to guess has len() > 1")
#     if len(answer_word) != len(masked_word):
#         raise InvalidWordException("Length of words is different")
#     if not answer_word or not masked_word:
#         raise InvalidWordException("Words are empty")
#     if answer_word == '' or masked_word == '':
#         raise InvalidWordException('Words are empty')
        
        
    try:
        len(character) = 1:
    except InvalidGuessedLetterException("Character to guess has len() > 1")
    try:
        len(answer_word) == len(masked_word):
    except InvalidWordException("Length of words is different")
    try:
        answer_word != '' and masked_word != '':
    except InvalidWordException('Words are empty')


        
    for i in answer_word.lower():
        answer_list.append(i)
        
    for i in masked_word.lower():
        mask_list.append(i)
        
    
    for a, m in zip(answer_list,mask_list):
        if a.lower() == m.lower():
            guesses += a.lower()
        elif character.lower() == a.lower() and m == "*":
            guesses += a.lower()
        else:
            guesses += m.lower()
#     if character.lower() not in answer_list:
#         print('Miss!')
#     else: 
#         print('Match!')
            
    return guesses
        
word = _uncover_word('Python', '*y****', 'z')
print(word)
# yest = _uncover_word('', '', 'x')
    



# test_word = 'Kitten'
# test_mask = '******'

# # print(len(test_word))
# # print(len(test_mask))

# game = _uncover_word(test_word, test_mask, 'e')
# print(game)

# # print(len(game))
# game2 = _uncover_word(test_word, game, 'N')
# print(game2)
# game3 = _uncover_word(test_word, game2, 'k')
# print(game3)
# game4 = _uncover_word(test_word, game3, 'z')

#     game = {
#         'answer_word': word_to_guess,
#         'masked_word': masked_word,
#         'previous_guesses': [],
#         'remaining_misses': number_of_guesses,
#     }
            

def guess_letter(game, letter):
    
    first = _uncover_word(game['answer_word'].lower(), game['masked_word'].lower(), letter.lower())
    
    if game['answer_word'] == game['masked_word'] or game['remaining_misses'] == 0:
        raise GameFinishedException()
        
    
    if letter.lower() in game['answer_word'].lower() and letter.lower() not in game['masked_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'].lower(), game['masked_word'].lower(), letter.lower())
        game['previous_guesses'].append(letter.lower())
    if game['remaining_misses']-1 >= 0 and letter.lower() not in game['answer_word'].lower():
        
        game['previous_guesses'].append(letter.lower())
        game['remaining_misses'] -= 1
    
    if "*" not in first:
        raise GameWonException()

        
    if game['remaining_misses'] == 0:
        raise GameLostException()

        

    
    return game







# hi = guess_letter(_get_random_word(LIST_OF_WORDS), 'k')
# print(hi)
# hi2 = guess_letter(_get_random_word(LIST_OF_WORDS), 'e')
# print(hi2)

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

# game = start_new_game()
# print(game)

# test = guess_letter(game, 't')
# print(test)
# test2 = guess_letter(game, 'N')
# print(test2)
# test3 = guess_letter(game, 'z')
# print(test3)

