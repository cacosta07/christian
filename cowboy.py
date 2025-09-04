import sys
import os
import time
import random
import numpy as np
from sty import RgbFg, Style, fg, bg, ef, rs

txt_sleep = .2

def write(*args):
    for arg in args:
        for char in str(arg):
            sys.stdout.write(str(char))
            sys.stdout.flush()
            time.sleep(.05 * txt_sleep)


def instant(*args):
    for arg in args:
        sys.stdout.write(arg)
        sys.stdout.flush()


fg.orange = Style(RgbFg(255, 150, 30))
fg.li_orange = Style(RgbFg(255, 190, 60))
fg.brown = Style(RgbFg(110, 50, 20))

#☀︎◐
# ┌╖
# ┤╠╝
#╘╞╟
# ┤╟
#█▓▒░

def dayArt():
    instant("\n  " + fg.white + "☀︎" + fg.orange +
            "      ░░░░  ┌╖          ░░░░░░░░     \n")
    instant("     ┌╖  ░░░░░ ┤╠╝   ┌╖    ░░░░░░░░     \n")
    instant("  ▓  ┤╟ ░░░░░░╘╞╟   ╘╡╟  ░░░░▓░░░░░░░░  \n")
    instant("▐▓▓▒▒╡╟▒▒▓▓▒▒▒▒┤╟▒▒▒╘╡╟▒▒▒▒▒▓▓▓▓▒▒▒▓▓▒▒▌\n")
    instant(fg.brown)
    instant("▐██████████████████████████████████████▌")
    instant(rs.all + "\n")


def nightArt():
    instant(bg.da_blue)
    instant("\n  " + fg.white + "◐" + fg.blue +
            "      ░░░░  ┌╖          ░░░░░░░░     \n")
    instant("     ┌╖  ░░░░░ ┤╠╝   ┌╖    ░░░░░░░░     \n")
    instant("  ▓  ┤╟ ░░░░░░╘╞╟   ╘╡╟  ░░░░▓░░░░░░░░  \n")
    instant("▐▓▓▒▒╡╟▒▒▓▓▒▒▒▒┤╟▒▒▒╘╡╟▒▒▒▒▒▓▓▓▓▒▒▒▓▓▒▒▌\n")
    instant(fg.da_cyan)
    instant("▐██████████████████████████████████████▌")
    instant(rs.all + "\n")


def dayTown():

    instant("\n  " + fg.white + "☀︎" + fg.li_orange +
            r"              /ô\                    " + "\n")
    instant(r"      /ô\      /╓╬┼╬╖\        ±         " + "\n")
    instant(r"    /ó╬╬╬ò\  /╧╩╩╩╪╩╩╩╧\     /ô\   ░░░  " + "\n")
    instant(r" ░░/╨╨╨╨╨╨╨\ ▐═▀═▀╬▀═▀═▌ ░░ /╨╨╨\ ░░░░░ " + "\n")
    instant(r"▐░░▐ ▓▌ ▀▀ ▌░▐ ▓▌ ║ ▓▌ ▌░░░░▐■▓■▌░░░░░░▌" + "\n")
    instant(fg.brown)
    instant(r"▐██████████████████████████████████████▌")
    instant(rs.all + "\n")


def nightTown():
    instant(bg.da_blue)
    instant("\n  " + fg.white + "◐" + fg.blue +
            r"              /ô\                    " + "\n")
    instant(r"      /ô\      /╓╬┼╬╖\        ±         " + "\n")
    instant(r"    /ó╬╬╬ò\  /╧╩╩╩╪╩╩╩╧\     /ô\   ░░░  " + "\n")
    instant(r" ░░/╨╨╨╨╨╨╨\ ▐═▀═▀╬▀═▀═▌ ░░ /╨╨╨\ ░░░░░ " + "\n")
    instant(r"▐░░▐ ▓▌ ▀▀ ▌░▐ ▓▌ ║ ▓▌ ▌░░░░▐■▓■▌░░░░░░▌" + "\n")
    instant(fg.da_cyan)
    instant(r"▐██████████████████████████████████████▌")
    instant(rs.all + "\n")


