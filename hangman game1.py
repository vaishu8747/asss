import random

moives=["houseful four",
        "bala",
        "krish",
        "race3",
        "chichore",
        "DDLG"]
name = input("Enter Name :")
print("WELCOME" + name)
totalturns = 10
print("so let's get started")
print("Following are the rules of the game:")
print("You will be given" + str(totalturns) + "chance to guess movie correctly")
print("OKAY!!!....LET'S PLAY")
print("Type exit if not want to play")
q='y'
while True:
    choosenletters = []
    random.shuffle(moives)
    moive = orgmovie = random.choice(moives).lower()
    #choice replace with shuffle due to repetition
    if q =="y" or q =='yes':
        turns = totalturns
        for i in moive:
            if i not in 'aeiou':
                moive = moive.replace(i,'-')
        print('Guess movie' + moive)
        while(turns >= 1):
            guess = input("guess character:")
            guess = guess.lower()
            if(guess == 'exit'):
                exit(0)
            if guess in orgmovie:
                for x in range(0,len(moive)):
                    if orgmovie[x] == guess:
                        guessmovie =list(moive)
                        guessmovie[x] = guess
                        moive = "".join(guessmovie)
            else:
                if guess in choosenletters:
                    print("This letter already choosen. Try another one.")
                    continue
                choosenletters.append(guess)
                turns -=1
                print("Turn chance Remain : " + str(turns))
            print(moive)
            if(moive == orgmovie):
                print('You Won!!!!')
                break
            if(turns == 0):
                print("Better Luck Next Time!!!")
                print("Correct Word is :" + orgmovie.upper())
        q = input("Wanna Play hangman Again?")
        q = q.lower()
        if(q != 'y' and q != 'yes'):
            break