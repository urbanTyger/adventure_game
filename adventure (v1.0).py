import time
import random
from Audio.sounds import effects
from os import system, name  # needed for clearing the screen


# function lists
areas = ["House", "Lake", "Temple", "Cave", "Castle", "Fountain", "Cabin"]
Old_man_places = ["Cabin", "Castle", "Temple"]
zeus = random.choice(Old_man_places)
godly_items = ["Sheild of Athens", "Sword of Manil","Bag of Hell-Coins", "Peach", "Laughing Duck", "Glasses of Vision"]
standard_items = ["Copper sheild", "Sword of Useless Hope",
                  "Diamond Knife", "Helmet of Paris", "Battle stick", "Spear of the Mouse", "Pearl of the Sacred Clam", "Sacred Clam"]
items_desc = ["protects you immensly from attacks, limiting attack damage.", "cuts like a blade forged from the Sun, dealing major damage!",
              "helps you cross 'over' and bargain should you perish", "tempts and poisons the beast when it is off guard, should you hit its' mouth",
              "makes the monster laugh hard enough to eternally sleep (Super powered attack)", "helps you to see how much strength and items a monster has during a battle", "gives you some additional protection against damage.",
              "slashes more 'hopefull?'...", "gives sharp slashes", "protects your head better, obviously", "helps you fight better than your fists alone ", "....um, I actually have no idea..lol",
              "helps you sense the monsters' strength", "helps you sense if the monster has eaten anything useful"]
task = ["eating a burger", "drinking a cocktail","baking a cake", "singing horribly", "petting a cat", "swimming", "painting", "sculpting"]
monsters = ["gorgon", "medusa", "Burning Hell-Eagle", "Dragon", "Possessed King","Talking Cobra", "midnight fairy", "pink Elf", "rabid kanye west"]
m_final_attack = ["hisses you to death in the form of a song, a top-1000 chart hitter of the time.", "easily turns you to stone.", "screams burning hell-fire, toasting all of the worlds' dreams.", "eats you in a slow and painful chew.",
                  "makes the evil spirit possess you, destroying your will to live.", "talks you to death and then bites you with poison for good measure.",
                  "casts a hex on you, making you suffocate", "explodes taking out the world. Goodbye humanity.", "raps until you join his entourage, thereby destroying the world."]
minions = ["water elf", "troll", "golum", "bear", "fox", "minotaur",
           "phoenix", "rat", "bat", "gorilla", "cerebus", "pikachun", 
           "rattlesnake", "evil unicorn", "demon", "vulture", "lion", "land shark", 
           "dwarf", "giant"]
# empty lists
areas_been = []
monster = []
inventory = []
enemy_inv = []
enemy_battle = [0,0,0]
hero_health = [50, 100, 0]
# music and effects
boss_battle_music = ["boss_battle", "intense_battle", "battle_scorpio", "slayer"]
monster_sounds = ["stab", "roar", "kick", "jab"]
defeated_sounds = ["death", "deathtune", "lost", "pianoloss"]
hits = ["ow", "ugh", "*", "stab", "kick"]
background_music = ["background", "big", "chillout", "epic", "chase", "greatbattle"]

music = random.choice(background_music)
effects(music)
currently_playing = [music]


def build_monster():
    monster.clear()
    monster.append(random.choice(monsters))  # 0
    monster.append(random.choice(areas))  # 1 areas
    monster.append(random.randint(50, 250))  # 2 health
    monster.append(random.choice(monster_sounds))  # 3 sound of hitting
    for x in range(len(monsters)):
        if monster[0].lower() == monsters[x].lower():
            monster.append(m_final_attack[x])  # 4 match final attack with chosen boss monster
        else:
            x += 1


def check_location(place):
    if monster[1] == place:
        print(f"The {monster[0].upper()} is here!\n")
        show_stats("basic")
        text("Do you want to fight it now? ('y'es or 'n'o)", "?")
        print(end="\033[m--> ")
        battle = input()
        if battle.lower() == "yes" or battle == 'y':
            fight(monster[0], place)
        else:
            text(f"You run away from the {monster[0].upper()} as you are not ready and afraid...", "story")
            choose_path()
    else:
        if dice_roll(10) > 4:
            enemy = random.choice(minions)
            text(f"You found a {enemy} to fight!", "action")
            fight(enemy, place)


def dice_roll(number):
    return random.randint(1, number)


