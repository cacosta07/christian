import sys
import os
import time
import random
from colorama import Fore, Back, Style

txt_sleep = 0

def write(*args):
    for arg in args:
        for char in str(arg):
            sys.stdout.write(str(char))
            sys.stdout.flush()
            time.sleep(.02 * txt_sleep)

### vars

print("\n\n\n\n\n\n\n\n\n\n\n")

dist_to_travel = 4000
player_position = 0
horde_position = -100
health = 100
alertness = 100
food = 10
water = 10
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
    global alertness
    global food
    global water

    if typed == "a":
        game_time += 1
        mvmt = random.randint(160,240)
        write("You have run ",mvmt," meters.\n")
        player_position += mvmt
        hunger -= random.randint(6,10)
        thirst -= random.randint(8,12)
        horde_position += 100
        gamecheck()
        menu()
    if typed == "s":
        game_time += 1
        hunger -= random.randint(1,4)
        thirst -= random.randint(2,6)
        mvmt = random.randint(80,120)
        horde_position += 100
        write("You have walked ",mvmt," meters.\n")
        player_position += mvmt
        gamecheck()
        menu()
    if typed == "p":
        os.system('cls')
        write("Quitting...")
        exit()
    if typed == "d":
        check(str.lower(input("Input: ")))
    if typed == "f":
        if food > 0:
            if hunger <= 85:
                hunger += random.randint(5,15)
                food -= 1
                write("You have eaten ", random.choice(foodtypes),"\n")
            else:
                write("You are not hungry enough.")
        else:
            write("You have nothing to eat.\n")
        check(str.lower(input("\nInput: ")))
    if typed == "g":
        if water > 0:
            if thirst <= 85:
                thirst += random.randint(5,15)
                water -= 1
                write("You have drank ", random.choice(drinktypes),"\n")
            else:
                write("You are not thirsty enough.")
        else:
            write("You have nothing to drink.\n")
        check(str.lower(input("\nInput: ")))
    else:
        menu()

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



def menu():
    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(Fore.GREEN)
    print("\n\n\n\n\n\n\n═══════════════ Watch ════════════════")

    print("Hour: ", game_time)
    print("Distance left: ", dist_to_travel - player_position, "m")
    print("Horde distance: ", player_position - horde_position, "m", end="")

    print("══════════════════════════════════════")

    print(Fore.BLUE)
    print("\n┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Status ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    print("Health: ", health," %")
    print("\nFood left: ", food," food")
    print("Water left: ", water," water")
    print("\nAlertness: ", alertness," %")
    print("Hunger: ", hunger," %")
    print("Thirst: ", thirst," %")

    print("\n\n┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")

    print("A = Run")
    print("S = Walk\n")
    print("D = Rest")
    print("F = Eat")
    print("G = Drink\n")
    print("Enter to refresh")
    print("P to Quit")

    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n")
    check(str.lower(input("Input: ")))

menu()
