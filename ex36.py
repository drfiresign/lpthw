from sys import exit
import time


# variables go here
key = False
drunk = False
num_through_cave = 1
how_drunk = 0

# possible location values are:
# shore, river, entry, hall, cellar, armory, hallway
loc = ''

# story now begins on a raft, which crashes upon a shore

def start():
    global how_drunk
    global key
    global drunk
    global num_through_cave

    key = False
    drunk = False
    how_drunk = 0

    print("You are rafting down a river.")
    print('')
    print("Your raft hits a boulder breaking into two.")
    print("""You are knocked across the bow of your raft, 
and the stern is consumed in the rock's undertow.""")
    print('')
    # time.sleep(3)
    print("""Your raft careens into the river shore,
tossing you from the bow and onto the beach. 
The landing knocks the wind out of your lungs and you pass out.""")
    print('')
    # time.sleep(3)
    print("You awake on a river shore.")
    print('')
    if num_through_cave != 1:
        print(f"There are {num_through_cave} broken rafts next to you.")
    else:
        print("There is a broken raft next to you.")
    print("""The birds are chirping and the sun is shining.
Your eyes open as the sun transits across your face, and you stand up.""")
    print('')
    # time.sleep(3)
   
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
    # time.sleep(3)
    print("""A strong smell of toast fills your nostrils and as you pass out,
you think of your wasted youth and the lost feelings of love and graditude
that the years of traveling have erased from your life.""")
    print('')
    # time.sleep(3)
    print("""The last time you thought of your sister and how long ago you last spoke,
you only felt shame.""")
    print('')
    # time.sleep(3)
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
    loc = 'river'

    if not drunk:
        print("""You walk closer to the river on your right.

As you approach the water, you can faintly hear a sweet melody.
You step into the glistening water, ignoring the wreckage next to you.
The deeper you step into the water, the stronger the song becomes.

The water rises; as it passes your chin you feel warm and safe.
The water enters your mouth and you drift into a slumber.""")
        dead("You have drown.")

    elif drunk:
        print("The wine you drank makes you sleepy.")
        print("""
You hear a song in the distance as you approach the water, but you stumble
over your own feet. A well placed rock causes you to trip and you slam your
head on the corner of the raft. You pass out to the comforting sound of a
distant sirens song.""")
        shore()

# entry function
def entry():
    global loc

    if num_through_cave == 1 and loc == 'shore':
        print("You continue down the dimly lit cave.")
        print("""'Just for a while' you think. Just long enough for you to make sure there isn't
anything inside you can use to repair the raft.""")
        print('')
        # time.sleep(3)
        print("""Just as you think it's gotten so dark you may not be able to
find the way out, you suddenly see a flickering in the distance. 
Could that be candlelight?""")
        print('')
        print("""You move closer to investigate and as you round a corner,
the small cave opens into a large entryway.""")
        # time.sleep(3)
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
    # time.sleep(3)
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
    global key
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
        # time.sleep(3)
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
        # find the key
        print("You find a few scraps of paper, but nothing of value on them.")
        print("One suit does yield a small hexagonal box.")
        print("It has some markings on it which you can't read,")
        print("and a small button that looks like it's been rusted stuck.")
        print('')
        # time.sleep(3)
        print("Keep the box and papers? YES or NO?")
        print('')

        choice = input("> ").lower()

        if 'y' in choice:
            key = True
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
    global how_drunk
    loc = 'cellar'

    if not drunk:
        print("""
The steps down become more and more narrow. You become grateful for the torch
you found earlier as these small steps seem hard to manage on your own.""")
        # time.sleep(3)
        print("""
After what seems like an eternity, you reach a landing at the end of the steps.
The air is humid and chilly, and before you stretches a deep hall full of barrels.""")
        # time.sleep(3)
        print("They are full of wine!")
        print('')
        # time.sleep(3)
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
            # time.sleep(3)
            print("You drink deeply from the cask, and your cheeks feel flushed.")
            drunk = True
            how_drunk += 1

        if 'n' in choice:
            print("You feel too uncertain to indulge right now.")
            print("Perhaps after you've made sure there are no more surprises here.")

    else:
        print("You stumble down the steps, missing several.")
        print("You try to steady yourself on the wall,")
        print("but slip and tumble down the remaining steps.")
        print('')
        # time.sleep(3)
        print("Damn! That hurts! Thank goodness for the wine from earlier or")
        print("you'd be in a sorry shape.")
        print('')
        print("'What's one more?' you think to yourself?")
        print("You load up on another few swigs from a fresh cask, then head back upstairs.")
        how_drunk += 1

        if how_drunk >= 3:
            print("Your vision blurs and you begin to see double.")
            print("You might have had just a bit too much this time.")
            print("The world fades and you die in a puddle of your own vomit.")
            print("All done. Bye Bye.\n")
            exit(0)

        # time.sleep(3)
        entry()
    
    print("You decide to head back upstairs.")
    print('')
    entry()

