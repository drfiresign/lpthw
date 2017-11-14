from sys import exit
import time


# variables go here
item = False
drunk = False
num_through_cave = 1
item = False
# possible location values are:
# shore, river, entry, hall, cellar, armory, hallway
loc = ''

# story now begins on a raft, which crashes upon a shore

def start():
    print("You are rafting down a river.")
    print('')
    print("Your raft hits a boulder breaking into two.")
    print("""You are knocked across the bow of your raft, 
and the stern is consumed in the rock's undertow.""")
    print('')
    time.sleep(3)
    print("""Your raft careens into the river shore,
tossing you from the bow and onto the beach. 
The landing knocks the wind out of your lungs and you pass out.""")
    print('')
    time.sleep(3)
    print("You awake on a river shore.")
    print('')
    if num_through_cave != 1:
        print(f"There are {num_through_cave} broken rafts next to you.")
    else:
        print("There is a broken raft next to you.")
    print("""The birds are chirping and the sun is shining.
Your eyes open as the sun transits across your face, and you stand up.""")
    print('')
    time.sleep(3)
   
    shore()

# dead function
def dead(why):
    print(why, "All done. Bye bye.\n")
    exit(0)

# heart attack function
# used in moments of indecisiveness
def heartattack():
    print("""You feel indecisive.
A pain grips your left arm as your face contorts in a grimace.
The feeling that you've just never amounted to much in life enters your mind.""")
    print('')
    time.sleep(3)
    print("""A strong smell of toast fills your nostrils and as you pass out,
you think of your wasted youth and the lost feelings of love and graditude
that the years of traveling have erased from your life.""")
    print('')
    time.sleep(3)
    print("""The last time you thought of your sister and how long ago you last spoke,
you only felt shame.""")
    print('')
    time.sleep(3)
    dead("You have had a heart attack.")

# shore function
def shore():
    global loc
    loc = 'shore'

    # see a river and an entrance to a cave
    print("You are standing on a river shore.")
    print("To the RIGHT is a river, to the LEFT is a cave.")
    print("Which way shall you go?")
    
    choice = input("> ").lower()

    # You can enter the cave
    if "l" in choice:
        print("You enter the large cave opening.")
        entry()
    # You can visit the river
    elif "r" in choice:
        river()
    else:
        heartattack()

# river function
def river():
    global loc
    global drunk
    global item
    loc = 'river'

    if not item and not drunk:
        print("""You walk closer to the river on your right.

As you approach the water, you can faintly hear a sweet melody.
You step into the glistening water, ignoring the wreckage next to you.
The deeper you step into the water, the stronger the song becomes.

The water rises; as it passes your chin you feel warm and safe.
The water enters your mouth and you drift into a slumber.""")
        dead("You have drown.")

    elif drunk and not item:
        print("The wine you drank makes you sleepy.")
        print("""
You hear a song in the distance as you approach the water, but you stumble
over your own feet. A well placed rock causes you to trip and you slam your
head on the corner of the raft. You pass out to the comforting sound of a
distant sirens song.""")
        shore()
    else:
        endgame()

# entry function
def entry():
    global loc

    if num_through_cave == 1 and loc == 'shore':
        print("You continue down the dimly lit cave.")
        print("""'Just for a while' you think. Just long enough for you to make sure there isn't
anything inside you can use to repair the raft.""")
        print('')
        time.sleep(3)
        print("""Just as you think it's gotten so dark you may not be able to
find the way out, you suddenly see a flickering in the distance. 
Could that be candlelight?""")
        print('')
        print("""You move closer to investigate and as you round a corner,
the small cave opens into a large entryway.""")
        time.sleep(3)
        print('')
        print("""This entryway is barren with only a few candles illuminating
the room. You see an unused torch on the ground, as though it were waiting for you...""")
        print("You pick up the torch and light it with the flame from the candles.")
        print('')

    loc = 'entry'

    # you see an armory, wine cellar and a hall
    print("You see to your RIGHT an armory.")
    print("To your LEFT, a cellar smelling strongly of wine.")
    print("In FRONT of you is a dark and poorly lit room.")
    print("From what you can see it may be a statue or throne room.")
    print("You could EXIT the cave and to back to the shore.")
    time.sleep(3)
    print('')
    print("Which way shall you go?")

    choice = input("> ").lower()
    # armory function
    if 'r' in choice:
        print("Perhaps there will be something of value in the armory.")
        armory()
    # wine cellar function
    elif 'l' in choice:
        print("'That can't be what I think it is', you tell yourself.")
        print("You decide to descend into the cellar to make sure...")
        cellar()
    elif 'e' in choice:
        print("You think you've wasted enough time here.")
        print("You'd better return to the surface and get to work on the raft.")
        print('')
        shore()
    # hall function
    else:
        print("You decide to enter the larger room.")
        hall()


