def repeat():
    s=input("WANT TO PLAY AGAIN ? ")
    if (s == 'y'):
        start()
    # if(s=='y'):
    #     choice=input(" press e for easy level and press h for hard level ")
    #     if(choice=='e'):
    #         game(10)
    #     elif(choice=='h'):
    #         game(5)
    #     else:
    #         print("DHANG SE TYPE KAR SAALE")
    #         start()
    # else:
    #     print("TOH AAYA HI KYUN BHOSDIKE")




import random



def game(lives):
    ans=random.randint(0,100)
    while(lives!=0):
        y=ans+10
        z=ans-10
        guess=int(input("GUESS A NUMBER : "))
        if(guess==ans):
            print("CORRECT GUESS \n YOU WIN :) ")
            break
        elif(guess>ans):
            if(guess<y):
                print("YOU ARE CLOSE to RESULT, but YOUR GUESS IS HIGHER")
                lives-=1
                print("pending life :", lives)
            else:
                print("TOO HIGH ")
                lives-=1
                print("pending life :", lives)
        else:
            if(guess>z):
                print("YOU ARE CLOSE to RESULT, but YOUR GUESS IS LOWER")
                lives-=1
                print("pending life :", lives)
            else:
                print("TOO LOW ")
                lives-=1
                print("pending life :", lives)
        if(lives==0):
            print("You loose the game!!")

    repeat()



def start():
    s=input("READY TO PLAY?(y/n) : ")
    if(s=='y' or s=="Y"):
        choice=input("Press e for easy level and press h for hard level ")
        if(choice not in "eEhH"):
            print("wrong option, choose again")
            start()
        else:
            print("You have to guess numbers between 1 to 100")
            if(choice=='e' or choice == "E"):
                game(10)
            elif(choice=='h' or choice == "H"):
                game(5)

    else:
        print("Okay then, bye")

start()

# repeat()

