# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Slow")
define l = Character("Loris")
define sl = Character("Slow & Loris")
define vb = Character("Vampire Bat")
define cr = Character("Crested Rat")
define sh = Character("Shrew")
define ll = Character("Landlord")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bombe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    # This ends the game.

    return