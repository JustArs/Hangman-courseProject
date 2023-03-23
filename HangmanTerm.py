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
    while len(wor) > 9:
        wor = r.get_random_word()
    print (len(wor)) 
    print("Your word: ",wor)
    letter = split(wor)
    print(letter)
    
    
    newArr = []
    for i in range(len(wor)) :
        newArr.append("?")
    
    print (newArr)
    print (newArr)
    b = secret("a",newArr,wor)
    print (b)

    

def main():
    HangmanTerm()

if __name__ == "__main__":
    main()

