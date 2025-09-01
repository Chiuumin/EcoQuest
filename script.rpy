# Declare characters used by this game. The color argument colorizes the # name of the character.

define c = Character("Cindy", color="#ffe6cc", image="c")

define p = Character("Professor", color="#ffe6cc")

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

# The game starts here.
label start:
    scene medina_lacson with fade
    
    "Cindy, is a college student in BPSU, she loved sitting at the front of the Medina Lacson building."
    
    c neutral "She uses it as her comfort place. It is full of green grass, sunflowers and trees."

    "But recently, the air felt warm, the sun was not gentle as before, the sunflowers had withered."
    
    scene become_classroom with dissolve

    "In class, their professor discussed the impact of climate change and how the earth's temperature had already increased."
    
    "Now she understands why her surroundings is not the same as before, and why the sun is getting hotter day by day."
    scene beside_sarigamit with fade
    "As she took a walk she noticed the overflowing trash bin. Wrappers, plastic cups, and used face masks spill onto the grass."

    menu choice_1:
        "Pick up the trash, and throw it to trash bin":
            jump choice1_path

        "Ignore the trash and continue to walk":
            jump choice2_path

# Pick up the trash, and throw it to trash bin
label choice1_path:
    "While picking up the trash from the ground, Cindy smiled."
    c happy "A little action can be big someday."
    $ eco_meter += 5
    jump continuation_1


# Ignore the trash and continue to walk
label choice2_path:
    "As she walked by, she felt guilty."
    c curious "Next time, i'll pick up the trash if I see one."
    jump continuation_1


label continuation_1:
    scene medina_lacson with fade
    "As she continues to walk, Cindy pauses as she goes past to the once-green field, noticing the faded sunflowers."
    "A sigh slips from her lips."
    c curious "Hmm? What are the causes of pollution?"

    menu causes_of_pollution:
        "I don't know":
            c neutral "Maybe I'll ask my professor later or I'll search it online."
            jump ask_professor

        "I think vehicles and the increasing population":
            c happy "I notice that the smoke from cars contributes to air pollution. And since the population of students is increasing, more food stalls mean more packaging... more waste. Maybe that's the reason why managing the waste is difficult."
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

    "After class, Cindy thought about what decision she would make. She also wondered if she would do what her professor said."

    menu apply_advice:
        "I think it's too much if I do that.":
            jump apply_no

        "I should apply what my professor said.":
            jump apply_yes

# The path for not applying the advice
label apply_no:
    c "There's no change if I do that or not, maybe I should just share facts online, it can be helpful too. It's too much for me to do alone."

    "Cindy got home, she decided not to do anything, and just go to sleep."

    c "There are so many people out there who can do that, not just me, so I should rest and save my energy."
    jump create_website_prompt

# The path for applying the advice
label apply_yes:
    $ eco_meter += 10
    c "I have nothing to lose if I try to follow my professor's advice. Who knows, maybe one day I might influence others too."

    "Cindy got home and she decided to make a change."

    c "Tomorrow I'll bring a reusable tumbler, pick up trash if I can and maybe I should start posting eco-facts on my social media."
    jump create_website_prompt

# The prompt about creating a website
label create_website_prompt:
    c "What if I use my knowledge as a computer science student to create a website? That gives other students an awareness on what the cause of climate change, and what can we do?"

    menu create_website:
        "Create a website":
            jump website_yes

        "I should just sleep, it's impossible.":
            jump website_no

# The path for creating a website
label website_yes:
    $ eco_meter += 20
    c "Yes, I'll create one. Creating a website can help them to be aware."

    "She created a website and before she went to sleep, she posted eco-facts on her social media."

    "Tomorrow morning she presented it to her professor who said..."

    p "This was wonderful! Try to talk to the student council about this 'Clean and Green' website you created."

    "After she talks to the student council she walks with a smile and feels proud of herself."

    "She passed by again to Medina Lacson and saw another student picking up plastic."

    c "Even though the sunflowers disappear, at least there are students who start to take care of the surroundings."

    jump end_good

# The path for not creating a website
label website_no:
    c "My knowledge is not enough, and besides I'm not the only one who cares about the environment, I'll leave everything to them, they can do it."

    "She also said..."

    c "There are so many people out there who can do that, not just me, so I should rest and save my energy."

    "Before she went to sleep, she just posted eco-facts on her social media account thinking it could be helpful."

    "Tomorrow morning she decided to go to Medina Lacson and sit there while she's looking around and she notices the trash and continuous fading color of the grass."

    c "There is still trash, the color of the grass continues to fade and...the sunflowers are gone."

    jump end_bad

# Good ending
label end_good:
    if eco_meter >= 30:
        c "One small step... creates ripples."
        "GOOD END: Your actions created a lasting change. Your final eco-meter score is: [eco_meter]."
    else:
        "NEUTRAL END: You made an effort, but the change was small. Your final eco-meter score is: [eco_meter]."
    return

# Bad ending
label end_bad:
    "BAD END: Actions matter more than words."
    "Your final eco-meter score is: [eco_meter]."
    return

