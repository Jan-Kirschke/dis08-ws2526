# Data Structures

# Data Structures

> [!NOTE]
> Remember [bashcrawl](https://gitlab.com/slackermedia/bashcrawl) from the other lab exercise? Now we are going back the "dungeon setting" but **this time you will actually implement parts of the game!**

## Comma Code

**Source:** https://automatetheboringstuff.com/2e/chapter4/

Say you have a list value like this:

```
spam = ['apples', 'bananas', 'tofu', 'cats']
``` 

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list is passed to your function.

## Coin Flip Streaks

**Source:** https://automatetheboringstuff.com/2e/chapter4/

For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

You can start with the following template:

```python
import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.

    continue

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
```

## Fantasy Game Inventory

**Source:** https://automatetheboringstuff.com/2e/chapter5/

You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value `{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}` means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named `displayInventory()` that would take any possible “inventory” and display it like the following:

```
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
``` 
**Hint:** You can use a for loop to loop through all the keys in a dictionary.

You can start with the following template:

```python
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        continue
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
```

## List to Dictionary Function for Fantasy Game 

**Source:** https://automatetheboringstuff.com/2e/chapter5/

Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

```python
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
```

Write a function named `addToInventory(inventory, addedItems)`, where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The `addToInventory()` function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. 

The previous program (with your `displayInventory()` function from the previous project) would output the following:

```
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
```

Your code could look something like this:

```python
def addToInventory(inventory, addedItems):
    # your code goes here
    return

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
```

> [!IMPORTANT]
> Please provide your implementations in a Jupyter notebook called `inventory.ipynb` and commit it to your repository.
