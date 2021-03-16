import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("The Maze")
entry = tk.Entry(fg="Blue", bg="Red", width=50)
entry.pack()

T = False
global lst_of_choices


def click_to_continue():
    action = ttk.Button(root, text="Click To Continue")
    T = True
    action.pack()


def intro():
    str_back = "\nThe Year is 1774. \n"
    str_back += "\nPrimitivity has settled over Humanity again. The practise of Human Sacrifices has resumed.\n"
    str_back += "\nYou have been selected as one of the 12 tributes, being sacrificed to the Labyrinth.\n"
    str_back += "\nYour end goal? To Survive. Bloodthirsty and feral monsters roam this maze, and so much more....\n"
    str_back += "\nRules : "
    str_back += "\n1. Enter the text up,down,left,right to move your character across the map.\n"
    str_back += "\n2. You may encounter dangerous enemies,mysterious rooms and walls.\n"
    str_back += "\n3. If you chose to flee the enemy your health decreases by 20.\n"
    str_back += "\n4. Your health is reset to 100 after every fight.\n"
    str_back += "\n5. You get 100 points for every enemy defeated.\n"
    str_back += "\n6. Gold coins can be found in the mysterious rooms.\n"
    str_back += "\n7.Find 500 gold coins to win the game.\n"
    intro_label1 = tk.Label(
        text=str_back,
        fg="white",
        bg="red",
        width=35,
        height=25
    )
    intro_label1.pack()
    click_to_continue()
    if T:
        intro_label1.forget()


intro()


class Playerchoice:
    def display(self):
        str1 = "There are three main types of characters. Archer, Magician, Knight \n"
        str1 += "\nThese are the attributes for the different characters : \n"
        str1 += "\nArcher deals 40 damage but takes 14 damage with every hit. He uses a bow and arrow \n"
        str1 += "\nMagician deals 30 damage but takes 10 damage with every hit. He uses a magic staff \n"
        str1 += "\nKnight d2als 50 damage but takes 18 with every hit. He uses a sword and shield. \n"
        character_label1 = tk.Label(
            text=str1,
            fg="white",
            bg="red",
            width=35,
            height=35
        )
        character_label1.pack()

    def __init__(self):
        self.archer = {'Name': "Archer", 'Weapon': 'Bow&Arrow', 'Damage': 40, 'Health Loss': 14}
        self.magician = {'Name': "Magician", 'Weapon': 'Magic Staff', 'Damage': 30, 'Health loss': 10}
        self.knight = {'Name': "Knight", 'Weapon': 'Sword and Shield', 'Damage': 50, 'Health Loss': 18}
        self.choice = ""


P = Playerchoice()


def input_taker(lst_of_choices):
    lst_of_choices = ["Archer", "Magician", "Knight"]
    P.choice = entry.get()
    global role_select
    str = f"You entered :{P.choice}"
    if not P.choice.isdigit():
        str += "\nPlease enter acceptable choice"
        error_label = tk.Label(
            text=str,
            fg="white",
            bg="red",
            width=30,
            height=5
        )
        error_label.pack()
    else:
        choice = int(P.choice)
        print(count + 1)
        if not choice in range(1, count + 1):
            str += "\nInvalid choice"
            error_label = tk.Label(
                text=str,
                fg="white",
                bg="red",
                width=30,
                height=30
            )
            error_label.pack()
            choice = ""
        else:
            lst = list(lst_of_choices)
            choice = lst[choice - 1]
            str += f"\nYou selected :{choice}"
            label.config(text=str)
            label.pack()
            role_select = choice
            take_input1()


def take_input1():
    global role_select
    str = "**********************************************************"
    str += f"\n{role_select} plays"
    label1 = tk.Label(
        text=str,
        fg="white",
        bg="brown",
        width=30,
        height=10
    )
    label1.pack()
    entry1 = tk.Entry(fg="yellow", bg="brown", width=50)
    entry1.pack()
    button1 = tk.Button(text="Click for selecting action", command=take_input1)
    button1.pack()


