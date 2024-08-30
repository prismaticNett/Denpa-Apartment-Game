# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Slow")
define l = Character("Loris")
define sl = Character("Slow & Loris")
define vb = Character("Vampire Bat")
define cr = Character("Crested Rat")
define sh = Character("Shrew")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    vb "Welcome to apartments. Isn't life beautiful?"
   
    s "Hi, I'm Slow--"

    l "And I'm Loris."

    sl "We're the cigarette brothers."
    # This ends the game.

    return