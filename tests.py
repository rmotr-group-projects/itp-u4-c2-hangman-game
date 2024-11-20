import pytest
from hangman.game import (
    start_new_game, guess_letter, _get_random_word, _mask_word, _uncover_word)
from hangman.exceptions import *

# passing
def test_uncover_word_with_empty_word():
    """Words are empty"""
    with pytest.raises(InvalidWordException):
        _uncover_word('', '', 'x')

# passing
def test_uncover_word_with_invalid_character():
    """Character to guess has len() > 1"""
    with pytest.raises(InvalidGuessedLetterException):
        _uncover_word('aaa', '***', 'xyz')

# passing
def test_uncover_word_with_invalid_masked_word():
    """Length of words is different"""
    with pytest.raises(InvalidWordException):
        _uncover_word('aaa', '**********', 'x')

# passing
def test_uncover_word_with_correct_character():
    word = _uncover_word('Python', '******', 'y')
    assert word == '*y****'

# passing
def test_uncover_word_with_miss_character():
    word = _uncover_word('Python', '******', 'z')
    assert word == '******'

# passing
def test_uncover_word_with_repeated_elements():
    word = _uncover_word('rmotr', '*****', 'r')
    assert word == 'r***r'

# passing
def test_uncover_word_with_all_equal_characters():
    word = _uncover_word('aaa', '***', 'a')
    assert word == 'aaa'

# passing
def test_uncover_word_with_misses_and_guesses():
    word = _uncover_word('Python', '******', 'y')
    assert word == '*y****'

    word = _uncover_word('Python', '*y****', 'z')  # Miss!
    assert word == '*y****'

    word = _uncover_word('Python', '*y****', 'n')
    assert word == '*y***n'

    word = _uncover_word('Python', '*y***n', 'o')
    assert word == '*y**on'

    word = _uncover_word('Python', '*y**on', 'x')  # Miss!
    assert word == '*y**on'

    word = _uncover_word('Python', '*y**on', 'a')  # Miss!
    assert word == '*y**on'

# passing
def test_uncover_word_is_case_insensitive_same_case():
    word = _uncover_word('Python', '******', 'P')
    assert word == 'p*****'

# passing
def test_uncover_word_is_case_insensitive_different_case():
    word = _uncover_word('Python', '******', 'p')
    assert word == 'p*****'

# passing
def test_get_random_word_with_one_word():
    list_of_words = ['rmotr']
    word_to_guess = _get_random_word(list_of_words)
    assert word_to_guess == 'rmotr'

# passing
def test_get_random_word_with_many_words():
    list_of_words = ['rmotr', 'python', 'intro']
    word_to_guess = _get_random_word(list_of_words)
    assert word_to_guess in list_of_words

# passing
def test_get_random_word_with_empty_list():
    with pytest.raises(InvalidListOfWordsException):
        word_to_guess = _get_random_word([])

# passing
def test_mask_word_with_valid_word():
    masked = _mask_word('Python')
    assert masked == '******'

# passing
def test_mask_word_with_empty_string():
    with pytest.raises(InvalidWordException):
        masked = _mask_word('')

# passing
def test_start_new_game_initial_state():
    # This test verifies that you haven't changed start_new_game
    game = start_new_game(['Python'], number_of_guesses=3)
    assert game == {
        'answer_word': 'Python',
        'masked_word': '******',
        'previous_guesses': [],
        'remaining_misses': 3,
    }

# passing
def test_game_with_one_correct_guess():
    game = start_new_game(['Python'])
    guess_letter(game, 'y')
    assert game['masked_word'] == '*y****'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['y']

# passing
def test_game_with_two_correct_guesses_same_move():
    game = start_new_game(['rmotr'])
    guess_letter(game, 'r')
    assert game['masked_word'] == 'r***r'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['r']

#  passing
def test_game_with_one_incorrect_guess():
    game = start_new_game(['Python'])

    guess_letter(game, 'x')  # Miss!
    assert game['masked_word'] == '******'
    assert game['remaining_misses'] == 4  # (5 - 1)
    assert game['previous_guesses'] == ['x']

# passing
def test_game_with_several_incorrect_guesses():
    game = start_new_game(['Python'])

    guess_letter(game, 'x')  # Miss!
    assert game['masked_word'] == '******'
    assert game['remaining_misses'] == 4
    assert game['previous_guesses'] == ['x']

    guess_letter(game, 'z')  # Miss!
    assert game['masked_word'] == '******'
    assert game['remaining_misses'] == 3
    assert game['previous_guesses'] == ['x', 'z']

# passing
def test_game_with_several_correct_guesses():
    game = start_new_game(['Python'])

    guess_letter(game, 'y')
    assert game['masked_word'] == '*y****'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['y']

    guess_letter(game, 'o')
    assert game['masked_word'] == '*y**o*'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['y', 'o']

    guess_letter(game, 't')
    assert game['masked_word'] == '*yt*o*'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['y', 'o', 't']

# passing
def test_game_with_several_correct_and_incorrect_guesses():
    game = start_new_game(['Python'])

    guess_letter(game, 'y')
    assert game['masked_word'] == '*y****'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['y']

    guess_letter(game, 'x')  # Miss!
    assert game['masked_word'] == '*y****'
    assert game['remaining_misses'] == 4
    assert game['previous_guesses'] == ['y', 'x']

    guess_letter(game, 'o')
    assert game['masked_word'] == '*y**o*'
    assert game['remaining_misses'] == 4
    assert game['previous_guesses'] == ['y', 'x', 'o']

    guess_letter(game, 'z')  # Miss!
    assert game['masked_word'] == '*y**o*'
    assert game['remaining_misses'] == 3
    assert game['previous_guesses'] == ['y', 'x', 'o', 'z']

