from .exceptions import *
import random

# Complete with your own, just for fun :)
# LIST_OF_WORDS = []

big_string = '''At eight o'clock Kutuzov rode to Pratz at the head of Miloradovich's fourth column, the one 
which was to take the place of the columns of Przebyszewski and Langeron, which had already gone 
down. He greeted the men of the head regiment and gave the order to move, thus showing that he intended to 
lead the column himself. Having ridden to the village of Pratz, he halted. Prince Andrei, one of the enormous 
number of persons constituting the commander in chief's suite, stood behind him. Prince Andrei felt excited, irritated, 
and at the same time restrainedly calm, as a man usually is when a long-desired moment comes. He was firmly convinced 
that this was the day of his Toulon or his bridge of Arcole. How it would happen, he did not know, but 
he was firmly convinced that it would be so. The locality and position of our troops were known to him, as 
far as they could be known to anyone in our army. His own strategic plan, which there obviously could be no thought
of carrying out now, was forgotten. Now, entering into Weyrother's plan, Prince Andrei pondered the possible
happenstances and came up with new considerations, such as might call for his swiftness of reflection and decisiveness.'''

def slice_string(string):
    list_of_words = []
    sliced_string = string.split()
    for word in sliced_string:
        if ',' not in word and '.' not in word:
            list_of_words.append(word)
        
    return list_of_words

# print(slice_string(big_string))
# Output of function over big_string:

LIST_OF_WORDS = ['At', 'eight', "o'clock", 'Kutuzov', 'rode', 'to', 'Pratz', 'at', 'the', 'head', 'of', "Miloradovich's", 
'fourth', 'the', 'one', 'which', 'was', 'to', 'take', 'the', 'place', 'of', 'the', 'columns', 'of', 'Przebyszewski', 'and', 
'which', 'had', 'already', 'gone', 'He', 'greeted', 'the', 'men', 'of', 'the', 'head', 'regiment', 'and', 'gave', 'the', 'order', 
'to', 'thus', 'showing', 'that', 'he', 'intended', 'to', 'lead', 'the', 'column', 'Having', 'ridden', 'to', 'the', 'village', 
'of', 'he', 'Prince', 'one', 'of', 'the', 'enormous', 'number', 'of', 'persons', 'constituting', 'the', 'commander', 'in', "chief's", 
'stood', 'behind', 'Prince', 'Andrei', 'felt', 'and', 'at', 'the', 'same', 'time', 'restrainedly', 'as', 'a', 'man', 
'usually', 'is', 'when', 'a', 'long-desired', 'moment', 'He', 'was', 'firmly', 'convinced', 'that', 'this', 'was', 'the', 
'day', 'of', 'his', 'Toulon', 'or', 'his', 'bridge', 'of', 'How', 'it', 'would', 'he', 'did', 'not', 'but', 'he', 'was', 
'firmly', 'convinced', 'that', 'it', 'would', 'be', 'The', 'locality', 'and', 'position', 'of', 'our', 'troops', 'were', 
'known', 'to', 'as', 'far', 'as', 'they', 'could', 'be', 'known', 'to', 'anyone', 'in', 'our', 'His', 'own', 'strategic', 
'which', 'there', 'obviously', 'could', 'be', 'no', 'thought', 'of', 'carrying', 'out', 'was', 'entering', 'into', "Weyrother's",
'Prince', 'Andrei', 'pondered', 'the', 'possible', 'happenstances', 'and', 'came', 'up', 'with', 'new', 'such', 'as', 
'might', 'call', 'for', 'his', 'swiftness', 'of', 'reflection', 'and']

def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException(Exception)
    return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException(Exception)
    masked = ('*' * len(word))
    return masked
    
# print(_mask_word('hell'))    


def _uncover_word(answer_word, masked_word, character):
    n_word = ''
    if not answer_word:
        raise InvalidWordException(Exception)
    if len(character) > 1:
        raise InvalidGuessedLetterException(Exception)
    if len(answer_word) != len(masked_word):
        raise InvalidWordException(Exception)
    for i in range(len(answer_word)): 
        if answer_word[i].lower() == character.lower(): # answer_word[i]? answer_word at position/index i?
            n_word += character.lower()
        else:
            n_word += masked_word[i]
    return n_word
    
def guess_letter(game, letter):
    """
    You don't need an if statement to check that, you are just reading the game state
    from game.
    Ok they're trying to guess a letter, I should check to see if that letter is in the answer word
    I need to check the game state to find that out.
    Oh it is in the answer word, I need to uncover that in the masked word then, again modify game state
    It wasn't a miss so I don't need to modify remaining misses, but I do have to update previous guesses
    again modify game state.
    game is a dictionary, you need to access all that stuff from *in* the dictionary
    
    Just write the code to pass the test you're working on. You can build the logic up from there.
    
    Pseudo code:
    if letter in answer:
        unmask word
    else:
        modify remaining guesses
    add letter to previous guesses
    
    game['answer_word']
    ALL game state stuff is part of the game dictionary, it must be read from the dictionary and any
    updates need to be made to the dictionary
    
    I need to go get my son up from his nap, I'll leave this to you for now.
    """
    # OK but I still don't get the concept of that logic you mention. 
    # OK thks
    if not '*' in game['masked_word']:
            raise GameFinishedException
    if letter.lower() in game['answer_word'].lower(): # need to lower both so comparing apples to apples
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
        if not '*' in game['masked_word']:
            raise GameWonException
        
    else:
        game['remaining_misses'] -= 1
        game['previous_guesses'].append(letter.lower())
        if game['remaining_misses'] == 0:
            raise GameLostException
    if game['remaining_misses'] == 0:
        raise GameFinishedException
        
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
