#   FOR RECURSIVE CALL
def repeat():
    t = input(" WANNA PLAY THE GAME AGAIN ? ")
    if t == 'y':
        blackjack()
    else:
        print("THANK YOU")


import random


def blackjack():
    #   Player_total is global because its value hasto be updated with in the functions and that updated value have to effect the actual value
    global player_total
    l = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player = []
    computer = []

    player_total = 0
    computer_total = 0

    for i in range(2):
        player.append(random.choice(l))
        computer.append(random.choice(l))
        player_total += player[i]
        computer_total += computer[i]

    if (player_total > 21 and 11 in player):
        i = player.index(11)
        player[i] = 1
        player_total -= 10

    print("your cards are : ", player, "your total is :", player_total)
    # print("computer cards are : ",computer, "computer total is :",computer_total)
    print("computer 1st card is : ", computer[0])
    print()

    def passs():
        total = computer_total
        while (total < 17):

            computer.append(random.choice(l))
            # print(computer[-1])
            total += computer[-1]

            if (total > 21 and 11 in computer):
                i = computer.index(11)
                computer[i] = 1
                total -= 10

        print("computer cards are :", computer, "computer total is =", total)

        if (total > 21):
            print("COMPUTER SCORE EXCEEDS 21, YOU WIN THE GAME :) ")
            print()
            repeat()
        else:
            print("your cards are : ", player, "your total is :", player_total)
            if (player_total > total):
                print("YOU WIN :) ")
                print()
                repeat()
            elif (player_total < total):
                print("YOU LOOSE :( ")
                print()
                repeat()
            else:
                print("MATCH DRAW :| ")
                print()
                repeat()

    def add(total):
        global player_total
        x = random.choice(l)
        player.append(x)

        if (player_total > 21 and 11 in player):
            i = player.index(11)
            player[i] = 1
            player_total -= 10
            return x
        print("your cards are : ", player, "your total is :", total + x)
        return x

    def choose():
        choice = input("ADD CARD(y) OR PASS(n) :")
        if (choice == 'y'):
            global player_total
            player_total += add(player_total)

            if (player_total > 21 and 11 in player):
                i = player.index(11)
                player[i] = 1
                player_total -= 10
                print("your cards are : ", player, "your total is :", player_total)

            if (player_total > 21):
                print("YOUR SCORE EXCEEDS 21, YOU LOOSE THE GAME :( ")
                print()
                repeat()
            else:
                choose()

        else:
            passs()

    choose()


blackjack()



