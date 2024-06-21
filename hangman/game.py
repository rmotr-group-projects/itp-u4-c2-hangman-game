from .exceptions import *
from random import choice

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["coding", "puppy", "love", "master"]


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException()
    
    word_to_guess = choice(list_of_words)
    return word_to_guess
 
# a list of word can contain only one word
# a list of word can contain many words
#when there is no word, it raises "InvalidListOfWordsException"

def _mask_word(word):
    if word == "":
        raise InvalidWordException()
    
    masked = word.replace(word, "*"*len(word))
    return masked

#the len of the word will be the length of the masked word
#word cannot be empty, otherwise raise "InvalidWordException"

def _uncover_word(answer_word, masked_word, character):
    if len(character) > 1:
        raise InvalidGuessedLetterException()
    
    if len(answer_word) != len(masked_word):
        raise InvalidWordException()
    
    if answer_word == "" or masked_word == "":
        raise InvalidWordException()
    
    updated_word = ""
    
    for indx, (c, r) in enumerate(zip(answer_word, masked_word)):
        if c.lower() == character.lower():
            updated_word += character.lower()
        elif c.lower() != character.lower():
            updated_word += r.lower()

    return updated_word


'''
#both answer_word and masked_word cannot be empty
#the length of the charater needs to be more than 1
#the charater is case "insensitive"
#the length of two words need to be the same
#when the character is in the answer_word, do not mask it even when it is a repeated element in the answer_word
#when the character is not in the answer_word, mask it
#the character can be changed again and further guessed!
'''


def guess_letter(game, letter):

    if game["answer_word"] == game["masked_word"] or game["remaining_misses"] <= 0:
        raise GameFinishedException()

    previous_masked = game['masked_word']
    updated_masked = _uncover_word(game['answer_word'], previous_masked, letter)
    
    if previous_masked == updated_masked:
        game["remaining_misses"] -= 1
    
    else:
        game["masked_word"] = updated_masked
        
    game["previous_guesses"].append(letter.lower())    
    
    if game["answer_word"] == game["masked_word"]:
        raise GameWonException()
        
        
    if game["remaining_misses"] <= 0:
        raise GameLostException()


'''
#the user initial the game (start_new_game and default guesses)
#the user enter a letter. If the letter is in the updated_word, means there is certain right guess, so the remaining missing remain the same, otherwise, the reamaining missinsg reduce by 1
#the game["masked_Word"] shall be updated if there is any right guess
# the game["previous_guesses"] shall store the letter in the list

'''
#the letter is case "insensitive"


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

'''
#when new game starts, the state is settled. 
#the game can have default 5 guesses
#when the guess is correct, it returned updated masked_word and the remaining_misses remain the same, otherwise, it reduces by 1
#the previous guess will be stored in the "previous_guesses"
#when the user guess everything correctly before the remaining_misses become 0, it raises "GameWonException"
#if the user already won and continue to play, then it raises "GameFinishedException", same as alraedy lost
#if the remaining_misses is 0, then it raises "GameLostException"

'''