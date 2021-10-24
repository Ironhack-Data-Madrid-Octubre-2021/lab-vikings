# Let's pay
import vikingsClasses as vc
import sys
print("Welcome to this game, the war beteewn the armis it is about to start...")
print(" You have to choose your character:")
print("Press 1 to be the viking Lord of War", vc.Viking.__doc__)
print("Press 1 to be the saxon King", vc.Saxon.__doc__)
selection = input(print("What is your decision? press 1 or 2"))
if selection == 1:
    print("your choice is Viking Lord of War!!! " )
elif selection == 2:
    print("your choice is the King of all Saxons!!! " )
else: 
    selection
