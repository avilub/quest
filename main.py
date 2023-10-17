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

print("You encounter a Wolf")
time.sleep(0.1)
wolf()
q1d1()
print("idk")
