import time
import re
import shutil
import json

T_WIDTH = shutil.get_terminal_size().columns

def print_hori_line():
    print()
    print("-" * T_WIDTH)

def display_title():
    print("\nHello! Welcome to the game!")
    time.sleep(1)
    print("\nIn order to navigate through this program...")
    time.sleep(1)
    print("\nYou will be presented with various options...")
    time.sleep(1)
    print("\nEither type in a string of letters...")
    time.sleep(1)
    print("\nOr select the letter in parentheses in order to proceed...")
    time.sleep(1)

def get_player_name():
    print_hori_line()

    while True:
        valid = False

        name = input("\nEnter your name: ")
        valid = re.search("^[A-Za-z_ ]+$", name)

        if valid:
            return name
        else:
            print("Enter only a string of letters.")

def choose_class():
    print("\nClass options are (F)ighter or (R)anger.")

    while True:
        class_choice = input("\nType F or R to select your class: ")
        class_choice = class_choice.upper()

        if class_choice == "F" or class_choice == "FIGHTER":
            break
        elif class_choice == "R" or class_choice == "RANGER":
            break
        else:
             print("Enter F or R.")

    class_choice = map_class_choice(class_choice)

    print(f"\nYou have selected the {class_choice.title()}!")
    time.sleep(1)
    print(f"\nWe wish you safe journies on your adventures...")
    time.sleep(1)

    return class_choice

def map_class_choice(class_choice):
    class_choices = { "F": "FIGHTER", "R": "RANGER" }
    if class_choice in class_choices:
        return class_choices[f"{class_choice}"]
    else:
        return class_choice

def disp_story(class_choice):
    if class_choice == "FIGHTER":
        decisions = fighter_story()
    elif class_choice == "RANGER":
        decisions = ranger_story()
    return decisions

def fighter_story():
    decisions = []
    
    time.sleep(2)
    print_hori_line()

    choice = orc_approaches()
    decisions.append(choice)
    choice_two = orc_consequence(choice)
    decisions.append(choice_two)

    outcomes = decisions_outcome_map(decisions)
    disp_outcome(outcomes)

    return (decisions, outcomes)

def orc_approaches():
    print("\nBefore you lies a gruesome field of battle...")
    time.sleep(1)
    print("\nBoth sides, men and orc alike, lain slain...")
    time.sleep(1)
    print("\nA big orc approaches you and thrusts his wicked sword towards you..")
    time.sleep(1)
    print("\nYour sword feels heavy in your hand...")
    time.sleep(1)
    print("\nDo you (b)lock with your shield or (p)arry with your sword?")

    while True:
        choice = input("(B)lock/(P)arry: ")
        choice = choice.upper()

        if choice == "B" or choice == "BLOCK":
            choice = "BLOCK"
            break
        elif choice == "P" or choice == "PARRY":
            choice = "PARRY"
            break

    return choice

def orc_consequence(choice):
    if choice == "BLOCK":
        print("\nSuccess! The orc's attack leaves him off balanced...")
        time.sleep(1)
        print("\nDo you (R)un away or (S)trike back?")

        while True:
            choice_two = input("(R)un/(S)trike: ")
            choice_two = choice_two.upper()

            if choice_two == "R" or choice_two == "RUN":
                print("\nYou flee and lose your honor!")
                time.sleep(1)
                choice_two = "RUN"
                break
            elif choice_two == "S" or choice_two == "STRIKE":
                print("\nYou deal a killing blow and gain honor!")
                time.sleep(1)
                choice_two = "STRIKE"
                break
    elif choice == "PARRY":
        print("\nFailure! Your body moves your sword too slowly...")
        time.sleep(1)
        print("\nYou crumple to the ground knowing this is the end...")
        time.sleep(1)
        print("\nDo you (P)ray for forgiveness or (C)urse the day of your birth?")

        while True:
            choice_two = input("(P)ray/(C)urse: ")
            choice_two = choice_two.upper()

            if choice_two == "P" or choice_two == "PRAY":
                print("\nYou die with honor!")
                time.sleep(1)
                choice_two = "PRAY"
                break
            elif choice_two == "C" or choice_two == "CURSE":
                print("\nYou die without honor!")
                time.sleep(1)
                choice_two = "CURSE"
                break

    return choice_two