def battle_damages(enemy):
    # damage[0] is enemy damage level | damage[1] is hero attack levels with modifiers from inventory
    damages = [4, 6]
    # Weapon modifiers
    if "Sword of Manil" in inventory:
        damages[1] = 75
    elif "Peach" in inventory and enemy in monsters:
        damages[1] = 888
        text("Your first attack will use the Godly 'Peach'", "story")
        update_inventory("-Peach")
        time.sleep(3)
    elif "Laughing Duck" in inventory and enemy in monsters:
        damages[1] = 999
        text("Your first attack will use the Godly given 'Laughing Duck'", "story")
        update_inventory("-Laughing Duck")
        time.sleep(3)
    elif "Sword of Useless Hope" in inventory:
        damages[1] = dice_roll(25)
    elif "Diamond Knife" in inventory:
        damages[1] = 17
    elif "Battle stick" in inventory:
        damages[1] = 12
    elif "Spear of the Mouse" in inventory:
        damages[1] = 8
    # Armor modifiers
    if "Sheild of Athens" in inventory:
        if enemy in minions:
            damages[0] = 2
        else:
            damages[0] = 7
    elif "Copper sheild" in inventory and "Helmet of Paris" in inventory:
        if enemy in minions:
            damages[0] = 8
        else:
            damages[0] = 22
    elif "Copper sheild" in inventory or "Helmet of Paris" in inventory:
        if enemy in minions:
            damages[0] = 12
        else:
            damages[0] = 28
    else:
        if enemy in minions:
            damages[0] = 20
        else:
            damages[0] = 36
    return damages


def fight(enemy, place):
    # customizing battles with enemies
    if enemy in minions:
        text(f"You must fight the {enemy} at the {place}...\n", "action")
        enemy_battle[0] = dice_roll(40)
        enemy_battle[1] = enemy_battle[0]
        enemy_inv.clear()
        found = random.choice(standard_items)
        drop_item = dice_roll(20)
        if drop_item >= 9:
            if found not in inventory:
                enemy_inv.append(found)
        drop_health = dice_roll(50)
        if drop_health >= 20:
            enemy_inv.append("Health+ Potion")
        time.sleep(2)
        music_background("minion_battle", currently_playing)
    else:
        enemy_inv.clear()
        enemy_inv.append("Souls of the fallen")
        text(f"\nYou decide to fight the {enemy} at the {place}...\n", "action")
        enemy_battle[0] = monster[2]
        enemy_battle[1] = enemy_battle[0]
        time.sleep(2)
        music_background(random.choice(boss_battle_music), currently_playing)
    while enemy_battle[0] > 0:
        damage = battle_damages(enemy)
        enemy_battle[2] = dice_roll(damage[0])
        hero_health[2] = dice_roll(damage[1])
        if dice_roll(10) >= 4:
            show_stats(enemy,place, hero_health, enemy_battle)
            if dice_roll(10) > 7:
                effects(monster[3])
            enemy_battle[0] -= hero_health[2]
            if enemy_battle[0] <= 0:
                enemy_battle[0] = 0
                enemy_battle[2] = 0
                show_stats(enemy, place,hero_health, enemy_battle)
                effects("monster")
                effects("victory")
                text(f"You have defeated the {enemy}.", "action")
                if enemy in minions:
                    if len(enemy_inv) > 0 and enemy_inv[0] in standard_items:
                        text(f"The defeated {enemy} has dropped something...", "story")
                        update_inventory("+" + found)
                    if drop_health >= 20:
                        if hero_health[0] < .99 * hero_health[1]:
                            text("\033[mYou have gained some health.", "action")
                            print(end="\n")
                            hero_health[0] += dice_roll(hero_health[1]-hero_health[0])
                            
                    show_stats("basic")
                else:
                    time.sleep(5)
                    game_over()
        else:
            hit = random.choice(hits)
            injury_sounds(hit)
            hero_health[0] -= enemy_battle[2]
            if hero_health[0] <= 0:
                hero_health[0] = 0
                hero_health[2] = 0
                show_stats("+"+enemy,place, hero_health, enemy_battle)
                music_background(random.choice(defeated_sounds), currently_playing)
                if enemy in minions:
                    text(f"You have been stopped and defeated by the {enemy}...", "action")
                else:
                    text(f"You have perished as the {monster[0]} {monster[4]}\n", "action")
                effects("maniaclaugh")
                time.sleep(4)
                if "Bag of Hell-Coins" in inventory:
                    #clearScreen()
                    effects("hell")
                    text("\nYou open your eyes in the land of the forgotten...", "story")
                    time.sleep(4)
                    text("Sir Hades, takes your Hell-Coins in exchange for a new life, sending you back to save the world...\n", "story")
                    inventory.remove("Bag of Hell-Coins")
                    (text("Good luck warrior!", "speech"))
                    print(end="\n")
                    hero_health[0] = random.randint(55, 90)
                    choose_path()
                text("\nThanks for playing. Would you like to play again?", "story")
                yes_no("begin_quest", "exit")
            show_stats("+"+enemy, place,hero_health, enemy_battle)
    time.sleep(1)


