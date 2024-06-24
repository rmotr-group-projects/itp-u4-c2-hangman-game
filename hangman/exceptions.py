class InvalidListOfWordsException(Exception):
    print("Invalid list of words exception raised")


class InvalidWordException(Exception):
    print("InvalidWordException raised")


class GameWonException(Exception):
    print("You won the game! Congrats!")


class GameLostException(Exception):
    print("You lost the game!")


class GameFinishedException(Exception):
    print("Game Finished!")


class InvalidGuessedLetterException(Exception):
    print("Incorrect letter. Try again!")
