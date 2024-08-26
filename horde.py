import sys
import os
import time
import random

txt_sleep = .05

def write(*args):
    for arg in args:
        for char in str(arg):
            sys.stdout.write(str(char))
            sys.stdout.flush()
            time.sleep(.025 * txt_sleep)

### vars

dist_to_travel = 4000
player_position = 0
horde_position = -100
health = 100
sleep = 0
food = 25
water = 25
hunger = 50
thirst = 50
game_time = 0

write("A zombie apocalypse has broken out...")
time.sleep(.6 * txt_sleep)
write(" oooooooooooo...")
time.sleep(.3 * txt_sleep)
write(" scary\n")
time.sleep(.6 * txt_sleep)

("Your goal is to make it 4km away from the starting position, to reach a military base. A horde of zombies are following you, be quick.\n\n")

foodtypes = ["Canned peaches","MRE","Tomato Soup","Canned Chicken","Canned Peas","Fresh apple","Chicken nuggets","Grilled cheese","Salad","a Burrito","a Rock","Rice","Pizza slice","Old Sandwich","Spam","a Bag of chips","Pie slice","Cardboard","Canned tuna"]
drinktypes = ["Water","Water","Water","Water","Milk","Smoothie"]
def check(typed):
    global game_time
    global player_position
    if typed == "p":
        os.system('cls')
        write("Quitting...")
    elif typed == "q":
        status()
        menu()
    elif typed == "a":
        game_time += 1
        player_position += random.randint(80,120)
        menu()
    elif typed == "s":
        game_time += 1
        player_position += random.randint(25,45)
        menu()
    else:
        check(str.lower(input("Input error, please try again: ")))

def statcheck(typed):
    global food
    global water
    global hunger
    global thirst
    global sleep
    if typed == "p":
        os.system('cls')
        write("Quitting...")
    elif typed == "q":
        menu()
    elif typed == "d":
        statcheck(str.lower(input("Input: ")))
    elif typed == "f":
        if food > 0:
            food += random.randint(5,15)
            write("You have eaten ", random.choice(foodtypes),"\n")
        else:
            write("You have nothing to eat.\n")
        statcheck(str.lower(input("Input: ")))
    elif typed == "g":
        if water > 0:
            water += random.randint(5,15)
            write("You have drank ", random.choice(drinktypes),"\n")
        else:
            write("You have nothing to drink.\n")
        statcheck(str.lower(input("Input: ")))
    else:
        statcheck(str.lower(input("Input error, please try again: ")))

def status():
    print("\n\n\n┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Status ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    write("\nHealth: ", health," %")
    write("\n\nFood left: ", food," food")
    write("\nWater left: ", water," water")
    write("\n\nTiredness: ", sleep," %")
    write("\nHunger: ", hunger," %")
    write("\nThirst: ", thirst," %")

    print("\n\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")

    write("Q = Menu\n")
    write("D = Rest\n")
    write("F = Eat\n")
    write("G = Drink\n")
    write("P to Quit\n")

    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n")
    statcheck(str.lower(input("Input: ")))

def menu():
    print("\n\n\n════════════════ Menu ════════════════")

    write("\nHour: ", game_time)
    write("\nDistance left: ", dist_to_travel - player_position, "m")
    write("\nHorde distance: ", player_position - horde_position, "m")

    print("\n\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")

    write("Q = Status\n")
    write("A = Run\n")
    write("S = Walk\n")
    write("P to Quit\n")

    print("══════════════════════════════════════\n")
    check(str.lower(input("Input: ")))

menu()