# Declare characters used by this game. The color argument colorizes the # name of the character.

define c = Character("Cindy", color="#ffe6cc", image="c")

define p = Character("Professor", color="#ffe6cc")

define a = Character("Alberto", image ="a")

define eco_meter = 0

# CINDY Sprite Config

# Blinking Sprite using Ren'Py's ATL Feature.
image side c neutral:
    "images/side c 1.png"
    3
    "images/side c 2.png"
    0.5
    repeat

image side c curious:
    "images/side c 3.png"
    3
    "images/side c 4.png"
    0.5
    repeat

image side c happy:
    "images/side c 5.png"
    3
    "images/side c 6.png"
    0.5
    repeat

image side c angry:
    "images/side c 7.png"
    3
    "images/side c 8.png"
    0.5
    repeat

# ALBERTO Sprite Config

image a happy:
    zoom 0.5
    "images/a 1.png"
    3
    "images/a 2.png"
    0.5
    repeat

# The game starts here.
label start:
    scene medina_lacson with fade
    
    "Cindy, is a college student in BPSU, she loved sitting at the front of the Medina Lacson building."
    
    c neutral "She uses it as her comfort place. It is full of green grass, sunflowers and trees."

    "But recently, the air felt warm, the sun was not gentle as before, the sunflowers had withered."
    
    scene bacomm_classroom with dissolve

    show p serious

    p "The Earth's temperature has increased by more than 1°C already. That may sound small, but it’s enough to change ecosystems."

    p "Climate change isn’t some faraway issue, it’s affecting us here, now."
    
    "Cindy understood why her favorite spot wasn’t the same as before, and why the sun was harsher every day."

    hide p serious

    scene beside_sarigamit with fade
    "As Cindy and Alberto walked, they noticed an overflowing trash bin, the wrappers, plastic cups, and face masks spilling onto the grass."

    show a happy
    a "Bestie, the place is getting worse... Should we do something?"
    
    menu choice_1:
        "Pick up the trash, and throw it to trash bin":
            jump choice1_path

        "Ignore the trash and continue to walk":
            jump choice2_path

    
# Pick up the trash, and throw it to trash bin
label choice1_path:

    
    "While picking up the trash from the ground, Cindy smiled."

    c happy "A little action can be big someday."

    hide a happy

    $ eco_meter += 5
    jump continuation_1


# Ignore the trash and continue to walk
label choice2_path:

    hide a happy

    "As she walked by, she felt guilty."

    c curious "Next time, i'll pick up the trash if I see one."
    jump continuation_1


label continuation_1:
    scene medina_lacson with fade
    "As she continues to walk, Cindy pauses as she goes past to the once-green field, noticing the faded sunflowers."
    "A sigh slips from her lips."
    c "Hmm? What are the causes of pollution?"

    menu causes_of_pollution:
        "I don't know":
            c "Maybe I'll ask my professor later or I'll search it online."
            jump ask_professor

        "I think vehicles and the increasing population":
            "I notice that the smoke from cars contributes to air pollution. And since the population of students is increasing, more food stalls mean more packaging... more waste. Maybe that's the reason why managing the waste is difficult."
            jump ask_professor_simple

# The dialogue path for choosing "I don't know"
label ask_professor:
    scene bacomm_classroom with dissolve

    "Back in the classroom, Cindy raises her hand and asks her professor."

    c "Sir, what are the causes of pollution?"

    p "The smoke from vehicles, factories, waste and sometimes the populations. Since the world population are increasing they can also contribute to pollution, that can cause our environment to slowly destroy."

    c "So Sir, what can we do as students to help aid it?"

    jump professor_answer

# The dialogue path for choosing "I think..."
label ask_professor_simple:
    scene bacomm_classroom with dissolve

    "Back in the classroom, Cindy raises her hand and asks her professor."

    c "Sir, what can we do as students to help with climate change?"

    jump professor_answer

# The professor's response, shared by both dialogue paths
label professor_answer:
    p "Good question, Cindy. Start small. Refuse single-use plastics, use reusable containers, conserve energy, and educate others. Climate change isn’t just a big problem—it's a collection of small actions repeated every day."

    p "It may feel small, but when many do it—it changes everything."

    "After class, Cindy reflected on her decision."

    menu apply_advice:
        "I think it's too much if I do that.":
            jump apply_no

        "I should apply what my professor said.":
            jump apply_yes

# If Cindy refuses to apply
label apply_no:
c "There's no change if I do it or not. Maybe I’ll just share facts online, that’s enough."
"Cindy got home and decided not to act, telling herself others would take care of it."

jump create_website_prompt


# If Cindy applies the advice
label apply_yes:

$ eco_meter += 10

c "I’ll try. Tomorrow, I’ll bring my reusable tumbler, pick up trash when I can, and post eco-facts on social media."


# Reference to ENSO platform (realistic touch!)

c "Hey, maybe I can also use ENSO’s 20% discount when I bring my own tumbler. Saves money *and* the planet."


jump create_website_prompt

# Cindy considers creating a website
label create_website_prompt:

c "What if I use my Computer Science skills to create a website that spreads awareness?"
a "That’s a great idea! We can include eco-facts, equality messages, and even link it to ENSO’s programs."


menu create_website:
    "Create a website":
        jump website_yes

    "I should just sleep, it’s impossible.":
        jump website_no


# Website path YES (positive outcome)
label website_yes:

    $ eco_meter += 20
    # CG Suggestion: Cindy coding at her laptop with Alberto beside her

    c "Yes, I'll create one. This way, more people can learn and take action."

    "They stayed up late, building a colorful site with eco-tips and slogans like 'Protect the Earth, Protect Each Other.'"

    "The next day, they presented it to their professor."

    p "This is wonderful! Share this with the student council—they’ll love it."

    "The student council soon organized a Clean and Green Week inspired by their project."


    scene Medina_lacson with fade
    # CG Suggestion: Students cleaning together, Cindy & Alberto smiling

    "They passed by Medina Lacson and saw students cleaning, watering plants, and bringing tumblers."

    c "Even though the sunflowers disappeared, hope is growing in their place."

    jump end_good


# Website path NO (negative outcome)

label website_no:
    c "My knowledge isn’t enough… I’ll just leave it to others."

    "Before sleeping, Cindy only posted some eco-facts on social media."

    scene Medina_lacson with fade
    # CG Suggestion: Empty, faded field with scattered trash

    "The next morning, Cindy sat in Medina Lacson again. The grass had faded, trash was scattered, and the sunflowers were gone."

    c "Nothing has changed… it only got worse."

    jump end_bad

    # GOOD END
    label end_good:
    c "GOOD END: Small steps, big ripples. You helped inspire change!"
    "Your final eco-meter score is: [eco_meter]"
    return

# BAD END
label end_bad:
    "BAD END: Words without action change nothing."
    "Your final eco-meter score is: [eco_meter]"
    return


