import sys
import os
import time
import random
from colorama import Fore, Back, Style

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
print(Style.RESET_ALL)
print(Fore.RED)
write("A zombie apocalypse has broken out...")
time.sleep(.6 * txt_sleep)
write(" oooooooooooo...")
time.sleep(.3 * txt_sleep)
write(" scary\n")
time.sleep(.6 * txt_sleep)

("Your goal is to make it 4km away from the starting position, to reach a military base. A horde of zombies are following you, be quick.\n\n")

foodtypes = ["Canned peaches","MRE","Tomato Soup","Canned Chicken","Canned Peas","Fresh apple","Chicken nuggets","Grilled cheese","Salad","a Burrito","a Rock","Rice","Pizza slice","Old Sandwich","Spam","a Bag of chips","Pie slice","Cardboard","Canned tuna"]
drinktypes = ["Water","Water","Water","Water","Milk","Smoothie","Dr. Pepper","Pepsi","Coca-Cola","Coffee","Orange juice"]
def check(typed):
    global game_time
    global player_position
    global horde_position
    global hunger
    global thirst
    if typed == "p":
        os.system('cls')
        write("Quitting...")
    elif typed == "q":
        status()
        menu()
    elif typed == "a":
        game_time += 1
        mvmt = random.randint(160,240)
        write("You have run ",mvmt," meters.\n")
        player_position += mvmt
        hunger -= random.randint(6,10)
        thirst -= random.randint(8,12)
        horde_position += 100
        gamecheck()
        menu()
    elif typed == "s":
        game_time += 1
        hunger -= random.randint(1,4)
        thirst -= random.randint(2,6)
        mvmt = random.randint(80,120)
        horde_position += 100
        write("You have walked ",mvmt," meters.\n")
        player_position += mvmt
        gamecheck()
        menu()
    else:
        menu()

def statcheck(typed):
    print
    global food
    global water
    global hunger
    global thirst
    global sleep
    if typed == "p":
        os.system('cls')
        write("Quitting...")
        exit()
    elif typed == "q":
        menu()
    elif typed == "d":
        statcheck(str.lower(input("Input: ")))
    elif typed == "f":
        if food > 0:
            if hunger <= 85:
                hunger += random.randint(5,15)
                write("You have eaten ", random.choice(foodtypes),"\n")
            else:
                write("You are not hungry enough.")
        else:
            write("You have nothing to eat.\n")
        statcheck(str.lower(input("\nInput: ")))
    elif typed == "g":
        if water > 0:
            if thirst <= 85:
                thirst += random.randint(5,15)
                write("You have drank ", random.choice(drinktypes),"\n")
            else:
                write("You are not thirsty enough.")
        else:
            write("You have nothing to drink.\n")
        statcheck(str.lower(input("\nInput: ")))
    else:
        status()

def gamecheck():
    global hunger
    global thirst
    global health
    if hunger <= 0:
        health -= random.randint(5,15)
        hunger = 0
        write(Back.WHITE + "\nYou are dying of hunger! Eat some food to bring your hunger level up.")
        print(Style.RESET_ALL)
    if thirst <= 0:
        health -= random.randint(5,15)
        thirst = 0
        write(Back.WHITE + "\nYou are dying of thirst! Drink something to bring your thirst level up.")
        print(Style.RESET_ALL)
    if health <= 0:
        health = 0
        write(Back.RED + "you die")
        exit()

def event():
    if random.randint(0,15) == 15:
        print(Fore.RED +"event")

def status():
    print(Fore.BLUE)
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
    print(Fore.GREEN)
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
