from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = [
    'green',
    'blue',
    'red',
    'white',
    'black',
    'yellow',
    'navy',
    'magenta',
    'brown',
    'pink',
    'purple',
    'gray',
    'teal',
    'ivory'
    ]

#Checking word in list_of_words, if not in the parameter elevate it to exception. If in parameter return word
 
def _get_random_word(list_of_words):
    
    if not list_of_words:
        raise InvalidListOfWordsException
    else: 
        random_word = random.choice(list_of_words)
    return random_word
    
    
#If word not in parameter word raise exception, otherwise return out length of word with ****
def _mask_word(word):

    if not word:
        raise InvalidWordException
    else:
        word = '*' * len(word)
    return word

#Three parameter, search each parameter. If not in parameter raise exceptions. 
def _uncover_word(answer_word, masked_word, character):
    

    if not answer_word or not masked_word:      #similar things and same raise exception, you can check both things in the same if
        raise InvalidWordException
    
#    if not masked_word:
#        raise InvalidWordException
        
    if len(character) > 1:
        raise InvalidGuessedLetterException
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    if character.lower() in answer_word.lower():
        
#Locate position of character in answer_word
        char_positions = []
        
        for index, char in enumerate(answer_word):
            if char.lower() == character.lower():
                char_positions.append(index)
        
#Replace masked_word to list    
        replace_maskword_to_list = list(masked_word)
        
#Replace asterisk with character
        for num in char_positions:
            replace_maskword_to_list[num] = character.lower()
        
#Change list back to string
        output = ''
        for char in replace_maskword_to_list:
            output += char
        return output
    
    else:
        return masked_word


#Define function guess_letter with two parameters guessings letters in the string.
def guess_letter(game, letter):
    
    if game["remaining_misses"] == 0:
        raise GameFinishedException
        
    if game["answer_word"] == game["masked_word"]:
        raise GameFinishedException 
    
    guess = _uncover_word(game["answer_word"], game["masked_word"], letter)
    
    if guess == game["masked_word"]:
        game["remaining_misses"] = game["remaining_misses"] - 1
    else:
        game["masked_word"] = guess
        
    game["previous_guesses"].append(letter.lower()) 
    
    if guess == game["answer_word"]:
        raise GameWonException
     
    if game["remaining_misses"] == 0:
        raise GameLostException
    
    return guess
    
#Santiago code for guesses
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