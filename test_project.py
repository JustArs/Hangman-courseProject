import pytest
from HangmanTerm import secret
from Hangman import FindLetterBack

def test_secret():

    assert secret("e", [" ? "," ? "," ? "," ? "], ["t","e","s","t"], )  == [" ? ", "e"," ? "," ? "]
    assert secret("a", [" ? "," ? "," ? "," ? "], ["t","e","s","t"], )  == [" ? ", " ? "," ? "," ? "]

def test_FindLetterBack1():
    word = ["t","e","s","t"]
    newArr = [" ? "," ? "," ? "," ? "]
    mistakes = 1
    rightLets = 1
    assert FindLetterBack("t") == 2

def test_FindLetterBack2():
    word = ["t","e","s","t"]
    newArr = [" ? "," ? "," ? "," ? "]
    mistakes = 1
    rightLets = 1
    assert FindLetterBack("a") == 2






