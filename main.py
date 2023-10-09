import random
h = 20
d = 1
dificulty = 1
critchance = 5

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
        print("test")
        if d > wd:
            inv.append("Bone Sword (+0.5⚔︎)")
            d = d + 0.5
            print("You won the fight and earned (1x Bone Sword(+0.5⚔︎))")
            pass
        elif d < wd:
            h = h - q1ran1
            print("You lost the fight and lost " + str(q1ran1) + "♥")
            pass
        elif d == wd:
            if ran1 > 0.5:
                inv.append("Bone Sword(+0.5⚔︎)")
                d = d + 0.5
                print("You won the fight and earned (1x Bone Sword(+0.5⚔︎))")
                pass
            elif ran1 < 0.5:
                h = h - q1ran1
                print("You lost the fight and lost "+str(q1ran1)+"♥")
                pass
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