# passing
def test_guess_word_is_case_insensitve():
    game = start_new_game(['Python'])

    guess_letter(game, 'p')
    assert game['masked_word'] == 'p*****'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['p']

    guess_letter(game, 'N')
    assert game['masked_word'] == 'p****n'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['p', 'n']

# passing
def test_game_wins_first_try():
    game = start_new_game(['aaa'])

    with pytest.raises(GameWonException):
        guess_letter(game, 'a')
        assert game['masked_word'] == 'aaa'
        assert game['remaining_misses'] == 5
        assert game['previous_guesses'] == ['a']

# passing 
def test_game_loses_first_try():
    game = start_new_game(['Python'], number_of_guesses=1)

    with pytest.raises(GameLostException):
        guess_letter(game, 'x')  # Miss!
        assert game['masked_word'] == '******'
        assert game['remaining_misses'] == 0
        assert game['previous_guesses'] == ['x']

# passing
def test_game_wins_several_moves_repeated_words():
    game = start_new_game(['aba'])

    guess_letter(game, 'a')
    assert game['masked_word'] == 'a*a'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['a']

    with pytest.raises(GameWonException):
        guess_letter(game, 'b')
        assert game['masked_word'] == 'aba'
        assert game['remaining_misses'] == 5
        assert game['previous_guesses'] == ['a', 'b']

# passing
def test_game_wins_several_moves():
    game = start_new_game(['abc'])

    guess_letter(game, 'a')
    assert game['masked_word'] == 'a**'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['a']

    guess_letter(game, 'c')
    assert game['masked_word'] == 'a*c'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['a', 'c']

    with pytest.raises(GameWonException):
        guess_letter(game, 'b')
        assert game['masked_word'] == 'abc'
        assert game['remaining_misses'] == 5
        assert game['previous_guesses'] == ['a', 'c', 'b']

# passing
def test_game_wins_several_moves_some_misses():
    game = start_new_game(['abc'])

    guess_letter(game, 'a')
    assert game['masked_word'] == 'a**'
    assert game['remaining_misses'] == 5
    assert game['previous_guesses'] == ['a']

    guess_letter(game, 'x')  # Miss!
    assert game['masked_word'] == 'a**'
    assert game['remaining_misses'] == 4
    assert game['previous_guesses'] == ['a', 'x']

    guess_letter(game, 'c')
    assert game['masked_word'] == 'a*c'
    assert game['remaining_misses'] == 4
    assert game['previous_guesses'] == ['a', 'x', 'c']

    guess_letter(game, 'z')  # Miss!
    assert game['masked_word'] == 'a*c'
    assert game['remaining_misses'] == 3
    assert game['previous_guesses'] == ['a', 'x', 'c', 'z']

    with pytest.raises(GameWonException):
        guess_letter(game, 'b')
        assert game['masked_word'] == 'abc'
        assert game['remaining_misses'] == 3
        assert game['previous_guesses'] == ['a', 'x', 'c', 'z', 'b']

# passing
def test_game_loses_several_guesses():
    game = start_new_game(['Python'], number_of_guesses=3)

    guess_letter(game, 'x')  # Miss!
    assert game['masked_word'] == '******'
    assert game['remaining_misses'] == 2
    assert game['previous_guesses'] == ['x']

    guess_letter(game, 'z')  # Miss!
    assert game['masked_word'] == '******'
    assert game['remaining_misses'] == 1
    assert game['previous_guesses'] == ['x', 'z']

    with pytest.raises(GameLostException):
        guess_letter(game, 'a')  # Miss!
        assert game['masked_word'] == '******'
        assert game['remaining_misses'] == 0
        assert game['previous_guesses'] == ['x', 'z', 'a']

# passing
def test_game_loses_with_some_correct_guesses():
    game = start_new_game(['Python'], number_of_guesses=3)

    guess_letter(game, 'y')
    assert game['masked_word'] == '*y****'
    assert game['remaining_misses'] == 3
    assert game['previous_guesses'] == ['y']

    guess_letter(game, 'x')  # Miss!
    assert game['masked_word'] == '*y****'
    assert game['remaining_misses'] == 2
    assert game['previous_guesses'] == ['y', 'x']

    guess_letter(game, 'z')  # Miss!
    assert game['masked_word'] == '*y****'
    assert game['remaining_misses'] == 1
    assert game['previous_guesses'] == ['y', 'x', 'z']

    guess_letter(game, 't')
    assert game['masked_word'] == '*yt***'
    assert game['remaining_misses'] == 1
    assert game['previous_guesses'] == ['y', 'x', 'z', 't']

    with pytest.raises(GameLostException):
        guess_letter(game, 'a')  # Miss!
        assert game['masked_word'] == '******'
        assert game['remaining_misses'] == 0
        assert game['previous_guesses'] == ['y', 'x', 'z', 't', 'a']

# passing
def test_game_already_won_raises_game_finished():
    game = start_new_game(['aaa'])

    with pytest.raises(GameWonException):
        guess_letter(game, 'a')
        assert game['masked_word'] == 'aaa'
        assert game['remaining_misses'] == 5
        assert game['previous_guesses'] == ['a']

    with pytest.raises(GameFinishedException):
        guess_letter(game, 'x')  # Doesn't matter

# passing
def test_game_already_lost_raises_game_finished():
    game = start_new_game(['Python'], number_of_guesses=1)

    with pytest.raises(GameLostException):
        guess_letter(game, 'x')  # Miss!
        assert game['masked_word'] == '******'
        assert game['remaining_misses'] == 0
        assert game['previous_guesses'] == ['x']

    with pytest.raises(GameFinishedException):
        guess_letter(game, 'n')  # Doesn't matter
