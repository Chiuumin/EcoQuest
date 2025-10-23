# Declare characters used by this game. The color argument colorizes the # name of the character.

define c = Character("CINDY", color="#ff8400", image="c")

define p = Character("PROFESSOR", color="#140056")

define a = Character("ALBERTO", image ="a")

define k = Character("KAREN", image = "k", color="#c5e127")

define eco_meter = 0

# NVL characters are used for the phone texting
define c_nvl = Character("Cindy", kind=nvl, callback=Phone_SendSound)
define a_nvl = Character("Alberto", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# TRANSFORM POSITION Sprite Config

#transform slightleft:
#    xpos 0.25
#    ypos 1.0

#transform slightright:
#    xpos 0.75
#    ypos 1.0

#transform center:
#    xpos 0.5
#    ypos 1.0


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

image p slightsmile2:
    zoom 0.5
    "images p 3.png"
    

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

image a curious:
    zoom 0.5
    "images/a 6.png"
    3
    "images/a 7.png"
    0.5
    repeat

#KAREN SPRITE CONFIG

image k neutral:
    zoom 0.5
    "images/k 1.png"
    3
    "images/k 2.png"
    0.5
    repeat

image k smirk:
    zoom 0.5
    "images/k 3.png"
    3
    "images/k 4.png"
    0.5
    repeat

image k provoked:
    zoom 0.5
    "images/k 5.png"
    3
    "images/k 6.png"
    0.5
    repeat

#BG and CG CONFIG
image sunflower:
    "images/Sunflower1.png"
    1.0
    "images/Sunflower2.png"
    1.0
    repeat

image cg1:
    "images/cg1.png"
    1.0
    "images/cg1o5.png"
    0.5
    repeat

#MINIGAME RESULT CONFIG
image win:
    "images/win1.png"
    1.0
    "images/win2.png"
    1.0
    repeat

image lose:
    "images/lose1.png"
    1.0
    "images/lose2.png"
    1.0
    repeat

image medina_lacson = "images/Medina_lacson.jpg"
image comfort = "images/Comfort_space.jpg"
image bacomm = "images/bacomm.jpg"
image library = "images/Bpsu_lib.jpg"
image store = "images/Store.jpg"
image congrats = "images/congratulations.png"
image Under_tree = "images/Under_tree.jpg"
image Black = "images/Black.png"

# The game starts here.
label start:
    scene medina_lacson with fade

    play music "audio/gentle warmth.mp3" loop fadein 2.5
    
    "Sina Cindy at Alberto ay mga college students sa BPSU. Madalas silang umupo sa harap ng Medina Lacson Building, na nagsilbing kanilang pahingahan."
    
    scene comfort

    "Palagi silang tumatambay dito upang magpahinga mula sa mga mabibigat na talakayin sa eskuwela."

    scene sunflower

    "Nangingibabaw sa lugar na ito ang luntiang damo na parang masarap higaan, mga namumukadkad na sunflower na tila ba masarap pitasin."

    "Sa madalas nilang pagtambay sa harap ng Medina Lacson, higit pang tumibay ang pagkakaibigan nina Cindy at Alberto."

    scene comfort with fade

    show a happy

    "Doon din natuklasan ni Cindy na kabilang si Alberto sa LGBTQ+, bagay na mas lalo niyang hinangaan."

    "Simula noon, mas naging makulay ang kanilang samahan: lagi na silang nagtatawanan, sabay na nag-aaral, at walang sawang nagbabahagi ng mga pangarap nila sa kanilang buhay."

    show a neutral

    "Ngunit nitong mga huling linggo, unti-unti nilang napapansin ang kakaibang pagbabago sa lugar."

    "Ramdam nila na umiinit ang simoy ng hangin, hindi na kasing-sariwa ng dati ang nalalanghap nilang hangin, at ang dating malulusog na sunflower ay nagsimulang malanta."

    c neutral "Ang init na ng panahon, hindi na talaga ito tulad ng dati…"

    c curious "Dapat siguro makinig tayo nang mabuti kay sir. Baka may kinalaman dito 'yung climate change na sinasabi niya."

    hide a neutral

    jump classroom_scene

label classroom_scene:
    scene bacomm with fade

    show p slight smile
    p "Okay class, quick question—napansin niyo ba na parang mas mainit na ngayon kaysa dati?"

    c neutral "Opo sir! Parang everyday finals week, walang hangin sa labas ng SG."

    show a curious at left

    show p slight smile at right

    a "True po! Baka pwede nang magluto ng itlog sa semento sa init!"

    p "HAHA! Pero seryoso, tama ‘yan. At ngayon, tatalakayin natin kung bakit nag-iiba ang klima."

    p "Una, ang pangunahing dahilan ng pag-init ng mundo ay ang pagdami ng greenhouse gases tulad ng Carbon Dioxide (CO₂), Methane (CH₄), at Nitrous Oxide (N₂O)."
    p "Kadalasan galing ito sa pagsunog ng fossil fuels—yung ginagamit sa pabrika, sasakyan, at planta ng kuryente."
    p "Dahil dito, naiipon ang init sa atmosphere at unti-unting tumataas ang temperatura ng mundo."

    p "Cindy, gusto mo bang hulaan kung ano ang pinaka-sentro ng problema rito?"
    
    menu question1:
        p "Ano ang pangunahing sanhi ng pag-init sa mundo?"
        "Pagdami ng greenhouse gases mula sa fossil fuels.":
            $ eco_meter += 10
            p "Tama! Ang greenhouse gases mula sa fossil fuels ang dahilan."

        "Pagdami ng halaman.":
            $ eco_meter -= 10
            p "Mali. Ang mga halaman nga ang tumutulong mag-absorb ng carbon."
        "Pag-inom ng softdrinks.":
            $ eco_meter -= 10
            p "Mali. Walang kinalaman dito ang softdrinks—maliban na lang kung carbonated atmosphere ang gusto mo..."

    p "Ika-dalawa, malaking bahagi ng problema ay galing din sa iresponsableng gawain ng tao."
    p "Halimbawa, maling pagtatapon ng basura—lalo na ng plastik. Alam niyo bang tumatagal ito ng daan-daang taon bago mabulok?"

    c neutral "Kaya pala ang daming plastic cup sa canteen na parang hindi nauubos"

    menu question2:
        p "Ano ang epekto ng plastik sa kalikasan?"
        "Tumutulong maglinis ng kapaligiran.":
            $ eco_meter -= 10
            p "Mali. Ang plastik ay nakakadagdag ng polusyon."
        "Tumagal ng daan-daang taon bago mabulok at nakakalason kapag sinunog.":
            $ eco_meter += 10
            p "Tama! Isa ito sa mga pinaka-seryosong problema sa kalikasan."
        "Nakakaganda ng tanawin.":
            $ eco_meter -= 10
            p "Mali. Plastik pollution? Hindi yan aesthetic, class."

    p "Ang usok naman mula sa mga pabrika at tambutso ay nagdaragdag ng carbon emissions."

    show a happy
    a "Lalo na po ‘yung mga jeep sa tapat ng Main Gate! Instant greenhouse effect."

    menu question3:
        p "Saan karaniwang nanggagaling ang carbon emissions?"
        "Sa mga halaman at puno.":
            $ eco_meter -= 10
            p "Mali. Ang mga halaman pa nga ang tumutulong maglinis ng hangin."
        "Sa pabrika, sasakyan, at pagsunog ng fossil fuels.":
            $ eco_meter += 10
            p "Tama! Iyan ang pangunahing pinagmumulan ng emissions."
        "Sa pag-inom ng tubig.":
            $ eco_meter -= 10
            p "Mali. Tubig ay life, hindi carbon source."

    p "Ang mga ganitong gawain ay hindi lang nakasisira sa kalikasan, kundi pati sa ating kalusugan."

    menu question4:
        p "Ano ang epekto ng maruming hangin at tubig?"
        "Nagdudulot ng hika, ubo, diarrhea, cholera.":
            $ eco_meter += 10
            p "Tama! Nakakasama ito sa kalusugan ng tao."

        "Nagiging mas masarap ang pagkain.":
            $ eco_meter -= 10
            p "Mali. Hindi natin gusto ng microplastics sa ulam."
        "Walang epekto sa tao.":
            $ eco_meter -= 10
            p "Mali. Tayo ang unang naaapektuhan!"

    p "At sa kabuhayan, dahil sa sobrang init at pagbaha, bumababa ang ani ng mga magsasaka at huli ng mga mangingisda."

    menu question5:
        p "Ano ang epekto ng climate change sa kabuhayan?"
        "Naaapektuhan ang ani at huli ng isda.":
            $ eco_meter += 10
            p "Tama! Kaya nagiging mahirap makakuha ng sapat na pagkain."

        "Mas dumarami ang pagkain.":
            $ eco_meter -= 10
            p "Mali. Mas kumokonti ang resources dahil sa init at baha."
        "Walang epekto sa ekonomiya.":
            $ eco_meter -= 10
            p "Mali. Malaki ang epekto nito sa ating ekonomiya."

    p "Kaya class, tandaan: ang climate change ay hindi lang isyu ng kalikasan—ito ay isyu ng tao at ng ating kinabukasan."
    p "Bilang kabataan, puwede nating bawasan ang basura, magtipid ng enerhiya, at suportahan ang mga proyektong pangkalikasan."
    p "Kung hindi tayo kikilos ngayon, maipapamana natin ang problema sa susunod na henerasyon."

    hide p
    show a neutral at center
    stop music fadeout 1.5

    "Ngayon ay mas malinaw na kay Cindy at Alberto kung bakit nagbabago ang klima—at kung paano sila maaaring maging bahagi ng solusyon."

    a "Grabe pala talaga. Naaalala ko ‘yung mga basura sa labas ng Medina..."

    c neutral "Oo nga, parang connected lahat, no? Dapat may gawin talaga tayo."



    jump medina_scene

label medina_scene:
    scene medina_lacson with fade

    play music "audio/Happy smile.mp3" loop fadein 2.5

    "Pagkatapos ng klase, dumaan sina Cindy at Alberto sa tapat ng Medina. Agad nilang napansin ang umaapaw na basurahan at mga nagkalat na plastic wrapper sa damuhan."

    c neutral "Hay, Bestie. Sabi na nga ba. Parang wala nang pakialam ang ibang estudyante sa ating kapaligiran—ang daming basurang nagkalat."

    menu:
        "Ano ang gagawin nila?"
        "Pulutin ang mga basura":
            $ eco_meter += 10
            show a curious
            a "Bestie, walang magbabago kung tititigan lang natin 'to."
            show a happy
            a "Maliit man ang aksyon na ito, pero kung mas marami tayong matutulungan, mas magiging malinis ulit ang lugar."
            
            #CALL DRAG AND DROP MINI-GAME

            jump game_start

        "Iwasan ang basurahan":
            $ eco_meter -= 10

            show a neutral
            a "Grabe, nakakadiri naman tignan yung basurahan na yan."

            c neutral "Sa ibang araw nalang tayo mag pulot kapag may gamit na tayo."

            "Hindi nila pinansin ang basurahan kaya lalo pang dumami ang kalat sa paligid."

            jump library_scene
        
# -------------------------
# LIBRARY SCENE (Website path)
# -------------------------
label library_scene:

    scene library with fade
    show cg1
    "Dahil gusto nilang magsimula agad, naisipan nina Cindy at Alberto na gumawa ng isang **Facebook page** muna habang pinaplano ang mas malaking website."
    
    "Dinisenyo ni Cindy ang layout at nag-upload ng content tungkol sa pagbabawas ng basura at recycling tips."
    
    "Nagdagdag naman si Alberto ng makukulay na graphics at mga quotes tungkol sa kalikasan, gamit ang kanyang creative eye."

    hide cg1
    stop music fadeout 1.0

    jump karen_conflict

# -------------------------
# KAREN CONFLICT
# -------------------------
label karen_conflict:

    scene bacomm with fade
    "Kinabukasan, habang nasa klase sila, nakita ni Karen ang kanilang page sa kanyang cellphone. Agad siyang nagbigay ng sarkastikong komento."

    show k neutral at center
    k "Ang taas talaga ng pangarap ng dalawang 'to. Kunwari pang naglilinis, mga pasikat, bida-bida."

    "May ilan na natawa sa comment ni Karen ngunit may ilan ding naging intresado sa page."

    menu:
        "Ano ang gagawin nila?"

        "Patulan si Karen":
            $ eco_meter -= 10

            c angry "Ano bang problema mo sa ginagawa namin, ha? Kung wala kang planong tumulong, 'wag kang manggulo!"

            show a neutral at left

            a "Kung wala kang maaambag dito, wag mong sirain ang ginagawa namin. Sa 'yo na yang negativity mo!"

            show k provoked at right

            "Nag-walk out si Karen nang padabog. Kumalat sa campus ang kanilang away. Ang pagtuon ng atensyon ay nalipat mula sa adbokasiya patungo sa away-personal."

            jump house_scene

        "Hayaan na lang at mag-focus":
            $ eco_meter -= 10

            show a happy at left

            show k neutral at right 

            a happy "Hayaan mo na, beh. Wag tayong magpababa sa level niya. Focus tayo sa goal natin."

            c neutral "Oo nga. Hindi dapat tayo paapekto sa sinabi nya, at lalong hindi tayo pwede panghinaan ng loob"
            jump house_scene

label house_scene:
    show store with fade  
    
    "Kinagabihan, nag-text si Cindy kay Alberto. Ang kanilang simpleng Facebook page ay naging insentibo para mas pagbutihin ang kanilang advocacy."
     
    nvl_narrator "16:28"
    c_nvl "Bes, dahil CS students tayo, puwede tayong gumawa ng website gamit ang coding skills natin."   

    a_nvl "Sige! Ako bahala sa posters at slogans."

    a_nvl "Kaso teh"

    a_nvl "kung gagawa tayo ng website, hindi ba mas maganda na ipakita natin yung platforms ng ENSO?"

    a_nvl "para maging epektibo ang advocacy nila"

    c_nvl "Tama ka dyan! Meet up tayo malapit sa SG para i-strategize yung website content"
    jump coding_scene


label  coding_scene:
    scene Under_tree with fade

    menu:
        "Coding Challenge!"
        "Ipagpatuloy kahit mahirap":
            $ eco_meter += 20

            show a happy

            "Gabi-gabi, nagpuyat sina Cindy at Alberto upang mag-brainstorm."
            
            "Naglabasan ang maraming errors, bugs, at frustration, pero hindi sila sumuko hangga't sa natapos din ang website—isang komprehensibong hub para sa environmental awareness."

            jump game_start2
        
        "Sumuko at stick na lang sa FB":
            $ eco_meter -= 20

            show a neutral

            c neutral "andaming error ayuko na!"

            a "di ganon kalawak ang knowledge natin sa coding, okay na siguro ang fb page natin."
            "Nadismaya si Cindy at nag-agree na mag-stick na lang sila sa FB page"
            jump fb_page

#-----------------------
#FACULTY SCENE
#-----------------------

label faculty_scene:
    scene bacomm with fade
    "Pagkaraan ng ilang linggo, inilusad nila ang website at pinakita ito sa kanilang propesor."

    show p slight smile
    p "Uy, ang ganda nito ah! Hindi lang informative, malinaw pa yung pagkaka-explain ninyo."

    c happy "Salamat po, Sir! Ang saya kasi parang worth it lahat ng puyat at kape."

    show a happy at left
    show p slight smile at right
    a "Oo nga po, Sir. Akala po namin ay may kulang pa, buti na lang pasado pala sa inyo."
    
    p "Naku, pasado lang? Hindi lang pasado, impressive! Dahil dito, bibigyan ko pa kayo ng extra grade para sa midterms."
    
    c happy "Talaga po, Sir? Yehey! Thank you po!"

    show p slight smile
    p "Sige, ipakita niyo yan sa ENSO, ha? Para matulungan kayo na ipromote toh sa public at ma-inspire din yung ibang estudyante sa ginawa niyo."

    c neutral "Opo, sir. gagawin po namin best namin."

    show a happy
    a "Told you, worth it 'toh. Salamat po, prof, malaking tulong 'yung tiwala niyo."    
   
    p "Good job. Ituloy niyo yan, I can see the potential."

    jump student_council


# -------------------------
# STUDENT COUNCIL (Q&A)
# -------------------------
label student_council:

    scene medina_lacson with fade

    "Sa wakas, nakarating sina Cindy at Alberto sa tapat ng Medina. Laking gulat nila nang makita si Karen."

    show k smirk
    k "Oh, Cindy, Alberto! Ano namang ginagawa niyo rito?" 
    c curious "Nandito kami para mag-present sa ENSO ng website na ginawa namin." 

    show k provoked
    menu:
        k "Pero ano naman ang magagawa ng mga simpleng tao para makatulong?" 
        "Tamang pagtatapon ng basura at pagtitipid sa resources":
            $ eco_meter += 10
            a "Tama! Kahit maliit na bagay malaking tulong na ‘yon."
        "Wala silang magagawa":
            $ eco_meter -= 10
            a "Mali, lahat tayo kaya gumawa ng pagbabago kahit maliit lang ang role natin sa mundo."

        "Kumain ng maraming fastfood":
            $ eco_meter -= 10
            a "Hindi ‘yan nakakatulong sa environment."

    show k neutral
    menu:
        k "Kung gano’n, ano ba ang epekto nito sa atin mismo?"
        "Mas madalas ang pagbaha, maruming hangin at tubig":
            $ eco_meter += 10
            a "Tama! Direkta tayong apektado ng climate change."

        "Mas masarap ang pagkain":
            $ eco_meter -= 10
            a "Mali. Ang epekto ay kalamidad at problema sa kalusugan."

        "Walang epekto sa tao":
            $ eco_meter -= 10
            a "Mali. Tayo ang unang apektado ng climate change."

    
    show k smirk 

    k "Alam niyo… nahihiya ako sa mga sinabi ko dati. Tama kayo. Mukhang mas malaki ang impact ng ginagawa niyo kaysa sa pag-aaway namin dati. Gusto ko humingi ng sorry."

    c happy "Walang problema, Karen. Ang mahalaga, ngayon nagbago yung pananaw mo. Mas magiging malakas tayo kung sama-sama at iisang boses tayo." 

    show a happy at left
    show k smirk at right

    a happy "Salamat, Karen. At bilang pambawi, gusto mo bang tumulong sa amin? Ibig sabihin, hindi lang ito advocacy namin ni Cindy kundi para ito sa lahat."

    k "Gusto ko. Bilang parte ng Council, itutulak ko ang website niyo para maging official platform ng campus para sa environmental awareness." 

    jump advocacyEvent_scene


# -------------------------
# ADVOCACY EVENT
# -------------------------
label advocacyEvent_scene:

    scene medina_lacson with fade

    "Dahil sa tulong ni Karen, ginawang official platform ng Student Council ang website nina Cindy at Alberto. Naglunsad sila ng campus-wide advocacy event."

    show k smirk at left
    show a happy at right
    k "Ang saya pala ng ganito. Totoo nga, lahat tayo may parte sa pagbabago."

    c happy "Tama ka. Totoo nga na small actions can make a difference."

    a "At kapag sama-sama, mas malaki ang impact."

    jump ending

# -------------------------
# FACEBOOK PAGE PATH (BAD/NEUTRAL)
# -------------------------
label fb_page:

    scene library with fade
    "Nag-stick sina Cindy at Alberto sa Facebook page."
    "Sa una, maraming estudyante ang natuwa pero makalipas ang ilang linggo nabawasan ang followers."
    "Dagdag pa, ang away na nangyari sa pagitan nila ni Karen at ang pag-report ni Karen sa kanilang page ay nagdulot ng pagbagal ng pagkalat nito."

    menu:
        "Ano ang gagawin nila?"

        "Ipagpatuloy kahit mahirap":
            $ eco_meter -= 10
            scene library with fade
            "Kahit kaunti lang ang nakaka-appreciate, patuloy pa rin sina Cindy at Alberto sa pagpo-post."

            "Minsan isa o dalawang estudyante lang ang nagla-like o nagko-comment, pero hindi sila tumigil."

            "Naging maliit na sulok sa internet ang kanilang pahina—may ilang loyal followers na sumusuporta, ngunit hindi ito naging sapat para makapagsimula ng mas malaking pagbabago."

            "Nakaramdam sila ng kaunting fulfillment dahil kahit papaano ay may natututo, pero ramdam din nila ang limitadong epekto ng kanilang effort."

            c curious "Bestie... siguro ganito na lang muna. Hindi man malaki ang epekto, pero at least may natutulungan pa rin."

            show a happy
            a "Oo nga, beh. Hindi lahat ng laban malaki agad ang resulta."
        
            jump near_ending

        "Sumuko na lang":
            $ eco_meter -= 20
            scene Black with fade 
            "Sa sobrang dami ng problema at kakulangan ng suporta, tuluyan na silang sumuko."
            "Hindi na na-update ang page at tuluyang natigil ang advocacy."
            jump near_ending

# -------------------------
# NEUTRAL ENDING
# -------------------------
label near_ending:

    scene bacomm with fade
    "Pagkatapos ng ilang buwan, dumating ang araw ng evaluation."
    "Tinawag sila ni Professor upang ipresenta ang kanilang nagawa."
    show p slight smile
    p "Maganda ang effort ninyo, Cindy at Alberto. Kahit nahirapan kayo, hindi kayo sumuko." 
    p "Pero sa totoo lang, kulang pa ang naging epekto ng inyong proyekto. Umabot man ito sa ilan, hindi ito naging sapat para makapagpabago ng malakihan. At darating ang araw na makakalimutan din ito ng lahat kaya mababalewala ang hirap at pagod nyo." (Serious)

    scene Hallway with fade 
    "Cindy at Alberto ay naglakad palabas ng silid, dala ang kunting saya at panghihinayang."
    c happy "At least, may natulungan naman tayo kahit konti, bestie." 
    show a happy
    a "Tama ka. Hindi man ito grand success, pero may naitanim tayong maliit na binhi ng pagbabago, na sana'y tumagal..." 

    scene comfort with fade
    "Habang naglalakad, napansin nila ang isang estudyanteng nakabasa ng kanilang post at nag-iwas ng paggamit ng plastik."
    "Ngumiti sila, dahil kahit kaunti, may nagbago."
    jump ending


# -------------------------
# ENDINGS BASED ON ECO METER
# -------------------------
label ending:

    if eco_meter >= 70:
        jump good_ending 
    elif eco_meter >= 50:
        jump neutral_ending
    else:
        jump bad_ending


label good_ending:
    if eco_meter == 100:
        show 100
    elif eco_meter == 90:
        show 90
    elif eco_meter == 80:
        show 80
    else: 
        show 70

    "Naging inspirasyon sila sa iba, naayos ang waste management sa campus, dumami ang sumali sa environmental activities, at mas inclusive ang komunidad."
    "Congratulations! you've accumaled a total score of [eco_meter]."
    return

label neutral_ending:
    if eco_meter == 60:
        show 60
    else:
        show 50
    "Maliit man ang naging epekto, pero may kaunting binhi paring naitanim para sa pagbabago."
    return

label bad_ending:
    if eco_meter == 40:
        show 40
    elif eco_meter == 30:
        show 30
    elif eco_meter == 20:
        show 20
    else:
        show 10 
    "Dahil pinanghinaan sila ng loob at walang suporta, tuluyang nasira ang kanilang project. Nanatiling madumi ang paligid at mas lumala ang problema."
    return


    