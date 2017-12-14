class InvalidListOfWordsException(Exception):
    print("\t Your list is not valid. Please try again")


class InvalidWordException(Exception):
    print("\t Your word is not valid. Please try again")


class GameWonException(Exception):
    print("\t YES! You win!")


class GameLostException(Exception):
    print("\t :( OH NO! You Lose!")


class GameFinishedException(Exception):
    print("\t game over")


class InvalidGuessedLetterException(Exception):
    print("\t That's not a valid letter guess!")