def injury_sounds(character):
    if dice_roll(10) > 8:
        effects(character)

def line_inventory(inventory):
    if len(inventory) == 0:
        in_bag = "~ Nothing ~"
    else:
        in_bag = ""
    for x in range(len(inventory)):
        if x < len(inventory)-1:
            in_bag += inventory[x] + " ~ "
        else:
            in_bag += inventory[x]
    return in_bag

def stat_color(hero_enemy_array):
    if hero_enemy_array[0] <= hero_enemy_array[1]*.33:
        stat_color = "\033[31;1m" 
    elif hero_enemy_array[0] <= hero_enemy_array[1]*.66:
        stat_color = "\033[33;1m" 
    else:
        stat_color = "\033[32;1m" 
    return stat_color


def healthbar(hero_enemy_array):
    reset = "\033[m\033[36m"
    i = 0
    bargraph = ""
    if hero_enemy_array[0] <= 0:
        bargraph = " - dead - "
    else:
        while i < hero_enemy_array[0]/2:
            bargraph += "|"
            i += 1
    return(f"[ {stat_color(hero_enemy_array)}{bargraph} {reset}]")
    



def show_stats(name, place="path", hero=hero_health, enemy=enemy_battle):
    # will modify in next version
    header = "\033[m\033[36m[\033[36;1m "
    reset = "\033[m\033[36m"
    hero_color = stat_color(hero_health)
    enemy_color = stat_color(enemy) 
    if name.lower() == "basic":
        print(f"{header}Hero Health{reset}: {hero_color}{str(hero[0]).zfill(3)} {reset}of {hero[1]}  |  \033[m\033[36;1mInventory{reset}: \033[32;1m {line_inventory(inventory)} {reset}]\n")
    elif name[0] == "+":
        clearScreen()
        print(f"{reset} BATTLE versus a {name[1:].capitalize()} at the {place}\n")
        print(f"{header}Hero Health{reset}: {hero_color}{str(hero[0]).zfill(3)} {reset}of {hero[1]}  |  \033[m\033[36;1mInventory{reset}: \033[32;1m {line_inventory(inventory)} {reset}]")
        print(f"{healthbar(hero)} \033[33mThe {name[1:].capitalize()} hit you{reset} | \033[31;1m-{enemy[2]}\033[m")
        print("\n")
        if "Glasses of Vision" in inventory or "Sacred Clam" in inventory and "Pearl of the Sacred Clam" in inventory:
            print(f"{header}{name[1:].capitalize()} Health{reset}: {enemy_color}{str(enemy[0]).zfill(3)} {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m {line_inventory(enemy_inv)} {reset}]")
            print(f"{healthbar(enemy)} \033[33m\n")
        elif "Sacred Clam" in inventory:
            print(f"{header}{name[1:].capitalize()} Health{reset}: ??? {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m {line_inventory(enemy_inv)} {reset}]")
            print(f"[ ? Unable to Sense ? {reset}] \033[33m\n")
        elif "Pearl of the Sacred Clam" in inventory:
            print(f"{header}{name[1:].capitalize()} Health{reset}: {enemy_color}{str(enemy[0]).zfill(3)} {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m ? Unable to Sense ? {reset}]")
            print(f"{healthbar(enemy)} \033[33m\n")
        else:
            print(f"{header}{name[1:].capitalize()} Health{reset}: ??? {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m ? Unable to Sense ? {reset}]")
            print(f"[ ? Unable to Sense ? {reset}] \033[33m\n")
    else:
        clearScreen()
        print(f"{reset} BATTLE versus a {name.capitalize()} at the {place}\n")
        print(f"{header}Hero Health{reset}: {hero_color}{str(hero[0]).zfill(3)} {reset}of {hero[1]}  |  \033[m\033[36;1mInventory{reset}: \033[32;1m {line_inventory(inventory)} {reset}]")
        print(f"{healthbar(hero)} \033[33m")
        print("\n")
        if "Glasses of Vision" in inventory or "Sacred Clam" in inventory and "Pearl of the Sacred Clam" in inventory:
            print(f"{header}{name.capitalize()} Health{reset}: {enemy_color}{str(enemy[0]).zfill(3)} {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m {line_inventory(enemy_inv)} {reset}]")
            print(f"{healthbar(enemy)} \033[33mYou hit the {name}{reset} | \033[31;1m-{hero[2]}\033[m\n")
        elif "Sacred Clam" in inventory:
            print(f"{header}{name.capitalize()} Health{reset}: ??? {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m {line_inventory(enemy_inv)} {reset}]")
            print(f"[ ? Unable to Sense ? {reset}] \033[33mYou hit the {name}{reset} | \033[31;1m-{hero[2]}\033[m\n")
        elif "Pearl of the Sacred Clam" in inventory:
            print(f"{header}{name.capitalize()} Health{reset}: {enemy_color}{str(enemy[0]).zfill(3)} {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m ? Unable to Sense ? {reset}]")
            print(f"{healthbar(enemy)} \033[33mYou hit the {name}{reset} | \033[31;1m-{hero[2]}\033[m\n")
        else:
            print(f"{header}{name.capitalize()} Health{reset}: ??? {reset}  |  \033[m\033[36;1mDroppable{reset}: \033[32;1m ? Unable to Sense ? {reset}]")
            print(f"[ ? Unable to Sense ? {reset}] \033[33mYou hit the {name}{reset} | \033[31;1m-{hero[2]}\033[m\n")
    time.sleep(1)
        


