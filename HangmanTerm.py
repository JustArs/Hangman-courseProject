from random import randint

def split(s):
    return [char for char in s]

def HangmanTerm():

    words = ["write", "change", "squirrel", "title"]
    wordid = randint(0,3)
    print("wordid......", wordid)
    selWord = words[wordid]
    print("selWord.....", selWord)
    letters = split(selWord)
    print(letters)

def main():
    HangmanTerm()

if __name__ == "__main__":
    main()