def ranger_story():
    decisions = []
    
    time.sleep(2)
    print_hori_line()

    choice = rabbit_approaches()
    decisions.append(choice)
    choice_two = rabbit_consequence(choice)
    decisions.append(choice_two)

    outcomes = decisions_outcome_map(decisions)
    disp_outcome(outcomes)

    return (decisions, outcomes)

def rabbit_approaches():
    print("\nYou find yourself in a lush, green forest...")
    time.sleep(1)
    print("\nA small, white rabbit hops into view...")
    time.sleep(1)
    print("\nDo you (s)hoot the rabbit or (t)ame it?")

    while True:
        choice = input("(S)hoot/(T)ame: ")
        choice = choice.upper()

        if choice == "S" or choice == "SHOOT":
            choice = "SHOOT"
            break
        elif choice == "T" or choice == "TAME":
            choice = "TAME"
            break

    return choice

def rabbit_consequence(choice):
    if choice == "SHOOT":
        print("\nSuccess! The rabbit falls to the ground...")
        time.sleep(1)
        print("\nDo you (p)repare the rabbit to eat or (l)eave?")

        while True:
            choice_two = input("(P)reapre/(L)eave: ")
            choice_two = choice_two.upper()

            if choice_two == "P" or choice_two == "PREPARE":
                print("\nYou keep the hunter's code by eating what you kill and gain honor!")
                time.sleep(1)
                choice_two = "PREPARE"
                break
            elif choice_two == "L" or choice_two == "LEAVE":
                print("\nYou spurn the hunter's code by not eating a animal you killed and lose honor!")
                time.sleep(1)
                choice_two = "LEAVE"
                break
    elif choice == "TAME":
        print("\nFailure! The rabbit hops away since you are a ranger not a druid...")
        time.sleep(1)
        print("\nDo you (s)earch for other food sources or (n)ap instead?")

        while True:
            choice_two = input("(S)earch/(N)ap: ")
            choice_two = choice_two.upper()

            if choice_two == "S" or choice_two == "SEARCH":
                print("\nYou are a hard worker and gain honor!")
                time.sleep(1)
                choice_two = "SEARCH"
                break
            elif choice_two == "N" or choice_two == "NAP":
                print("\nYou are a lazy ranger and lose honor!")
                time.sleep(1)
                choice_two = "NAP"
                break

    return choice_two

def decisions_outcome_map(decisions):
    c1_map = {
        "BLOCK": "SUCCESSFUL",
        "PARRY": "UNSUCCESSFUL",
        "SHOOT": "SUCCESSFUL",
        "TAME": "UNSUCCESSFUL"
    }

    c2_map = {
        "RUN": "WITHOUT HONOR",
        "STRIKE": "WITH HONOR",
        "CURSE": "WITHOUT HONOR",
        "PRAY": "WITH HONOR",
        "LEAVE": "WITHOUT HONOR",
        "PREPARE": "WITH HONOR",
        "NAP": "WITHOUT HONOR",
        "SEARCH": "WITH HONOR"
    }

    outcomes = [c1_map[decisions[0]], c2_map[decisions[1]]]
    return outcomes

def disp_outcome(outcomes):
    print(f"\nIn your life you were generally {outcomes[0]} with your actions and lived {outcomes[1]}.")

def save_to_JSON(name, class_choice, decisions, outcomes):
    filename = "Text_Adventure_Save.json"
    data = {
        "name": name,
        "class_choice": class_choice,
        "decisions": decisions,
        "outcomes": outcomes
    }

    with open(filename, "w") as file:
            json.dump(data, file, indent=4)

def replay_check():
    print_hori_line()
    print("\nPlay again?")
    
    while True:
        choice = input("(Y)es/(N)o: ")
        choice = choice.upper()

        if choice == "Y" or choice == "YES":
            print_hori_line()
            print("\nStarting a new game..")
            time.sleep(1)
            return True
        elif choice == "N" or choice == "NO":
            print_hori_line()
            print("\nQuitting...")
            time.sleep(1)
            return False
        else:
            print("Type Y or N...")

def main():
    running = True

    while running:
        decisions = []

        display_title()
        name = get_player_name()
        class_choice = choose_class()
        decisions, outcomes = disp_story(class_choice)
        save_to_JSON(name, class_choice, decisions, outcomes)
        running = replay_check()

main()
