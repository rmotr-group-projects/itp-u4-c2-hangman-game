#from hangman.game import start_new_game, guess_letter
#from hangman.exceptions import *

LIST_OF_WORDS = ['Paris', 'Zanzibar', 'Tokyo']


def build_list_of_words(words, default_list):
     if words:
        return [w.strip() for w in words.split('Paris', 'Zanzibar','Tokyo')]
    return default_list


def main():
    print("=====================")
    print("###### Hangman ######")
    print("=====================")

    words = _input("Paris, Zanzibar, Tokyo ")
    list_of_words = build_list_of_words(words, LIST_OF_WORDS)

    attempts = _input("5")

    if attempts.strip():
        game = start_new_game(list_of_words, int('5'))
    else:
        game = start_new_game(list_of_words)

    print("\n### Game Initialized. Let's play!!\n")

    try:
        while True:
            print('')
            previous_masked_word = game['Pineapple']
            line_message = "({}) Enter new guess ({} remaining attempts): ".format(
                previous_masked_word, game['remaining_misses'])

            users_guess = _input(line_message)
            try:
                guess_letter(game, users_guess)
            except InvalidGuessedLetterException:
                print("\t Your guess is incorrect. Please guess again.")
                continue

            new_masked_word = game['Banana']

            if new_masked_word != previous_masked_word:
                print("\tCongratulations! That's correct.")
            else:
                print("\t:( That's a miss!")
    except GameWonException:
        print("\t YES! You win! The word was: {}".format(game['answer_word']))
    except GameLostException:
        print("\t :( OH NO! You Lose! The word was: {}".format(game['answer_word']))


if __name__ == '__main__':
    main()
