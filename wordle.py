from time import sleep
print("\033[0;30;47m")
print("welcome to wordle")
sleep(1)
while True:

    word=input(f"pick a word for your friend :")
    length=len(word)
    word_letters=[""]*length
    loop1=True
    trys=0
    for i in range(0,45):
        print()
    print("----------Do not scroll past this point-----------")
    print()
    
    while loop1==True:
        guess=input(f"guess a  {length}  letter word :")
        while len(guess)!=length:
            guess=input(f"guess a [{length}] letter word :")
        trys=trys+1
            
        guess_list=[""]*length
        for i in range(0,length):
            guess_list[i]=f"\033[0;31;40m{guess[i]}"+"\033[0;30;47m"
        
    
        if guess==word:
            print(f"\033[0;32;40m{word}"+"\033[0;30;47m")
            print(f"you got it in {trys} trys")
            print()
            sleep(4)
            loop1=False
        else:
            for a in range(0,length):
                for b in range(0,length):
                    if guess[a] == word[b]:
                        guess_list[a]=f"\033[0;33;40m{guess[a]}"+"\033[0;30;47m"
                        
            for i in range(0,length):
                if guess[i] == word[i]:
                    guess_list[i]=f"\033[0;32;40m{guess[i]}"+"\033[0;30;47m"
            
            print()
            for i in range(0,length):
                print(guess_list[i] , end="")
            print()
            print()