def yes_no(func1, func2):
    print("Please type 'yes' or 'no'...")
    choice = input(" --> ")
    while choice != "yes" or choice != "no":
        if "yes" in choice.lower() or "y" in choice.lower():
            build_monster()
            exec(func1 + '()')
        elif "no" in choice.lower() or "n" in choice.lower():
            exit()
        else:
            print("Please type 'yes' or 'no'...")
            choice = input(" --> ")


def clearScreen():
    # for windows os
    if name == 'nt':
        _ = system('cls')
    # for mac and linux os(The name is posix)
    else:
        _ = system('clear')



def text(lines, type):
    # depending on type of text given, will be shown in different colors
    if type == "action":
        print(f"\033[33m{lines}")
    elif type == "speech":
        print(f" \033[35m'{lines}'")
    elif type == "story":
        print(f"\033[m{lines}")
    elif type == "?":
        print(f"\033[30;45m{lines}")
    elif type == "stat":
        print(
            f"    \033[m\033[36m{lines}\033[m\033[36mof {hero_health[1]} ]")
    else:
        print("\033[m", end="")
    time.sleep(waiting(lines))



def waiting(text):
    # based on sentance length, waiting time is calculated with a minumum of 2 seconds
    words = 0
    for ch in text:
        if(ch.isspace()):
            words += 1
    words /= 20
    if words <= 1.5:
        words = 0
        return words
    else:
        return (words)


def update_inventory(item):
    if item[0] == "+":
        inventory.append(item[1:])
        effects(item[0])
        text(f"You now have a \033[32;1m{item[1:].upper()}.", "action")
        print(end="\n")
    elif item[0] == "-":
        inventory.remove(item[1:])
        effects(item[0])
        print(end="\n")
        text(f"You have lost a \033[31;1m{item[1:].upper()}.", "action")
    elif item[0] == "*":
        inventory.remove(item[1:])
        effects(item[0])
        text(f"You have dropped a \033[37;1m{item[1:].upper()}.", "action")
        print(end="\n")
    inventory.sort()
   

def start_adventure():
    clearScreen()
    intro()


