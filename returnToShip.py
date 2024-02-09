from pathlib import Path
from datetime import datetime
from datetime import timedelta
import subprocess

def reset():
    with open("./bag/treasure.jpg", "w") as keyfile:
        keyfile.write("lost")

    print("    You are swimming as fast as you can towards the boat but you can")
    print("    feel the water begin to pull you back as the sea monster opens its")
    print("    giant mouth.")
    print("    You kick with all your might, sure that you are about to breath your")
    print("    last breath.")
    print("    ")
    print("    ")
    print("    Suddenly... The treasure bag slips out of your hand!")
    print("    It swirls down through the water and into the mouth of the sea monster.")
    print("    The beast's mouth snaps closed and it jets away into the depth of the")
    print("    ocean, taking with it the treasure.")
    print("    You are safe... but will you attempt the dive again?")


def win():

    print("    You are swimming as fast as you can towards the boat but you can")
    print("    feel the water begin to pull you back as the sea monster opens its")
    print("    giant mouth.")
    print("    You kick with all your might, sure that you are about to breathe your")
    print("    last breath.")
    print("    ")
    print("    ")
    print("    Suddenly... A hand appears!")
    print("    You've made it to the boat! The crew pulls you into the boat, just in")
    print("    time to avoid the sea monster's vicious maw.")
    print("    You're safe at last!")
    print("    Now you can finally show off the treasure you risked your life for...")
    print("    Use open treasure.jpg to take a peek.")


now = datetime.now()
if not Path("adventure/seafloor/coral_reef/.timer").exists():

    print("    Your adventure has only just begun. You are not yet ready to return") 
    print("    to the ship. More secrets await you in the ocean's depths.")

else:
    if Path("./bag/treasure.jpg").exists() or Path("./treasure.jpg").exists():
        win()

    else:
        print("    You forgot your treasure bag! Hurry back to get it before the sea monster")
        print("    hides it away forever!")
        print("    HINT: Do you use the mv command to move the treasure up to this directory?")
