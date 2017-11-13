from sys import exit
import time


# variables go here
key = False
drunk = False
num_through_cave = 1

# story now begins on a raft, which crashes upon a shore

def start():
    print("""
You are rafting down a river.

Your raft hits a boulder breaking into two.
You are knocked across the bow of your raft as the stern is consumed in the
rock's undertow.

Your raft careens into the river shore, tossing you from the bow and onto the
beach. The landing knocks the wind out of your lungs and you pass out.""")
    time.sleep(2)
    print("You awake on a river shore.")
    if num_through_cave != 1:
        print(f"There are {num_through_cave} broken rafts next to you.")
    else:
        print("There is a broken raft next to you.")
    print("""The birds are chirping and the sun is shining.
Your eyes open as the sun transits across your face, and you stand up.\n""")
    time.sleep(2)
    
    field()

# dead function
def dead(why):
    if drunk:
        print("Your vision blurs and you begin to see double.")
        print("You might have had just a bit too much this time.")
        print("The world fades and you die in a puddle of your own vomit.")
        print("All done. Bye bye.\n")
    else:
        print(why, "All done. Bye bye.\n")
        exit(0)

# heart attack function
# used in moments of indecisiveness
def heartattack():
    print("""
You feel indecisive.\n
A pain grips your left arm as your face contorts in a grimace.
The feeling that you've just never amounted to much in life enters your mind.
""")
    time.sleep(2)
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

# field function
def field():
    # see a river and an entrance to a cave
    print("You are standing on a river shore.")
    print("To the RIGHT is a river, to the LEFT is a cave.")
    print("Which way shall you go?\n")
    
    choice = input("> ").lower()

    # You can enter the cave
    if "l" in choice:
        cave()
    # You can visit the river
    elif "r" in choice:
        river()
    else:


# river function
def river():
    print("""
You walk closer to the river on your right.

As you approach the water, you can faintly hear a sweet melody.
You step into the glistening water, ignoring the wreckage next to you.
The deeper you step into the water, the stronger the song becomes.
        
The water rises; as it passes your chin you feel warm and safe.
The water enters your mouth and you drift into a slumber.\n""")

    dead("You have drown.")

# cave function
def cave():
    pass
    # you see an armory
    # you see a wine cellar
    # you see a hall (of heroes)
    print("You see to your RIGHT an armory.")
    print("To your LEFT, a cellar smelling strongly of wine.")
    print("In FRONT of you is a dimly lit room.\nFrom what you can see it may be a statue or throne room.")

    print("Which way shall you go?\n")

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
def armory():
    print("You enter the armory.")
    pass
    # you see many suits of armor
    # you can search the room
        # find a key
        # key = True
    # skip the room
        # return to cave function

# wine cellar function
def cellar():
    print("You decend to the cellar.")
    pass
    # you see many casks
        # give them names
    # you can drink from a cask
        # drunk = True
        # spawn separate dialog options for drunk
    # skip the room
        # return to cave function

# hall function
def hall():
    print("You enter the hall.")
    pass
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
def passage():
    print("You tentatively enter the hallway.")
    pass
    # ???
    # profit!
start()
