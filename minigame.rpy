# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image fields = "images/fields.jpg"

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        # Python Logic to check if the placement is correct.
        if (store.draggable == "bottle" and store.droppable == "Plastic Bin") or \
        (store.draggable == "paper" and store.droppable == "Paper Bin"):
            store.is_correct = True
        elif (store.draggable == "paper1" and store.droppable == "Paper Bin") or \
        (store.draggable == "papercup" and store.droppable == "Paper Bin" ):
            store.is_correct = True
        elif (store.draggable == "bottle1" and store.droppable == "Plastic Bin"):
            store.is_correct = True
        else:
            store.is_correct = False

        # Set the hide variable based on the name of the dragged item
        if store.draggable == "bottle":
            store.bottle_hide = True
        elif store.draggable == "bottle1":
            store.bottle_hide = True
        elif store.draggable == "paper":
            store.paper_hide = True
        elif store.draggable == "paper1":
            store.paper1_hide = True
        elif store.draggable == "papercup":
            store.papercup_hide = True

        return True

label game_start:
    default correct = 0
    default incorrect = 0
    default bottle_hide = False
    default paper_hide = False
    default paper1_hide = False
    default papercup_hide = False
    default bottle1_hide = False

    scene fields

    "Welcome to the trash sorting minigame!"

    "Simply drag and drop the trash to the corresponding bin it should be disposed to."
    
    # Start the main game loop by showing the screen.
    show screen setDragImages
    jump game_loop

label game_loop:
    # We now wait for a drag and drop event.
    call screen setDragImages

    # This part of the code is only reached after the screen returns,
    # which happens when an item is dropped.
    "The [draggable] was put into the [droppable]"

    if is_correct:
        $ correct += 1
        "That's the right place!"
    else:
        $ incorrect += 1
        "Oh, that's not quite right."

    # Check if the game is over.
    if (correct + incorrect) >= 5:
        jump sortCheck

    # This is the key change: we re-show the screen with the new variable states.
    show screen setDragImages
    jump game_loop

label sortCheck:
    hide screen setDragImages # Hide the screen before showing the result.
    image win = "win.png"
    image lose = "lose.png"

    if correct ==5:
        show win
        "You sorted all the trash correctly! You win!"
        jump continuation
    elif correct ==3:
        show win
        "You're getting there!"
        jump continuation
    else:
        show lose
        "You made a mistake. Better luck next time!"
        jump continuation

label continuation:
    "Nagpatuloy silang maglinis..."

    show a neutral
    a "Alam mo, parang ganito rin ang pagtingin ng iba patungkol sa gender..."

            
    a "Na kapag babae ka or bahagi ka ng LGBTQ+ community, wala kang magagawa, dahil para sa kanila lalaki parin ang mas maraming magagawa"
    show a happy
    a "Pero tignan mo tayo ngayon—pinapakita natin na kahit sino, puwedeng magbigay ng ambag sa komunidad."

    c happy "Tama ka, ang ganda ng punto mo."

    jump library_scene

    return

screen setDragImages:
    # The screen displays the drag and drop elements.
    text "sort the trash appropriately!":
        pos (70, 600)
        bold True
        color "#00000066"

    # CONTENTS
    text "correct = [correct]":
        pos (70, 650)
        bold True
        color "#00000066"

    text "wrong = [incorrect]":
        pos (70, 690)
        bold True
        color "#00000066"

    draggroup:
        drag:
            drag_name "Plastic Bin"
            xanchor 0.5
            xpos 0.5
            xoffset -200
            ypos 700
            child "images/plastic_bin_image.png"
            draggable False
            droppable True
            drag_raise False

        drag:
            drag_name "Paper Bin"
            xanchor 0.5
            xpos 0.5
            xoffset 200
            ypos 700
            child "images/paper_bin_image.png"
            draggable False
            droppable True
            drag_raise False


        if not bottle_hide:
            drag:
                drag_name "bottle"
                xpos 300
                ypos 100
                child "images/plastic_cup_image.png"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True

        if not bottle1_hide:
            drag:
                drag_name "bottle1"
                xpos 800
                ypos 100
                child "images/plastic_cup2_image.png"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True

        if not paper_hide:
            drag:
                drag_name "paper"
                xpos 600
                ypos 120
                child "images/paper_ball_image.png"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True

        if not paper1_hide:
            drag:
                drag_name "paper1"
                xpos 900
                ypos 100
                child "images/paper2_ball_image.png"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True

        if not papercup_hide:
            drag:
                drag_name "papercup"
                xpos 1000
                ypos 100
                child "images/paper_cup_image.png"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True