import sys
import os
import time
import random
from colorama import Fore, Back, Style

txt_sleep = 1


def write(*args):
    for arg in args:
        for char in str(arg):
            sys.stdout.write(str(char))
            sys.stdout.flush()
            time.sleep(.06 * txt_sleep)

def instant(*args):
    for arg in args:
        sys.stdout.write(arg)
        sys.stdout.flush()
### vars

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

dist_to_travel = 5000
player_position = 0
horde_position = -100
health = 100
alertness = 100
food = 4
water = 4
hunger = 70
thirst = 80
game_time = 0
print(Style.RESET_ALL)
print(Fore.RED)
write("A zombie apocalypse has broken out...")
time.sleep(.6 * txt_sleep)
write(" oooooooooooo...")
time.sleep(.3 * txt_sleep)
write(" scary.\n\n")
time.sleep(.6 * txt_sleep)
write("Your goal is to make it 5km away from the starting position, to reach a military base. A horde of zombies are following you, be smart.\n\n")

foodtypes = [
    "Canned peaches", "MRE", "Tomato Soup", "Canned Chicken", "Canned Peas",
    "Fresh apple", "Chicken nuggets", "Grilled cheese", "Salad", "a Burrito",
    "a Rock", "Rice", "Pizza slice", "Old Sandwich", "Spam", "a Bag of chips",
    "Pie slice", "Cardboard", "Canned tuna"
]
drinktypes = [
    "Water", "Water", "Water", "Water", "Milk", "Smoothie", "Dr. Pepper",
    "Pepsi", "Coca-Cola", "Coffee", "Orange juice", "Sludge","Blood","Cooking oil",
    "Lemonade","McDonalds Sprite"
]


def check(typed):
    global game_time
    global player_position
    global horde_position
    global hunger
    global thirst
    global alertness
    global food
    global water

    if typed == "q":
        explore()
    if typed == "t":
        tips()
    if typed == "a":
        game_time += 1
        mvmt = random.randint(160, 240)
        write("You have run ", mvmt, " meters.\n")
        player_position += mvmt
        hunger -= random.randint(6, 10)
        thirst -= random.randint(8, 12)
        alertness -= random.randint(4,12)
        horde_position += 100
        gamecheck()
    if typed == "s":
        game_time += 1
        hunger -= random.randint(1, 4)
        thirst -= random.randint(2, 6)
        alertness -= random.randint(2,5)
        mvmt = random.randint(60, 120)
        horde_position += 100
        write("You have walked ", mvmt, " meters.\n")
        player_position += mvmt
        gamecheck()
    if typed == "p":
        os.system('cls')
        write(Style.RESET_ALL + "Quitting...")
        exit()
    if typed == "d":
        if alertness < 100:
            alertness += 40
            game_time += 2
            hunger -= random.randint(1, 3)
            thirst -= random.randint(2, 4)
            horde_position += 200
            if alertness > 100:
                alertness = 100
            write("You rest for two hours. You are now ", alertness,
                  "% alert.\n")
            gamecheck()
        else:
            write("You try to sleep but aren't tired.\n")
    if typed == "f":
        if food > 0:
            if hunger <= 99:
                hunger += random.randint(10, 20)
                food -= 1
                if hunger > 100:
                    hunger = 100
                write("You have eaten ", random.choice(foodtypes), "\n")
                write("Hunger level is now ",hunger,"%\n")
            else:
                write("You are not hungry enough.\n")
        else:
            write("You have nothing to eat.\n")
    if typed == "g":
        if water > 0:
            if thirst <= 99:
                thirst += random.randint(5, 20)
                water -= 1
                if thirst > 100:
                    thirst = 100
                write("You have drank ", random.choice(drinktypes), "\n")
                write("Thirst level is now ",thirst,"%\n")
            else:
                write("You are not thirsty enough.\n")
        else:
            write("You have nothing to drink.\n")
    if typed == "":
        menu()
    check(str.lower(input("Input: ")))


