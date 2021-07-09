install:
	pip install --upgrade pip &&\
		pip install -r dev-requirements.txt

test:
	python -m pytest -vv tests.py

lint:
	pylint --disable=R,C hangman/game.py

all: install lint