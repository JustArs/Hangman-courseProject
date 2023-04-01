from random import randint
from  random_word  import  RandomWords

def split(s):
    return [char for char in s]

def secret(letter,SecrWord,word):
    for i in range(len(word)):
        if(word[i] == letter):
            SecrWord[i] = letter
    return SecrWord


def HangmanTerm():
    r  =  RandomWords ()
    wor = r.get_random_word()
    while len(wor) > 7:
        wor = r.get_random_word()
    letter = split(wor)



    return(letter)
    
    
    
    

def main():
    HangmanTerm()

if __name__ == "__main__":
    main()