def jailArt():
    instant(bg.da_red + fg.orange + "\n")
    instant("       ▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄       \n")
    instant("       ▐│Ω     █ █▀█ █ █      Ω│▌       \n")
    instant("   ░░  ▐│     ▄█ █▀█ █ █▄▄     │▌       \n")
    instant("   ░░░ ▐│                ╒╤╤╤╕ │▌  ┌╖   \n")
    instant(" ░░░░░ ▐│     ▄▀▀▀▀▄     │││││ │▌░░┤╠╝  \n")
    instant(" ░░░░░ ▐│    ▐║    ║▌    ╞╪╪╪╡ │▌░╘╞╟ ░ \n")
    instant(" ░░░░░░▐│    ▐╠╤╕╒╤╣▌    │││││ │▌░░┤╟ ░ \n")
    instant("▐▒▒▒▒▒▒▐│    ▐╠╧╛╘╧╣▌    ╘╧╧╧╛ │▌▒▒▒▒▒▒▌\n")
    instant("▐██████████████████████████████████████▌")
    instant(rs.all + "\n")

### vars

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

dist_to_travel = 20000
isInTown = 0
isInJail = 0
isDay = 0
player_position = 0
police_position = -100
health = 100
alertness = 100
money = 20 + random.randint(-5, 5)
food = 4
water = 4
hunger = 70
thirst = 80
game_time = 0

print(rs.all)

foodtypes = [
    #"Canned peaches", "MRE", "Tomato Soup", "Canned Chicken", "Canned Peas",
    #"Fresh apple", "Chicken nuggets", "Grilled cheese", "Salad", "a Burrito",
    #"a Rock", "Rice", "Pizza slice", "Old Sandwich", "Spam", "a Bag of chips",
    #"Pie slice", "Cardboard", "Canned tuna"
    "Canned Peaches", "Tomato Soup", "Canned Peas", "a Fresh Apple", "a Salad",
    "a Taco", "a Rock", "a Burrito", "an Old Sandwich", "a Pie Slice", "a Rusty Nail",
    "Canned Corn", "Oat Biscuits", "Cheese", "Pumpernickel Muffin", "a Carrot",
    "a Pickle", "a Hard-Boiled Egg", "a Rotten Apple", "a Granola Bar", "a Candy Bar",
    "a Chicken Drumstick", "a whole living fish", "Beef Jerky", "Beef Jerky", 
    "a Hardtack Cracker", "a Hardtack Cracker", "Cornbread", "Wild Berries",
    "Soggy Bread", "Rotten Meat", "Moldy Cheese", "Canned Chicken", "Canned Tuna", 
    "Salt Pork", "Leather", "Fruit Leather", "Pemmican" ,"Pemmican", "Pemmican",
    "Crow Meat", "Lizard Meat", "a T-Bone Steak", "Teeth"
]
drinktypes = [
    #"Water", "Water", "Water", "Water", "Milk", "Smoothie", "Dr. Pepper",
    #"Pepsi", "Coca-Cola", "Coffee", "Orange juice", "Sludge", "Blood",
    #"Cooking oil", "Lemonade", "McDonalds Sprite"
    "Water", "Water", "Water", "Water", "Water", "Water", "Water", "Muddy Water",
    "Tea", "Milk", "Milk", "Old Milk", "Whiskey", "Moonshine", "Beer", "Ale",
    "Vinegar", "Lemonade", "Mystery Goo", "Coca-Cola", "Cider", "Hot Chocolate"
]

##############intro

dayArt()
time.sleep(1.5 * txt_sleep)
write(
    fg.li_yellow +
    "You are a wanted criminal, on the run from\nthe law after failing to rob a bank.\n"
)
write(
    "You have to make it 20km away from the starting\nposition to find somewhere safe to stay.\n\n", player_position
)
write("The police are following you,")
time.sleep(.5 * txt_sleep)
write(" good luck.\n\n")
time.sleep(1)


