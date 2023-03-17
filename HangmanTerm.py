from random import randint
from  random_word  import  RandomWords

def split(s):
    return [char for char in s]

def HangmanTerm():
    r  =  RandomWords ()
    wor = r.get_random_word()
    while len(wor) > 9:
        wor = r.get_random_word()
    print (len(wor)) 
    print("Your word: ",wor)
    letter = split(wor)
    print(letter)
    

def main():
    HangmanTerm()

if __name__ == "__main__":
    main()