def gamecheck():
    global horde_position
    global player_position
    global hunger
    global thirst
    global health
    global alertness

    if (alertness <= 25) and not (alertness <= 0):
        write(Back.WHITE + "\nYou start to hear the horde approach closer... maybe it is time to run.")
        print(Style.RESET_ALL + Fore.YELLOW)

    if hunger <= 0:
        health -= random.randint(5, 15)
        hunger = 0
        write(Back.WHITE +
            "\nYou are dying of hunger! Eat some food to bring your hunger level up.")
        print(Style.RESET_ALL + Fore.YELLOW)

    if thirst <= 0:
        health -= random.randint(5, 15)
        thirst = 0
        write(Back.WHITE +
            "\nYou are dying of thirst! Drink something to bring your thirst level up.")
        print(Style.RESET_ALL + Fore.YELLOW)

    if alertness <= 0:
        alertness = random.randint(20, 40)
        health -= 10
        horde_position += 400
        write(Back.WHITE +
            "\nYou fall unconsious where you are and wake up 4 hours later. You are now ",alertness, "% alert.")
        print(Style.RESET_ALL + Fore.YELLOW)

    if (player_position - horde_position <= 50) and not (player_position - horde_position <= 0):
        write(Back.WHITE + "\nYou start to hear the horde approach closer... maybe it is time to run.")
        print(Style.RESET_ALL + Fore.YELLOW)

    if (player_position - horde_position <= 0) and not (player_position - horde_position <= 50):
        health -= 45
        write(Style.RESET_ALL + Back.RED + "\nTHE HORDE IS HERE, you have lost 45 health. Move ",abs(player_position - (horde_position+100))," meters or die.")
        print(Style.RESET_ALL + Fore.YELLOW)
        if abs(player_position - (horde_position+100)) >= 220:
            health = 0
            write(Back.RED + Fore.BLACK + "\nTHE HORDE IS HERE, you couldnt escape.")
            print(Style.RESET_ALL)

    if alertness >= 80:
        health += 5

    if health > 100:
        health = 100

    if health <= 0:
        health = 0
        instant(Back.RED + Fore.BLACK)
        time.sleep(1 * txt_sleep)
        write(".")
        time.sleep(1 * txt_sleep)
        write(".")
        time.sleep(1 * txt_sleep)
        write(".\n")
        time.sleep(1 * txt_sleep)
        write("Your ears are ringing...\n")
        time.sleep(1 * txt_sleep)
        write("Your vision gets blurry...\n")
        time.sleep(1 * txt_sleep)
        write("You have died.")
        instant(Style.RESET_ALL)
        exit()

    if player_position >= 5000:
        write("\nYou see a large wall of concrete and barbed wire, a light shines on you...")
        time.sleep(2 * txt_sleep)
        write(Fore.LIGHTGREEN_EX + "\nThe gate opens and military personell walk out and pull you in. They see the horde coming, but its no match against the military.")
        write("You have sucessfully walked 5 kilometers without dying! Its time to take a good long nap...")
        write("\nIt took you ",game_time," hours.")
        write("\nThe horde was ",player_position - horde_position," meters away.")
        instant(Style.RESET_ALL)
        exit()
    if random.randint(1, 12) == random.randint(1, 12):
        event()

def explore():
    global alertness
    global horde_position
    global food
    global water
    try:
        exploretime = abs(round(float(input("\nHow many hours do you want to explore for?\n"))))
    except:
        write("Input was not a valid number... exiting to menu.\n")
        menu()
    try:
        if horde_position + (100 * exploretime) > player_position:
            write(
                Back.WHITE +
                "\nThe horde will arrive at your position if you choose to explore for ",exploretime," hours. Choose 0 hours to stop exploring."
            )
            print(Style.RESET_ALL + Fore.YELLOW)
            exploretime = round(int(input("\nHow many hours do you want to explore for?\n")))
    except:
        write("Input was not a valid number... exiting to menu.\n")
        menu()
    horde_advance = random.randint(90,100)
    write("\nExploring... ")
    time.sleep(1 * txt_sleep)
    plusfood = round((random.uniform(0,10) * exploretime)/10)
    pluswater = round((random.uniform(0,20) * exploretime)/10)
    horde_position += horde_advance * exploretime
    alertness -= random.randint(3,6) * exploretime
    write("You have found ",plusfood," food, and ",pluswater," drinks.\n")
    write("The horde has advanced by ",horde_advance * exploretime," meters.\n")
    write("You are ",alertness,"% alert after searching for ",exploretime," hour(s).\n\n")
    food += plusfood
    water += pluswater
    gamecheck()

events = ["trip","foundfood","foundwater","robbed","runningcar","explosion","medkit","distracthorde","trade"]