def intro():
    text(f"You are a herald of Olympus, relaxing whilst {random.choice(task)}.", "story")
    effects("thunder")
    build_monster()
    text("One day, you see a great darkness coming to take over the world.", "story")
    text("For a few days, you watch from mount Olympus all of the mayem happening.", "story")
    text("Oh no, the darkness is winning!", "story")
    text("A light glimmers in the corner of your eye", "action")
    text(f"You see a path leading to the reason of this war, a {monster[0].upper()} like never before seen!", "story")
    text(f"Can the humans defeat this threat on their own, or should you help?", "story")
    text("If you leave Olympus, all your godly powers will be removed, and you will become mortal.", "story")
    text("You can also never return. For once you have helped the humans, Zeus will have you exiled.", "story")
    text("Do you leave Olympus to save humanity? ('yes' or 'no')", "?")
    print(end="\033[m --> ")
    choice = input()
    if "yes" in choice.lower() or "y" in choice.lower():
        text("You decide to be the hero whose story will be told for generations.", "story")
        text("You walk past the gates of Olympus, and wave to Hercules, who says...", "story")
        print(end="\n")
        text("Without your abilities, you may be unable to sense the stregth of your enemy.", "speech")
        text(f"Be sure to check all places multiple times until you find some useful artifacts and weapons.", "speech")
        effects("uhhuh")
        text(f"If you find the old man, he should be able to give you information on your current inventory.", "speech")
        text(f"Here is a something to help you defeat that {monster[0].upper()}. So...try not to die, Cuz.", "speech")
        text(f"May the gods be with you.", "speech")
        print(end="\n")
        text("You take the item from Hercules.", "action")
        begin_quest()
    elif "no" in choice.lower() or "n" in choice.lower():
        text("You decide to let humanity's destiny decide itself and watch the world burn...", "story")
        text("Deep down, you are truly evil 'Bwahahahahahahaaaaaaa!!!!'\n", "story")
        text("Goodbye!", "story")
    else:
        yes_no("begin_quest", "exit")
        


def wiseman(place):
    text(f"You walk throughout the {place}, following the voice of the old man until you find him.", "story")
    text("The old man speaks...", "story")
    print(end="\n")
    text("Welcome warrior. I can help you since you have found me.", "speech")
    text("If you do not have a weapon to fight the monster, you 'may' not defeat it. Keep searching the land repeatedly until you do.", "speech")
    text("Now, ask me a question of one item in your inventory and I will tell you its' benefit.", "speech")
    effects("drinking")
    text("\nWith a smirk, the old man waits after taking a sip of beer...", "story")
    if len(inventory) > 0:
        for item in range(len(inventory)):
            print(f"{item+1}. {inventory[item]}")
        # check if input int or string
        choice = int(input(" --> "))
        if choice > 0 and choice <= len(inventory):
            index = 0
            if inventory[choice-1] in godly_items:
                while inventory[choice-1] != godly_items[index]:
                    index += 1
                print(end="\n")
                text(f"The {inventory[choice-1].upper()} {items_desc[index]}", "speech")
            else:
                index = 0
                while inventory[choice-1] != standard_items[index]:
                    index += 1
                text(f"The {inventory[choice-1].upper()} {items_desc[index+6]}", "speech")
            if hero_health[0] < .99 * hero_health[1]:
                text(f"Along with that, here is some health.", "speech")
                text(f"\nThe old man gives you a health upgrade!", "story")
                hero_health[1] += int(dice_roll(hero_health[0])/2)
                hero_health[0] += dice_roll(hero_health[1]-hero_health[0])
                print(end="\n")
                show_stats("basic")
        else:
            effects("drinking")
            text("The old man, unable to understand you, takes another sip of beer, then dies and vanishes!", "story")
            text(f"You can hear a laughing soul leave the {place}.", "story")
            choose_path()
    else:
        time.sleep(3)
        text("Ahhh...you have nothing...well you better get on the hunt my friend. Time is running out!", "story")
    effects("zeus")
    text("The old man smiles at you. Then in a blink, he vanishes!", "story")
    choose_path()


def begin_quest():
    inventory.clear()
    areas_been.clear()
    hero_health[1] = 100
    update_inventory("+" + random.choice(godly_items))
    effects(random.choice(hits))
    text("\033[mYou have lost all godly abilities, and the transformation has left you weak.\n", "action")
    
    hero_health[0] = random.randint(25, 80)
    
    show_stats("basic")
    text("You walk down from mount Olympus to the area you have seen before.", "action")
    choose_path()


def game_over():
    clearScreen()
    effects("bagpipe")
    text(f"The danger is over, you have won and saved the world from the {monster[0].upper()}.", "story")
    text("As the darkness lifts, you can hear the world celebrating.", "story")
    text("Stories are told of the hero that saved the world, but was never seen again.\n", "story")
    text("\nThanks for playing. Would you like to play again?", "story")
    yes_no("begin_quest", "exit")


