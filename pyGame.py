#!/usr/bin/env python3

import os
import sys
import glob
import string
import shutil
import random

killers = ['Bill','Jim','Sally','Phill']

killer = random.choice(killers)
killers.remove(killer)
suspect1 = random.choice(killers)
killers.remove(suspect1)
suspect2 = random.choice(killers)
killers.remove(suspect2)
suspect3 = random.choice(killers)



#Print statements
print("You're a detective and you have to catch a murderer\n")
print("All of the people involved are still on the scene\nIt is your job to ask the correct questions to find the murderer\n")
print("Option 1 is the mansion murder")
print("Option 2 happened in science club")
print("Option 3 is somethin")

while True:
    #Choose case loop
    choose1 = input("Please choose your case: ")
    while True:
        if choose1 == "1":
            print("You chose the mansion murder")
            print("They've found Jessica dead with " + suspect1)
            print("1 for " + suspect1 + "\n2 for " + suspect2 + "\n3 for " + killer + "\n4 for " + suspect3)
            choose2 = input("Who would you like to question first: ")
            while True:
                if choose2 == "1":
                    options = {'1': 'We drank some wine and she died', '2': 'I was sitting right in front of her',
                            '3': 'It was not me, I think she was poisened'}
                    print("You chose " + suspect1)
                    print("1 for What happened?\n2 for Where were you?\n3 for who did it?")
                    answer = input()
                    if answer in options:
                        print(options[answer])
                    if answer == "back":
                        break
                    else:
                        print("ERROR, please enter 1, 2, or 3")
                if choose2 == "2":
                    options = {'1': 'I was not there', '2': 'I was in the library', '3': 'You should ask ' + suspect1}
                    print("You chose " + suspect2)
                    print("1 for What happened?\n2 for Where were you?\n3 for who did it?")
                    answer = input()
                    if answer in options:
                        print(options[answer])
                    if answer == "back":
                        break
                    else:
                        print("ERROR, please enter 1, 2, or 3")

                if choose2 == "3":
                    options = {'1': 'I was not there', '2': 'I was in the library', '3': 'You should ask ' + suspect1}
                    print("You chose " + killer)
                    print("1 for What happened?\n2 for Where were you?\n3 for who did it?")
                    answer = input()
                    if answer in options:
                        print(options[answer])
                    if answer == "back":
                        break
                    else:
                        print("ERROR, please enter 1, 2, or 3")

                if choose2 == "4":
                    options = {'1': 'I was not there', '2': 'I was in the library', '3': 'You should ask ' + suspect1}
                    print("You chose " + suspect3)
                    print("1 for What happened?\n2 for Where were you?\n3 for who did it?")
                    answer = input()
                    if answer in options:
                        print(options[answer])
                    if answer == "back":
                        break
                    else:
                        print("ERROR, please enter 1, 2, or 3")

                #Quit suspect questioning loop
                if choose2 == "quit":
                    print("THANKS FOR PLAYING")
                    break
                else:
                    print("Please enter 1, 2, 3, or 4")


        if choose1 == "2":
            print("You chose science club")
            print("They've found Mr.Johnson dead with all the students in class except " + suspect2)
            print("1 for " + suspect1 + "\n2 for " + suspect2 + "\n3 for " + killer + "\n4 for " + suspect3)
            choose2 = int(input("Who would you like to question first: "))

        if choose1 == "3":
            print("I'm workin on it")

        if choose1 == "quit":
            print("THANKS FOR PLAYING")
            break

        else:
            print("Please enter 1, 2, or 3")


