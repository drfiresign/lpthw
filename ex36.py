from sys import exit
import time


# variables go here
key = False
drunk = False


# begin in a field

def start():
    print("\n\tYou awake in a field.")
    print("\tThe birds are chirping and there is a faint sound of running water.")
    print("\tYour eyes open as the sun transits across your face, and you stand up.\n")
    time.sleep(2)

    field()

# dead function
def dead(why):
    if drunk:
        print("\tYour vision blurs and you begin to see double.")
        print("\tYou might have had just a bit too much this time.\n")
        print("\tThe world fades and you die in a puddle of your own vomit.\n")
        print("\tAll done. Bye bye.\n")
    else:
        print("\t", why, "All done. Bye bye.\n")
        exit(0)

# field function
def field():
    # see a river and an entrance to a cave
    print("\tYou are standing in a field.")
    print("\tTo the right is a river, to the left is a cave.")
    print("\tWhich way shall you go?\n")
    
    choice = input("> ").lower()

    # You can enter the cave
    if "l" in choice:
        cave()
    # You can visit the river
    elif "r" in choice:
        river()
    else:
        print("""
        You feel indecisive.
        A pain grips your left arm as your face contorts in a grimace.
        The feeling that you've just never amounted to much in life enters your mind.
        """)
        time.sleep(3)
        print("""
        A strong smell of toast fills your nostrils and as you pass out, you think
        of your wasted youth and the lost feelings of love and graditude that the
        years of traveling have erased from your life.
        """)
        time.sleep(2)
        print("""
        The last time you thought of your sister and how long ago you last spoke,
        you only felt shame.
        """)
        time.sleep(2)
        dead("You have had a heart attack.")


# river function
def river():
    print("""
        You walk towards the sound of the river.

        As you approach the water, you can faintly hear a sweet melody.
        You step into the glistening water.
        The deeper you go the stronger the song becomes.
        
        The water rises; as it passes your chin you feel warm and safe.
        The water enters your mouth as you drift into a dream, and you drown.\n""")

    dead("You have died.")

# cave function
def cave():
    pass
    # you see an armory
    # you see a wine cellar
    # you see a hall (of heroes)
    print("\tYou see to your right an armory.")
    print("\tTo your left, a cellar smelling strongly of wine.")
    print("\tIn front of you is a dimly lit room.\n\tFrom what you can see it may be a statue or throne room.")

    print("\tWhich way shall you go?")

    choice = input("> ").lower()
    # armory function
    if 'r' in choice:
        armory()
    # wine cellar function
    elif 'l' in choice:
        cellar()
    # hall function
    else:
        hall()


# armory function
    # you see many suits of armor
    # you can search the room
        # find a key
        # key = True
    # skip the room
        # return to cave function

# wine cellar function
    # you see many casks
        # give them names
    # you can drink from a cask
        # drunk = True
        # spawn separate dialog options for drunk
    # skip the room
        # return to cave function

# hall function
    # if you have the key
        # find the passage to... where?
    # if you don't have the key
        # you pull a level and the door closes sealing you in
        # your torch begins to fade
        # you starve to death in total darkness
    # if you have the key and are drunk
        # you stumble into a wall and break through into a treasure chamber
    # if you don't have the key and are drunk
        # you stumble onto a floor switch activating a trap door which impales you on spikes
        # you feel no pain because of how drunk you are

# passage function
    # ???
    # profit!
start()
