##정의############################################################################################

init:

    ##배경##

    image bg door = "images/bg/정문.png"
    image bg doorf = "images/bg/정문축제.png"
    image bg garden = "images/bg/정원.png"
    image bg gardenf = "images/bg/정원축제.png"
    image bg dorm = "images/bg/기숙사.png"
    image bg cellar = "images/bg/지하실.png"
    image bg floor = "images/bg/복도.png"
    image bg floorf = "images/bg/복도축제.png"
    image bg toffice = "images/bg/교무실.png"
    image bg clas = "images/bg/교실.png"
    image bg clasf = "images/bg/교실축제.png"
    image bg library = "images/bg/도서관.png"
    image bg council = "images/bg/학생회실.png"
    image bg science = "images/bg/과학실.png"
    image bg black = "images/bg/검은화면.png"

    ##만화##

    image opening1 = "images/toon/오프닝1.png"
    image opening2 = "images/toon/오프닝2.png"
    image opening3 = "images/toon/오프닝3.png"
    image opening4 = "images/toon/오프닝4.png"
    image opening5 = "images/toon/오프닝5.png"
    image opening6 = "images/toon/오프닝6.png"

    image ending111 = "images/toon/1-1엔딩1.png"
    image ending112 = "images/toon/1-1엔딩2.png"
    image ending113 = "images/toon/1-1엔딩3.png"
    image ending114 = "images/toon/1-1엔딩4.png"
    image ending115 = "images/toon/1-1엔딩5.png"
    image ending116 = "images/toon/1-1엔딩6.png"

    image ending121 = "images/toon/1-2엔딩1.png"
    image ending122 = "images/toon/1-2엔딩2.png"
    image ending123 = "images/toon/1-2엔딩3.png"
    image ending124 = "images/toon/1-2엔딩4.png"
    image ending125 = "images/toon/1-2엔딩5.png"
    image ending126 = "images/toon/1-2엔딩6.png"

    image ending211 = "images/toon/2-1엔딩1.png"
    image ending212 = "images/toon/2-1엔딩2.png"
    image ending213 = "images/toon/2-1엔딩3.png"
    image ending214 = "images/toon/2-1엔딩4.png"
    image ending215 = "images/toon/2-1엔딩5.png"
    image ending216 = "images/toon/2-1엔딩6.png"

    image ending221 = "images/toon/2-2엔딩1.png"
    image ending222 = "images/toon/2-2엔딩2.png"
    image ending223 = "images/toon/2-2엔딩3.png"
    image ending224 = "images/toon/2-2엔딩4.png"
    image ending225 = "images/toon/2-2엔딩5.png"
    image ending226 = "images/toon/2-2엔딩6.png"

    ##오디오##

    #music calm = "audio/bg/잔잔한.mp3"
    #music fear = "audio/bg/긴장되는.mp3"

    #sound knock = "audio/ef/노크.mp3"

    ##캐릭터##

    define r = Character("루비", color="#ff1e4e")
    image ruby:
        "images/char/루비1.png"
        pause 2.0
        "images/char/루비2.png"
        pause 0.1
        "images/char/루비3.png"
        pause 0.1
        "images/char/루비2.png"
        pause 0.1
        repeat

    define d = Character("다비", color="#69d942")
    image davy:
        "images/char/다비1.png"
        pause 2.0
        "images/char/다비2.png"
        pause 0.1
        "images/char/다비3.png"
        pause 0.1
        "images/char/다비2.png"
        pause 0.1
        repeat

    define f = Character("플로리아", color="#ffe600")
    image flor:
        "images/char/플로리아1.png"
        pause 2.0
        "images/char/플로리아2.png"
        pause 0.1
        "images/char/플로리아3.png"
        pause 0.1
        "images/char/플로리아2.png"
        pause 0.1
        repeat

    define e = Character("에드윈", color="#3b3c66")
    image edw:
        "images/char/에드윈1.png"
        pause 2.0
        "images/char/에드윈2.png"
        pause 0.1
        "images/char/에드윈3.png"
        pause 0.1
        "images/char/에드윈2.png"
        pause 0.1
        repeat

    define c = Character("회장", color="#00eab6")
    image chair:
        "images/char/회장1.png"
        pause 2.0
        "images/char/회장2.png"
        pause 0.1
        "images/char/회장3.png"
        pause 0.1
        "images/char/회장2.png"
        pause 0.1
        repeat

    define m = Character("반장", color="#ff8db8")
    image moni:
        "images/char/반장1.png"
        pause 2.0
        "images/char/반장2.png"
        pause 0.1
        "images/char/반장3.png"
        pause 0.1
        "images/char/반장2.png"
        pause 0.1
        repeat

    define t = Character("선생님", color="#550075")
    image tea:
        "images/char/선생님1.png"
        pause 1.0
        "images/char/선생님2.png"
        pause 0.5
        "images/char/선생님3.png"
        pause 0.5
        "images/char/선생님2.png"
        pause 0.5
        repeat

    define ab = Character("에이비", color="#ff7b00")
    image aby:
        "images/char/에이비1.png"
        pause 1.0
        "images/char/에이비2.png"
        pause 0.5
        "images/char/에이비3.png"
        pause 0.5
        "images/char/에이비2.png"
        pause 0.5
        repeat

    define cd = Character("신디", color="#0011ff")
    image cdy:
        "images/char/신디1.png"
        pause 1.0
        "images/char/신디2.png"
        pause 0.5
        "images/char/신디3.png"
        pause 0.5
        "images/char/신디2.png"
        pause 0.5
        repeat

    ##UI##


    ##아이템##


    ##단서##


    ##이펙트##

    transform rightsp:
        xalign 0.5
        linear 0.4 xalign 0.9

    transform leftsp:
        xzoom -1.0
        xalign 0.5
        linear 0.4 xalign 0.1

    transform rightmsp:
        xalign 0.5
        linear 0.3 xalign 0.65

    transform leftmsp:
        xzoom -1.0
        xalign 0.5
        linear 0.3 xalign 0.35

    transform rightrv:
        xzoom -1.0
        xalign 0.9

    transform leftrv:
        xalign 0.1


