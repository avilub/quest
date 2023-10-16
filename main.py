import random
h = 20
d = 1
dificulty = 1
critchance = 5
critdamage = 1.5

inv = []
def playeraddinventory():
    item1 = input("what would you like to add to your inventory?: ")
    inv.append(item1)

def inventory_check():
    lowerinput = input("do you want to see your inventory? [Y/N]: ")
    capsinput = lowerinput.upper()
    if capsinput == "Y":
        print(inv)
    elif capsinput == "N":
        pass
    else:
        print("not a valid input")

def q1d1():
    global h
    global d
    wh = 5
    wd = 0.5
    ran1 = random.random()
    q1ran1 = random.randint(1,5)

    print("You encounter a Wolf (♥5) (⚔︎0.5) | You have " + "(" + str(h) + "♥)" + " " + "(" + str(d) + "⚔︎)")
    q1q1d2 = input("Run or Fight?:")
    q1q1d2 = q1q1d2.lower()

    if q1q1d2 == "run":
        print("test")
        pass

    elif q1q1d2 == "fight":




    
    else:
        print("not a valid input")
        q1d1()

def q1d2():
    global h
    global d
    global health
    global damage
    lh = 5
    ld = 1
    qran1 = random.random()
    q2ran1 = random.randint(1,10)

    print("You encounter a Lion (♥10) (⚔︎1) | You have " + "(" + str(h) + "♥)" + " " + "(" + str(d) + "⚔︎)")
    q2q1d2 = input("Run or Fight?:")
    q2q1d2 = q2q1d2.lower()

    if q2q1d2 == "run":
        print("test")
        pass

    elif q2q1d2 == "fight":
        if d > ld:
            inv.append("Lion Tooth Dagger (+1⚔︎)")
            d = d + 1
            print("You won the fight and earned (1x Lion Tooth Dagger(+1⚔︎))")
            pass
        elif d < ld:
            h = h - q2ran1
            print("You lost the fight and lost " + str(q2ran1) + "♥")
            pass
        elif d == ld:
            if qran1 > 0.5:
                inv.append("Lion Tooth Dagger (+1⚔︎)")
                d = d + 1
                print("You won the fight and earned (Lion Tooth Dagger (+1⚔︎))")
                pass
            elif qran1 < 0.5:
                h = h - q2ran1
                print("You lost the fight and lost "+str(q2ran1)+"♥")
                pass
    else:
        print("not a valid input")
        q1d2()

def check_game_over():
    global h
    if h <= 0:
        print("Game over. Your health reached 0 or below.")
        end_game()

def end_game():
    print("Thanks for playing!")
    exit()


name = input("Whats your name?")
q1d1()
check_game_over()
inventory_check()
q1d2()
check_game_over()
inventory_check()

print("health: " + str(h) + " damage: " + str(d)+" difficulty: " + str(dificulty))

#check inv for weapons that give perks
#add battles/quests that are randomly selected from dificulty ratings



#hi






import random
import time

h = 20
d = 1
difficulty = 1
crit_damage = 1.5
wh = 5
wd = 1
wc = 1.5

inv = []

def q1d1():
    global h
    global d
    print("You encounter a Wolf (" + str(wh) + "♥) (" + str(d) + "⚔︎)""| You have (" + str(h) + "♥) (" + str(d) + "⚔︎)")
    wolf()

def wolf():
    global h
    global d
    global wh
    global wd
    global wc

    while wh > 0:
        ran1 = random.randint(1, 101)
        q1ran1 = random.randint(1, 101)
        time.sleep(0.1)
        print("You: " + str(h) + "♥ " + "Wolf: " + str(wh) + "♥")
        qthing = input("Run or Fight?: ")
        qthing = qthing.lower()

        if qthing == "run":
            print("You escape with " + str(h) + "♥")
            break
        elif qthing == "fight":
            time.sleep (0.5)

            if int(ran1) >= 10:
                print("You damage the wolf for " + str(d) + "♥")
                wh = wh - d
                time.sleep(1)

                if int(q1ran1) >= 10:
                    print("The wolf counters and damages you for " + str(wd) + "♥")
                    h = h - wd
                elif int(q1ran1) < 10:
                    print("The wolf counters effectively and damages you for " + str(wc) + "♥")
                    h = h - wc

            elif int(ran1) < 10:
                print("You make a critical hit on the wolf for " + str(crit_damage) + "♥")
                wh = wh - crit_damage
                time.sleep(1)

                if int(q1ran1) >= 10:
                    print("The wolf counters and damages you for " + str(wd) + "♥")
                    h = h - wd
                elif int(q1ran1) < 10:
                    print("The wolf counters effectively and damages you for " + str(wc) + "♥")
                    h = h - wc



        else:
            print("not valid")
            wolf()

        if int(wh) == 0:
            print("you win")
            break
        if h <= 0:
            end_game()
    else:
        print("not a valid input")
        q1d1()

def end_game():
    print("Game over.")
    exit()

def next():
    print("next quest")
    pass
q1d1()
next()
