# Declare characters used by this game. The color argument colorizes the # name of the character.

define c = Character("Cindy", color="#ffe6cc", image="c")

define p = Character("Professor", color="#140056")

define a = Character("Alberto", image ="a")

define k = Character("Karen", image = "k", color="#c5e127")

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

image a neutral:
    zoom 0.5
    "images/a 3.png"
    3
    "images/a 4.png"
    0.5
    repeat


#BG CONFIG
image sunflower:
    "images/sunflower1.jpg"
    1.5
    "images/sunflower2.png"
    1.5
    repeat

image medina_lacson = "images/Medina_lacson.jpg"
image comfort = "images/Comfort_space.jpg"


# The game starts here.
label start:
    scene medina_lacson with fade
    
    "Sina Cindy at Alberto ay mga college students sa BPSU. Madalas silang umupo sa harap ng Medina Lacson Building, na nagsilbing kanilang pahingahan"
    
    scene comfort

    "Palagi silang tumatambay dito upang magpahinga mula sa mga mabibigat na talakayin sa eskuwela"

    scene sunflower

    "Nangingibabaw sa lugar na ito ang luntiang damo na parang masarap higaan, mga namumukadkad na sunflower na masarap pitasin, at naglalakihang puno sa paligid na masarap silungan sa tuwing mainit o umuulan"

    "Sa madalas nilang pagtambay sa harap ng Medina Lacson, higit pang tumibay ang pagkakaibigan nina Cindy at Alberto."

    "Doon din natuklasan ni Cindy na kabilang si Alberto sa LGBTQ+, bagay na mas lalo niyang hinangaan."



    