##게임시작############################################################################################

label start:

    show bg doorf
    with fade

    "오늘은 마법 학교에서 축제를 하는 날이다.\n등교하는 모두의 발걸음에 들뜬 마음이 가득하다."

    show ruby
    with dissolve

    r "음~음~\♬"
    r "어, 플로리아! 여기!"

    hide ruby with None
    show ruby at rightsp
    show flor at leftsp
    with dissolve

    r "좋은 아침이야, 플로리아!\n같이 들어가자!"

    f "안녕, 루비.\n축제날이라 더 들떠있구나."

    r "그럼! 내가 축제날을 얼마나 기다렸는데!\n저 안에 즐거운 일들이 가득하다구!"

    d "애들아! 우리도 같이 가자!"

    show edw at rightmsp
    show davy at leftmsp
    with dissolve

    f "안녕, 다비. 에드윈도 안녕."

    d "안녕, 플로리아.\n신난 루비 상대하느라 아침부터 고생이 많다."

    r "플로리아가 너인줄 알아?\n플로리아는 그런 생각 안 해."

    d "플로리아 성격이 좋긴 하지."

    r "니가 안 좋은 거야.\n에드윈도 그런 생각 안 하거든?"

    e "\·\·\·\·\·\·."

    d "푸핫! 에드윈 아무 말도 안 하는데?\n에드윈은 거짓말을 진짜 못한다니까."

    r "으으\·\·\·. 너 이리 와봐!"

    f "다들 진정해. 이제 곧 교실이야.\n다비도 루비 그만 놀리고."
    f "에드윈, 다비 좀 부탁할게.\n우리는 정원 좀 더 구경하다 가려고."

    e "(끄덕)"

    hide ruby
    hide flor
    hide davy
    hide edw
    show bg gardenf
    with fade

    "다들 축제 시작 준비가 한창이다."

    show ruby at rightsp
    show flor at leftsp
    with dissolve

    r "우와\·\·\·. 예쁘다!"

    f "일단 한번 둘러보고 몇군데 정해서 이따 다같이 와보자."
    f "이번에 미래를 점 치는 체험을 준비한 곳도 있대.\n개인 마력 흐름을 읽어서 운명을 알 수 있다나?"

    r "정말? 너무 재밌겠다! 꼭 애들이랑 같이 해보자!"

    f "좋아. 아, 저기인가봐."

    r "어? 점을 봐주기에는 되게 좁아보이는데?"

    f "저 체험은 사람이 봐주는 게 아니야."
    f "수정구에 자기 마력을 넣어주면\n수정구에 미래가 보이는 아티팩트 체험이야."

    r "그런 아티팩트가 우리 학교에 있다고?!"

    f "물론 실제 미래가 보이는 게 아니야.\n주입한 마력의 성질에 따라 다른 연출을 보여줄 뿐이지."

    r "그렇구나~ 다들 어떤 결과가 나올까 궁금하다!"

    hide ruby
    hide flor
    show bg clasf
    with fade

    "먼저 교실로 향한 다비와 에드윈.\n교실에서도 분주히 움직이는 학생들이 많다."

    show davy at rightsp
    show edw at leftsp
    with dissolve

    e "다비, 너 요즘 루비에게 장난이 더 심해진 것 같아."

    d "\·\·\·. 딱히 그렇지 않은 거 같은데."

    e "\·\·\·. 우리 같이 지낸 세월이 10년이잖아."
    e "오늘은 좋은 날이야. 다같이 즐겁게 보내고 싶어.\n이따 애들 오면 여기저기 같이 가보자."

    d "그래, {color=#ff0000}{b}좋은 날{/b}{/color}이니까."

    hide davy with None
    show davy at rightrv with dissolve

    e "어디 가려고?"

    d "아, 화장실~ 애들 오면 먼저 가~"

    hide davy with dissolve

    e "\·\·\·\·\·\·."

    show ruby at rightsp
    show flor at rightmsp
    with dissolve

    "\(잠시 후\)"

    r "다비는 어디 갔어?"

    e "화장실에 다녀온다고 먼저 가있으래."

    f "\·\·\·. 그래, 그럼 우리 먼저 내려가자."

    hide ruby
    hide flor
    hide edw
    show bg gardenf
    with fade

    show edw at leftsp
    show ruby at rightsp
    show flor at rightmsp
    with dissolve

    r "우리 저거 먹으러 가자!"

    "즐거운 시간을 보낸 루비와 플로리아, 그리고 에드윈."
    "어느덧 축제는 막바지를 향해 가고\·\·\·."

    r "아~ 재미있었다! 근데 다비는 도대체 왜 안 나타나?"
    r "아까 봤던 아티팩트 체험 같이 해보려고 했는데\·\·\·."

    f "시간이 얼마 안 남았으니까 우선 우리끼리 해보자."

    r "아쉽지만 어쩔 수 없지. 일단 들어가자!"

    hide ruby
    hide flor
    hide edw

    show bg floorf
    with fade

    show edw at leftsp
    show ruby at rightsp
    show flor at rightmsp
    with dissolve

    "각자 결과를 보고 다시 모여서 돌아가는 아이들."

    r "다들 아티팩트로 어떤 걸 봤어?\n나는 축제 준비할 때 썼던 소품들을 뒤적이는 내 모습을 봤어."
    r "이상하지? 분명 미래를 보여준다고 했는데 말이야.\n실망이야\·\·\·. 플로리아는 어때?"

    f "나도 기대했는데 아티팩트에 문제가 있는 것 같아.\n아무것도 보이지 않았어."

    r "역시 그렇지? 에드윈은 어땠어?"

    e "나도 아무것도 보이지 않았어.\n다만 보라색의 옅은 빛줄기를 본 것 같아."

    f "에드윈도? 나도 그랬어. 그러면서도 가슴이 약간 답답한 느낌\·\·\·."

    #play music fear fadein 1.5

    e "!! 으윽! 컥!!"

    r "에드윈! 왜 그래?! 괜찮아?!"

    f "루비! 일단 여긴 내가 상황을 지켜볼테니 어서 보건 선생님을 불러와!"

    hide ruby with None
    show ruby at rightrv with dissolve

    r "알겠어! 금방 다녀올게!"

    hide ruby with dissolve

    f "!! 흐윽! 큭!! 이건\·\·\·."

    hide edw
    hide flor
    window hide

    ##오프닝만화##

    show bg black
    with fade
    pause 0.1

    show opening1
    with Dissolve(1.0)
    pause

    show opening2
    with Dissolve(1.0)
    pause

    show opening3
    with Dissolve(1.0)
    pause

    show opening4
    with Dissolve(1.0)
    pause

    show opening5
    with Dissolve(1.0)
    pause

    show opening6
    with Dissolve(1.0)
    pause

    hide opening1
    hide opening2
    hide opening3
    hide opening4
    hide opening5
    hide opening6

    show bg floor
    with fade

    "과거로 가는 회중시계를 찾는 과정(미완)"

    show ruby at rightsp
    show davy at leftsp
    with dissolve

    r "\(\·\·\·. 분명 학생회실은 내가 꼼꼼히 살펴봤어.\n다비가 거짓말을 하는 걸까?\)"
    r "\(하지만 회장의 자리에서 발견된 게 사실이라면\n분명 회장도 수상한 게 사실이야.\)"