def boss_fight():
    global player_score
    health = 100
    boss = ""
    boss_health = 0
    boss_damage = 0
    boss_loss = 0
    status = ""
    str_boss = ""
    n = random.randint(1, 10)
    if n % 2 == 0:
        boss = "Minotaur"
    else:
        boss = "Goblin King"
    if boss == "Minotaur":
        boss_health = 100
        boss_damage = 40
        boss_loss = 40
    else:
        boss_health = 100
        boss_damage = 35
        boss_loss = 35
    counts = 0
    countdef = 0
    i = True
    boss_turn = ["Get out of the way.", "Block", "Counter-Attack."]
    player_turn = ["Attack.", "Special Attack"]
    str_boss += "\nATTENTION"
    str_boss += "\nSomething lurks in the shadows. You see a huge figure move around. You draw your weapon, steeling yourself."
    str_boss += f"\nThe Huge Figure comes closer and closer. It appears before you. It is the {boss}\n"
    str_boss += "\nIt is time...\n"
    str_boss += "\n              F I G H T             \n"
    str_boss += f"\nThe {boss} attacks first. You need to move quick\n"
    while health > 0 and boss_health > 0:
        str_boss += f"\nYou know what to do. Select a option to counter enemies attack {boss_turn}. \n"
        if i:
            str_boss += '\nIT"S HIS TURN TO ATTACK\n'
            defend = input_taker(boss_turn)
            if defend == "Get out of the way.":
                str_boss += "\nYou get out of the way yet the attack does some minor damage!!\n"
                health -= boss_damage / 4
                str_boss += f"\nYour health is {health}\n"
            elif defend == "Block":
                if countdef == 0:
                    str_boss += "\nYou stand your ground. The attack has no effect on you this time.\n"
                    str_boss += "\nYou cannot defend for 3 turns now\n"
                    countdef = 3
                else:
                    str_boss += f"\nYou  cannot defend for {countdef} more turns!\n"
                    str_boss += "You try to get out out of the way.\n"
                    health -= boss_damage / 4
                    str_boss += f"\nYour health is now{health}\n"
            elif defend == "Counter-Attack.":
                str_boss += "You show nerves of steel. You decide to parry the attack. You also stun the boss with your courage.\n"
                boss_health -= (boss_loss / 4)
                str_boss += f"Its health is {boss_health}\n"
            countdef -= 1
            i = False
        elif not i:
            str_boss += "\nYOUR TURN TO ATTACK\n"
            str_boss += "\nIt's your turn to attack now. No time to rest.\n"
            attack = input_taker(player_turn)
            if attack == 1:
                str_boss += "\nYou attack the enemy, and it sustains some damage.\n"
                boss_health -= boss_loss
            else:
                if counts == 2:
                    str_boss += "\nYou take a deep breath. It's time. You summon energy from the four corners of the Earth...\n"
                    str_boss += "\n...AND RELEASE IT IN A SINGLE SHOUT!!!\n"
                    boss_health -= boss_loss * 1.5
                    str_boss += f"\nIts health is now {boss_health}\n"
                    counts = 0
                else:
                    str_boss += f"\nYou don't have enough energy to use this attack yet! You need to wait for {2 - counts} turns.\n"
                    str_boss += "\nYou decide to use a regular attack.\n"
                    boss_health -= boss_loss
                    str_boss += f"\nIt's health is now {boss_health}\n"
                i = True
            counts += 1
    if health <= 0:
        status = "Dead"
        str_boss += "\n       Y O U  D I E D       \n"
        exit()
    elif boss_health <= 0:
        status = "Alive"
        str_boss += "\n      D E M O N  V A N Q U I S H E D       \n"
        player_score += 200
        return status, player_score
    boss_label = tk.Label(
        text=str,
        fg="white",
        bg="blue",
        width=100,
        height=100

    )
    boss_label.pack()


role_select = ""
window = tk.Tk()
str = "Select one of the following:"

for count, option in enumerate(lst_of_choices):
    str += f"\n{count + 1}:{option}"
count = len(lst_of_choices)
label = tk.Label(
    text=str,
    fg="white",
    bg="blue",
    width=30,
    height=10
)
label.pack()
map = [["Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall"],
       ["Wall", "Floor", "Floor", "Floor", "Room", "Floor", "Wall"],
       ["Wall", "Floor", "Room", "Floor", "Floor", "BossEnemy", "Wall"],
       ["Wall", "Floor", "Floor", "Floor", "Enemy", "Floor", "Wall"],
       ["Wall", "Enemy", "Floor", "Start", "Floor", "Floor", "Wall"],
       ["Wall", "Floor", "BossEnemy", "Floor", "Room", "Floor", "Wall"],
       ["Wall", "Floor", "Floor", "Enemy", "Floor", "Floor", "Wall"],
       ["Wall", "Wall", "Wall", "Wall", "Wall", "Wall", "Wall"]]
map_row = 4
map_column = 3
gold_coins = 0
health = 100
player_score = 0
map_walls = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (2, 0),
             (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (1, 6), (2, 6), (3, 6), (4, 6),
             (5, 6), (6, 6), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()
P.display()
button = tk.Button(text="Click for selecting role", command=input_taker)
button.pack()

root.mainloop()
