from sys import exit
import time


# begin in a field

def start():
    print("You awake in a field.")
    print("The birds are chirping and there is a faint sound of running water.")
    print("Your eyes open as the sun transits across your face, and you stand up.\n")
    time.sleep(2)

    field()

# dead function
def dead(why):
    print(why, "All done. Bye bye.")
    exit(0)

# field function
def field():
    # see a river and an entrance to a cave
    print("You are standing in a field.")
    print("To the right is a river, to the left is a cave.")
    print("Which way shall you go?")
    
    choice = input("> ").lower()

    # You can enter the cave
    if "l" in choice:
        cave()
    # You can visit the river
    elif "r" in choice:
        river()
    else:
        print("""You feel indecisive.
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
    print("""You walk towards the sound of the river.
As you approach the water, you can faintly hear a sweet melody.
You step into the glistening water.
The deeper you go the stronger the song becomes
The water rises; as it passes your chin you feel warm and safe
The water enters your mouth as you drift into a dream, and you drown.""")

    dead("You have died.")

# cave function
def cave():
    pass
    # you see an armory
        # armory function

    # you see a wine cellar
        # wine cellar function

    # you see a hall (of heroes)
        # hall function

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