##메인분기그룹############################################################################################

    menu:

        r "\(음\·\·\·. 그래도 역시 내가 더 의심스러운 건\·\·\·.\)"

        "다비":
            call jct1 from _call_jct1
            menu:
                "다비":
                    jump jct11
                "회장":
                    jump jct12
                "반장":
                    jump jct13

        "회장":
            call jct2 from _call_jct2
            menu:
                "다비":
                    jump jct21
                "회장":
                    jump jct22
                "반장":
                    jump jct23


##1분기##

label jct1:

    hide ruby
    hide davy

    show bg cellar

    return

##1-1분기##

label jct11:

    jump ending11

    return

##1-2분기##

label jct12:

    jump ending12

    return

##1-3분기##

label jct13:

    jump ending12

    return

##2분기##

label jct2:

    hide ruby
    hide davy

    "지하실에 도달하는 과정(미완)\n범인 선택"

    show bg cellar

    return

##2-1분기##

label jct21:

    jump ending21

    return

##2-2분기##

label jct22:

    jump ending22

    return

##2-3분기##

label jct23:

    jump ending22

    return


##엔딩만화그룹############################################################################################

##1-1엔딩만화##

label ending11:

    return

##1-2엔딩만화##

label ending12:

    return

##2-1엔딩만화##

label ending21:

    return

##2-2엔딩만화##

label ending22:

    window hide
    show bg black
    with fade
    pause 0.1

    show ending221
    with Dissolve(1.0)
    pause

    show ending222
    with Dissolve(1.0)
    pause

    show ending223
    with Dissolve(1.0)
    pause

    show ending224
    with Dissolve(1.0)
    pause

    show ending225
    with Dissolve(1.0)
    pause

    show ending226
    with Dissolve(1.0)
    pause

    return