# hall function
def hall():
    global num_through_cave
    global drunk
    global loc
    global key 
    loc = 'hall'

    print("You enter the hall.")

    # if you don't have the key and are drunk
    if not key and drunk:
        # you stumble onto a floor switch activating a trap door which impales you on spikes
        print("As you stumble into the main hall,")
        print("you notice your senses have been *greatly* dulled.")
        print('')
        print("As you wander between statues, you notice the writing on the base of each.")
        print("You cannot read the language, but you're pretty sure that doesn't")
        print("have anything to do with how much wine you've had.")
        # time.sleep(3)
        # you feel no pain because of how drunk you are
        print('')
        print("You lean against one statue, and it starts to shift under your weight.")
        print("As it slides across the floor, you hear sounds of whirring and clicking.")
        # time.sleep(3)
        print('')
        print("The tiles under your feet suddenly give way as the clicking comes to a halt.")
        print("You fall several feet very rapidly, and come to sudden stop.")
        print('')
        # time.sleep(3)
        print("You suddenly taste something metallic. You look down and see you've been impaled on a spike.")
        print("You're very happy for the wine you have flowing in your system right now.")
        print("'Without it you'd be in a lot of pain', you think as you slowly lose conciousness.")
        dead("You blissfully pass out in a drunken haze as you slowly bleed out.")

    # if you have the key and are drunk
    elif key and drunk:
        print("""You stumble into the main hall, noticing how exuberantly you move.
The hall suddenly becomes alive with the sounds of previous Galas and Balls.
You mime twirling in circles as though dancing with the ancient elite.""")
        # time.sleep(3)
        print("""You spin faster and faster, more and more wildly with each step.
As you complete another revolution, you suddenly crash into the wall on your left.
Stone and brick come tumbling down on your head. You've dropped the torch in the confusion.""")
        # time.sleep(3)
        print("""You lie on the ground expecting the ceiling to fall at any moment,
and as the dust clears, you see the torch light glittering off 100,000 gold coins neatly
stacked in bags, ready for the hauling away.""")
        print('')
        print("Next to that is a perfectly maintained raft, ready and waiting for use.")
        print("You seem to have gotten just drunk enough to find the right combination of actions.")
        print("Now the only thing left for you to decide is what to buy with your newfound loot!.")

        dead("You found 100,000 gold coins and a functional raft! Time to head home and feel good about life.")
        # you stumble into a wall and break through into a treasure chamber

    # if you don't have the key
    elif not key and not drunk:
        print("""You step carefully into the hall.
In front of you are row after row of statue. You only understand some of the words
inscribed in their bases. Words like 'impale' and 'push'. You walk through inspecting
each statue for something like a clue when you notice that the staff of one statue
seems like it might be a level.""")
        print("You think to yourself, 'I guess I don't have a choice here do I?")
        print("You pull the lever.")
        # time.sleep(3)
        print("Nothing happens.")
        # time.sleep(5)
        print("... for a minute or so.")
        print("There's a loud sound as the door for the statuary collapses in on itself.")
        print("In your fright you drop your torch, and it goes it out completely.")
        # time.sleep(3)
        dead("You've sealed yourself in and lost your torch! You will die in this room, very, very slowly.")
        # you pull a level and the door closes sealing you in
        # your torch begins to fade
        # you starve to death in total darkness

    else:
        print("As you move from statue to statue you see one that stands out.")
        print("It seems to have a similar hexagonal shape carved into it as the box you found earlier.")
        print("You examine both under the torch light.")
        # time.sleep(3)
        print("The box seems to be a key for this particular statue.")
        print("You place the box in the hexagonal hole at the statues base, and try turning it.")
        print('')
        print("Against all odds, it clicks into place!")
        print('')
        print("The statue shudders and clicking and whirring, it slides to the right")
        print("revealing a passage way below.")
        print("You hop down into the passage and hear the sound of running water.")
        print("There seems to be a light at the end of this tunnel! You quickly run towards it.")

        # time.sleep(3)
        print("Approaching the light and the sound of running water, you see that there is another river here.")
        print("Perhaps it's the same river, or a different one? In either case, there's a raft awaiting you.")
        print("You hop in the raft without a second though and shove off for the future.")
        
        num_through_cave += 1
        start()
        

start()