def event():
    global food
    global water
    global health
    global game_time
    global player_position
    global horde_position
    if player_position < 5000:
        print(Fore.MAGENTA + "\n░░░░░░░░░░░░ RANDOM EVENT ░░░░░░░░░░░░\n")
        event = random.choice(events)
        if event == "trip":
            if water > 0 and food > 0:
                write("You tripped... it didnt hurt, but you seem to be missing something from your bag...")
                if random.randint(0,1) == 1:
                    food -= 1
                else:
                    water -= 1
            else:
                write("You tripped... brushed it off... and walked away unscathed.")
        if event == "foundfood":
            write("While looking around, you found a lunchbox with some food in it... how lucky!")
            food += 1
        if event == "foundwater":
            write("While looking around, you see a drink that has been left alone, finders keepers!")
            water += 1
        if event == "robbed":
            time.sleep(1 * txt_sleep)
            write(".")
            time.sleep(1 * txt_sleep)
            write(".")
            time.sleep(1 * txt_sleep)
            write(".\n")
            time.sleep(1 * txt_sleep)
            write("You wake up dizzy in a room next to your bag... your head hurts, and your bag is empty... you were robbed.")
            food = 0
            water = 0
            health -= 10
            game_time += 1
            horde_position += 100
        if event == "runningcar":
            write("You spot a car in the distance, its left alone and is running. You hop in and drive until it... quickly fails. Dang.")
            write("\nYou were able to move 200 meters.")
            player_position += 200
        if event == "explosion":
            write("Hissssss.......\n")
            write("BOOM! A bomb exploded near you! It hurt terribly... as expected.")
            health -= 40
        if event == "medkit":
            write("You trip over something on the floor... its dusty and half-buried... its a medkit! You are healthy now.")
            health = 100
        if event == "distracthorde":
            write("Just for a second, you look back and see that the horde is missing... they are distracted while chasing somebody else.\n")
            write("The horde has travelled backwards by 150 meters.")
            horde_position -= 150
        if event == "trade":
            write("A man hiding in a hole calls out to you, he desperately needs food- and is willing to trade his drinks.\n")
            if str.lower(input("Give him food? y/n ")) == "y":
                if food >= 1:
                    write("The man thanks you and hands you two drinks in turn for one of your food items. He gives a smile and you carry on.")
                    food -= 1
                    water += 2
                else:
                    write("You apologize to the man and carry on, as you have no food.")
            else:
                write("You ignore the man and carry on.")

        print("\n\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print(Style.RESET_ALL + Fore.YELLOW)
    gamecheck()

def tips():
    print(Fore.WHITE + "\n════════════════════ Tips ════════════════════\n")

    write("Every hour, the horde moves around 100 meters.\n")
    write("Resting will always take 2 hours.\n")
    write("Falling unconsious from being too tired is extremely dangerous.\n")
    write("Walking is half as fast, but far over twice as efficient.\n")
    write("You get thirsty faster than you get hungry, but water is easier to find.\n")
    write("Random events can be good or bad, hope that you get one of the good ones.\n")
    write("Almost everything takes away a small amount of alertness.\n")
    write("Having a high alertness heals you by 5 Health every hour.\n")
    write("Dying is really, REALLY bad for the human body.\n")

    print(Fore.WHITE + "\n══════════════════════════════════════════════\n" + Fore.YELLOW)


def menu():

    def opendanger(type, subtype):
        if type == "basic" and subtype <= 20:
            instant(Fore.RED)
        if type == "inventory" and subtype < 1:
            instant(Fore.RED)
        if type == "horde" and subtype < 50:
            instant(Fore.RED)

    def closedanger():
        instant(Fore.BLUE)

    print(Style.RESET_ALL)
    print(Fore.YELLOW + "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    print(Fore.GREEN + "═══════════════ Watch ════════════════")

    print("Hour:", game_time)
    print("Distance left:", dist_to_travel - player_position, "m")
    opendanger("horde", player_position - horde_position)
    print("Horde distance:", player_position - horde_position, "m")
    instant(Fore.GREEN)

    print(Fore.GREEN + "══════════════════════════════════════")

    print(Fore.BLUE)
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Menu ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    opendanger("basic", health)
    print("Health:", health, "%")
    closedanger()
    opendanger("inventory", food)
    print("\nFood left:", food, "food")
    closedanger()
    opendanger("inventory", water)
    print("Water left:", water, "water")
    closedanger()
    opendanger("basic", alertness)
    print("\nAlertness:", alertness, "%")
    closedanger()
    opendanger("basic", hunger)
    print("Hunger:", hunger, "%")
    closedanger()
    opendanger("basic", thirst)
    print("Thirst:", thirst, "%")
    closedanger()

    print("┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")

    print("A = Run")
    print("S = Walk\n")
    print("Q = Explore\n")
    print("D = Rest")
    print("F = Eat")
    print("G = Drink\n")
    print("Enter to refresh menu")
    print("T for Tips")
    print("P to Quit")

    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n")
    print(Fore.YELLOW + "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

    check(str.lower(input("Input: ")))

txt_sleep = .5

menu()
