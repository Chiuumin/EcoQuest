# Declare characters used by this game. The color argument colorizes the # name of the character.

define c = Character("Cindy", color="#ffe6cc", image="c")

define p = Character("Professor", color="#140056")

define a = Character("Alberto", image ="a")

define k = Character("Karen", image = "k", color="#c5e127")

define eco_meter = 0

# NVL characters are used for the phone texting
define c_nvl = Character("Cindy", kind=nvl, callback=Phone_SendSound)
define a_nvl = Character("Alberto", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

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

#PROFESSOR Sprite Config

image p slight smile:
    zoom 0.5
    "images/p 1.png"
    3
    "images/p 2.png"
    0.5
    repeat

image p slight smile2:
    zoom 0.5
    "images/ p 3.png"
    

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
    "images/Sunflower1.png"
    1.0
    "images/Sunflower2.png"
    1.0
    repeat

image medina_lacson = "images/Medina_lacson.jpg"
image comfort = "images/Comfort_space.jpg"
image bacomm = "images/bacomm.jpg"
image library = "images/Bpsu_lib.jpg"
image store = "images/Store.jpg"

# The game starts here.
label start:
    scene medina_lacson with fade

    play music "audio/gentle warmth.mp3" loop fadein 2.5
    
    "Sina Cindy at Alberto ay mga college students sa BPSU. Madalas silang umupo sa harap ng Medina Lacson Building, na nagsilbing kanilang pahingahan."
    
    scene comfort

    "Palagi silang tumatambay dito upang magpahinga mula sa mga mabibigat na talakayin sa eskuwela."

    scene sunflower

    "Nangingibabaw sa lugar na ito ang luntiang damo na parang masarap higaan, mga namumukadkad na sunflower na masarap pitasin, at naglalakihang puno sa paligid na masarap silungan sa tuwing mainit o umuulan."

    "Sa madalas nilang pagtambay sa harap ng Medina Lacson, higit pang tumibay ang pagkakaibigan nina Cindy at Alberto."

    scene comfort with fade

    show a happy

    "Doon din natuklasan ni Cindy na kabilang si Alberto sa LGBTQ+, bagay na mas lalo niyang hinangaan."

    "Simula noon, mas naging makulay ang kanilang samahan: lagi na silang nagtatawanan, sabay na nag-aaral, at walang sawang nagbabahagi ng mga pangarap nila sa kanilang buhay."

    show a neutral

    "Ngunit unti-unti nilang napapansin ang pagbabago sa lugar."

    "Ramdam nila na umiinit ang simoy ng hangin, hindi na kasing-sariwa ng dati ang nalalanghap nilang hangin, at ang dating malulusog na mirasol ay nagsimulang malanta."

    c neutral "Ang init na ng panahon, hindi na talaga ito tulad ng dati…"

    hide a neutral

    jump classroom_scene

label classroom_scene:
    scene bacomm with fade

    show p slight smile
    p "Okay class, ngayong araw ay tatalakayin natin ang tungkol sa klima at ang epekto ng climate change."

    p "Una, ang pangunahing sanhi ng pag-init ng mundo o global warming ay ang patuloy na pagdami ng greenhouse gases gaya ng Carbon Dioxide (CO₂), Methane (CH₄), at Nitrous Oxide (N₂O)."

    p "Karaniwan itong nagmumula sa pagsunog ng fossil fuels katulad ng langis, uling, at gas—na ginagamit sa pabrika, sa sasakyan, at sa mga planta ng kuryente."

    p "Dahil dito, naiipon ang init sa ating atmosphere at unti-unting tumataas ang temperatura ng mundo."

    p "Cindy."

    menu question:
        p "Ano ang pangunahing sanhi ng pag-init sa mundo?"
        "Pagdami ng Greenhouse gases.":
            $ eco_meter += 1
            p "Tama! Greenhouse gases mula sa fossil fuels ang dahilan."
        "Pagdami ng halaman":
            $ eco_meter -= 1
            p "Mali, ang mga halaman ay nakakatulong pa nga sa pag-absorb ng carbon."
        "Pag-inom ng softdrinks":
            $ eco_meter -= 1
            p "Mali. Walang kaugnayan ang softdrinks dito."

    p "Ikalawa, hindi natin maikakaila na malaking bahagi rin ng problema ay dahil sa ating pagiging iresponsableng tao."

    p "Ang maling pagtatapon ng basura, lalo na ng plastik, ay nagdudulot ng polusyon sa lupa at karagatan. Tandaan, ang plastik ay maaaring tumagal ng daan-daang taon bago mabulok, at kapag ito’y sinunog, nagiging lason pa ito sa hangin."

    menu:
        p "Ano ang epekto ng plastik sa kalikasan?"
        "Tumutulong maglinis ng kapaligiran":
            $ eco_meter -= 1
            p "Mali. Ang plastik ay nakakapagdulot ng polusyon."
        "Tumagal ng daan-daang taon bago mabulok at nakakalason kapag sinunog":
            $ eco_meter += 1
            p "Tama! Isa ito sa mga pinaka-seryosong problema sa kalikasan."
        "Nakakaganda ng tanawin":
            $ eco_meter -= 1
            p "Mali. Ang plastik ay nakakasira ng tanawin at kapaligiran."

    p "Ang usok mula sa mga pabrika at tambutso ng sasakyan ay nagdaragdag ng carbon emissions na lalo pang nagpapainit sa ating mundo."

    menu:
        p "Saan karaniwang nanggagaling ang carbon emissions?"
        "Sa mga halaman at puno":
            $ eco_meter -= 1
            p "Mali, nakakatulong ang mga halaman sa paglinis ng hangin."
        "Sa pabrika, sasakyan, at pagsunog ng fossil fuels":
            $ eco_meter += 1
            p "Tama! Iyan ang pangunahing pinagmumulan ng emissions."
        "Sa pag-inom ng tubig":
            $ eco_meter -= 1
            p "Mali. Walang kaugnayan dito ang pag-inom ng tubig."

    p "Ang mga ganitong gawain ay hindi lamang nakasisira sa kalikasan, kundi nagdudulot din ng panganib sa ating kalusugan at pang-araw-araw na pamumuhay."

    p "Alam nyo ba na malaki ang epekto nito sa tao, lalo na sa ating kalusugan?"

    menu:
        p "Ano ang epekto ng maruming hangin at tubig?"
        "Nagdudulot ng hika, ubo, diarrhea, cholera":
            $ eco_meter += 1
            p "Tama! Nakakasama ito sa kalusugan ng tao."
        "Nagiging mas masarap ang pagkain":
            $ eco_meter -= 1
            p "Mali. Wala itong kinalaman sa lasa ng pagkain."
        "Walang epekto sa tao":
            $ eco_meter -= 1
            p "Mali. Tayo ang unang naaapektuhan."

    p "Sa ating pangkabuhayan naman—dahil sa mas matinding init at pagbaha, naaapektuhan ang ani ng mga magsasaka at huli ng mga mangingisda."

    menu:
        p "Ano ang epekto ng climate change sa kabuhayan?"
        "Naaapektuhan ang ani at huli ng isda":
            $ eco_meter += 1
            p "Tama! Kaya nagiging mahirap ang pagkakaroon ng sapat na pagkain."
        "Mas dumarami ang pagkain":
            $ eco_meter -= 1
            p "Mali. Mas kumokonti ang resources dahil sa init at baha."
        "Walang epekto sa ekonomiya":
            $ eco_meter -= 1
            p "Mali. Malaki ang epekto sa ekonomiya ng bansa."

    p "Kaya class, always remember na ang climate change ay hindi lang isyu ng kalikasan, kundi isyu rin ng tao at ng ating kinabukasan."

    p "Bilang kabataan at mamamayan, tungkulin nating baguhin ang ating gawi.. Pwede nating bawasan ang basura, magtipid sa enerhiya, at suportahan ang mga organisasyong pangkalikasan."

    p "Kung hindi tayo kikilos ngayon, maipapamana natin ang problema sa susunod na henerasyon."

    "Ngayon ay mas naiintindihan na ni Cindy kung bakit iba na ang kanyang paligid at kung bakit tila ba mas umiinit ang panahon nitong mga nakaraan."

    jump medina_scene

label medina_scene:
    scene medina_lacson with fade

    "Pagkatapos ng klase, dumaan sina Cindy at Alberto sa tapat ng Medina, napansin nila ang umaapaw na basurahan"

    c neutral "Parang wala nang pakialam ang ibang estudyante sa ating kapaligiran—ang daming basurang nagkalat"

    menu:
        "Ano ang gagawin nila?"
        "Pulutin ang mga basura":
            $ eco_meter += 1
            a happy "Bestie, walang magbabago kung tititigan lang natin 'to."
            
            a "Maliit man ang aksyon na ito, pero kung mas marami tayong matutulungan, mas magiging malinis ulit ang lugar."
            
            "Nagpatuloy silang maglinis..."
            
            #CALL DRAG AND DROP MINI-GAME
            
            a neutral "Alam mo, parang ganito rin ang pagtingin ng iba patungkol sa gender..."

            a "Na kapag babae ka or bahagi ka ng LGBTQ+ community, wala kang magagawa, dahil para sa kanila lalaki parin ang mas maraming magagawa"

            a "Pero tignan mo tayo ngayon—pinapakita natin na kahit sino, puwedeng magbigay ng ambag sa komunidad."

            c happy "Tama ka, ang ganda ng punto mo."

            jump library_scene

        "Iwasan ang basurahan":
            $ eco_meter -= 1
            a angry "Grabe, nakakadiri naman tignan yung basurahan na yan."

            c neutral "Sa ibang araw nalang tayo mag pulot kapag may gamit na tayo."

            "Hindi nila pinansin ang basurahan kaya lalo pang dumami ang kalat sa paligid."

            jump library_scene
        
# -------------------------
# LIBRARY SCENE (Website path)
# -------------------------
label library_scene:

    scene library with fade
    "Sa vacant time nila, naisipan nina Cindy at Alberto na gumawa ng Facebook page muna habang pinaplano ang mas malaking website"
    
    "Dinisenyo ni Cindy ang layout at nag-upload ng content tungkol sa pagbabawas ng basura."
    
    "Nagdagdag naman si Alberto ng makukulay na graphics at mga quote"

    jump karen_conflict

# -------------------------
# KAREN CONFLICT
# -------------------------
label karen_conflict:

    scene bacomm with fade
    "Kinabukasan, nakita ni Karen ang kanilang page, kaya pinaringgan nya ang dalawa."

    k "Ang taas talaga ng pangarap ng dalawang 'to. Kunwari pang naglilinis, mga pasikat, bida-bida."

    "May ilan na natawa sa comment ni Karen ngunit may ilan ding naging intresado sa page."

    menu:
        "Ano ang gagawin nila?"

        "Patulan si Karen":
            $ eco_meter -= 1

            c "Ano bang problema mo sa ginagawa namin, ha?"

            a "Kung wala kanbg maaambag dito, wag mong sirain ang ginagawa namin."

            "Nag-walkout si Karen nang padabog, at nagkalat sa campus ang kanilang away."
            jump house_scene

        "Hayaan na lang at mag-focus":
            $eco_meter -= 1

            a happy "Hayaan mo na, beh. Dadami rin tayo at may pagbabago ring mangyayari."

            c "Oo nga. Hindi dapat tayo paapekto sa sinabi nya, at lalong hindi tayo pwede panghinaan ng loob"
            jump house_scene

label house_scene:
    show store with fade  
    
    "Kinagabihan, nag-text si Cindy kay Alberto."
     
    nvl_narrator "16:28"
    c_nvl "Bes, dahil CS students tayo, puwede tayong gumawa ng website gamit ang coding skills natin."   

    a_nvl "Sige! Ako bahala sa posters at slogans." 
    
    
    return






    