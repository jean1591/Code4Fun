#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simulation of the Monty Hall problem:

Suppose you're on a game show, and you're given the choice of three doors.
Behind one door is a car, behind the other, goats. You can pick a door, say
n°1, and the host, who knows what's behind the door opens another, say n°3,
which has a goat. He then say to you: "Do you want to pick door n°2?" Is it
to your advantage to switch your choice?
"""

# IMPORTS
import random
import matplotlib.pyplot as plt
import numpy as np


def montyHall():
    """
    Simulates the Monty Hall problem
    @return: boolean: True if win, False otherwise
    """

    # Creates set of doors and shuffles it
    initialDoors = [1, 2, 3]
    random.shuffle(initialDoors)
    
    # ---------- TOUR 1 ----------
    
    # Random pick for winning door: behind this door is the price
    winningDoor = random.choice(initialDoors)
    
    # Pick the last door in the list and returns it
    myInitialDoor = initialDoors.pop()
    
    # Makes sure montyHallDoor is different from winningDoor
    montyHallDoor = initialDoors[0]
    if montyHallDoor == winningDoor:
        montyHallDoor = initialDoors[1]
    initialDoors.remove(montyHallDoor)
        
    # ---------- TOUR 2 ----------
    # At this point, myInitialDoor and winningDoor are different from montyHallDoor
    # but myInitialDoor can be the winningDoor
        
    # Create a secondary list with myInitialDoor, and the remaining door from
    # Tour 1
    finalDoors = []
    finalDoors.append(myInitialDoor)
    finalDoors.append(initialDoors[0])
    
    # Change my door for remaining door
    myFinalDoor = finalDoors[1]
    
    if myFinalDoor == winningDoor:
        return True
    return False


# ---------- DISPLAY RESULT ----------

# Number of tries
countMax = 10000

# Occurences of True and False
trues = 0
falses = 0

# Run montyHall() countMax times
for element in range(countMax):
    test = montyHall()
    # Increments trues or falses
    if test:
        trues += 1
    else:
        falses += 1


# Display result as percentages of winning and losing
print("Chances of winning: " + str(round(trues / (countMax / 100), 2)), "%")
print("Chances of losing: " + str(round(falses / (countMax / 100), 2)), "%")