# armory function
def armory():
    global item
    global loc
    global drunk
    loc = 'armory'

    print("You enter the armory.")

    # you see many suits of armor
    if not drunk:
        print("""
There are many suits of armor here. The walls are decorated with the armor of
twenty different houses, perhaps more. They all glisten in the torchlight.""")
        print('')
        print("You wonder if there is anything of value hidden in their pockets.")
    else:
        print("The wine has made you a bit tipsy and you trip over a discarded helmet.")
        print("You fall head first into an oversized boot, you head stuck in the opening.")
        print("It takes some doing, but you finally work your way out.")
        time.sleep(3)
        print("You look around and see a handful of suits of armor.")
        print("They don't really look all that special.")
        print("They're pretty dirty actually.")
        print('')

    print("Do you SEARCH the room, or RETURN to the entryway?")
    print('')
    # you can search the room
    choice = input("> ").lower()

    if 's' in choice:
        print("You decide to search the suits for anything of value.")
        print('')
        # find a item
        print("You find a few scraps of paper, but nothing of value on them.")
        print("One suit does yield a small hexagonal box.")
        print("It has some markings on it which you can't read,")
        print("and a small button that looks like it's been rusted stuck.")
        print('')
        time.sleep(3)
        print("Keep the box and papers? YES or NO?")
        print('')

        choice = input("> ").lower()

        if 'y' in choice:
            item = True
            print("You decide to keep the box and papers, stuffing them in your pockets.")
            print('')
        else:
            print("You leave the papers and box behind and return to the entryway.")
            print('')

        entry()

    elif 'r' in choice:
        print("'Nothing but old junk.' you think to yourself.")
        print("You decide to return to the entryway.")
        print('')
        entry()
    else:
        heartattack()

# wine cellar function
def cellar():
    global loc
    global drunk
    loc = 'cellar'

    if not drunk:
        print("""
The steps down become more and more narrow. You become grateful for the torch
you found earlier as these small steps seem hard to manage on your own.""")
        time.sleep(3)
        print("""
After what seems like an eternity, you reach a landing at the end of the steps.
The air is humid and chilly, and before you stretches a deep hall full of barrels.""")
        time.sleep(3)
        print("They are full of wine!")
        print('')
        time.sleep(3)
        print("""
They mostly seem to be intact and each seems more inviting than the last.""")
        print("Should you test one? Just for curiousity's sake? YES or NO?")
        print('')

        choice = input("> ").lower()

        # you can drink from a cask
        if 'y' in choice:
            print("""
You close your eyes and count to 10, spinning around in a circle. You're so giddy
you can hardly contain yourself. You slow to stop, pointing a one you've decided
to call Charlie. Uncorking Charlie, you find a sweet scent rising to meet you.
""")
            time.sleep(3)
            print("You drink deeply from the cask, and your cheeks feel flushed.")
            drunk = True

        if 'n' in choice:
            print("You feel too uncertain to indulge right now.")
            print("Perhaps after you've made sure there are no more surprises here.")

    else:
        print("You stumble down the steps, missing several.")
        print("You try to steady yourself on the wall,")
        print("but slip and tumble down the remaining steps.")
        print('')
        time.sleep(3)
        print("Damn! That hurts! Thank goodness for the wine from earlier or")
        print("you'd be in a sorry shape.")
        print('')
        print("'What's one more?' you think to yourself?")
        print("You load up on another few swigs from a fresh cask, then head back upstairs.")
        time.sleep(3)
        entry()
    
    print("You decide to head back upstairs.")
    print('')
    entry()

# hall function
def hall():
    global drunk
    global loc
    global item
    loc = 'hall'

    print("You enter the hall.")
    # if you have the item
        # you find the item
    # if you don't have the item
        # you pull a level and the door closes sealing you in
        # your torch begins to fade
        # you starve to death in total darkness
    # if you have the item and are drunk
        # you stumble into a wall and break through into a treasure chamber
    # if you don't have the item and are drunk
        # you stumble onto a floor switch activating a trap door which impales you on spikes
        # you feel no pain because of how drunk you are

# passage function
def passage():
    global drunk
    global loc
    global item
    loc = 'passage'

    print("You tentatively enter the passageway.")
    pass
    # ???
    # profit!

# you have the item, and you return to the raft
def endgame():
    pass
start()