def going_to(place):
    text(f"You decide to go to the {place}.", "story")
    text(f"After a slight journey, you are at the {place}.", "story")
    exec(place + '('+f"'{place}'"+')')


def choose_path():
    music_background(music, currently_playing)
    text("Finding nothing else, you walk to the central path.", "action")
    print(f"\033[30;45m\nWhere would you like to go? (Choose from 1 to {len(areas)})\033[m")
    for path in range(len(areas)):
        print(f"{path+1}. {areas[path]}")
    choice = input(" --> ")
    clearScreen()
    # check for int or string
    while check_num(choice) == False:
        text(f"Please type a 'number' from 1 to {len(areas)}.", "story")
        choose_path()
    choice = int(choice)
    if choice > 0 and choice <= len(areas):
        going_to(areas[choice-1])
    else:
        text(f"Sorry that does not exist. Choose from 1 to {len(areas)}.", "story")
        choose_path()

def music_background(title, currently_playing):
    if title != currently_playing[0]:
        currently_playing[0] = title
        effects(title)
        

def check_num(variable):
    try:
        int(variable)
        return True
    except ValueError:
        return False

def House(place):
    if place in areas_been:
        text(f"Again, you knock on the {place} door.", "action")
    else:
        text(
            f"At the {place}, you knock on the door but hear nothing.", "action")
        areas_been.append(place)
    check_location(place)
    choose_path()


def Lake(place):
    if place in areas_been:
        text(
            f"Since you know nothing is around, you jump directly into the {place}.", "action")
    else:
        text(f"At the {place}, you see nothing suspicous.", "story")
        text(f"You jump into the {place} to have a closer look.", "action")
        areas_been.append(place)
    check_location(place)
    choose_path()


def Cave(place):
    if place in areas_been:
        text(f"Being here before, you bravely walk into the {place}.", "action")
    else:
        text(f"At the {place}, you cautiously walk in.", "action")
        areas_been.append(place)
    check_location(place)
    choose_path()


def Castle(place):
    if place in areas_been:
        text(f"You cross the drawbridge and enter the {place}.", "action")
    else:
        text("The castle drawbridge is up and you cannot enter.", "story")
        text(f"At the {place}, you see a person looking over at you.", "story")
        text("The dark figure yells over to you.", "story")
        text("I have seen you in my visions, please come in warrior!", "speech")
        effects("bridge")
        text("The drawbridge is dropped.", "action")
        areas_been.append(place)
        if dice_roll(10) >= 3 and zeus == place:
            wiseman(place)
        else:
            text(f"You search the {place} for the dark figure to no avail, but can hear laughter echoing the halls...", "story")
    check_location(place)
    choose_path()

def Cabin(place):
    if place in areas_been:
        text(f"You slowly enter the {place}.", "action")
    else:
        text("The door is slightly open, so you kick it down.", "story")
        text("You faintly see a shadow of something running in the backgroud.", "story")
        text(f"You chase deeper into the dark and lonely {place}.", "action")
        areas_been.append(place)
        if dice_roll(10) >= 3 and zeus == place:
            wiseman(place)
        else:
            text(f"You search the {place} to no avail.", "story")
    check_location(place)
    choose_path()

def Temple(place):
    if place in areas_been:
        text(f"You walk into the {place}.", "action")
    else:
        text(f"You smile as you walk up to the {place}.", "story")
        text("Faintly, you hear a voice speaking to itself.", "story")
        areas_been.append(place)
        if dice_roll(10) >= 3 and zeus == place:
            wiseman(place)
        else:
            text(f"You search the {place} but find nothing this time.", "story")
    check_location(place)
    choose_path()

def Fountain(place):
    if place in areas_been:
        text(f"Again, you stand in front of the {place}.", "action")
    else:
        text(
            f"At the {place}, you look and admire its craftsmanship.", "action")
        areas_been.append(place)
    check_location(place)
    choose_path()


def check_req():
    try:
        import pygame
        start_adventure()
    except ImportError:
        print("\n\n\033[31;1m*** Missing Module ***\n")
        print("\033[mA needed module is missing to experience the game fully.")
        print("You can either:")
        print("\n1. Install the module named 'pygame' - 'pip install pygame'. ")
        print("2. Play the 'adventure_no_sound.py' file instead.")
        print("\nThank you\n")


check_req()

