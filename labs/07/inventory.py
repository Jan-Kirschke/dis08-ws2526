# Excercise 1
"""
Write a function that takes a list value as an argument and returns a string 
with all the items separated by a comma and a space, with and inserted before 
the last item. For example, passing the previous spam list to the function would 
return 'apples, bananas, tofu, and cats'. But your function should be able to work 
with any list value passed to it. Be sure to test the case where an empty list is 
passed to your function.
"""
spam = ['apples', 'bananas', 'tofu', 'cats']

def list_function(liste: list):
    if not liste:
        print("Liste ist leer")
    output_string: str = ""
    for eintrag in liste:
        if liste.index(eintrag) == len(liste) -1:
            output_string += eintrag
        elif liste.index(eintrag) == len(liste) -2:
            output_string += eintrag + " and "
        else:
            output_string += eintrag + ", "

    return output_string

print()
print("Excerise 1")
print(list_function(spam))

"""
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” 
for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” 
If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail 
results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random. 
A human will almost never write down a streak of six heads or six tails in a row, even though it is highly 
likely to happen in truly random coin flips. Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a 
randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the 
first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks 
if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we 
can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, 
the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

You can start with the following template:

"""
import random


durchläufe = 100
würfe_pro_durchlauf = 10_000

def einen_würfel_test_durchlauf():
    numberOfStreaks_pro_durchlauf = 0
    alle_würfe_liste: list = []
    for experimentNumber in range(würfe_pro_durchlauf):
        coin_flip = "H" if random.randint(0, 1) == 1 else "T"
        alle_würfe_liste.append(coin_flip)

    state: str = alle_würfe_liste[0]     # das ist der erste status, der wert des ersten wurfes
    counter = 1     # weil ich in state schon den ersten reinspeichere

    for i in range(len(alle_würfe_liste)-1):
        if alle_würfe_liste[i + 1] == state:
            counter += 1
        else:
            state = alle_würfe_liste[i + 1] 
            counter = 1
        if counter ==6:
            numberOfStreaks_pro_durchlauf += 1
            counter = 0     # weil ich keine überlappende streaks möchte
    return numberOfStreaks_pro_durchlauf

numberOfStreaks = 0
for versuch in range(durchläufe):
    numberOfStreaks += einen_würfel_test_durchlauf()

durchschnitt = numberOfStreaks / durchläufe

print()
print("Excerise 2")
print(f"Durchschnittliche Anzahl Streaks pro {würfe_pro_durchlauf} Würfe: {durchschnitt}")

bkjfkbsdbfkabsdkfb

# Fantasy Game Inventory
""" This is the expected output
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total += int(v)
    print("Total number of items: " + str(item_total))

print()
print("Excerise 3")
displayInventory(stuff)

# List to Dictionary Function for Fantasy Game
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

print()
print("Excerise 4")
displayInventory(inv)