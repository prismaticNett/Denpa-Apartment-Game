﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Slow")
define l = Character("Loris")
define sl = Character("Slow & Loris")
define vb = Character("Vampire Bat")
define cr = Character("Crested Rat")
define sh = Character("Shrew")
define ll = Character("Landlord")
$ fear = 0 ##our fear meter
$ tenants_saved = [] ##will append the names of each tenant as they leave


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bombe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show vampirebat placeholder


    vb "Why are you here?"
    vb "What do you want from me?" with vpunch

    ll "..."

    show sloris placeholder    
    jump meter
    

    # These display lines of dialogue.
    
    # This ends the game.

    return

label meter:
    $ randomNum = renpy.random.randint(-3,3)
    if randomNum < 0:
        $ changed = "decreased"
        $ randomNum = randomNum*-1
    else:
        $ changed = "increased"
    
    $ meter = renpy.random.choice(["foo","bar"])
    vb "your %(meter)s meter! it %(changed)s by %(randomNum)s"
    return