def check(typed):

    if isInJail:
        return jail()

    global game_time
    global isInTown
    global isDay
    global player_position
    global police_position
    global hunger
    global money
    global thirst
    global alertness
    global food
    global water

    if typed == "q":
        explore()
    if typed == "w":
        if isInTown == 1:
            townShop()
    if typed == "t":
        tips()
    if typed == "a":
        game_time += 1
        mvmt = random.randint(360, 440)
        if isInTown:
            write("You have run ", mvmt, " meters out of town.\n")
            isInTown = 0
        else:
            write("You have run ", mvmt, " meters.\n")
        player_position += mvmt
        hunger -= random.randint(6, 10)
        thirst -= random.randint(8, 12)
        alertness -= random.randint(4, 12)
        police_position += 200
        gamecheck()
    if typed == "s":
        game_time += 1
        hunger -= random.randint(1, 4)
        thirst -= random.randint(2, 6)
        alertness -= random.randint(2, 5)
        mvmt = random.randint(180, 220)
        police_position += 200
        if isInTown:
            write("You have walked ", mvmt, " meters out of town.\n")
            isInTown = 0
        else:
            write("You have walked ", mvmt, " meters.\n")
        player_position += mvmt
        gamecheck()
    if typed == "p":
        os.system('cls')
        write(rs.all + "Quitting...")
        exit()
    if typed == "d":
        if alertness < 100:
            alertness += 30 + (isInTown * 10) + (np.abs(isDay-1)*10)
            game_time += 2
            hunger -= random.randint(1, 3)
            thirst -= random.randint(2, 4)
            police_position += 400
            if alertness > 100:
                alertness = 100
            if isInTown:
                if isDay:
                    write("You rest for two hours in a hotel. You are now ",
                      alertness, "% alert.\n")
                else:
                    write("You rest for two hours in a hotel at night. You are now ",
                      alertness, "% alert.\n")
            else:
                if isDay:
                    write("You rest for two hours. You are now ", alertness,
                      "% alert.\n")
                else:
                    write("You rest for two hours at night. You are now ", alertness,
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
                write("You have eaten ", random.choice(foodtypes))
                print("\nHunger is now", hunger, "%\n")
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
                write("You have drank ", random.choice(drinktypes))
                print("\nThirst is now", thirst, "%\n")
            else:
                write("You are not thirsty enough.\n")
        else:
            write("You have nothing to drink.\n")
    if typed == "":
        instant("Refreshing...\n")
        menu()
    check(str.lower(input("Input: ")))


def gamecheck():
    global police_position
    global player_position
    global hunger
    global money
    global thirst
    global health
    global alertness
    global game_time
    global isDay

    if (game_time // 12) % 2 == 0:
        if not isDay:
            if isInTown:
                dayTown()
                write(fg.yellow)
            else:
                dayArt()
                write(fg.yellow)
        isDay = True
    else:
        if isDay:
            if isInTown:
                nightTown()
                write(fg.yellow)
            else:
                nightArt()
                write(fg.yellow)
        isDay = False

    if (alertness <= 25) and not (alertness <= 0):
        write(
            bg.white + fg.black +
            "\nYou are getting really tired, sleeping when you get the chance would be smart."
        )
        print(rs.all + fg.li_yellow)

    if hunger <= 0:
        health -= random.randint(5, 15)
        hunger = 0
        write(
            bg.white + fg.black +
            "\nYou are dying of hunger! Eat some food to bring your hunger level up."
        )
        print(rs.all + fg.li_yellow)

    if thirst <= 0:
        health -= random.randint(5, 15)
        thirst = 0
        write(
            bg.white + fg.black +
            "\nYou are dying of thirst! Drink something to bring your thirst level up."
        )
        print(rs.all + fg.li_yellow)

    if alertness <= 0:
        alertness = random.randint(20, 40)
        health -= 10
        game_time += 4
        police_position += 800
        write(
            bg.white + fg.black +
            "\nYou fall unconsious where you are and wake up 4 hours later. You are now ",
            alertness, "% alert.")
        print(rs.all + fg.li_yellow)

    if (player_position - police_position
            <= 75) and not (player_position - police_position <= 0):
        write(
            bg.white + fg.black +
            "\nYou start to hear the cops approach closer... maybe it is time to run."
        )
        print(rs.all + fg.li_yellow)

    if (player_position - police_position <= 0):
        write(rs.all + bg.red + "\nTHE COPS ARE HERE! Move ",
              abs(player_position - (police_position + 200)),
              " meters or get arrested.")
        print(rs.all + fg.li_yellow)
        if abs(player_position - (police_position + 200)) >= 220:
            write(bg.red + fg.black + "\nThe police have taken you in.")
            print(rs.all)
            jail()

    if alertness >= 80:
        health += 5

    if health > 100:
        health = 100

    if health <= 0:
        health = 0
        instant(bg.red + fg.black)
        time.sleep(1 * txt_sleep)
        write(".")
        time.sleep(1 * txt_sleep)
        write(".")
        time.sleep(1 * txt_sleep)
        write(".\n")
        time.sleep(1 * txt_sleep)
        write("You have died.")
        time.sleep(1)
        instant(rs.all)
        exit()

    if player_position >= 20000:
        write(
            "A voice calls out to you from the distance, you walk towards it...\n"
        )
        time.sleep(2 * txt_sleep)
        write(
            fg.li_green +
            "Hey, I know you! You're on the bounty pages!\nCome with me, I can help you out of the state.\n"
        )
        time.sleep(2 * txt_sleep)
        write("\nIt took you ", game_time, " hours.")
        write("\nThe police were ", player_position - police_position,
              " meters away.")
        instant(rs.all)
        exit()
    if random.randint(1, 10) == 5:
        event()


def explore():
    global alertness
    global police_position
    global money
    global food
    global water
    try:
        exploretime = abs(
            round(
                float(
                    input("\nHow many hours do you want to explore for?\n"))))
    except:
        write("Input was not a valid number... exiting to menu.\n")
        menu()
    try:
        if police_position + (200 * exploretime) > player_position:
            write(
                bg.white + fg.black +
                "\nThe cops will arrive at your position if you choose to explore\nfor ",
                exploretime, " hours. Choose 0 hours to stop exploring.")
            print(rs.all + fg.li_yellow)
            exploretime = abs(
                round(
                    float(
                        input("\nHow many hours do you want to explore for?\n")
                    )))
    except:
        write("Input was not a valid number... exiting to menu.\n")
        menu()
    police_advance = random.randint(180, 200)
    
    if isInTown:
        write("\nExploring town... ")
        time.sleep(1 * txt_sleep)
        plusfood = round((random.uniform(0, 15 * (exploretime))) / 30)
        pluswater = round((random.uniform(0, 20 * (exploretime))) / 30)
        plusmoney = round((random.uniform(0, 10 * (exploretime))) / 10)
    else:
        write("\nExploring... ")
        time.sleep(1 * txt_sleep)
        plusfood = round((random.uniform(0, 10 * (exploretime * 3))) / 20)
        pluswater = round((random.uniform(0, 20 * (exploretime * 2))) / 20)
        plusmoney = round((random.uniform(0, 15 * (exploretime))) / 10)
    police_position += police_advance * exploretime
    alertness -= random.randint(3, 6) * exploretime
    write("You have found ", plusfood, " food, ", pluswater, " drinks, and ",
          plusmoney, " dollars.\n")
    write("The police have advanced by ", police_advance * exploretime,
          " meters.\n")
    write("You are ", alertness, "% alert after searching for ", exploretime,
          " hour(s).\n\n")
    food += plusfood
    water += pluswater
    money += plusmoney
    gamecheck()


events = [
    "trip", "foundfood", "foundwater", "robbed", "healthtonic", "trade", "rob",
    "train",
    "town", "town", "town", "town", "town", "town"
]


def town():
    global money
    global food
    global water
    global health
    global alertness
    global police_position
    global player_position
    global game_time
    global isInTown

    isInTown = 1

    if isDay:
        dayTown()
    else:
        nightTown()

    write("\nYou have entered a town, you\ncan buy food and water here.\n")
    write("You have ", money, "$ to spend.\n")

    townShop()


def townShop():

    def checkShop(typed):
        global money
        global food
        global water
        global health
        global alertness
        global police_position
        global player_position
        global game_time
        global isInTown

        if typed == "a":
            if money >= 5:
                money -= 5
                food += 1
                write("You have bought food for 5$.\n")
            else:
                write("You dont have enough money.\n")
        if typed == "s":
            if money >= 3:
                money -= 3
                water += 1
                write("You have bought water for 3$.\n")
            else:
                write("You dont have enough money.\n")
        if typed == "d":
            if money >= 10:
                money -= 10
                health += 30
                if health > 100:
                    health = 100
                write("You have bought a health tonic for 10$.\n")
                write("You are now 30% healthier.\n")
            else:
                write("You dont have enough money.\n")
        if typed == "f":
            if food >= 1:
                money += 5
                food -= 1
                write("You have sold food for 5$.\n")
            else:
                write("You dont have any food to sell.\n")
        if typed == "g":
            if water >= 1:
                money += 3
                water -= 1
                write("You have sold water for 3$.\n")
            else:
                write("You dont have any water to sell.\n")
        if typed == "h":
            if money >= 15:
                money -= 15
                alertness += 40
                if alertness > 100:
                    alertness = 100
                write("You have drank a fresh coffee for 15$.\n")
                write("You are now 40% more awake.\n")
            else:
                write("You dont have enough money.\n")

        if typed == "q":
            try:
                if str.lower(input("The police will be atleast 400 meters away from you, are you sure? y/n ")) == "y":
                    if player_position - police_position > 200:
                        write("You rob the shop and run out of town.\n")
                        money += random.randint(20, 70)
                        food += random.randint(1, 3)
                        water += random.randint(1, 4)
                        game_time += 1
                        isInTown = 0
                        if player_position - police_position > 400:
                            police_position = 400
                        menu()
                    else:
                        write("No, it's too risky. The police are too close.\n")
                        townShop()
            except:
                townShop()
        if typed == "":
            instant("Refreshing...\n")
            menu()
        townShop()

    print(fg.orange)
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Shop ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    print("A = Buy food")
    print("S = Buy water")
    print("D = Buy health tonic")
    print("H = Buy fresh coffee\n")
    print("F = Sell food")
    print("G = Sell water\n")
    print("Q = Rob the shop\n")

    print("Enter to go back to menu")

    print("┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")
    checkShop(str.lower(input("Shop: ")))


def jail():
    global game_time
    global money
    global food
    global water
    global health
    global hunger
    global thirst
    global alertness
    global police_position
    global player_position
    global isInJail
    global escapeChance

    if isInJail == 0:  
        money = round(money/2)
        food = 0
        water = 0
        health += 5
        escapeChance = random.randint(2, 20)
        if health > 100:
            health = 100
        if alertness < 0:
            alertness = 10

        isInJail = 1
        jailArt()

    def checkJail(typed):
        global game_time
        global money
        global food
        global water
        global health
        global hunger
        global thirst
        global alertness
        global police_position
        global player_position
        global isInJail
        global escapeChance
        if typed == "a":
            game_time += 1
            health += 1
            hunger -= random.randint(4,7)
            thirst -= random.randint(4,8)
            alertness -= random.randint(10,14)
            money += 1
            escapeChance += random.randint(0,2)
            write("You worked hard for an hour, earning a whole dollar.\n")
        if typed == "s":
            if random.randint(0,1) == 1:
                write("You intimidate a prisoner, ")
                if not random.randint(0,2) == 1:
                    write("and he fights back.\nYou earn nothing and look like a fool.\n")
                    money -= 1
                    health -= random.randint(4,12)
                    alertness -= random.randint(6,12)
                else:
                    instant(ef.bold)
                    write("and he gives in, handing over what\nlittle money he saved up. Monster.\n")
                    instant(rs.ef)
                    money += random.randint(2, 5)
                    escapeChance += random.randint(0,1)
            else:
                write("\nYou intimidate a guard, ")
                if not random.randint(0,3) == 1:
                    write("and he fights back. He thinks of\nyou as a fool but your cellmates respect it.\n")
                    health -= random.randint(4,12)
                    escapeChance += random.randint(2,7)
                    alertness -= random.randint(6,12)
                else:
                    instant(ef.bold)
                    write("he didn't let you out, but\nstill seems scared of you.\n")
                    instant(rs.ef)
                    escapeChance += random.randint(8,17)
        if typed == "d":
            write()
        if typed == "f":
            if game_time % 6:
                write("\nIt isn't chow time yet.\n")
            else:
                hunger += random.randint(50,60)
                game_time += 1
                write("\nYou take a tray of food back to\nyour cell to eat in peace.\n")
        if typed == "g":
            thirst += 30
            write("\nYou sip some water from the sink.\n")

        if typed == "q":
            if escapeChance + (15 if alertness > 80 else 0) < 30:
                write("\nThe chance of escaping successfully is less than 30%\n")
                if str.lower(input("Continue? y/n ")) == "y":
                    if random.randint(0,100) < escapeChance + (15 if alertness > 80 else 0):
                        write("You successfully escape! However, they noticed fairly quickly and\nare back on your tail.")
                        isInJail = 0
                        player_position += 500
                        police_position = player_position - 500
                        menu()
                    else:
                        write("You have failed to escape. Dummy.\n\n")
                        if money > 0:
                            write("A guard catches you and throws you back in your cell, all\nof that work for nothing, he even took your money...\n\n")
                        else:
                            write("A guard catches you and throws you back in your cell, he\ntried to search your pockets for money, but found nothing")
                            time.sleep(.3 * txt_sleep)
                            instant(".")
                            time.sleep(.3 * txt_sleep)
                            instant(".")
                            time.sleep(.3 * txt_sleep)
                            instant(".")
                            time.sleep(.4 * txt_sleep)
                            write(" Broke boy.\n\n")
                        money = 0
                        escapeChance = random.randint(2,10)
                        alertness -= 5
        if typed == "":
            instant("Refreshing...\n")
            jail()

        checkJail(str.lower(input("Input: ")))
    if alertness >= 80:
        health += 5

    if health > 100:
        health = 100

    if hunger > 100:
        hunger = 100

    if thirst > 100:
        thirst = 100

    if escapeChance > 100:
        escapeChance = 100

    if health <= 0:
        health = 0
        instant(bg.red + fg.black)
        time.sleep(1 * txt_sleep)
        write(".")
        time.sleep(1 * txt_sleep)
        write(".")
        time.sleep(1 * txt_sleep)
        write(".\n")
        time.sleep(1 * txt_sleep)
        write("You have died.")
        time.sleep(1)
        instant(rs.all)
        exit()

    if alertness <= 0:
        alertness = random.randint(20, 40)
        health -= 10
        game_time += 4
        write(
            bg.li_red + fg.black +
            "\nYou fall unconsious where you are and wake up 4 hours later. You are now ",
            alertness, "% alert.")
        print(rs.all + fg.li_red)

        jail()
    
                    

            
            

    time.sleep(1 * txt_sleep)

    print(fg.da_red)
    print("╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪ Jail ╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪\n")

    instant("Hour: ", str(game_time))
    if isDay:
        instant(" ☀︎\n")
    else:
        instant(" ◐\n")

    instant("\nMoney left: ", str(money), "$\n")
    instant("Health: ", str(health), "%\n")
    instant("Alertness: ", str(alertness), "%\n")
    instant("Hunger: ", str(hunger), "%\n")
    instant("Thirst: ", str(thirst), "%\n")

    print("┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")

    print("A = Work")
    print("S = Intimidate")
    print("D = Rest")

    if game_time % 6:
        instant(ef.dim)
    instant("\nF = Eat Mush")
    if game_time % 6:
        instant(" (Not chow time)")
    instant(rs.ef)

    print("\nG = Drink Water\n")
    
    instant("Q = Attempt Escape (", str(escapeChance), "%")
    if alertness > 80:
        instant(" + 15% Alertness Boost)\n")
    else:
        instant(")\n")
    
    print("\n╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪╪\n" + fg.li_red)
    checkJail(str.lower(input("Input: ")))



def event():
    global food
    global water
    global health
    global game_time
    global player_position
    global police_position
    global money

    if player_position < 19800 and player_position - police_position > 0:
        event = random.choice(events)
        if event != "town":
            print(fg.li_magenta + "\n░░░░░░░░░░░░ RANDOM EVENT ░░░░░░░░░░░░\n")
        if event == "town":
            town()
        if event == "trip":
            if water > 0 and food > 0:
                write(
                    "You tripped. it didnt hurt, but you seem\nto be missing something from your bag..."
                )
                if random.randint(0, 1) == 1:
                    food -= 1
                else:
                    water -= 1
            else:
                write(
                    "You tripped... brushed it off...\nand walked away unscathed."
                )
        if event == "foundfood":
            write(
                "While looking around, you found a lunchbox\nwith some food in it... how lucky!"
            )
            food += 1
        if event == "foundwater":
            write(
                "While looking around, you see a drink that\nhas been left alone, finders keepers!"
            )
            water += 1
        if event == "robbed":
            time.sleep(1 * txt_sleep)
            write(".")
            time.sleep(1 * txt_sleep)
            write(".")
            time.sleep(1 * txt_sleep)
            write(".\n")
            time.sleep(1 * txt_sleep)
            write(
                "You wake up dizzy behind a boulder next to your bag.\nYour head hurts, and your bag is empty... you were robbed.\n"
            )
            food = 0
            water = 0
            health -= 10
            game_time += 1
            police_position += 200
            money = 0
        if event == "healthtonic":
            write(
                "You trip over something on the floor... its dusty and half-buried...\nits a full health tonic! You feel much better now.\n"
            )
            health = 100
        if event == "trade":
            write(
                "A man jumps out of a bush and calls to you, he desperately needs food-\nand is willing to trade his drinks.\n"
            )
            if str.lower(input("Give him food? y/n ")) == "y":
                if food >= 1:
                    write(
                        "The man thanks you and hands you two drinks in turn for one\nof your food items. He gives a smile and you carry on.\n"
                    )
                    food -= 1
                    water += 2
                else:
                    write(
                        "You apologize to the man and carry on, as you have no food.\n"
                    )
            else:
                write("You ignore the man and carry on.\n")
        if event == "rob":
            write(
                "You see a wealthy looking man and his guard riding on a stagecoach.\n"
            )
            if str.lower(input("Rob him? y/n ")) == "y":
                if random.randint(0, 4) == 2:
                    write(
                        "You try to rob the man, but the guard attacks you.\n")
                    write(
                        "You fight back and gather some money, but lose 20 health.\n"
                    )
                    money += random.randint(5, 15)
                    health -= 20

                else:
                    write(
                        "You rob the man successfully and run away with his money.\n"
                    )
                    money += random.randint(30, 50)
        if event == "train":
            write("You hop on a train that stopped nearby, and it takes you a little\nwhile away but eventually stops again.")
            player_position += 1200

        print("\n\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print(rs.all + fg.li_yellow)
        gamecheck()

def tips():
    print(fg.white + "\n════════════════════ Tips ════════════════════\n")

    write("• Every hour, the police advance around 200 meters.\n")
    write("• Resting will always take 2 hours.\n")
    write(
        "• Falling unconsious from being too\ntired is extremely dangerous.\n")
    write("• Sleeping at night and or sleeping in a hotel\nallows you rest very well\n")
    write("• Walking is half as fast, but far over twice as efficient.\n")
    write(
        "• Searching for food and water isn't efficient\nin towns, as they are already scoured.\n"
    )
    write(
        "• You get thirsty faster than you get hungry,\nbut water is easier to find.\n"
    )
    write(
        "• Random events can be good or bad,\nhope that you get one of the good ones.\n"
    )
    write("• Almost everything takes away a small amount of alertness.\n")
    write("• Having a high alertness heals you by 5 Health every hour.\n")
    write("• Dying is really, REALLY bad for the human body.\n")

    print(fg.white + "\n══════════════════════════════════════════════\n" +
          fg.li_yellow)

def menu():
    global isInTown
    global isInJail

    if isInJail:
        return jail()

    def opendanger(type, subtype):
        if type == "basic" and subtype <= 20:
            instant(fg.red)
        if type == "inventory" and subtype < 1:
            instant(fg.red)
        if type == "police" and subtype < 50:
            instant(fg.red)

    def closedanger():
        instant(fg.li_blue)

    print(rs.all)
    print(fg.li_yellow + "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    print(fg.green + "═══════════════ Watch ════════════════")

    instant("Hour: ", str(game_time))
    if isDay:
        instant(" ☀︎\n")
    else:
        instant(" ◐\n")
    print("Distance left:", dist_to_travel - player_position, "m")
    opendanger("police", player_position - police_position)
    print("Police distance:", player_position - police_position, "m")
    instant(fg.green)

    print(fg.green + "══════════════════════════════════════")

    print(fg.li_blue)
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Menu ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    opendanger("basic", health)
    instant("Health: ", str(health), "%")
    closedanger()
    opendanger("inventory", money)
    instant("\nMoney left: ", str(money), "$\n")
    opendanger("inventory", food)
    print("\nFood left:", food, "food")
    closedanger()
    opendanger("inventory", water)
    print("Water left:", water, "water")
    closedanger()
    opendanger("basic", alertness)
    instant("\nAlertness: ", str(alertness), "%\n")
    closedanger()
    opendanger("basic", hunger)
    instant("Hunger: ", str(hunger), "%\n")
    closedanger()
    opendanger("basic", thirst)
    instant("Thirst: ", str(thirst), "%\n")
    closedanger()

    print("┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉")

    if (isInTown == 1):
        
        print(fg.orange + ef.bold + "W = Explore the shops\n" + fg.li_blue + rs.ef)

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
    print(fg.li_yellow + "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")

    check(str.lower(input("Input: ")))

txt_sleep = .5
menu()