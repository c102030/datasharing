#!/usr/bin/env python3
"""
A text-based Choose-Your-Own-Adventure game.
Run it with:  python3 samurai.py
Don't read the source if you want to play it for real.
"""

import os
import sys
import textwrap
import time

WIDTH = 78


def _clear():
    os.system("cls" if os.name == "nt" else "clear")


def _wrap(text):
    paragraphs = text.strip().split("\n\n")
    out = []
    for p in paragraphs:
        out.append(textwrap.fill(" ".join(p.split()), width=WIDTH))
    return "\n\n".join(out)


def _slow(text, delay=0.012):
    if not sys.stdout.isatty():
        print(text)
        return
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch not in " \n":
            time.sleep(delay)
    print()


def _ask(prompt="> "):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nThe wind carries your tale away unfinished.")
        sys.exit(0)


# =============================================================================
# PASSAGES
#
# Each passage is keyed by integer id.  Fields:
#   text:    narrative shown to the player
#   choices: list of (next_id, label) tuples for branching passages
#   ending:  one of "bad", "horrible", "ok", "good", "best" for terminal passages
#   title:   optional banner shown above the text (used for endings)
# =============================================================================

P = {}


def passage(pid, text, choices=None, ending=None, title=None):
    P[pid] = {
        "text": text,
        "choices": choices or [],
        "ending": ending,
        "title": title,
    }


# ---------------------------------------------------------------------------
# CHAPTER 1 — ASH ON THE MOUNTAIN
# ---------------------------------------------------------------------------

passage(1,
    "The rain on Mount Suzaku tastes of ash.\n\n"
    "You return from a three-day pilgrimage carrying nothing but a wooden bowl "
    "and a wakizashi at your hip. You are Takeshi, last disciple of Master "
    "Akiyama Ryūnosuke. The path winds upward through pine and mist — and there, "
    "where the Tōkin-ji monastery should sit beneath its weathered tile roof, "
    "you see only smoke.\n\n"
    "The great gate hangs broken on one hinge. Crows circle.",
    [(2, "Run to the gate"),
     (3, "Approach silently from the trees"),
     (4, "Circle to the rear cliff path")])

passage(2,
    "You sprint. Your sandals slap the wet stones. Smoke claws your throat "
    "as you cross the threshold. Six bodies lie in the courtyard — robed "
    "brothers you have known since boyhood, cut down at their morning prayer. "
    "Beyond them the dōjō still burns.\n\n"
    "Someone groans behind a fallen beam.",
    [(5, "Lift the beam"),
     (6, "Search for the master's chamber first"),
     (7, "Draw your blade and call out a challenge")])

passage(3,
    "You move through wet ferns, slow as a hunting cat. From the treeline you "
    "count the dead — six brothers in the yard, two more by the well. No "
    "attackers in sight. A single black banner has been driven point-down "
    "into the earth before the dōjō. Its symbol is a crescent moon eclipsing "
    "the sun.\n\n"
    "From inside the smoldering hall, you hear a single dry cough.",
    [(8, "Slip in through the kitchens"),
     (9, "Approach the banner first"),
     (10, "Climb to the roof to spy the attackers' trail")])

passage(4,
    "The rear path is narrow and old; the brothers used it for gathering wild "
    "mushrooms. You come up behind the meditation garden. Here, untouched by "
    "fire, sits Master Akiyama against the prayer stone. His robe is bright "
    "red where it should be grey. His sword lies broken across his knees.\n\n"
    "He sees you, and his cracked lips form your name.",
    [(11, "Kneel at his side immediately")])

passage(5,
    "Beneath the beam is young Jirō, the rice-novice — twelve summers old, "
    "more freckle than monk. His leg is crushed but his eyes find yours.\n\n"
    "\"The man with the moon... took the box from under the floor... master "
    "fought him... master is in the garden...\" He coughs blood. \"Don't... "
    "don't leave me here, brother Takeshi.\"",
    [(12, "Pick him up and carry him to safety"),
     (13, "Promise to return, then go to the master"),
     (14, "Give him a swift, merciful death")])

passage(6,
    "You leave the groan behind. The master's chamber is half-collapsed; "
    "the wall scroll of the heron is scorched black. The hidden floorboard "
    "beneath the writing desk has been pried up — the lacquered box that "
    "sat there for as long as you have lived is gone.\n\n"
    "When you return to the courtyard, the place where you heard the groan "
    "is silent. You will never know who it was.",
    [(15, "Go to the garden")])

passage(7,
    "\"COME OUT!\" you roar at the smoke. \"FACE ME!\"\n\n"
    "Only the crows answer. You stand alone in a courtyard of the dead, "
    "shouting at ghosts, while somewhere your dying master waits unseen.",
    [(15, "Lower your blade and search the grounds")])

passage(8,
    "You enter through the cold hearth. The cough came from the master's "
    "study — but when you reach it, only a scorched cushion remains, and "
    "a smear of blood leading toward the meditation garden.",
    [(15, "Follow the blood")])

passage(9,
    "The banner is taller than a man. Its black silk has been treated with "
    "something that will not burn. The crescent-and-sun crest is unfamiliar "
    "to you, but a fragment of paper has been pinned to the pole with a "
    "lacquered hairpin shaped like a hawk's feather.\n\n"
    "The paper reads, in elegant brushwork: *The seal is broken. The blade "
    "wakes. Old man, you should have stayed retired.*",
    [(16, "Take the hairpin and the paper, then find the master")])

passage(10,
    "You climb the bell-tower ladder. From its top you see, far below, a "
    "thin column of horsemen riding north along the river road — perhaps "
    "fifteen riders, moving fast. At their head rides a single figure on a "
    "grey horse, wearing red lacquered armour. He carries a long bundle "
    "across his saddle, wrapped in oilcloth.\n\n"
    "You memorize the direction. North. Always north.",
    [(15, "Descend and find your master")])

passage(11,
    "You drop to your knees in the wet moss. Master Akiyama's hand finds "
    "yours; the grip that taught you the cut of the willow is feeble now.\n\n"
    "\"Takeshi... listen... it was Hayabusa. The moon... over his eye. He "
    "took the Yasha-no-Tachi. The seal we kept for thirty years... broken.\"\n\n"
    "He coughs. His blood is dark, dark.",
    [(17, "Ask who Hayabusa is"),
     (18, "Promise vengeance"),
     (19, "Ask what you must do")])

passage(12,
    "You lift Jirō. He is light as a sparrow. You carry him to the spring "
    "behind the kitchen and lay him in the moss. \"Master is in the "
    "garden,\" you whisper. \"I will return.\"\n\n"
    "When you do return, an hour later, the boy is still breathing. He will "
    "live. It costs you the master's last words — Akiyama was already gone "
    "when you reached the garden — but a life is a life.",
    [(20, "Search the master's body and the grounds")])

passage(13,
    "\"I swear it,\" you tell Jirō. You leave him propped against the beam "
    "and run to the garden. The master still breathes; barely.\n\n"
    "\"Takeshi... it was Hayabusa. The moon... over his eye. He took the "
    "Yasha-no-Tachi. The seal we kept for thirty years... broken.\"",
    [(17, "Ask who Hayabusa is"),
     (18, "Promise vengeance"),
     (19, "Ask what you must do")])

passage(14,
    "You tell yourself it is mercy. You tell yourself the leg cannot be "
    "saved, that the boy will only suffer. The cut is clean and quick. "
    "Jirō's eyes go wide, then empty.\n\n"
    "Something small and bright in you dies with him. You feel it go.",
    [(21, "Go to the garden, colder than before")])

passage(15,
    "You step into the meditation garden. Master Akiyama is propped against "
    "the prayer stone, his breath rattling like wind in dry reeds. His eyes "
    "find yours.",
    [(11, "Kneel beside him")])

passage(16,
    "You pocket the paper and the heavy little hairpin. The pin is cold; "
    "colder than rain has any right to make it. You go to the garden.",
    [(11, "Kneel beside the master")])

passage(17,
    "\"Hayabusa Mōri,\" the master whispers. \"Once my brother in the "
    "Way. Once my closest friend. He fell to pride and to a worse thing "
    "still. I thought him dead these thirty years. He came back for the "
    "blade. Always for the blade.\"\n\n"
    "His grip tightens. \"Listen. The Yasha must be sealed again. Not "
    "broken — sealed. Find the three winds. Fire, water, earth. Without "
    "all three, you bring only ruin.\"",
    [(22, "Ask about the three winds"),
     (23, "Ask why he never told you")])

passage(18,
    "\"I will kill him, master. I swear it on the willow and the moon.\"\n\n"
    "The old man's bloodied hand tightens on yours, and for the first "
    "time in your life you see something like fear in his eyes.\n\n"
    "\"No, Takeshi. *No.* Killing is the easy door. Listen — the Yasha-"
    "no-Tachi must be sealed, not broken. Find the three winds. Fire, "
    "water, earth. Without all three, vengeance brings only ruin.\"",
    [(22, "Ask about the three winds"),
     (24, "Repeat your vow despite him")])

passage(19,
    "\"The Yasha-no-Tachi must be sealed again. Not broken — sealed. The "
    "blade is older than this country and what sleeps in it is older "
    "still. Find the three winds, Takeshi. Fire on the mountain. Water at "
    "the shrine. Earth in the wood. Without all three — \"\n\n"
    "He breaks off, coughing.",
    [(22, "Ask about the three winds"),
     (25, "Ask if there is no other way")])

passage(20,
    "On the master's body you find his prayer beads, his broken sword "
    "(Kōgetsumaru, the moon-blade — its tang still sound), and a folded "
    "letter sealed with black wax that you have never seen before. In the "
    "embers of his chamber, the lacquered box is gone; the floorboard "
    "stands open like a wound.\n\n"
    "Where the gate-banner stood, you find only the empty pole. The "
    "killers took even that.",
    [(26, "Bury the master and the brothers, then descend the mountain")])

passage(21,
    "Master Akiyama still breathes when you reach him, but his eyes are "
    "far away. When he speaks your name, it is the voice of a man speaking "
    "to a stranger.\n\n"
    "He tells you of Hayabusa and the Yasha-no-Tachi and the three winds, "
    "but his words wash over you. You are still standing in the kitchen "
    "with a small body at your feet.",
    [(22, "Listen as best you can about the three winds")])

passage(22,
    "\"Three living winds remain who knew the binding,\" the master "
    "whispers. \"Fire — the hermit Donkō, on the slopes of Asahi. Water — "
    "the Maiden of the Tide-Shrine at Mikuriya. Earth — the spirit they "
    "call Old Bark, in the forest of Hōrai. Find them. Bring what you "
    "learn to the place where the blade was forged. Black Crow Castle. "
    "Hayabusa goes there. He cannot help going there.\"\n\n"
    "His hand falls open. From it drops a small wooden token carved with "
    "three brushstrokes.\n\n"
    "\"Takeshi... do not... do not take the blade for yourself. Promise me.\"",
    [(27, "Promise"),
     (28, "Hesitate to promise")])

passage(23,
    "\"Because you were a boy and the world is heavy enough.\" He smiles "
    "faintly. \"Forgive an old man his silences.\"",
    [(22, "Ask about the three winds")])

passage(24,
    "\"I will kill him, master, with or without your sealings.\"\n\n"
    "He closes his eyes. The disappointment on his face is a wound deeper "
    "than the one in his belly. \"Then at least... at least find the three "
    "winds first. Promise me that, my stubborn son.\"",
    [(22, "Listen as he tells you of the three winds")])

passage(25,
    "\"No other way. Steel cannot kill what is in the Yasha. Steel only "
    "feeds it.\"",
    [(22, "Listen as he tells you of the three winds")])

passage(26,
    "You dig until your hands bleed. You set the broken Kōgetsumaru atop "
    "the master's cairn, point downward, the old way. You read the death-"
    "sutra you remember and improvise the rest. The crows watch from the "
    "pines and do not laugh.\n\n"
    "At dusk you take from his body only the unsealed black letter and "
    "his prayer beads. You start down the mountain in the rain, knowing "
    "you go without the words he could not finish.",
    [(29, "Open the black letter on the road")])

passage(27,
    "\"I promise, master. I will not take the blade.\"\n\n"
    "He smiles — a real smile, weary and clear. \"Good. Good boy. The "
    "three winds, Takeshi. The three — \"\n\n"
    "His hand goes still in yours. The rain washes the rest away.",
    [(30, "Mourn, then begin")])

passage(28,
    "His eyes search yours. He sees the hesitation. After a long moment "
    "he says only, \"Ah. Then learn quickly, boy. Learn before the blade "
    "learns you.\"\n\n"
    "His hand goes still in yours.",
    [(30, "Mourn, then begin")])

passage(30,
    "You bury Master Akiyama at the foot of the prayer stone. You bury the "
    "brothers in the courtyard, one by one, naming each as you turn the "
    "earth. You bury little Jirō last of all, if you can find him.\n\n"
    "You take with you: the master's prayer beads; the wooden token with "
    "three brushstrokes; the tang and grip of Kōgetsumaru, his moon-blade, "
    "snapped a hand's-width above the guard; and whatever else you have "
    "claimed from the ruin. Then you start down the mountain in the rain.",
    [(31, "Descend")])

passage(29,
    "On the third switchback of the path you stop beneath a pine and unfold "
    "the master's letter.\n\n"
    "It is addressed to a name you do not know: *Kiri of the Hollow Reed.* "
    "The hand is the master's own. *If you receive this, the blade has "
    "woken. Come to Tōkin-ji. Bring what you swore to bring. — A.*\n\n"
    "Below the signature, the master has written one more line, in haste:\n\n"
    "*Do not trust the one with the second face.*",
    [(31, "Continue down the mountain")])

passage(31,
    "Night falls on Mount Suzaku as you reach the river road. The rain "
    "thins. Somewhere ahead, fifteen riders have ridden north with a "
    "wrapped bundle. Somewhere ahead, three winds wait. Somewhere ahead, "
    "a man with a moon-shaped scar over one eye carries a blade older than "
    "your country.\n\n"
    "At a fork in the road, a wooden post offers three painted arrows:\n\n"
    "  — North, along the river, to the post-town of Karasu-juku.\n"
    "  — East, into the bamboo wood, toward the village of Hisame.\n"
    "  — West, climbing again, to the hot spring of Yumura.",
    [(40, "North, along the river"),
     (60, "East, into the bamboo wood"),
     (80, "West, to the hot spring")])


# ---------------------------------------------------------------------------
# CHAPTER 2 — THREE ROADS
# ---------------------------------------------------------------------------

passage(40,
    "The river road is wide and mud-rutted. By moonrise you reach Karasu-juku — "
    "a single street of inns and tea-houses, smelling of woodsmoke and "
    "horse. A drunk is being noisily ejected from the larger of the two "
    "inns. Two ronin lounge under the lantern of the smaller. A girl in a "
    "torn travelling cloak sits alone on the temple steps, watching every "
    "rider that passes.",
    [(41, "Try the larger inn"),
     (42, "Try the smaller inn"),
     (43, "Approach the girl on the steps"),
     (44, "Slip past town entirely and follow the riders by night")])

passage(41,
    "The larger inn is loud with merchants and pilgrims. The innkeeper, a "
    "fat man with a kind mouth, sets you at a corner table with hot millet "
    "and pickled radish. Two tables over, three soldiers in red lacquered "
    "armour drink in silence. They wear no clan crest you recognize.\n\n"
    "The innkeeper, refilling your cup, murmurs: \"Don't stare, young "
    "master. Those came down off the north road this morning. They left "
    "the inn-girl crying.\"",
    [(45, "Buy the soldiers a round and listen"),
     (46, "Quietly ask the innkeeper what he knows"),
     (47, "Approach the inn-girl to ask why she cried")])

passage(42,
    "The smaller inn is half-empty. The two ronin under the lantern look "
    "you up and down and snort. The older of them, an enormous bearded "
    "man with one milky eye, calls out: \"Pretty sword, monk-boy. Real "
    "one? Or did your master let you carry it just for prayers?\"",
    [(48, "Ignore him and enter"),
     (49, "Answer his insult"),
     (50, "Compliment his sword in return")])

passage(43,
    "The girl on the steps looks up as you approach. She is perhaps your "
    "age, perhaps a year younger. Her cloak is good silk, badly torn. Her "
    "eyes are red but dry.\n\n"
    "\"If you are with them,\" she says quietly, \"finish it here. I will "
    "not run again.\"",
    [(51, "Tell her you are with no one"),
     (52, "Ask who 'they' are"),
     (53, "Sit beside her in silence")])

passage(44,
    "You skirt the town. You follow the river road by moonlight. After an "
    "hour you smell horses ahead, and a campfire that should not be there. "
    "You creep through the reeds.\n\n"
    "Six men in red armour sit around a fire. One of them is sharpening a "
    "naginata. They are not your fifteen — these are a smaller, separate "
    "force. They have a captive: a girl in a torn travelling cloak, "
    "bound at the wrists.",
    [(54, "Attack from the reeds"),
     (55, "Wait and watch"),
     (56, "Withdraw and circle further north")])

passage(45,
    "You signal the innkeeper for a flask, gesture to the soldiers' table. "
    "Their leader, a lean man with a burn-scar across his throat, raises "
    "an eyebrow but does not refuse.\n\n"
    "Three cups later, his tongue loosens enough that he complains about "
    "his lord — \"a hard man, a fast horse, a colder bed every winter\" — "
    "and lets slip that they are riding to *Black Crow* by way of the "
    "shrine road, with a *very particular* package.\n\n"
    "When you stand to leave, the burn-scarred man's hand catches your "
    "wrist. His grip is iron. \"You ask quiet questions, young man.\"",
    [(57, "Free your wrist and leave quickly"),
     (58, "Drop your hand toward your sword"),
     (59, "Laugh and say you only meant respect")])

passage(46,
    "The innkeeper, refilling your cup yet again, glances at the soldiers. "
    "\"They came down the north road. They paid in old square coin — the "
    "kind nobody mints since the war. They asked after a *shrine girl* "
    "who passed through three days ago. The inn-girl saw them grab a "
    "merchant's daughter by the hair on the road this morning and "
    "thought it was that shrine girl. It wasn't. They let her go but the "
    "child still hasn't stopped crying.\"\n\n"
    "He lowers his voice. \"You from up the mountain? From the temple?\"",
    [(100, "Admit it"),
     (101, "Deny it"),
     (102, "Ask him why he asks")])

passage(47,
    "You find the inn-girl out back, splitting firewood with too much "
    "force. She is twelve perhaps. When she sees your sword her eyes go "
    "round and she steps back, but she does not run.\n\n"
    "\"They said the moon man was coming through tomorrow,\" she "
    "whispers. \"They were arguing about whether to wait for him or push "
    "on. The one with the burn on his throat said *the master does not "
    "wait*. They mean to be at the old shrine by sundown tomorrow.\"",
    [(103, "Thank her and slip away"),
     (104, "Press for more details"),
     (105, "Give her one of your few coins")])

passage(48,
    "You walk past as if he had not spoken. He laughs — but lets you go. "
    "The innkeeper, a thin woman with a scar on her lip, says nothing as "
    "she sets a bowl of millet before you. Her eyes go once to the wooden "
    "token at your belt — three brushstrokes — and then quickly away.",
    [(106, "Eat in silence and watch the room"),
     (107, "Ask her about the token")])

passage(49,
    "\"My sword,\" you say, voice level, \"has seen the inside of three "
    "demons. Yours has seen the inside of three bottles. Speak again and "
    "I will show you the difference.\"\n\n"
    "The bearded ronin goes very still. The lantern creaks. His friend "
    "lays a hand on his shoulder; the bearded man shrugs it off and "
    "stands. He is taller than you by a head and broader than two of you.",
    [(108, "Draw"),
     (109, "Stand your ground without drawing"),
     (110, "Try to defuse with a bow")])

passage(50,
    "\"That is a fine blade,\" you tell him, eyeing the wrapped tsuka at "
    "his hip. \"Bizen work? The grip-binding suggests an old hand wound "
    "it. Forgive me for not bowing — I am road-weary.\"\n\n"
    "He stares. Then, slowly, he laughs — a real laugh, like rocks in a "
    "barrel. \"Bizen indeed. You have an eye, monk-boy. Come — sit, drink. "
    "Tell me what brings a temple sword down off the mountain in the "
    "rain.\"",
    [(111, "Sit and drink with him"),
     (112, "Politely decline and enter the inn")])

passage(51,
    "\"I am with no one,\" you tell her. \"I came down the mountain "
    "today.\"\n\n"
    "Her shoulders fall a hair's-breadth. \"Then for your own sake, "
    "stranger, walk past me. Men in red lacquered armour are looking for "
    "a girl my size and my hair and they are not particular about "
    "whether they have the right one.\"",
    [(113, "Sit beside her anyway"),
     (114, "Walk on as she asks"),
     (115, "Ask why they are looking for her")])

passage(52,
    "\"Men in red armour with no crest,\" she says, eyes on the road. "
    "\"They have been chasing me since Mikuriya. They killed the shrine "
    "maiden's old guardian on the steps of the tide-shrine. They want "
    "what she gave me before she — \"\n\n"
    "She breaks off and looks at you properly for the first time. "
    "\"Why are you asking?\"",
    [(116, "Show her your master's token"),
     (117, "Tell her about Tōkin-ji"),
     (118, "Lie that you only wished to help")])

passage(53,
    "You sit. Neither of you speaks. After a long while she says, without "
    "turning, \"Thank you.\" After a longer while she says, \"There is a "
    "tea-house two streets that way that the soldiers do not visit. "
    "Would you walk a frightened girl that far, samurai?\"",
    [(119, "Walk her there")])

passage(54,
    "You burst from the reeds with a wordless cry. The first soldier — "
    "still seated — never even reaches his weapon. The second turns and "
    "you take him across the throat.\n\n"
    "But four of them are on their feet now, and the captain is shouting "
    "orders, and a naginata sweeps low at your shins.",
    [(120, "Fight them all"),
     (121, "Grab the girl and run")])

passage(55,
    "You wait. The soldiers eat. The captain interrogates the girl in a "
    "bored voice; she gives him nothing. Eventually he strikes her, "
    "openhanded, and orders two men to take her into the trees. You "
    "understand what is about to happen.\n\n"
    "There is no more time for cleverness.",
    [(122, "Attack now, before they reach the trees"),
     (123, "Follow the two who take her into the trees and pick them off there")])

passage(56,
    "You retreat. The road is long and the night is young; you can outrun "
    "their pursuit and reach the next village by dawn. You tell yourself "
    "the girl is not your problem — you have a master to avenge, a blade "
    "to find, three winds to gather.\n\n"
    "You repeat this to yourself many times as you walk. By dawn you no "
    "longer believe it, but the road has carried you fifteen ri from her "
    "and there is no going back.",
    [(124, "Walk on toward the shrine road")])

passage(57,
    "You twist your wrist out of his grip — a turning he could have "
    "stopped, but does not — and bow. \"Forgive my impertinence, captain. "
    "I drink too quick.\"\n\n"
    "You go. He watches you all the way to the door. You feel his eyes on "
    "your back for an hour after.",
    [(125, "Sleep at the inn"),
     (126, "Push on into the night")])

passage(58,
    "Your hand falls to your sword. His hand never moves; he does not "
    "need it to. Three of his men are between you and the door before "
    "you have drawn an inch of steel.\n\n"
    "The captain smiles. \"Slow that hand, monk-boy. Sit. Tell me where "
    "you came down from.\"",
    [(127, "Lie"),
     (128, "Tell the truth and accept the consequences"),
     (129, "Try to fight your way out")])

passage(59,
    "You laugh — a forced laugh, but a passable one. \"I meant only "
    "respect, captain. I have a great-uncle in the red armour up "
    "country and I always like to hear what the road brings.\"\n\n"
    "He studies you a long moment. Then he lets your wrist go. \"Tell "
    "your great-uncle Burn-Throat sends regards. And tell him to keep "
    "his nephew off the north road for the next ten days.\"",
    [(125, "Sleep at the inn"),
     (126, "Push on into the night")])

passage(60,
    "The bamboo wood is darker than night has any right to make a forest. "
    "Your sandals whisper on fallen leaves. After an hour you smell wood "
    "smoke. After two, you see lanterns: the village of Hisame, a "
    "scattering of thatched roofs along a stream.\n\n"
    "At the village edge sits an old man on a flat stone, smoking a long "
    "pipe. He does not look up as you approach.\n\n"
    "\"You smell of ash and grief, young master,\" he says. \"Come no "
    "closer until you have told me which.\"",
    [(61, "Tell him: both"),
     (62, "Tell him only of the grief"),
     (63, "Ask who he is to bar your road")])

passage(61,
    "\"Both,\" you say. \"My temple is burned and my master is dead.\"\n\n"
    "The old man takes his pipe from his mouth. He looks at you for the "
    "first time. His left eye is missing; the right is the colour of old "
    "tea.\n\n"
    "\"Tōkin-ji,\" he says. Not a question.",
    [(64, "Ask how he knows"),
     (65, "Wait for him to continue")])

passage(62,
    "\"Grief,\" you say. \"I have lost — someone.\"\n\n"
    "He nods slowly. \"Grief is welcome in Hisame. We have plenty. Come "
    "warm yourself.\"\n\n"
    "But as you pass him, his old hand catches the hem of your sleeve "
    "and his single tea-coloured eye fixes you. \"Mind the ash you carry "
    "in, samurai. The thatch here is dry.\"",
    [(66, "Enter the village")])

passage(63,
    "\"And who are you,\" you ask, \"to bar a traveller's road?\"\n\n"
    "The old man laughs — a small, dry laugh. \"I am Genshin. Once I sat "
    "in a hall of pine and ash with a brother named Akiyama, and we "
    "argued about the right way to hold a brush. He always lost.\"\n\n"
    "He looks at you. \"You have his sword-tang at your belt. Therefore "
    "he is dead. Therefore I will bar nothing.\"",
    [(67, "Sit with him")])

passage(64,
    "\"Three nights ago,\" he says, \"I dreamed of a fire on Mount Suzaku. "
    "I dreamed of an old friend dying against a prayer stone. I dreamed "
    "of a man with a moon over his eye taking a blade from beneath a "
    "floor. And I dreamed of a boy with a broken sword in his belt "
    "walking down toward me through the bamboo.\"\n\n"
    "He taps his pipe out on the stone. \"I am Genshin. Your master and "
    "I were brothers in the Way, long ago. Sit.\"",
    [(67, "Sit")])

passage(65,
    "The old man waits. The pipe smoke curls. After a long silence he "
    "says: \"My name is Genshin. I have been waiting on this stone for "
    "three days for someone with your sword-tang at his belt. Sit.\"",
    [(67, "Sit")])

passage(66,
    "Hisame is a poor village — perhaps thirty roofs. Children peek from "
    "doorways. A blacksmith's forge stands cold. A young woman with a "
    "bandaged forearm draws water at the well; she watches you sidelong "
    "and does not call out a greeting.\n\n"
    "At the largest house, a small wooden plaque outside the door bears "
    "the three-brushstroke mark of your master's token.",
    [(68, "Knock at the door")])

passage(67,
    "You sit on the cold ground before his stone. He passes you the pipe "
    "without asking. You smoke. The bamboo creaks overhead.\n\n"
    "\"Tell me how he died,\" Genshin says.\n\n"
    "You tell him. You tell him about Hayabusa, the moon-scar, the "
    "Yasha-no-Tachi, the three winds. When you finish, the old man closes "
    "his single eye for a long minute.\n\n"
    "Then he says: \"I am one of the three winds, Takeshi. Fire. The "
    "hermit Donkō on Asahi is a fiction we invented to send fools "
    "wandering. Your master kept one wind close because he knew this "
    "day would come.\"",
    [(69, "Ask him to teach you the Fire wind"),
     (70, "Ask why he hid this from you all your life"),
     (71, "Ask if he will come with you")])

passage(68,
    "The door is opened by a tall woman of middle years with grey at her "
    "temples and a longbow leaning behind her. She looks at the broken "
    "sword-tang in your belt, then at your face, and says only:\n\n"
    "\"Genshin said you would come this week. He is at the village edge "
    "smoking his foul pipe. Go fetch him before he chokes himself, and "
    "then we three will eat.\"\n\n"
    "She closes the door before you can answer.",
    [(67, "Go find Genshin")])

passage(69,
    "Genshin smiles, slowly, around the pipe. \"Of course you may learn "
    "the Fire wind. But Fire is not a thing one *learns*, boy. Fire is a "
    "thing one *carries*, and most men who carry it burn themselves up "
    "before they reach the place they meant to set alight. Will you carry "
    "it carefully?\"",
    [(130, "Promise to carry it carefully"),
     (131, "Say honestly that you do not know")])

passage(70,
    "\"Because,\" he says, \"a boy who knows there is a sealing word "
    "spends his life trying to invent excuses to use it. Your master "
    "wanted you to grow up first.\"\n\n"
    "He looks at the broken sword-tang at your belt. \"He almost "
    "succeeded.\"",
    [(132, "Ask him to teach you the Fire wind now")])

passage(71,
    "He sighs. \"I am old, Takeshi. My one eye is failing. My knees ache "
    "in the rain. I will give you the Fire and a few hard truths, and I "
    "will pray for you at the prayer stone. But this road is yours. I "
    "was your master's wind, not yours.\"",
    [(132, "Accept this and ask for the Fire teaching")])

passage(80,
    "The west road climbs. Pine becomes cedar, cedar becomes cloud. By "
    "dawn you reach Yumura, a steaming little village where hot water "
    "bubbles out of the stones and the inn is built around its bath.\n\n"
    "There are few travellers at this hour. A wiry man in a peddler's "
    "robe nurses a cup of tea by the door. A young woman in plain "
    "clothes sits washing her hands at the bath's edge — but the hands "
    "are wrong. They are calloused in the places sword-hands are "
    "calloused, not the places weaver's hands are.",
    [(81, "Greet the peddler"),
     (82, "Sit at the bath, far from the woman"),
     (83, "Sit at the bath beside her")])

passage(81,
    "The peddler grins as you sit. \"Cold morning, master samurai. The "
    "bath is hot. The tea is hotter. The gossip is hottest.\" He pours "
    "you a cup uninvited. \"You came down from the mountain?\"\n\n"
    "Behind him, you see the woman at the bath's edge has gone very "
    "still — listening.",
    [(133, "Admit it"),
     (134, "Deny it"),
     (135, "Pay for the tea and leave without answering")])

passage(82,
    "You sit at the far end of the bath. The young woman pretends not "
    "to see you. The peddler at the door pretends not to see either of "
    "you. Steam rises.\n\n"
    "After a long minute the woman, without turning her head, says "
    "softly: \"The peddler is not a peddler. Don't look. He has been "
    "watching the road from this inn for two days. Walk out the back "
    "with me when I stand.\"",
    [(136, "Trust her and follow when she stands"),
     (137, "Stay where you are")])

passage(83,
    "You sit beside her. Her hand on the stone goes very still.\n\n"
    "\"Bold of you,\" she murmurs without looking at you. \"Either you "
    "are stupid, or you are the one I am waiting for, or you are the "
    "one I am supposed to kill. Tell me which.\"",
    [(138, "Show her the three-brushstroke token"),
     (139, "Tell her your master's name"),
     (140, "Ask if she has all three options or only those")])

# ---------------------------------------------------------------------------
# CHAPTER 2b — Karasu-juku follow-ups
# ---------------------------------------------------------------------------

passage(100,
    "\"From the temple,\" you say. \"It burned yesterday.\"\n\n"
    "The innkeeper's face goes still. He sets the flask down carefully, "
    "as if it were full of poison. \"Then drink up, young master, and "
    "follow me. There is someone in my back room who has been waiting "
    "three days for a man with your face.\"",
    [(141, "Follow him")])

passage(101,
    "\"From down the coast,\" you lie. \"I never saw the place.\"\n\n"
    "The innkeeper nods slowly. He believes you, or pretends to. He "
    "refills your cup and moves on. But the three soldiers two tables "
    "over have noticed your accent, and one of them is now watching you "
    "with an interest you do not enjoy.",
    [(142, "Pay quickly and leave"),
     (143, "Stay and brazen it out")])

passage(102,
    "\"Because,\" the innkeeper says, very softly, leaning on the table "
    "as if to refill your cup, \"a woman of the hidden village came "
    "through here yesterday asking after a young samurai with a "
    "three-brushstroke token. She paid in old square coin and said she "
    "would wait until tomorrow at the eastern shrine.\"\n\n"
    "He straightens, voice loud again: \"More millet, young master?\"",
    [(144, "Accept the millet and slip out toward the shrine at dawn")])

passage(103,
    "You thank her. She vanishes back into the woodshed.\n\n"
    "You return to your room thinking. The shrine on the eastern road — "
    "the old one — you remember the master mentioning it once, on a "
    "winter night.",
    [(125, "Sleep, then ride for the shrine before dawn")])

passage(104,
    "\"Did the burn-throat one give a name? A clan?\"\n\n"
    "She shakes her head. \"No clan. They were arguing about a *master*. "
    "And about a *blade*. The big one with the broken nose said *the "
    "blade should be in his hands by now*. The burn-throat said *not "
    "yet*. They were... not happy with each other.\"",
    [(103, "Thank her and slip away")])

passage(105,
    "You press a coin into her palm. Her eyes go round again. She "
    "whispers, \"You are kind, samurai. Be careful. The moon-faced one "
    "passes through tomorrow, the burn-throat said. Be far from this "
    "road by then.\"",
    [(103, "Thank her and slip away")])

passage(106,
    "You eat. You watch. The bearded ronin and his friend share a flask "
    "and a low, intermittent conversation that is not about you. After "
    "a time the bearded man stands, slings his sword, claps his friend "
    "on the shoulder, and leaves without a glance.\n\n"
    "The thin innkeeper, clearing your bowl, says: \"That one is Tetsu "
    "of the Burnt Hill. He has been drinking here for two nights waiting "
    "for someone. He will be on the north road by sunrise.\"",
    [(145, "Ask her what she meant by her glance at your token"),
     (146, "Pay and follow Tetsu at dawn")])

passage(107,
    "You touch the three-brushstroke token at your belt. \"You looked "
    "at this.\"\n\n"
    "She freezes only an instant. Then she sets your bowl down very "
    "carefully. \"My grandmother carried one of those, samurai. She "
    "told me one day a young man with grief in him would walk through "
    "the door wearing one, and that I should help him if I could.\"\n\n"
    "She glances at the ronin under the lantern. \"That one out there. "
    "Tetsu. He is not what he looks. He has been drinking here for two "
    "nights waiting for someone. I think it was you.\"",
    [(147, "Go speak with Tetsu honestly")])

passage(108,
    "You draw. The cut of the willow — your master's first lesson — "
    "comes up clean. The bearded ronin's blade meets yours with a clang "
    "that sets the lantern swinging.\n\n"
    "He is strong. Inhumanly strong. But he is also drunk, and you are "
    "very, very angry.",
    [(148, "Press the attack")])

passage(109,
    "You stand your ground but do not draw. \"I have come down from a "
    "fire,\" you say, \"and I have buried my teacher today. If you wish "
    "to die in this inn yard, draw. If you do not, drink and forget my "
    "face.\"\n\n"
    "The bearded man stares. Then, slowly, his shoulders relax. He sits "
    "back down. \"Sit, monk-boy. Drink with me. I am Tetsu of the Burnt "
    "Hill, and I have been waiting two days in this inn for a fool with "
    "a broken sword-tang at his belt.\"",
    [(149, "Sit with Tetsu")])

passage(110,
    "You bow — deep, formal, monastery-deep. \"Honoured swordsman. "
    "Forgive my road-weariness. I am no fit opponent for your edge "
    "tonight.\"\n\n"
    "The bearded ronin stares — then laughs so hard he nearly falls off "
    "the bench. \"Manners! In Karasu-juku! Sit, monk-boy. Drink with me. "
    "I am Tetsu of the Burnt Hill.\"",
    [(149, "Sit with Tetsu")])

passage(111,
    "You sit. Tetsu of the Burnt Hill pours you sake from a flask the "
    "size of a small child. His one milky eye fixes on the sword-tang at "
    "your belt — Kōgetsumaru, broken — and he goes still.\n\n"
    "\"That,\" he says quietly, \"was Akiyama's blade.\"\n\n"
    "\"Was,\" you say.\n\n"
    "Tetsu closes his good eye for a long second. \"Then I have been "
    "waiting in this inn yard for you, brother. Tell me what burned.\"",
    [(149, "Tell him everything")])

passage(112,
    "You bow politely and step past him into the inn. He does not "
    "follow. As you settle by the fire, the innkeeper murmurs: \"That "
    "one called Tetsu has been waiting two days for someone. He says "
    "his old captain sent him. Whether you are that someone or not is "
    "your business, samurai.\"",
    [(149, "Go back out and sit with Tetsu")])

passage(113,
    "You sit. The girl does not move away. After a long silence she "
    "says, quietly: \"I am called Ayane. My true name would only put "
    "you in worse danger than my false one.\"",
    [(150, "Show her the three-brushstroke token"),
     (151, "Ask about the shrine maiden she mentioned"),
     (152, "Ask why men in red armour hunt her")])

passage(114,
    "You bow and walk on. Ten steps later you stop. Twenty steps later "
    "you stop again. By thirty steps you have turned and walked back. "
    "She has not moved. She does not look up.\n\n"
    "\"My name is Takeshi,\" you say. \"My temple burned yesterday. "
    "Tell me your trouble.\"",
    [(113, "Sit with her")])

passage(115,
    "\"Because,\" she says wearily, \"I carry a thing the shrine maiden "
    "gave me before her guardian was murdered on the temple steps at "
    "Mikuriya. I do not know what it is. I only know I was told to keep "
    "it safe and bring it north, and now men in red armour want it back.\"",
    [(150, "Show her your token"),
     (153, "Ask what the thing is")])

passage(116,
    "You take the wooden token from your belt and lay it in her palm. "
    "Three brushstrokes, carved deep.\n\n"
    "She stares at it. Her eyes fill — angry, relieved, exhausted all "
    "at once.\n\n"
    "\"You came,\" she says. \"He sent word and he sent you. Then it is "
    "true — the old man is dead.\"",
    [(154, "Confirm it gently")])

passage(117,
    "\"My master taught at a monastery on Mount Suzaku,\" you say. \"It "
    "burned two days ago. Master Akiyama is dead.\"\n\n"
    "Her hands go to her mouth. After a long moment she whispers: "
    "\"Then I am one of the few who knows your enemy's name. Sit, "
    "samurai. Sit, and listen.\"",
    [(154, "Sit and listen")])

passage(118,
    "\"Only to help,\" you say.\n\n"
    "She looks at you a long moment, weighing. Then she looks away. "
    "\"Then walk on, kind stranger. I do not know you, and I am too "
    "tired tonight to trust kindness without a name.\"\n\n"
    "She rises and walks toward the tea-house. You can follow at a "
    "distance, or you can leave her to her fear.",
    [(119, "Follow her at a distance, quietly"),
     (155, "Leave her be, and ride out at dawn")])

passage(119,
    "You walk her the two streets to the tea-house. She does not "
    "speak. At the door she turns to you for the first time. Her face "
    "is much younger than her voice. \"Thank you. If we live, "
    "samurai — ask after Ayane at the shrine of Mikuriya.\"\n\n"
    "She goes inside.\n\n"
    "Standing in the dark, you realize three things at once: that the "
    "tea-house's back gate stands open; that two red-armoured men "
    "have just turned into the street behind you; and that you do not "
    "intend to leave her alone with what comes next.",
    [(156, "Slip in the back gate after her"),
     (157, "Confront the soldiers in the street"),
     (158, "Climb to the tea-house roof and watch")])

passage(120,
    "The naginata-bearer goes down first, but a spear-thrust catches "
    "you under the ribs. You feel it scrape bone. Three more soldiers "
    "are on you before the captain has finished shouting. You cut, and "
    "cut, and cut, and finally the world goes red and small and quiet.\n\n"
    "The last thing you see is the captain, alive, lifting the bound "
    "girl over his shoulder like a sack of rice.",
    None,
    "ending",
    )

passage(121,
    "You take the captain in the throat and the man with the naginata "
    "in the shoulder, and in the half-second of confusion you slash "
    "the girl's bonds, seize her wrist, and run.\n\n"
    "Arrows hiss past you in the dark. One nicks your ear. You crash "
    "through the reeds with her stumbling at your side, and somehow, "
    "somehow, the river swallows your tracks. By dawn you are five ri "
    "north, gasping in a thicket, bleeding from a dozen small wounds, "
    "with a furious and very alive young woman beside you.",
    [(159, "Ask her name")])

passage(122,
    "You explode out of the reeds. You take the first man with a "
    "downward cut and the second with a thrust before the others are "
    "fully on their feet. The captain shouts. The girl, bound, scrambles "
    "behind the fire-stones.\n\n"
    "Four against one. But you have surprise, and the fire-light at "
    "their backs blinds them, and your master taught you the cut of "
    "the willow on a wet morning when you were nine years old.",
    [(160, "Fight on")])

passage(123,
    "You wait until the two have taken her some distance from the fire, "
    "then you follow. The first goes down before he hears you come — "
    "your wakizashi between his ribs from behind. The second has time "
    "only to half-turn before your blade takes his sword-arm at the "
    "shoulder.\n\n"
    "The bound girl stares at you with eyes huge in the moonlight. "
    "\"Cut me loose,\" she whispers. \"Then run. There are four more "
    "at the fire.\"",
    [(161, "Cut her loose and slip away into the trees")])

passage(124,
    "You walk on. The morning is cold, the road empty. You sleep one "
    "night in a roadside shrine and dream of a girl crying in a tree-"
    "line.\n\n"
    "On the second day you reach the shrine road, the eastern fork, "
    "and there an old beggar with one milky eye stops you. \"You smell "
    "of grief and ash and a worse thing,\" he says. \"Cowardice keeps "
    "in the marrow, young master. Mind it does not become you.\"\n\n"
    "You give him a coin and walk on. He will trouble your dreams for "
    "the rest of your life. Whether your life is long is yet to be "
    "decided.",
    [(162, "Continue north toward Black Crow")])

passage(125,
    "You take a small room at the inn. You bar the door. You sleep with "
    "your wakizashi on your chest. You dream of fire on a mountain.\n\n"
    "An hour before dawn you wake — not to a sound, but to the absence "
    "of one. The inn has gone too quiet. You rise.",
    [(163, "Slip out the window"),
     (164, "Open the door with sword drawn")])

passage(126,
    "You shoulder your pack and walk back out into the rain. The "
    "innkeeper does not protest the lost coin. The road north is empty "
    "and shining wet. You walk until your legs shake, and then you "
    "walk another ri, and then another.\n\n"
    "By dawn you have left Karasu-juku far behind. You have also left "
    "any chance of meeting whoever the master sent for you. The road "
    "ahead is yours alone.",
    [(162, "Continue toward Black Crow")])

passage(127,
    "\"From down the coast,\" you say. \"Family matter.\"\n\n"
    "The captain studies you. He does not believe you. But the inn is "
    "crowded, and a fight here would cost him more than it would gain.\n\n"
    "\"Then walk on, *coastal* young master. Walk far. And do not let "
    "me find you north of this town tomorrow.\"\n\n"
    "You bow and go.",
    [(126, "Push on into the night")])

passage(128,
    "\"From the temple on Mount Suzaku,\" you say. \"My master is "
    "dead. I am hunting the man who killed him.\"\n\n"
    "The captain goes very still. The three soldiers behind him grow "
    "stiller still. The captain's burn-scarred throat moves once as he "
    "swallows.\n\n"
    "Then, softly, he says: \"Boy. You should not have told me that.\"",
    [(165, "Draw")])

passage(129,
    "You twist your wrist out of his grip and lunge for the door. A "
    "soldier steps into your path; you cut him down. Two more on you "
    "now. The inn erupts in screams.\n\n"
    "You make it to the threshold. A crossbow bolt takes you in the back.",
    None,
    "ending",
    )

# Fixing passage 120 and 129 which use legacy passage signature
P[120]["ending"] = "bad"
P[120]["title"] = "Death in the Reeds"
P[120]["choices"] = []
P[129]["ending"] = "bad"
P[129]["title"] = "Cut Down at the Threshold"
P[129]["choices"] = []


# ---------------------------------------------------------------------------
# CHAPTER 2c — Hisame deepening (Genshin, Fire wind)
# ---------------------------------------------------------------------------

passage(130,
    "\"Carefully, master Genshin. As carefully as I am able.\"\n\n"
    "He nods, slowly. \"Good. The honest answer would have been *I do "
    "not know yet*, but you are young, and pride is the proper sin of "
    "youth.\"\n\n"
    "He rises with a creak. \"Come. We will eat with Sister Kiri, who "
    "has waited longer than either of us. Then we will sit in the cold "
    "all night, and I will give you the Fire.\"",
    [(166, "Follow him to the tall woman's house")])

passage(131,
    "\"Honestly, master, I do not know how I will carry it.\"\n\n"
    "He is silent a long moment. Then he claps you on the shoulder. "
    "\"Better. Better and better. Come — Sister Kiri has been "
    "waiting.\"",
    [(166, "Follow him to the house")])

passage(132,
    "He nods. \"Come. We will eat with Sister Kiri, who has waited "
    "longer than either of us, and tonight we will sit in the cold and "
    "I will give you the Fire.\"",
    [(166, "Follow him")])

passage(133,
    "\"From the mountain,\" you say evenly. \"And the road is muddy "
    "and you talk too much.\"\n\n"
    "The peddler's grin widens a fraction. The young woman at the "
    "bath's edge has not moved. The steam between you is suddenly "
    "very thick.",
    [(167, "Stand and reach for your sword"),
     (168, "Stay seated and watch them both")])

passage(134,
    "\"From down the coast,\" you say. \"Family matter.\"\n\n"
    "He nods, sips his tea. The young woman by the bath has not moved. "
    "But after a beat, the peddler murmurs: \"Strange thing, young "
    "master. Two hours ago a man on a grey horse stopped here for "
    "water. He wore red lacquer, and a scar like a half-moon over one "
    "eye. He asked after a *coastal* young man with a broken sword-tang "
    "at his belt.\"\n\n"
    "The peddler smiles. \"You have very nice manners, *coastal* young "
    "master. But your eyes lie.\"",
    [(169, "Draw on him")])

passage(135,
    "You stand, lay a coin on the table, bow politely, and walk out "
    "into the morning. The peddler watches you go. The young woman by "
    "the bath stares at her own hands.\n\n"
    "Twenty steps up the road, the young woman catches up with you. "
    "\"You should not have come into the inn,\" she says, low and "
    "fast. \"He had a man on the roof. Walk with me, samurai. Do not "
    "look back.\"",
    [(170, "Walk with her")])

passage(136,
    "When she rises and moves through the inner curtain, you rise with "
    "her. The peddler at the door starts up — too late. You and the "
    "woman are through the back rooms and out into the kitchen yard "
    "before he is half on his feet.\n\n"
    "She turns to you in the alley. \"You either trust very quickly, "
    "samurai, or you are a fool. Either way — run.\"",
    [(170, "Run with her")])

passage(137,
    "You stay seated. The woman, after a long moment, stands and walks "
    "alone through the inner curtain. The peddler watches her go.\n\n"
    "Then he turns to you, smiles, and says: \"Wise, young master. She "
    "is not safe to know. Sit a while; have tea. Tell me of the temple "
    "that burned.\"",
    [(171, "Realize your mistake and try to leave"),
     (172, "Try to fight him")])

passage(138,
    "You set the wooden token on the stone beside her hand.\n\n"
    "Her eyes flicker to it; her shoulders drop a fraction. \"Then I am "
    "neither stupid nor required to kill you, samurai. I am Kiri of the "
    "Hollow Reed, and I have been three weeks on your master's road. "
    "Stand up slowly. The peddler at the door is one of theirs. He has "
    "a friend on the roof.\"",
    [(173, "Stand slowly and follow her lead")])

passage(139,
    "\"Akiyama Ryūnosuke,\" you say. \"He is dead.\"\n\n"
    "She closes her eyes. Just for a heartbeat. Then she opens them.\n\n"
    "\"Then we have very little time, samurai. The peddler at the door "
    "is one of theirs. He has a friend on the roof. Stand up slowly "
    "and follow me to the back.\"",
    [(173, "Stand and follow")])

passage(140,
    "She almost smiles.\n\n"
    "\"There are always more than three options, samurai. But for now "
    "let those be enough. Stand up slowly. The peddler at the door is "
    "one of theirs. Follow me out the back.\"",
    [(173, "Stand and follow")])


# ---------------------------------------------------------------------------
# CHAPTER 2 wrap-up — converging
# ---------------------------------------------------------------------------

passage(141,
    "The innkeeper leads you through the kitchens and a curtained "
    "doorway to a small back room. On the floor sit two travellers: a "
    "tall woman with grey at her temples and a longbow, and a slighter "
    "young woman with eyes like flint.\n\n"
    "The tall one rises. \"You are late, Takeshi-san. I am Genshin's "
    "wife, Hana. This is Kiri of the Hollow Reed. Your master sent "
    "word weeks ago, and three winds have already gathered for you. "
    "Sit, eat, and tell us which path you took down the mountain.\"",
    [(180, "Sit, eat, tell")])

passage(142,
    "You drop coin and rise. The soldier with the interested gaze rises "
    "with you. You make it as far as the door before he is at your "
    "elbow.\n\n"
    "\"Coastal young man,\" he murmurs. \"Walk slowly with me. My "
    "captain wishes a word.\"\n\n"
    "You feel the point of his short-sword against your kidney through "
    "your robe.",
    [(174, "Submit and walk with him"),
     (175, "Strike now")])

passage(143,
    "You stay. You eat too loud and laugh too loud and order more sake "
    "and pretend to be a coastal idiot. The soldier watches. After a "
    "while he loses interest. Eventually all three of them leave.\n\n"
    "The innkeeper, clearing your bowl, says under his breath: \"That "
    "was very brave or very stupid. There is a back room with two "
    "travellers waiting for you. One of them carries an old square "
    "coin and a longbow.\"",
    [(141, "Follow him")])

passage(144,
    "Two more bowls of millet appear. The innkeeper does not look at "
    "you again. You eat slowly, deliberately. You leave on the second "
    "watch, slipping out the back, and you take the east road to the "
    "old shrine through the cold dawn.\n\n"
    "At the shrine you find a tall woman with grey at her temples and "
    "a longbow leaning beside her, and a slighter young woman with "
    "eyes like flint sitting on the offering-stone.\n\n"
    "\"Takeshi-san,\" says the tall woman. \"I am Hana. This is Kiri. "
    "You are late, and your master is dead. Sit and tell us how.\"",
    [(180, "Sit and tell")])

passage(145,
    "\"My grandmother carried one like it,\" she says, very low, \"and "
    "she died on a hill above this town when her old master was killed "
    "on a mountain not unlike yours. She told me one day a young "
    "samurai would come bearing the same mark, and that I should send "
    "him to the eastern shrine an hour before dawn. So I am telling "
    "you now. The rest is yours.\"",
    [(146, "Pay and ride for the shrine before dawn")])

passage(146,
    "You ride. The eastern shrine sits among black cedars an hour "
    "north. As you approach you see a horse tied at the torii — a lean "
    "grey mare. On the shrine steps, a tall woman with grey at her "
    "temples and a longbow rises to meet you. Beside her sits a "
    "slighter young woman with eyes like flint.\n\n"
    "\"Takeshi-san,\" the tall woman says. \"I am Hana. This is Kiri. "
    "Your master is dead. Sit and tell us how.\"",
    [(180, "Sit and tell")])

passage(147,
    "You walk out into the lantern-light. Tetsu of the Burnt Hill looks "
    "up at you and grins, lopsided, with his good eye.\n\n"
    "\"There you are, monk-boy. Sit. I am Tetsu of the Burnt Hill. "
    "Akiyama Ryūnosuke was my captain when I was a younger and a worse "
    "man. The innkeeper said you wore a three-brush token. Therefore "
    "Akiyama is dead. Therefore we ride at dawn.\"",
    [(149, "Sit and tell him everything")])

passage(148,
    "You press. The cut of the willow becomes the cut of the river "
    "becomes the cut of the falling pine. Tetsu retreats one step, two, "
    "three — and on the third he laughs and brings his blade up flat, "
    "blocking your strike with a force that nearly snaps your wrist.\n\n"
    "\"Enough, monk-boy. *Enough.* I am not your enemy.\"\n\n"
    "He sheathes his sword. \"Sit. I am Tetsu of the Burnt Hill, and "
    "Akiyama Ryūnosuke was my captain. The broken tang at your belt "
    "is his. Therefore he is dead. Therefore we ride at dawn.\"",
    [(149, "Sit and tell him")])

passage(149,
    "You sit. You tell. Tetsu listens, jaw working, his good eye fixed "
    "on the lantern. When you reach the part where the master speaks of "
    "the three winds, Tetsu closes his eye and breathes out slowly.\n\n"
    "\"Then I am one of your three,\" he says at last. \"Earth. Hayabusa "
    "took the blade and your master sent your three winds out years ago "
    "knowing this would come. The Maiden of the Tide-Shrine is the Water. "
    "Genshin in Hisame is the Fire. I am the Earth. We meet at the old "
    "shrine on the eastern road, dawn, two days hence. There is a "
    "kunoichi named Kiri who carries the missing piece of all three.\"\n\n"
    "He pours you more sake. \"Sleep, monk-boy. Tomorrow we ride.\"",
    [(180, "Sleep and ride")])

passage(150,
    "You take the token out and lay it in her palm. Her fingers close "
    "around it.\n\n"
    "\"Then your master sent you,\" she says, almost gently. \"And he is "
    "dead, or you would not have it. I am Ayane of Mikuriya. My old "
    "guardian was killed on the steps of the tide-shrine three weeks "
    "ago. She gave me what she gave me. She said only — *find Akiyama. "
    "Or anyone he sends.*\"",
    [(176, "Ask what she carries")])

passage(151,
    "\"The shrine maiden,\" Ayane says, very softly, \"was my mother. "
    "She was the Maiden of the Tide-Shrine, the keeper of the Water "
    "wind, until the men in red armour came up the temple steps and "
    "killed her old guardian.\n\n"
    "\"Before she died, she gave me the sealing-mantra. Carved it into "
    "my memory in a single afternoon, the way one carves into "
    "driftwood. She told me to carry it north until I found a man with "
    "a broken sword-tang at his belt and a three-stroke token at his "
    "hand.\"",
    [(176, "Ask what she carries")])

passage(152,
    "\"Because,\" Ayane says, \"my mother was the keeper of the Water "
    "wind, and she gave me the sealing-mantra before they took her on "
    "the steps of the tide-shrine. They want it back. They want it "
    "*gone*. Their master cannot use the Yasha-no-Tachi while the "
    "mantra survives outside his hands.\"",
    [(176, "Ask what the mantra does")])

passage(153,
    "\"A breath,\" she says. \"My mother gave me a breath. A few words. "
    "An old song that means nothing to anyone but my mother and "
    "whatever god watches the tides.\" She glances at you, sharper. "
    "\"Why do you care, stranger?\"",
    [(150, "Show her your token")])

passage(154,
    "\"He died yesterday morning,\" you say. \"He spoke of the three "
    "winds. He told me to find a girl who carries water, a hermit who "
    "carries fire, and a — \"\n\n"
    "\"And an earth,\" Ayane finishes, voice low. \"The third wind is "
    "a soldier. A man named Tetsu of the Burnt Hill. He was my "
    "mother's bodyguard before he was anyone's enemy. He is in this "
    "town tonight. He has been waiting for you.\"",
    [(177, "Ask her to take you to Tetsu now")])

passage(155,
    "You walk away. The morning finds you on the north road, alone, "
    "moving fast. You tell yourself there was nothing to be done.\n\n"
    "On the third day's ride you hear a story at a wayside teahouse: a "
    "young woman in a torn silk cloak was found dead in the alley "
    "behind a tea-house in Karasu-juku, throat cut, an old square coin "
    "pressed into her palm.\n\n"
    "You ride on. You ride very fast. There is a hollow in your chest "
    "now that no wind will ever quite fill.",
    [(162, "Continue toward Black Crow")])

passage(156,
    "You drop low under the gate and slip in. The tea-house garden is "
    "empty. Inside, you hear Ayane's voice — calm, controlled — "
    "answering questions you cannot quite make out.\n\n"
    "You move through the kitchen. In the front room, two red-armoured "
    "soldiers stand with their backs to you, blades drawn. Ayane sits "
    "on her heels before them, hands folded, expression unreadable.",
    [(178, "Attack from behind"),
     (179, "Step out into the open and challenge them"),
     (181, "Wait for an opening")])

passage(157,
    "You step into the soldiers' path. \"You will not enter that "
    "tea-house tonight,\" you say.\n\n"
    "They look at each other. They look back at you. They draw.\n\n"
    "There are two of them, but you have a temple's worth of rage in "
    "your sword-arm tonight, and the road is muddy.",
    [(182, "Fight")])

passage(158,
    "You climb to the tea-house roof. From there you can see the "
    "soldiers enter — and you can see, through a paper window, "
    "Ayane standing very calm before them, hands folded.\n\n"
    "She glances up. Just once. Her eyes find yours through the "
    "lattice. She gives the very smallest of nods.",
    [(183, "Drop through the roof at her signal")])

passage(159,
    "\"My name?\" she says, still gasping. \"I am Kiri of the Hollow "
    "Reed. I have been three weeks looking for you, samurai. Your "
    "master sent word the night before he died. He told me you would "
    "carry his sword-tang at your belt and his stubbornness in your "
    "jaw, and that I should find you before the red-armour did. I "
    "almost failed.\"\n\n"
    "She bandages her own forearm with strips of her sleeve. \"Thank "
    "you. For not riding past.\"",
    [(180, "Sit with her and tell her everything")])

passage(160,
    "You fight. Cut of the willow, cut of the river, cut of the "
    "falling pine. The captain dies first. The naginata-bearer dies "
    "second. The two spear-men retreat — and you take one in the "
    "back as he turns. The last drops his weapon and runs.\n\n"
    "When it is done, the bound girl is staring at you with eyes like "
    "two black coals. \"You came from the reeds,\" she whispers, "
    "\"like an oni. Cut me loose, samurai. We have to go.\"",
    [(159, "Cut her loose and run")])

passage(161,
    "You free her. The two of you slip into the trees as the campfire "
    "soldiers begin to call out for their missing comrades. By the time "
    "they realize what has happened, you and she are half a ri away, "
    "moving north through black woods.\n\n"
    "An hour later, in a stand of cedar, she sits and bandages her "
    "wrists with strips of her sleeve. \"I am Kiri of the Hollow Reed. "
    "I have looked for you three weeks. Your master sent word — \"\n\n"
    "\"I know,\" you say. And in the dark, you finally tell her what "
    "you saw at Tōkin-ji.",
    [(180, "Travel together to the shrine")])

passage(162,
    "You walk on, alone, north and north. Two days bring you to the "
    "shrine road. Three more bring you to the foothills of the "
    "Hōrai forest. You are alone. You are tired. You have not "
    "gathered any of the three winds.\n\n"
    "Black Crow Castle waits beyond the forest. You can press on "
    "alone, or you can turn aside to seek the Earth-wind in the forest "
    "of Hōrai before you go further.",
    [(184, "Press on alone toward Black Crow"),
     (185, "Turn aside into the forest of Hōrai to find Earth")])

passage(163,
    "You slip out the window onto the inn's rear roof and crouch among "
    "the wet thatch. Below, in the alley, three red-armoured soldiers "
    "are quietly closing on the inn's back door. Their captain — burn-"
    "scarred — directs them with hand signs.\n\n"
    "You have surprise, height, and a temple's worth of rage.",
    [(186, "Drop on the captain"),
     (187, "Slip across the rooftops and away")])

passage(164,
    "You open the door with sword drawn. The hallway is empty. The "
    "stair is empty. Downstairs, the common room is empty too — "
    "except for the burn-scarred captain, sitting at your table with "
    "your bowl, drinking your tea.\n\n"
    "\"There he is,\" the captain says quietly. \"I knew you would "
    "open the door instead of the window. Akiyama's students always "
    "did love a clean confrontation.\"\n\n"
    "Two soldiers step out from behind the curtain. Three more from "
    "the kitchen.",
    [(188, "Fight"),
     (189, "Talk")])

passage(165,
    "You draw. The captain draws. The three soldiers behind him draw. "
    "The inn explodes in screams as the patrons scramble for the door.\n\n"
    "You are a temple sword in a crowded room against four men. Your "
    "master taught you the cut of the willow on a wet morning when you "
    "were nine years old. You remember it now.",
    [(190, "Fight")])

passage(166,
    "Genshin's wife Hana sets bowls of mountain-vegetable stew before "
    "you and refuses to speak of the temple until you have eaten three "
    "bowls. \"A grieving man should not strategize hungry,\" she says.\n\n"
    "Afterward, while the rain hisses on the roof, the three of you "
    "speak long into the night. Genshin tells you of the Yasha-no-"
    "Tachi: a sword forged by a demon-smith on the slopes of Asahi, "
    "centuries ago. A blade that drinks the will of its wielder. A "
    "blade that Hayabusa carried once, briefly, in his youth — and "
    "lost himself to. Your master, Akiyama, bound the demon in it and "
    "sealed it under the floor of Tōkin-ji for thirty years.\n\n"
    "\"The seal was three-winded,\" Genshin says. \"Fire to break the "
    "blade's spirit. Water to bind the demon's voice. Earth to hold "
    "the iron still. All three must speak at once. Otherwise the demon "
    "merely shifts shape, and we are in a worse place than before.\"",
    [(191, "Ask where to find Water and Earth"),
     (192, "Ask about Hayabusa")])

passage(167,
    "Your hand goes to the hilt. The peddler's smile widens. \"Ah-ha,\" "
    "he says — and a knife is in his hand, where no knife was a "
    "breath before. \"There he is. The mountain in your eyes.\"\n\n"
    "Behind you, the young woman by the bath has stood. Steel "
    "whispers. One of you is going to die in this room in the next "
    "few seconds.",
    [(193, "Attack the peddler")])

passage(168,
    "You stay seated. The peddler's grin freezes — for the smallest "
    "flicker. He had expected you to bolt.\n\n"
    "The young woman by the bath rises smoothly and walks behind him. "
    "He turns his head a fraction too late. Her tanto comes up under "
    "his ribs in a movement so practiced you almost miss it.\n\n"
    "She lowers him gently to the floor. \"I am Kiri of the Hollow "
    "Reed,\" she says quietly. \"Your master sent word. Get up, "
    "samurai. We have an hour before his friend on the roof realizes "
    "this peddler is dead.\"",
    [(170, "Rise and follow")])

passage(169,
    "You draw. The peddler draws. The young woman by the bath rises — "
    "and her tanto comes out from her sleeve.\n\n"
    "Whose side she is on, you have a half-second to decide.",
    [(194, "Strike the peddler first"),
     (195, "Strike the young woman first"),
     (196, "Try to back away to the wall")])

passage(170,
    "You walk with her up the road. She does not look back. She does "
    "not speak until you are two ri north of Yumura, in a thicket "
    "above the river.\n\n"
    "\"I am Kiri of the Hollow Reed,\" she says. \"Your master sent for "
    "me a month ago. I have been looking for you for two weeks. The "
    "peddler at the inn was watching the west road for me. He has not "
    "been a peddler since the war.\"\n\n"
    "She studies you. \"Your master is dead, or you would not be on "
    "this road. Sit. Tell me. Then we will find Genshin in Hisame, "
    "and the soldier Tetsu in Karasu-juku, and at the end of that road "
    "we will all four ride for the place where the blade was forged.\"",
    [(180, "Sit and tell her")])

passage(171,
    "You realize, too late, that the peddler's eyes are entirely "
    "wrong — black through and through, no white at all. You rise. "
    "You reach for your sword.\n\n"
    "His hand catches your wrist before you have moved an inch. His "
    "grip is colder than rain. \"Ah, young master. Such a hurry. The "
    "tea is not even cold.\"",
    [(197, "Try to break free")])

passage(172,
    "You stand and draw. The peddler stands and smiles. His eyes are "
    "entirely black, no white at all. \"Oh good,\" he murmurs, "
    "delighted. \"I do enjoy this part.\"\n\n"
    "What you are fighting in this room is not human and never was.",
    [(198, "Fight whatever it is")])

passage(173,
    "You stand slowly. Kiri rises with you. She does not look at the "
    "peddler. She walks toward the inner curtain as if she has not a "
    "care in the world. You follow.\n\n"
    "Behind you, the peddler half-rises, hand twitching toward his "
    "robe — but a third figure has been sitting unnoticed in the "
    "corner this whole time, an old man in a faded grey robe smoking "
    "a long pipe. He says nothing. He merely *looks* at the peddler. "
    "The peddler sits back down.\n\n"
    "Kiri murmurs, \"That is Genshin. He has been waiting for us. "
    "Move.\"",
    [(199, "Follow them out the back")])

passage(174,
    "You walk with him. He marches you to a smaller side-room of the "
    "inn where the burn-scarred captain waits, alone, drinking tea.\n\n"
    "\"Sit, *coastal* young master. Tell me whose grandson you "
    "are.\"\n\n"
    "He pours you tea. The kid-glove veneer is paper thin.",
    [(200, "Tell him the truth and watch his face"),
     (201, "Try a more elaborate lie"),
     (202, "Take the cup")])

passage(175,
    "You spin and strike. Your wakizashi takes him in the throat before "
    "he has fully understood what is happening. The inn explodes in "
    "screams.\n\n"
    "You make the door — but the captain and two more soldiers are "
    "outside, waiting. Three against one in lantern-light, with no "
    "room to run.",
    [(190, "Fight")])

passage(176,
    "\"A few words,\" Ayane says. \"A breath. A song my mother sang "
    "into my ear for two hours on the steps of the tide-shrine, just "
    "before she — \"\n\n"
    "She breaks off. Then: \"It is called the Mantra of the Tide. It "
    "is the Water wind. Without it, the blade's demon cannot be "
    "silenced. Without it, even Fire and Earth together would only "
    "shift the demon, not bind it.\"",
    [(177, "Ask her to take you to Tetsu of the Burnt Hill")])

passage(177,
    "Ayane rises, brushing rain from her cloak. \"Then come, samurai. "
    "Tetsu is in the smaller inn under the lantern. He is loud and "
    "rude and ugly and you will trust him in five minutes. We will "
    "leave Karasu-juku before dawn and meet Genshin and Kiri at the "
    "eastern shrine.\"",
    [(180, "Go meet Tetsu with Ayane")])

passage(178,
    "You strike from behind. The first soldier drops without a sound. "
    "The second turns, half-draws, and Ayane — Ayane — strikes him in "
    "the throat with a hairpin you did not know she had.\n\n"
    "Two bodies on the tea-house floor. Ayane rises. \"You followed,\" "
    "she says. \"Good. We have to go. Now. There were three more "
    "outside.\"",
    [(180, "Flee together")])

passage(179,
    "You step out. \"This one is under my protection,\" you say.\n\n"
    "The soldiers turn. The first one laughs. The second does not.\n\n"
    "They charge.",
    [(182, "Fight them in the tea-house")])

passage(181,
    "You wait. The soldiers question Ayane; she answers in a low, "
    "calm voice. When the first one reaches for her hair, you move — "
    "but Ayane moves first. A hairpin flashes. The soldier reels back, "
    "throat opening.\n\n"
    "The second soldier turns. You take him from behind.",
    [(178, "Flee with her")])

passage(182,
    "Two soldiers in close quarters; lantern-light; mud and rain. You "
    "are a temple sword. The first one dies under your second cut. The "
    "second one is harder — he has a spear, and his reach is longer "
    "than yours.\n\n"
    "You take a cut along your forearm. You take him in the eye with "
    "the hilt of your wakizashi and finish him on the ground.",
    [(180, "Flee with Ayane into the night")])

passage(183,
    "You drop. Through the lattice and onto the back of the nearest "
    "soldier. Your weight bears him down; your blade finishes him "
    "before he hits the boards.\n\n"
    "The second soldier turns — and Ayane is on him. A hairpin in "
    "the throat. He drops like a sack.\n\n"
    "Ayane meets your eyes. \"You are *full* of surprises, "
    "samurai.\"",
    [(180, "Flee together into the night")])

passage(184,
    "You push on alone. By the seventh day you are tired, hungry, and "
    "more than a little mad with grief. The Hōrai forest looms to your "
    "left; you do not turn aside. The fields north of it are dotted "
    "with the black banners of Hayabusa's men.\n\n"
    "You have no Wind. You have only a broken sword-tang and a rage "
    "the size of a temple.",
    [(260, "Press on toward Black Crow alone")])

passage(185,
    "You turn aside into the forest of Hōrai. The trees here grow "
    "older as you walk — first cedar, then a kind of pine you have no "
    "name for, then trees that seem older than your country. The "
    "underbrush goes silent. The air goes still.\n\n"
    "At the foot of a tree wider than a temple gate, an old man sits "
    "with bark for skin. He does not move as you approach. His eyes "
    "open last of all.\n\n"
    "\"Late,\" he says. \"You are *late*, boy of Akiyama. But not too "
    "late. Sit.\"",
    [(220, "Sit with the Earth-wind alone")])


# ---------------------------------------------------------------------------
# CHAPTER 3 — THE THREE WINDS GATHER
# ---------------------------------------------------------------------------

passage(180,
    "Whatever path you took, the threads pull together. In the small "
    "hours before dawn you find yourself in a back room, or a hidden "
    "shrine, or a thicket of cedar, surrounded by some of your "
    "master's people:\n\n"
    "  — Genshin of Hisame, the one-eyed Fire-wind.\n"
    "  — Kiri of the Hollow Reed, the kunoichi your master sent for.\n"
    "  — and one of two others, depending on the road you walked.\n\n"
    "Above the wood-fire, Genshin speaks. \"We have four days, perhaps "
    "five, before Hayabusa reaches Black Crow Castle. We have the "
    "three winds — Fire, Water, Earth — and we have you, the boy of "
    "Akiyama. Tonight I begin to teach you the Fire. Tomorrow, "
    "Water. The day after, Earth. The fourth day we ride.\"",
    [(210, "Begin the Fire teaching")])

passage(191,
    "\"Water lives at the tide-shrine of Mikuriya,\" Genshin says. "
    "\"Or it did — the old maiden was killed three weeks ago. Her "
    "successor walks the road now, carrying the mantra. Kiri here was "
    "sent to find her.\"\n\n"
    "He looks at you. \"Earth is in Karasu-juku, in the body of an "
    "old soldier called Tetsu of the Burnt Hill. Your master's man, "
    "long ago. He has been drinking himself slowly to death waiting "
    "for this week.\"\n\n"
    "Kiri stirs. \"Tomorrow at first light I go for the Water-bearer. "
    "Tetsu we will meet at the eastern shrine on the third day.\"",
    [(210, "Agree to the plan")])

passage(192,
    "Genshin is silent a long moment. \"Hayabusa Mōri was the most "
    "gifted student of our generation. Akiyama and I were proud of "
    "him. Then he found the Yasha-no-Tachi in a cave above Asahi when "
    "he was eighteen years old. He carried it for ninety-one days "
    "before we caught him. By then there was very little of Hayabusa "
    "left.\n\n"
    "\"Akiyama and I and one other sealed the blade and tried to seal "
    "the man. We failed at the second part. Hayabusa escaped before "
    "the last words were spoken. We have not seen him in thirty years. "
    "We had hoped — \" the old man closes his eye. \"We had hoped he "
    "was dead.\"",
    [(193, "Ask if Hayabusa can be saved")])

passage(193,
    "\"Saved?\" Genshin's good eye opens slowly. \"That is a young "
    "man's question, Takeshi. I have not asked myself that question "
    "about Hayabusa in twenty-nine years.\n\n"
    "\"I do not know. The Yasha eats a man slowly. Hayabusa has worn "
    "it thirty years. Almost nothing of the boy I taught is likely to "
    "remain. *Almost* nothing. There is a kind of sealing that "
    "addresses the wielder as well as the blade — but it requires "
    "all three winds, the mantra perfectly sung, and an act of "
    "mercy from the boy of Akiyama that the boy of Akiyama may not "
    "wish to make.\"\n\n"
    "He looks at you steadily. \"It is your choice. The blade can "
    "always be broken instead. That is a cleaner road, and a worse "
    "one.\"",
    [(210, "Take this in and prepare for the teaching")])

passage(194,
    "Your blade reaches the peddler first. You catch him across the "
    "shoulder — but he laughs as your steel passes through him, and "
    "there is no resistance to your cut. He is not entirely there.\n\n"
    "The young woman by the bath strikes — at the peddler. Her tanto "
    "buries itself in the side of his neck. The peddler reacts to her "
    "blade in a way he did not react to yours: he falls, twitching, "
    "and goes still.\n\n"
    "\"He was a *gaki*,\" she says quietly. \"A hungry ghost. Steel "
    "blessed at the tide-shrine bites them. Yours, samurai, does "
    "not.\" She looks at you, weighing. \"I am Kiri of the Hollow "
    "Reed. Your master sent for me. Come.\"",
    [(170, "Follow her")])

passage(195,
    "You strike at the young woman. She moves like water — gone "
    "before your cut completes. Behind you, the peddler laughs, "
    "delighted.\n\n"
    "\"Oh, samurai,\" he murmurs. \"Oh, you should have trusted the "
    "one with the calloused hands. Now there is no one to vouch for "
    "you when I take your head north.\"",
    [(196, "Try to back to the wall")])

passage(196,
    "You step back, sword level, eyes on both of them. The peddler "
    "grins. The young woman — eyes flint-hard — *bows* to you, very "
    "slightly. Then she springs at the peddler.\n\n"
    "Her tanto finds the side of his neck. He falls, and is suddenly "
    "much smaller than he should be — a peddler-shaped sack of empty "
    "robe. Whatever was in it was not human.\n\n"
    "\"I am Kiri of the Hollow Reed,\" she says. \"Your master sent "
    "for me. Forgive the test — I had to know whether you would "
    "strike a stranger or wait. Come. There is a friend on the roof "
    "of this inn we must not meet.\"",
    [(170, "Follow her out")])

passage(197,
    "You strain against the grip. The peddler's hand is iron — colder "
    "than iron. His black eyes widen, drinking you in. \"Such a young "
    "fire,\" he murmurs. \"Such a *bright* one. Sit, monk-boy. "
    "Sit and let me have it.\"\n\n"
    "His other hand rises toward your face. You feel something in "
    "your chest beginning to be drawn out. You realize, distantly, "
    "that the woman by the bath has not moved — and that you no "
    "longer have the strength to draw your sword.",
    None)
P[197]["ending"] = "horrible"
P[197]["title"] = "Eaten by a Hungry Ghost"

passage(198,
    "Your steel passes through the thing in the peddler's robe with "
    "no resistance. It laughs and laughs as your cut comes back empty.\n\n"
    "By the third cut you understand. Your blade cannot bite this "
    "thing. By the fifth cut its hand is on your throat. By the "
    "sixth — the room is gone, and you are gone, and only the "
    "laughing is left.",
    None)
P[198]["ending"] = "horrible"
P[198]["title"] = "The Peddler's Smile"

passage(199,
    "You follow Kiri and the old monk Genshin out the back of the "
    "inn. The morning is barely grey. Behind you, in the bath-room, "
    "the peddler is still sitting where he sat, perfectly still, "
    "perfectly silent. The young woman who served the tea will find "
    "him in an hour and never speak of it again.\n\n"
    "Genshin walks beside you, smoking. \"You did well not to draw, "
    "boy. That was a *gaki*. Steel like yours would only have made "
    "it hungrier. I would have had to kill it for you, and I am old "
    "and would have charged double for the favour.\"",
    [(180, "Travel with them to the gathering")])

passage(200,
    "\"My master was Akiyama Ryūnosuke,\" you say. \"My temple "
    "burned. The man who took the Yasha-no-Tachi from beneath our "
    "floor is the man your captain calls master.\"\n\n"
    "The burn-scarred captain's tea cup pauses halfway to his mouth. "
    "He sets it down very carefully. The room is very quiet.\n\n"
    "Then, softly: \"Boy. I am sorry to hear about your temple. I am "
    "sorrier still that you told me. Hayabusa-sama gave a standing "
    "order: no surviving witness from the temple is to walk past "
    "Karasu-juku alive.\"\n\n"
    "He raises his hand. A door opens. Three soldiers step in.",
    [(190, "Fight")])

passage(201,
    "\"I am the third son of a salt-merchant from Sakai,\" you say, "
    "\"come north on family business that no longer concerns me. My "
    "grandfather was in red armour once, ages ago. I drink too quick "
    "and ask too much, captain, forgive me.\"\n\n"
    "The captain studies you a long moment. Then he says: \"Salt-"
    "merchant. Sakai. Family business. *No longer concerns you.* "
    "That is a poor lie, monk-boy, but it is an *interesting* poor "
    "lie. Sit. Drink. Tell me which monastery.\"\n\n"
    "He smiles. You realize, sickeningly, that he already knows.",
    [(200, "Tell him the truth")])

passage(202,
    "You take the cup. You sip. Your eyes lock with his over the "
    "rim.\n\n"
    "The tea is bitter — bitterer than tea should be. By the time "
    "you set the cup down your hand will not entirely obey you. By "
    "the time you try to stand, the room has tilted. By the time "
    "two soldiers lift you under the arms and carry you out the "
    "back, you cannot raise your sword.\n\n"
    "You wake in a cart, bound, somewhere north, with a hood over "
    "your head. The journey is long. The journey ends at Black Crow "
    "Castle, where you are taken before a man with a moon over his "
    "eye who does not even raise his head to greet you before he "
    "draws.",
    None)
P[202]["ending"] = "bad"
P[202]["title"] = "Bitter Tea"

# ---------------------------------------------------------------------------
# CHAPTER 3 — TRAINING WITH THE THREE WINDS
# ---------------------------------------------------------------------------

passage(210,
    "Three days. Three winds. Three teachers.\n\n"
    "On the first night, in the cold above Hisame, Genshin sits you "
    "before a wood-fire and gives you the Fire. It is not a technique "
    "of the sword. It is not a chant. It is a *posture* — a way of "
    "standing inside your own anger such that the anger does not "
    "stand inside you. He makes you hold it for six hours. By dawn "
    "you can light a candle by looking at it, and you have wept "
    "twice without knowing why.\n\n"
    "\"Carry it carefully, boy,\" Genshin says. \"You can burn down "
    "a castle with what you have learned. Or you can burn down "
    "yourself.\"",
    [(211, "Move on to the Water teaching")])

passage(211,
    "On the second day the Water-bearer joins you — and you discover, "
    "depending on which path you walked, that she is either Ayane of "
    "Mikuriya, daughter of the murdered maiden, or that Kiri carried "
    "the mantra herself from the dying maiden's mouth.\n\n"
    "Either way, the Water comes to you not as words but as a "
    "*song*. A song no one has written down in five hundred years. "
    "You sit on a flat stone above a stream while the Water-bearer "
    "sings it into your ear for six hours, low and patient. By "
    "dusk you can sing it back without error. By dusk your anger has "
    "gone strangely quiet inside you, and the air around your throat "
    "feels cool.\n\n"
    "\"This is the silencing,\" the Water-bearer says. \"When the "
    "demon in the blade speaks, you sing this. The demon cannot "
    "speak through what you sing.\"",
    [(212, "Move on to Earth")])

passage(212,
    "On the third day Tetsu of the Burnt Hill arrives at the eastern "
    "shrine on a tired horse with a flask the size of a small child "
    "tied at his saddle. (Or, if you skipped the Karasu-juku road "
    "entirely, the old Earth-wind in the forest of Hōrai meets you "
    "in his place — bark-skinned, silent, ancient.)\n\n"
    "Either way, Earth comes to you as a *stance*. A way of putting "
    "your feet on the ground such that the ground recognizes you. "
    "Earth has nothing to do with the sword. Earth is about the "
    "moment after the strike, when the demon would shift shape and "
    "slip away. Earth holds it still.\n\n"
    "By nightfall, the three winds sit in you uneasily, like three "
    "cats in one small basket. You cannot quite hold them all at "
    "once yet. Tetsu says: \"You will the day you need to. Or you "
    "will not. Either way, drink.\"",
    [(213, "Drink — and ride at dawn")])

passage(213,
    "Dawn. The three of you (or four, depending on the road you "
    "walked) ride north. Genshin stays behind — \"My knees, "
    "boy. My old, old knees.\" — but his Fire goes with you in "
    "your chest, hot and quiet.\n\n"
    "The ride to Black Crow takes four days. On the way, your "
    "companions tell you what they know:\n\n"
    "Hayabusa Mōri now holds a fortress that was once a monastery, "
    "above a black salt lake. His army is small — perhaps two "
    "hundred men — but utterly loyal, and his lieutenants are "
    "not all entirely human. The fortress's central tower holds the "
    "forge where the Yasha-no-Tachi was made, and Hayabusa intends "
    "to perform a *re-forging* there on the next full moon. The full "
    "moon is in six days.\n\n"
    "If he succeeds, the demon will no longer merely whisper. It "
    "will *walk*. The country will not survive it.",
    [(250, "Decide your approach to Black Crow")])


# ---------------------------------------------------------------------------
# CHAPTER 4 — THE EARTH-WIND IN HŌRAI (alternative branch)
# ---------------------------------------------------------------------------

passage(220,
    "You sit. The bark-skinned old spirit closes his eyes for a long "
    "time. The forest around you settles — not silent, but *attentive*.\n\n"
    "\"You walk alone,\" he says at last. \"You did not gather the "
    "others. That is a heavy stance for one body to hold, boy of "
    "Akiyama. But it is the stance you took.\"\n\n"
    "He lifts one bark-knuckled finger.\n\n"
    "\"I will give you Earth. I will give you the silence-song of the "
    "Water as the old maiden taught it to me a hundred years ago. I "
    "will give you the Fire-posture as Genshin's grandfather taught "
    "it to *me*. You will carry all three alone. You will arrive at "
    "Black Crow with no allies and no rest. You will likely die there.\"\n\n"
    "He opens one bark-lidded eye. \"You may still refuse, boy. The "
    "forest will hide you forever, if you ask.\"",
    [(221, "Refuse — accept the forest's hiding"),
     (222, "Accept the three winds, alone")])

passage(221,
    "\"I cannot do it alone,\" you say.\n\n"
    "The old spirit is silent a long moment. Then he says, very "
    "softly: \"Then live, boy. Forgive yourself for not being able "
    "to lift the mountain. The mountain has stood without you for "
    "ten thousand years and will stand without you a little longer.\"\n\n"
    "He lifts his bark-hand. The forest around you thickens. The "
    "path you came in by closes. By dusk you are no longer sure "
    "which direction the road was.\n\n"
    "You will live, in the forest of Hōrai, until you are an old "
    "man. You will become a small spirit yourself, perhaps. Your "
    "master's blade will be re-forged on the next full moon. The "
    "country beyond the forest will burn. You will hear of it only "
    "as rumour. The rumour will not make it any less true. The "
    "forest will hide you, and you will hide from yourself, and "
    "the small bright thing in you will dim, year by quiet year.",
    None)
P[221]["ending"] = "bad"
P[221]["title"] = "Hidden in Hōrai"

passage(222,
    "\"I will carry them,\" you say. \"Alone if I must.\"\n\n"
    "The old spirit nods once. He places one bark-knuckled hand on "
    "your chest. For one long heartbeat you feel three impossible "
    "things at once — a fire in your sternum, a song in your throat, "
    "and a weight in your soles like the foot of a mountain.\n\n"
    "Then the forest is silent again, and the spirit is gone, and "
    "you are alone on a flat stone with three winds rattling inside "
    "you uneasily.\n\n"
    "You stand. You walk out of Hōrai by a path that did not exist "
    "before. By dusk you are on the road to Black Crow.",
    [(250, "Approach Black Crow, alone")])


# ---------------------------------------------------------------------------
# CHAPTER 5 — APPROACHING BLACK CROW
# ---------------------------------------------------------------------------

passage(250,
    "Black Crow Castle stands above a black salt lake on the spur of "
    "a dead volcano. Its outer wall is half-broken; its inner keep "
    "is hard stone. The full moon is in six days and Hayabusa Mōri "
    "is already inside.\n\n"
    "You stop at the lake's southern edge with your companions (or "
    "alone, if you walked the lonely road). There are several ways "
    "in. You will choose only one.",
    [(251, "Sneak in by night, through the lake's salt-gate"),
     (252, "Walk in openly at dawn, as a pilgrim"),
     (253, "Storm the broken outer wall at dusk"),
     (254, "Wait. Let Hayabusa come to you")])

passage(251,
    "The salt-gate is a low water-tunnel where the lake feeds beneath "
    "the keep. Kiri (or you, if you came alone) knows the way. You "
    "wait until the moon is hidden behind the keep, then wade in to "
    "the chest, then to the shoulders, then under.\n\n"
    "Inside the salt-gate, the air is foul and cold. You climb a "
    "set of slick stone steps. You emerge in a cellar full of empty "
    "lacquer barrels. From above, you hear chanting.",
    [(270, "Climb toward the chanting")])

passage(252,
    "You walk the long causeway openly at dawn, robes belted, "
    "wakizashi shouldered, your token visible at your belt. You "
    "look like exactly what you are: a young samurai monk who has "
    "come to call upon the lord of Black Crow Castle.\n\n"
    "The gate-guards are not surprised. They have been told to "
    "expect you. They escort you inside with elaborate courtesy.\n\n"
    "Hayabusa Mōri receives you in the keep's great hall, alone, "
    "the Yasha-no-Tachi laid across his knees in its plain wooden "
    "scabbard. His moon-scar catches the lantern light.\n\n"
    "\"Takeshi-san. Akiyama's last. Sit. We have so much to discuss "
    "before the moon rises.\"",
    [(280, "Sit before Hayabusa Mōri")])

passage(253,
    "You storm the wall at dusk with Tetsu's old soldiers (he has, "
    "miraculously, raised forty men from his old regiment in three "
    "days — \"They owed me, monk-boy. They owe me less now\"). The "
    "outer wall falls in a quarter hour. The inner keep does not.\n\n"
    "By full dark the courtyard is a mess of bodies, and your "
    "companions are pinned at the inner gate by archers. You see "
    "Hayabusa's banner go up on the keep's roof. Time is gone.",
    [(265, "Press the inner gate alone"),
     (266, "Hold the courtyard with your friends and wait for daylight")])

passage(254,
    "You make camp at the lake's southern edge and wait. Your "
    "companions are uneasy. Tetsu drinks. Kiri sharpens a knife "
    "she has already sharpened.\n\n"
    "On the second night, Hayabusa comes down from the keep alone. "
    "He stands on the causeway under the half-moon, the Yasha-no-"
    "Tachi at his hip, and he calls your name across the salt.\n\n"
    "\"Takeshi-san. Akiyama's last. Will you not at least come "
    "speak with me before we kill each other?\"",
    [(280, "Walk out onto the causeway alone")])

passage(260,
    "You arrive at Black Crow on the seventh day, alone, with no "
    "wind in you and a broken sword-tang at your belt. You walk the "
    "causeway openly because you have no other plan. The guards do "
    "not even stop you. They escort you inside, smiling.\n\n"
    "Hayabusa Mōri receives you in the great hall, alone, the "
    "Yasha-no-Tachi across his knees.\n\n"
    "\"Takeshi-san,\" he murmurs. \"Akiyama's last. So thin. So "
    "tired. So *alone*. Sit.\"\n\n"
    "He smiles, kindly. His moon-scar twists. \"I have been hoping "
    "you would come alone. Sit.\"",
    [(281, "Sit with him alone, three winds short")])


# ---------------------------------------------------------------------------
# CHAPTER 6 — INSIDE BLACK CROW
# ---------------------------------------------------------------------------

passage(265,
    "You leave Tetsu and Kiri at the gate and slip through the "
    "lower courtyard alone. Two soldiers see you and die for it. "
    "You climb the kitchen stairs, then the inner stairs, then the "
    "stairs to the high hall — and there, with the moon coming up "
    "behind him through a paper screen, Hayabusa Mōri waits.",
    [(280, "Face him alone")])

passage(266,
    "You hold the courtyard. Tetsu's old soldiers fight magnificently "
    "but die one by one. By midnight, the courtyard is yours but "
    "you have lost thirty men. Tetsu is gut-wounded and grey. Kiri "
    "is bleeding from a shoulder. Genshin's Fire in you is the only "
    "thing holding the line.\n\n"
    "On the keep's roof, Hayabusa's banner has been replaced by a "
    "long crimson one, and a long, slow chanting has begun. The "
    "full moon is climbing.",
    [(267, "Charge the keep door alone before the moon clears the keep"),
     (268, "Stay with your wounded and finish this in the morning")])

passage(267,
    "You leave them. You sprint across the courtyard, up the keep "
    "steps, through the broken inner door. Hayabusa is in the high "
    "chamber with the Yasha-no-Tachi unsheathed, surrounded by "
    "candles. He turns as you enter.\n\n"
    "He is older than you expected. His moon-scar is real. His eyes "
    "are not the demon's; the demon is in the blade, not yet in "
    "him. He has been *waiting* — not for the moon, but for you.",
    [(280, "Face him")])

passage(268,
    "You stay. You hold your wounded. You wait for daylight. By "
    "dawn the chanting on the roof has finished, and a long, low "
    "horn has sounded over the salt lake, and Hayabusa Mōri walks "
    "down out of the keep alone with the Yasha-no-Tachi bare in "
    "his hand.\n\n"
    "He is no longer entirely Hayabusa. The demon has come most of "
    "the way out. His shadow on the stones is wrong, taller than it "
    "should be.\n\n"
    "Your companions cannot help you now.",
    [(283, "Step out alone to meet him at dawn")])

passage(270,
    "You climb. The chanting grows louder. You emerge in a "
    "storeroom behind a great curtain. Through the curtain you see "
    "the inner hall — and at its centre, Hayabusa Mōri kneels "
    "before a forge that has been re-lit for the first time in "
    "centuries. The Yasha-no-Tachi lies on the anvil before him. He "
    "is alone. The moon is not yet full but it is close.",
    [(271, "Strike from behind the curtain"),
     (272, "Step out and call his name"),
     (273, "Wait — and sing the Water-mantra from cover")])


# ---------------------------------------------------------------------------
# CHAPTER 7 — CONFRONTATION
# ---------------------------------------------------------------------------

passage(271,
    "You step through the curtain. Hayabusa does not turn. You raise "
    "your sword. You take three steps. Your blade is high. He does "
    "not turn.\n\n"
    "And then, at the last possible instant, he does — and his cut "
    "comes from below, faster than your eye can follow.\n\n"
    "But Genshin's Fire-posture moves in you without your asking, "
    "and your body falls half an inch lower than it should — and his "
    "cut takes only the edge of your sleeve.",
    [(290, "Press the fight")])

passage(272,
    "\"Hayabusa!\" you call. He looks up. The moon-scar twists.\n\n"
    "\"Takeshi. Akiyama's last. Come, then. Come into the light "
    "where I can see you.\"\n\n"
    "He rises. He lifts the Yasha-no-Tachi from the anvil. The blade "
    "is bare. It does not catch the lantern-light properly — it "
    "*swallows* the lantern-light.\n\n"
    "\"Speak, boy. Then we fight.\"",
    [(291, "Demand he surrender the blade"),
     (292, "Ask him why he killed your master"),
     (293, "Begin the Water-mantra")])

passage(273,
    "You stay behind the curtain. You begin, very softly, the song. "
    "The Water-mantra. It is a song no one has sung in this hall in "
    "five hundred years, and the moment the first note leaves your "
    "throat, the Yasha-no-Tachi on the anvil rings like a struck "
    "bell.\n\n"
    "Hayabusa rises. He turns, slowly. He cannot see you. He listens.\n\n"
    "His expression is — strangely — not anger. It is *grief*.",
    [(294, "Step out as you sing")])

passage(280,
    "Hayabusa Mōri waits. He is taller than you expected, and "
    "thinner, and old. His face would once have been handsome. The "
    "moon-shaped scar over his right eye is fresh — fresher than "
    "thirty years would suggest. The Yasha-no-Tachi rests across "
    "his knees.\n\n"
    "\"Sit, boy of Akiyama. Before we draw, let us at least speak.\"",
    [(295, "Sit and speak")])

passage(281,
    "You sit. Hayabusa pours you tea from a black iron pot. His "
    "hands are old. His eyes are the eyes of a man who has been "
    "drowning for thirty years.\n\n"
    "\"You came alone, Takeshi-san. Why?\"\n\n"
    "You have no winds. You have no allies. You have only your "
    "rage, and the broken sword-tang of Kōgetsumaru at your belt.",
    [(282, "Accuse him"),
     (284, "Try to listen"),
     (285, "Strike him across the table")])

passage(282,
    "\"You killed my master.\"\n\n"
    "He inclines his head. \"I did. He died well. He died trying to "
    "seal me again, as he sealed me thirty years ago. He did not "
    "succeed. I am sorry, Takeshi-san. He was my brother once.\"\n\n"
    "He sets the cup down. \"You have come without your three "
    "winds. That means you must mean to die here. Very well. Drink "
    "the tea first. Akiyama would have wanted you to be polite.\"",
    [(285, "Strike him across the table"),
     (286, "Drink the tea first")])

passage(283,
    "You walk out into the courtyard at dawn. The salt lake is "
    "still. Hayabusa Mōri stands ten paces away — and a black thing "
    "stands behind him, taller than the keep, made of shadow. You "
    "can barely look at it.\n\n"
    "The demon has very nearly walked. You are very nearly alone "
    "against a god.\n\n"
    "You have Fire, you have Water, you have Earth, but you do not "
    "have your friends, and you are tired beyond tired. You will "
    "die here. The only question is what you do before you do.",
    [(287, "Sing all three winds at once and strike"),
     (288, "Drop your sword and walk forward unarmed")])

passage(284,
    "You take a slow breath. You bow, fractionally. \"I am here. "
    "I will listen.\"\n\n"
    "Hayabusa is silent a long time. Then, quietly:\n\n"
    "\"I have carried the Yasha-no-Tachi for thirty years, Takeshi-"
    "san. Thirty years. There is very little of me left. Tomorrow "
    "night, on the full moon, the blade will be re-forged in this "
    "hall, and what is left of me will be eaten. After that — there "
    "will only be the *yasha*. I had hoped Akiyama would come "
    "himself. I had not hoped to be — caught — by his last student. "
    "You are very young.\"\n\n"
    "He smiles, faintly. \"There is one thing, perhaps, you can do. "
    "But you are alone, boy, and the thing requires four winds, not "
    "three, and the fourth wind I cannot give you.\"",
    [(289, "Ask what the fourth wind is")])

passage(285,
    "You strike. The cut of the willow rises in you. You take the "
    "tea-pot, the table, and a chunk of Hayabusa's robe — but his "
    "old hand has come up faster than any old hand should, and the "
    "Yasha-no-Tachi is bare between you before your blade has "
    "completed its arc.\n\n"
    "The hall lights itself up. He is on his feet. You are on yours. "
    "And the demon in the blade is *delighted*.",
    [(290, "Press the fight")])

passage(286,
    "You drink. The tea is bitter. The hall is very still.\n\n"
    "When you set the cup down, Hayabusa stands. \"Now we fight, "
    "Takeshi-san. I am sorry. The blade will not let me let you "
    "live.\"\n\n"
    "He draws.",
    [(290, "Draw and fight")])

passage(287,
    "You begin the song. The Water-mantra rises out of you, "
    "thinning, into the still salt air. You hold the Fire-posture. "
    "You set your feet for Earth.\n\n"
    "Hayabusa lifts the Yasha-no-Tachi. He looks at you with "
    "something that might be pity. The black shadow behind him "
    "raises an arm taller than the keep.\n\n"
    "Your three winds are good. They are *very* good. But you are "
    "one body, and you are tired, and the demon has nearly walked, "
    "and the song falters on its second verse because you have "
    "nothing left to give it.\n\n"
    "The shadow falls on you. The Fire goes out. The Water dries. "
    "The Earth lets go. Hayabusa, the last of him still in there "
    "somewhere, weeps.",
    None)
P[287]["ending"] = "bad"
P[287]["title"] = "Three Winds, One Body"

passage(288,
    "You drop your sword. You walk forward unarmed. Hayabusa stares. "
    "The shadow behind him pauses.\n\n"
    "\"What are you *doing*, boy?\" Hayabusa whispers.\n\n"
    "You walk all the way to him. You touch his moon-scar with two "
    "fingers, very gently. The shadow flinches.\n\n"
    "And you sing. Water. You hold the Fire. You set your feet for "
    "Earth. And you do something the master never taught you, "
    "because the master did not know it could be done — you give "
    "the song to Hayabusa. You sing it *into him*, the way the old "
    "maiden sang it into her daughter.\n\n"
    "He stiffens. He drops the blade. He drops to his knees. The "
    "shadow behind him *thins*, like smoke in wind, and is gone.",
    [(300, "Stand with him as he weeps")])

passage(289,
    "\"The fourth wind,\" Hayabusa says, very softly, \"is mercy. "
    "An act of forgiveness from the one who has every right to "
    "withhold it. A choice. Akiyama would have given it to me, I "
    "think. But he is dead, and you are not him, Takeshi-san. You "
    "are young, and your grief is fresh.\n\n"
    "\"I do not ask it of you. I tell you only that without it, "
    "the sealing tomorrow will fail at its last step, and the "
    "blade will eat us both.\"",
    [(310, "Take the night to think about it")])

passage(290,
    "Hayabusa Mōri is the swordsman your master told you he was. "
    "His cuts come from places yours has never been. He moves "
    "around his own age and stiffness with a kind of contemptuous "
    "grace. The Yasha-no-Tachi sings in his hand and the demon in "
    "the blade *helps* him.\n\n"
    "But Genshin's Fire is in you, and the Water-mantra is in your "
    "throat, and Tetsu's Earth is under your feet. You are one "
    "young body holding three impossible winds. You will not last "
    "long. You may last long enough.",
    [(311, "Sing the Water-mantra as you fight"),
     (312, "Drop the song; fight for blood; trust your sword"),
     (313, "Try to disarm him rather than kill")])

passage(291,
    "\"Surrender the blade, Hayabusa. Lay it on the stone. We can "
    "yet seal it. My master's three winds are with me.\"\n\n"
    "His eyes are very, very tired. \"Three winds, Takeshi-san. "
    "There are four. Akiyama did not tell you the fourth, because "
    "he could not give it to you. He could only ask it of you.\"\n\n"
    "He lifts the Yasha-no-Tachi. \"And you have not learned to "
    "give it yet. Come, boy. Let us at least finish the form your "
    "master taught us both.\"",
    [(290, "Fight him")])

passage(292,
    "\"Why did you kill him?\"\n\n"
    "Hayabusa's smile is very small. \"Because he was the only "
    "person alive who could put me back in the box. Because the "
    "thing in this blade does not allow witnesses. Because I have "
    "not had a free thought in nineteen years, Takeshi-san, and I "
    "did not know what the blade would have me do until I had "
    "already done it.\"\n\n"
    "He rises. The Yasha-no-Tachi rises with him. \"I would say I "
    "am sorry, but the blade would laugh.\"",
    [(290, "Fight")])

passage(293,
    "You begin the song. The Water-mantra rises in the inner hall. "
    "Hayabusa staggers — a single step. The Yasha-no-Tachi rings, "
    "low and slow, like a struck bell at the bottom of a well.\n\n"
    "Hayabusa lifts the blade. His eyes are wet. \"Akiyama always "
    "could pick them, the *brilliant* old bastard. Boy — you are "
    "ten years younger than I was when I lost myself. Be a great "
    "deal more careful than I was. Now sing, and fight me, and let "
    "us see what your three winds and my thirty years come to.\"",
    [(290, "Fight while singing")])

passage(294,
    "You step out, still singing. Hayabusa stares — at first in "
    "disbelief, then in something more complicated. The Yasha-no-"
    "Tachi shrieks in his hand. His grip whitens on it.\n\n"
    "\"Boy of Akiyama,\" he says hoarsely, \"do you know what you "
    "are *doing*?\"",
    [(295, "Keep singing; walk toward him as you sing")])

passage(295,
    "You sit, opposite Hayabusa, in the great hall of Black Crow "
    "Castle. The Yasha-no-Tachi sits between you. He pours you tea "
    "from a black iron pot. His hand is old and steady.\n\n"
    "\"Akiyama always brewed it too long,\" Hayabusa murmurs. \"I "
    "have not improved on him. Drink, boy. Then tell me which of "
    "the three winds you carry tonight, and which you do not, "
    "and I will tell you whether your odds are stupid, very "
    "stupid, or merely poor.\"",
    [(296, "Tell him honestly which winds you have")])

passage(296,
    "You tell him. He listens. When you have finished, he closes "
    "his eyes a long moment.\n\n"
    "\"All three. Good. He found his three winds. He always did.\"\n\n"
    "He opens his eyes. \"Then I will not insult you with a "
    "warning, Takeshi-san. I will only tell you this: a sealing of "
    "the *blade* alone requires Fire, Water, and Earth, and ends "
    "with the blade returned to the floor of Tōkin-ji for "
    "another thirty years. A sealing of the *blade and the man* "
    "requires a fourth wind, which I cannot give you and which "
    "your master could not teach you. Choose now, before we "
    "fight, which sealing you intend. Once we draw, you will not "
    "have the breath to choose.\"",
    [(297, "Choose to seal only the blade"),
     (298, "Choose to seal blade and man — even without knowing what the fourth wind is")])

passage(297,
    "\"The blade,\" you say. \"I will seal the blade. The man — \"\n\n"
    "He nods. \"The man you will kill. Of course. Akiyama's last. "
    "I would have chosen the same at your age.\"\n\n"
    "He stands. The Yasha-no-Tachi rises with him. \"Then let us "
    "be done, Takeshi-san. Begin your song.\"",
    [(290, "Fight to seal the blade and kill the man")])

passage(298,
    "\"Both,\" you say. \"I do not know the fourth wind. I will "
    "find it as we fight, or I will die without it. But I will "
    "try.\"\n\n"
    "Hayabusa looks at you a long, strange moment. Then he bows. "
    "It is the deepest bow he has given anything in twenty years.\n\n"
    "\"Then, Takeshi-san, in this room tonight, I will fight you "
    "with everything I am. And the *yasha* in this blade will "
    "fight you with everything *it* is. And I pray, in whatever "
    "small place is left of me, that you find the fourth wind "
    "before the third one fails. Begin.\"",
    [(330, "Begin the great fight")])

passage(300,
    "Hayabusa kneels on the stones of the great hall. The Yasha-no-"
    "Tachi lies between you. He weeps the way men weep who have not "
    "been allowed to weep in a very long time — silently, and "
    "without dignity, and with relief.\n\n"
    "He looks up. His eyes are his own.\n\n"
    "\"Boy,\" he whispers. \"Akiyama's last. Thank you.\"",
    [(350, "Walk with him to the forge")])


# ---------------------------------------------------------------------------
# CHAPTER 7b — THE GREAT FIGHT
# ---------------------------------------------------------------------------

passage(310,
    "You sit through the night in the great hall. Hayabusa does not "
    "rise to attack. The Yasha-no-Tachi rests across his knees, "
    "occasionally ringing softly, like a struck bowl.\n\n"
    "You think about the fourth wind. You think about your master "
    "on the prayer stone. You think about little Jirō under the "
    "beam. You think about the woman you walked, or did not walk, "
    "to the tea-house.\n\n"
    "By dawn you have either understood mercy or you have not. "
    "There is no test for it but the next hour.",
    [(298, "Choose to seal blade and man, when the moon rises")])

passage(311,
    "You sing as you fight. The Water-mantra threads under your "
    "breath. The Yasha-no-Tachi shrieks every time it hits your "
    "blade — the demon in it is howling — and Hayabusa flinches "
    "minutely with each note, because the part of him that is "
    "still Hayabusa is *grateful*.\n\n"
    "You fight for what feels like an hour. It is perhaps four "
    "minutes. You take a cut along your ribs. You take a cut "
    "across your sword-hand. The song never leaves you.\n\n"
    "On the fifth minute Hayabusa's grip slips for half a "
    "heartbeat — and you see it, and the Earth-stance rises in "
    "you, and you make your last decision.",
    [(312, "Strike to kill"),
     (313, "Strike to disarm"),
     (320, "Sing louder; do not strike at all")])

passage(312,
    "You strike to kill. The cut of the falling pine. Your blade "
    "takes Hayabusa Mōri high in the chest.\n\n"
    "He sinks. The Yasha-no-Tachi falls from his hand and clangs on "
    "the stones, ringing.\n\n"
    "He looks up at you. He smiles, weakly. \"Thank you, Takeshi-"
    "san. Tell Genshin... tell Genshin he never could brew tea "
    "either.\"\n\n"
    "He dies on the stones of Black Crow Castle. The blade lies at "
    "your feet. It is still ringing. The demon is in it. The demon "
    "is not gone.",
    [(360, "Decide what to do with the blade")])

passage(313,
    "You strike to disarm. The cut of the willow, the cut your "
    "master taught you on a wet morning when you were nine years "
    "old. Your blade takes the Yasha-no-Tachi at the guard. The "
    "guard splits. The grip falls from Hayabusa's hand.\n\n"
    "The blade clangs to the stones. The demon in it shrieks. "
    "Hayabusa drops to one knee.\n\n"
    "\"Now, boy,\" he gasps. \"Sing the song. *Sing it now.* I "
    "will hold him back as long as I can.\"",
    [(320, "Sing the full sealing")])

passage(320,
    "You sing. Water under your breath. Fire in your sternum. Earth "
    "in your feet. You walk toward the fallen Yasha-no-Tachi. "
    "Hayabusa kneels on the stones, head bowed, holding back the "
    "thing in the blade by sheer will.\n\n"
    "Three winds. The blade rings, and rings, and *rings*.\n\n"
    "But three winds are not enough.\n\n"
    "The demon in the Yasha-no-Tachi rises out of the blade like "
    "steam. It has a face. The face is sorrow, not anger.\n\n"
    "You have a choice to make in the next heartbeat.",
    [(321, "Drive the blade through its own iron — break it"),
     (322, "Forgive Hayabusa aloud — give the fourth wind"),
     (323, "Take up the Yasha-no-Tachi yourself and finish the demon with its own steel")])

passage(321,
    "You raise your wakizashi. You bring it down on the Yasha-no-"
    "Tachi where it lies on the stones. The blade *splinters* — "
    "and the demon-steam screams as the iron snaps.\n\n"
    "The hall darkens. The Fire goes out. The Water dries. The "
    "Earth lets go. The demon, freed from its prison, *vanishes* "
    "into the stones — not destroyed, only loose. It will find "
    "another blade. It will find another fool. It will be back in "
    "a hundred years, or two hundred, or three.\n\n"
    "Hayabusa is dead on the stones — the demon took him on its "
    "way out. You stand alone in the hall holding two pieces of a "
    "broken sword.\n\n"
    "You walk out of Black Crow Castle a free man. The country is "
    "safe for two centuries. The blade you carried did its work. "
    "But somewhere, you know, a child is being born who will one "
    "day pick up another piece of iron and let the thing back in.\n\n"
    "You become a teacher. You teach for forty years. You die "
    "old, well loved, in a small temple by the sea. And every "
    "time the wind picks up at night, you remember the demon's "
    "face — sorrow, not anger — and you do not sleep until dawn.",
    None)
P[321]["ending"] = "good"
P[321]["title"] = "The Sword That Broke"

passage(322,
    "You stop. You drop to one knee beside Hayabusa Mōri. The "
    "demon-steam pauses, watching. The Fire holds. The Water "
    "holds. The Earth holds.\n\n"
    "You lay your hand on Hayabusa's bowed head. You speak — not "
    "loud, not for the hall, only for him.\n\n"
    "\"I forgive you,\" you say. \"For my master. For the temple. "
    "For everything. You were not free. I forgive you, brother of "
    "the Way.\"\n\n"
    "The fourth wind comes — not from the air, not from a "
    "teacher, but from inside you. Where there was only rage, "
    "there is now also pity. Where there was only grief, there "
    "is now also recognition.\n\n"
    "Hayabusa weeps. The demon-steam *changes*. Its face is "
    "still sorrow. But its sorrow now has somewhere to go.\n\n"
    "The four winds together speak the True Sealing. The demon "
    "is bound — not into another blade, not into the stones, but "
    "into a tiny, stoppered jar that has appeared, somehow, in "
    "your hand. The jar is no bigger than a child's fist. It is "
    "sealed with three brushstrokes.\n\n"
    "You stand. Hayabusa stands beside you. The Yasha-no-Tachi "
    "lies at your feet — an empty piece of iron now, no more "
    "alive than the floor.",
    [(390, "Walk out of Black Crow Castle with Hayabusa beside you")])

passage(323,
    "You drop your wakizashi. You bend and pick up the Yasha-no-"
    "Tachi.\n\n"
    "The moment the grip is in your palm, you know your mistake.\n\n"
    "The demon-steam pours back down into the blade. The blade "
    "warms in your hand — warmer than any blade should be. It "
    "fits your grip too well. It fits your *anger* too well. The "
    "Fire goes out. The Water dries. The Earth lets go. The "
    "winds were never in you, only beside you, and now you are "
    "alone with the blade.\n\n"
    "Hayabusa looks up. His face is grey. \"Boy,\" he whispers. "
    "\"Oh, *boy*. Put it down. Put it down. Put — \"\n\n"
    "You cut his head from his shoulders with the cut of the "
    "falling pine.\n\n"
    "The Yasha-no-Tachi sings, contented, in your hand.",
    [(398, "Walk out of Black Crow Castle a new lord")])


# ---------------------------------------------------------------------------
# CHAPTER 8 — THE GREAT FIGHT (full path)
# ---------------------------------------------------------------------------

passage(330,
    "Hayabusa rises. He bows. He draws the Yasha-no-Tachi.\n\n"
    "What follows is not a fight as you have been taught to fight. "
    "It is not a fight as he was taught to fight. It is two human "
    "beings holding back, between them, a thing older than the "
    "country — and one of them is half-eaten by the thing already.\n\n"
    "He cuts. You parry. The Water-mantra rises from your throat. "
    "He flinches. He cuts again. The Fire holds in your sternum. "
    "He laughs — and it is partly his laugh, and partly the demon's.\n\n"
    "For long minutes you are matched. The cut of the willow, the "
    "cut of the river, the cut of the falling pine. He knows them "
    "all — your master taught them to him forty years before he "
    "taught them to you.",
    [(331, "Hold; sing; wait for an opening to give the fourth wind")])

passage(331,
    "You hold. You sing. You wait.\n\n"
    "The opening comes — not because Hayabusa weakens, but "
    "because the demon, hating the song, *forces* him to overreach. "
    "His cut goes wide. Your blade is at his throat. He stops, "
    "frozen, breath caught.\n\n"
    "The hall is silent except for the song.\n\n"
    "You lower your blade. You drop it to the stones.\n\n"
    "You step forward. You take Hayabusa's old, scarred face in "
    "both your hands. You look him in the eye. The demon roars in "
    "the blade. The blade *trembles* in his grip.\n\n"
    "And you say, very quietly, what you came across half a "
    "country to learn how to say.\n\n"
    "\"I forgive you.\"",
    [(322, "Speak the fourth wind")])

passage(350,
    "You walk with Hayabusa to the forge. He does not speak. He "
    "carries the Yasha-no-Tachi like a man carrying his own coffin.\n\n"
    "At the forge, he sets the blade on the cold anvil. He turns "
    "to you.\n\n"
    "\"Now,\" he whispers, \"the True Sealing. All four winds. "
    "Fire. Water. Earth. And the fourth, that you have already "
    "given. Sing, Takeshi-san. Hold the posture. Set your feet. "
    "And do not — *do not* — pity me when the last word falls.\"",
    [(391, "Sing the True Sealing")])


# ---------------------------------------------------------------------------
# CHAPTER 9 — AFTER THE BLADE
# ---------------------------------------------------------------------------

passage(360,
    "The Yasha-no-Tachi lies on the stones. The demon is in it. "
    "Hayabusa is dead. The hall is yours. The moon is rising "
    "outside.\n\n"
    "You have four choices and only one of them is wise.",
    [(361, "Take the Yasha-no-Tachi back to Tōkin-ji for re-sealing"),
     (362, "Drive your wakizashi through the Yasha-no-Tachi and break it"),
     (363, "Carry the Yasha-no-Tachi to the salt lake and drop it in the deep water"),
     (364, "Take up the Yasha-no-Tachi yourself")])

passage(361,
    "You wrap the blade in a black cloth. You ride south. You "
    "ride for four days, eating little, sleeping less. You reach "
    "Tōkin-ji at dusk on the fifth day. The temple is a ruin. "
    "Your master's cairn still stands by the prayer stone.\n\n"
    "You re-bury the Yasha-no-Tachi under the prayer floor. You "
    "speak the three winds as best you can alone. You set "
    "Kōgetsumaru — what is left of it — over the spot, point "
    "downward, the old way.\n\n"
    "It is not a perfect sealing. Genshin would have rolled his "
    "eye at you. But it is a sealing, and it will hold.\n\n"
    "You stay at Tōkin-ji. You rebuild it, year by year. The "
    "children come back. The bell rings. The demon sleeps under "
    "your feet, and you remember it every day, and every day you "
    "do not take up the blade. That is your work. That is "
    "enough.",
    None)
P[361]["ending"] = "good"
P[361]["title"] = "The Long Watch"

passage(362,
    "You raise your wakizashi. You bring it down on the Yasha-no-"
    "Tachi. The blade *splinters* — and the demon-steam screams "
    "as the iron snaps.\n\n"
    "The demon is loose. It will find another blade. It will find "
    "another fool. It will be back in a hundred years.\n\n"
    "But not in *your* hundred years.\n\n"
    "You walk out of Black Crow a free man. The country is safe "
    "for two centuries. You become a teacher. You teach for forty "
    "years. You die old, well loved, in a small temple by the "
    "sea.",
    None)
P[362]["ending"] = "good"
P[362]["title"] = "The Snapped Blade"

passage(363,
    "You carry the Yasha-no-Tachi down to the salt lake. You wade "
    "in to the chest. You sink the blade into the black water and "
    "let it go.\n\n"
    "It is gone. The lake is deep. The lake is cold. No one will "
    "find it for a thousand years.\n\n"
    "But the lake is not nothing, and the demon is not bound — "
    "only hidden. In ninety years, when the salt lake dries in a "
    "drought, a small boy will find a black-iron sword half-"
    "buried in the cracked silt, and he will take it home, and he "
    "will be very, very excited about his find.\n\n"
    "You will not be alive to see this. But it will happen.",
    None)
P[363]["ending"] = "ok"
P[363]["title"] = "The Sword Beneath the Salt"

passage(364,
    "You bend and pick up the Yasha-no-Tachi. The moment the grip "
    "is in your palm, you know your mistake.\n\n"
    "The blade warms. It fits. It fits *terribly* well.\n\n"
    "You walk out of Black Crow Castle a new lord. The first "
    "village burns three days later. By the end of the year you "
    "rule six provinces. By the end of the second year, ten. The "
    "country calls you the Crimson Lord. The country calls you "
    "many things. None of them are *Takeshi*.\n\n"
    "Somewhere inside the blade, the small bright thing that "
    "used to be a temple-orphan named Takeshi flickers, "
    "occasionally — and is fed back to the demon, and goes "
    "quiet, and is fed back, and goes quiet.\n\n"
    "The country burns for a hundred years.",
    None)
P[364]["ending"] = "horrible"
P[364]["title"] = "The Crimson Lord"


# ---------------------------------------------------------------------------
# ENDINGS — terminal passages
# ---------------------------------------------------------------------------

passage(390,
    "You walk out of Black Crow Castle into a grey dawn. Hayabusa "
    "Mōri walks beside you, head bowed, holding the empty iron "
    "that used to be the Yasha-no-Tachi.\n\n"
    "At the causeway he stops. He turns to you. He bows — the "
    "deepest bow you have ever received.\n\n"
    "\"Akiyama's last,\" he says. \"You did what I could not. You "
    "did what Akiyama could not. You gave the fourth wind.\"\n\n"
    "He hands you the empty iron. He hands you the small "
    "stoppered jar.\n\n"
    "\"I will see to my men,\" he says. \"They are not bad men. "
    "They were ill-led. I will give them back their honour, and "
    "I will make this fortress a hospice, and I will spend the "
    "rest of my days here trying to be something other than what "
    "the blade made me. Will you come visit, one day?\"\n\n"
    "You will.\n\n"
    "You ride south with Kiri, with Tetsu, with Ayane — with all "
    "the friends the road gave you. The empty iron you leave at "
    "Tōkin-ji. The stoppered jar you bury beneath the prayer "
    "stone, beside your master.\n\n"
    "You marry one of the friends the road gave you, or perhaps "
    "you do not marry at all — the small life suits you. You "
    "rebuild the monastery. You teach. The bell rings again. "
    "Children come back. Genshin lives another twenty years, "
    "smoking too much. Hayabusa, in his hospice, lives twenty-"
    "two; he becomes, in his quiet way, the gentlest old man "
    "anyone in his province has ever met. He sends you letters. "
    "You keep them.\n\n"
    "The country has peace for a thousand years. The blade is "
    "iron. The demon is in a jar. You did the impossible thing. "
    "You did it because you were able, at the last possible "
    "moment, to forgive.\n\n"
    "Your master, in whatever place masters go, would be proud.",
    None)
P[390]["ending"] = "best"
P[390]["title"] = "The Fourth Wind"

passage(391,
    "You sing. Fire in your sternum. Water in your throat. Earth "
    "in your feet. And mercy, the fourth wind, in the hand you "
    "have laid on Hayabusa Mōri's shoulder.\n\n"
    "The True Sealing falls. The demon comes out of the iron in "
    "a long, slow exhalation. It does not howl. It does not "
    "rage. It looks at you — its face is sorrow, not anger — and "
    "it bows. Then it is in the small stoppered jar in your "
    "hand, and the jar seals itself with three brushstrokes.\n\n"
    "Hayabusa drops to his knees. He weeps. After a long time he "
    "looks up at you with eyes that are entirely his own.",
    [(390, "Walk out with him")])

passage(398,
    "You walk out of Black Crow Castle into a grey dawn. The "
    "Yasha-no-Tachi is at your hip. It is warmer than it should "
    "be. It is happier than it should be.\n\n"
    "Behind you, in the great hall, Hayabusa Mōri lies dead. So "
    "does your master's three-brush token, which you have "
    "dropped on the stones and not picked up.\n\n"
    "The first village burns three days later. By the end of "
    "the year you rule six provinces. The country calls you "
    "the Crimson Lord. The country calls you many things.\n\n"
    "None of them are *Takeshi*.\n\n"
    "The country burns for a hundred years.",
    None)
P[398]["ending"] = "horrible"
P[398]["title"] = "The Crimson Lord Rises"

passage(399,
    "You laugh — once, low. Then you sheathe your sword. You "
    "bow, to the empty hall, to the dead man on the stones, to "
    "your master a thousand miles away. You walk out of Black "
    "Crow Castle alone. The country has its peace, of a sort. "
    "You will never quite have yours.",
    None)
P[399]["ending"] = "ok"
P[399]["title"] = "The Walk Away"

# Make sure ending markers exist where we set them late
for pid in (120, 129, 197, 198, 202, 221, 287, 321, 322, 323, 361, 362, 363, 364, 390, 391, 398, 399):
    if pid in P and P[pid]["ending"] is None:
        # safety: any forgotten endings get a generic "bad"
        P[pid]["ending"] = "bad"


# ---------------------------------------------------------------------------
# CHAPTER 2c-continued — inn fights and side-paths
# ---------------------------------------------------------------------------

passage(186,
    "You drop. Twenty feet of wet thatch, then earth. You land on the "
    "burn-scarred captain's shoulders. His sword clatters on the "
    "stones. He goes down hard, you go down harder.\n\n"
    "Three soldiers scatter, then close. One of them dies on your "
    "wakizashi before you have entirely stood up. The captain, "
    "winded but alive, scrambles for his blade.",
    [(190, "Fight them all")])

passage(187,
    "You move along the wet thatch from roof to roof. Three roofs over, "
    "the alley falls away below you and there is a stable yard, and a "
    "horse, and you take it without permission and ride north into the "
    "dark.\n\n"
    "By dawn you are six ri up the road, alone, with no companions and "
    "no winds and an aching back. The captain at the inn does not "
    "follow you. The captain at the inn has other orders.\n\n"
    "A day later, on a stretch of road through bamboo, a single rider "
    "in plain travelling clothes overtakes you. \"You ride very loud, "
    "samurai,\" she murmurs. \"Slow down. I am Kiri of the Hollow "
    "Reed, and your master has been dead three days, and your road "
    "from here is not alone.\"",
    [(180, "Travel with her")])

passage(188,
    "You attack. The captain rises with a curse and meets you with "
    "his short-sword. The first two soldiers come in at your flanks. "
    "You take the left one with a thrust under the ribs. The right "
    "one's blade catches your shoulder; the pain is sharp and "
    "useful.",
    [(190, "Fight them all")])

passage(189,
    "You hold your sword low. \"Captain. I have buried my master "
    "today. I have no quarrel with you. Let me walk past your town "
    "and you will never see my face again.\"\n\n"
    "He smiles, slowly. \"Boy. *I* have no quarrel with you. But "
    "Hayabusa-sama gave a standing order. No witness from Tōkin-ji "
    "is to walk past Karasu-juku alive.\"\n\n"
    "He raises his hand. The soldiers step forward.",
    [(190, "Fight")])

passage(190,
    "You are one young samurai-monk in an inn full of soldiers.\n\n"
    "Cut of the willow. The first man falls.\n\n"
    "Cut of the river. The second man falls.\n\n"
    "Cut of the falling pine. The captain — burn-scarred, faster than "
    "his face suggests — meets your blade with his own. Steel on steel "
    "in the lantern-light. The other soldiers circle.\n\n"
    "You take a cut along your thigh. You take a cut across your "
    "forearm. The lantern goes out. The inn is in darkness — and in "
    "the darkness your master's first lesson is louder than your fear.",
    [(230, "Press the fight in the dark"),
     (231, "Break for the door"),
     (232, "Drop low and roll for the back stairs")])

passage(230,
    "In the dark, your sword finds throats by memory and by sound. "
    "You take the captain in the chest. You take a soldier in the "
    "neck. A blade scores your back. You turn, and turn, and turn — "
    "and at last you are alone, gasping, in a room of dead men.\n\n"
    "You stagger out into the rain. The inn is silent behind you. "
    "You have killed five men in less than a minute and you are "
    "bleeding from four places.\n\n"
    "Two streets over, in a back-room of the larger inn, two "
    "travellers are still waiting for you.",
    [(141, "Find them")])

passage(231,
    "You break for the door. A spear opens your thigh. You crash "
    "out into the inn-yard, bleeding badly, and run.\n\n"
    "You make it to a dark alley, two streets over, before your leg "
    "gives out. You collapse against a barrel. Footsteps approach.\n\n"
    "The footsteps belong to a tall woman with grey at her temples "
    "and a longbow over her shoulder. \"There you are, Takeshi-san. "
    "Genshin said you would arrive bleeding. He owes me a coin.\"",
    [(141, "Be carried to the back room")])

passage(232,
    "You drop. You roll. The back-stair curtain is two body-lengths "
    "away. You make it. You half-fall, half-run down the stair into "
    "the kitchen.\n\n"
    "The cook — a thin woman with a scar on her lip — meets you with "
    "a butcher's knife held very calmly. Her eyes go to the three-"
    "brushstroke token at your belt.\n\n"
    "\"Out the back,\" she says quietly. \"The grey-haired one is "
    "waiting in the alley.\" She tucks the knife back into her belt. "
    "\"Move, samurai. They will be down in a heartbeat.\"",
    [(141, "Go out the back")])


# ---------------------------------------------------------------------------
# CHAPTER 2d — the tide-shrine of Mikuriya (alt path)
# ---------------------------------------------------------------------------
# Side-arc reached when Ayane (or Kiri) tells Takeshi about Mikuriya
# and he chooses to detour there before going north.

passage(400,
    "Mikuriya is three days east, along the coast. The road follows "
    "white cliffs above grey water. Salt is in the air constantly. "
    "You make the journey with whichever companion travels with you "
    "— or alone, if you took the lonely road — and your dreams along "
    "the way are full of women singing.\n\n"
    "On the third evening you reach the tide-shrine. It sits on a "
    "rocky islet connected to the mainland by a causeway that floods "
    "twice a day. The shrine itself is a small wooden hall raised on "
    "old stilts. The torii is the colour of fading blood.\n\n"
    "The causeway is half-submerged. The tide is coming in.",
    [(401, "Wade across now while you still can"),
     (402, "Wait the night for low water"),
     (403, "Climb down the cliff and swim around")])

passage(401,
    "You wade. The water is cold and biting and rises to your "
    "shoulders before it begins to fall again. You reach the islet "
    "soaked to the bone. A lantern is lit in the shrine's window. "
    "Someone is there.\n\n"
    "You climb the worn steps. The door slides open before you "
    "knock.\n\n"
    "An old woman in faded white robes stands inside. Her hair is "
    "the colour of sea-foam. Her eyes are milk-white but they find "
    "your face exactly.\n\n"
    "\"You are wet,\" she says. \"You smell of grief, and of three "
    "winds badly held. Sit by the fire. We have time for one cup of "
    "tea before they come.\"",
    [(404, "Sit and ask who is coming")])

passage(402,
    "You wait the night on the cliff. You sleep in snatches. Around "
    "midnight you wake to footsteps below — three men in dark cloaks "
    "passing on the cliff path. They do not see you. They are moving "
    "toward the shrine.\n\n"
    "At dawn the causeway is dry. You cross. You find the shrine "
    "door broken in. Inside, an old woman in white robes lies dead "
    "before a cold hearth, her hair the colour of sea-foam, her milk-"
    "white eyes still open in surprise.\n\n"
    "The shrine has been ransacked. The water-mantra is gone. You "
    "are too late.",
    [(405, "Bury her and ride hard back to your companions")])

passage(403,
    "You climb down. You swim. The current is stronger than it "
    "looked, and you are pulled half a ri before you can fight your "
    "way to the islet's rocks.\n\n"
    "You climb up the stilts of the shrine, dripping, exhausted. The "
    "door is shut. From inside you hear a low chanting — not in any "
    "language you know.\n\n"
    "The chant is not the old woman's. It is too low. It is too many "
    "voices at once.",
    [(406, "Slide the door open silently"),
     (407, "Slam through the door with your sword drawn")])

passage(404,
    "She pours you tea from a kettle that has been on the hearth "
    "longer than you have been alive. The cup is warm. The tea is "
    "salt and ginger.\n\n"
    "\"Three men are coming,\" she says. \"Not the men in red "
    "armour — those have already come and gone, and killed my "
    "daughter on these steps three weeks ago. Tonight a different "
    "trouble walks the cliff path. *Gaki*, I think. The Yasha sends "
    "them ahead of itself.\"\n\n"
    "She looks at you with her milk-white eyes. \"You came for the "
    "Water-mantra. My daughter passed it to her own daughter on these "
    "steps before she died. The girl is north of you, on the road. "
    "If you came here to learn it from me direct, you have come a "
    "week too late and three days early.\"",
    [(408, "Ask what she means by 'early'")])

passage(405,
    "You bury the old woman in a hollow on the cliff above the "
    "shrine. You ride hard back along the coast. By the time you "
    "rejoin your companions, three days have been spent and you have "
    "learned nothing — but you have learned the *taste* of having "
    "been too late, and it stays in your mouth for the rest of the "
    "road.",
    [(180, "Rejoin the gathering")])

passage(406,
    "You slide the door open a finger's width. Inside, two figures "
    "in dark cloaks kneel before a candle. Their faces are wrong — "
    "blue-white, with too many teeth. They are chanting. On the "
    "floor between them, the old woman of Mikuriya lies with her "
    "eyes open and her chest rising and falling shallowly. Not dead. "
    "Not quite.\n\n"
    "*Gaki*. Hungry ghosts. Sent ahead of the blade.",
    [(409, "Attack from the doorway"),
     (410, "Slip in behind them")])

passage(407,
    "You slam the door open. Two figures in dark cloaks turn. Their "
    "faces are wrong. Their eyes are entirely black. They hiss like "
    "cats.\n\n"
    "You take the nearer one across the throat — your blade passes "
    "through with no resistance and the *gaki* laughs.\n\n"
    "Then the old woman of Mikuriya, lying on the floor between "
    "them, raises one trembling hand and *speaks*. A single word. "
    "The blue-white things scream and crumble into wet ash on her "
    "floor.\n\n"
    "She lowers her hand. She is very, very tired. \"You have "
    "Akiyama's tang at your belt,\" she says. \"Good. Come. Sit. "
    "Help me up. I will give you the Water.\"",
    [(404, "Sit by her fire")])

passage(408,
    "\"Three days early,\" she says, \"because the Yasha will be re-"
    "forged in six days, and you must arrive at Black Crow no later "
    "than the fifth. Three days here, three days back, leaves you "
    "*exactly* enough. No more.\"\n\n"
    "She sets down her cup. \"Sit, samurai. Tonight I will sing the "
    "Water-mantra into you the way I sang it into my daughter and "
    "she sang it into hers. By dawn the *gaki* will be at this door, "
    "and we will be ready, and you will leave at first light with "
    "the song carved into your throat.\"",
    [(411, "Sit and learn")])

passage(409,
    "You strike. The first *gaki* turns; your steel passes through "
    "it with no resistance. It laughs.\n\n"
    "Then the old woman, from the floor, raises one trembling hand "
    "and speaks a single word. Both *gaki* crumble into wet ash.\n\n"
    "She is breathing very shallowly. You kneel beside her. She "
    "fixes you with her milk-white eyes.\n\n"
    "\"Akiyama's last,\" she breathes. \"Good. Sit. Take my hand. I "
    "will sing the Water-mantra into you before I go. There is no "
    "time and there is no other way.\"",
    [(411, "Sit and learn — as she dies")])

passage(410,
    "You slip behind them. You take the first one with a thrust to "
    "the spine — your steel passes through with no resistance.\n\n"
    "The *gaki* turns. Both *gaki* turn. They smile, blue-white, "
    "with too many teeth.\n\n"
    "\"Ah,\" one of them whispers. \"A *bright* one.\"\n\n"
    "Steel is no good against them. You realize this too late.",
    None)
P[410]["ending"] = "horrible"
P[410]["title"] = "Eaten in the Tide-Shrine"

passage(411,
    "The old woman of Mikuriya takes your hand. She closes her milk-"
    "white eyes. She sings — low, low, low — and the mantra goes "
    "into you the way a wire is threaded into a flute. By the time "
    "the song is done, the old woman has stopped breathing. The "
    "candle has burned to a stub. The tide has gone out.\n\n"
    "You leave at dawn. You ride hard. You carry the Water-mantra "
    "in your throat all the way back to your companions, and when "
    "you arrive, Genshin looks into your eyes and says only: \"Ah. "
    "She gave it directly. I am sorry for her, and glad for you. "
    "Sit. We ride for Black Crow in two days.\"",
    [(180, "Return to the gathering with the Water yourself")])


# ---------------------------------------------------------------------------
# CHAPTER 2e — bandit road encounter (between Karasu-juku and the shrine)
# ---------------------------------------------------------------------------

passage(420,
    "Two ri up the north road you smell wood-smoke where no village "
    "should be. Through the trees you see an overturned merchant "
    "cart, three dead pack-ponies, and six bandits dividing a great "
    "pile of silk bolts on the road.\n\n"
    "An old merchant kneels in the mud with his hands tied. A young "
    "woman — his daughter, perhaps — kneels beside him, weeping "
    "silently. The bandits have not yet decided what to do with "
    "them.",
    [(421, "Charge them at once"),
     (422, "Loose an arrow from cover, if you carry one"),
     (423, "Walk out openly and demand they stand down"),
     (424, "Slip past — this is not your road")])

passage(421,
    "You charge. Six against one. The first three are easy — they "
    "are bandits, not soldiers, and your master taught you the cut "
    "of the willow. The fourth catches you across the cheek with a "
    "knife. The fifth gets a spear in his guard before you take him "
    "in the throat. The sixth runs.\n\n"
    "You let him run. The old merchant looks up at you with eyes "
    "huge in his weathered face.\n\n"
    "\"Young master,\" he whispers. \"My daughter and I owe you "
    "everything. We have nothing left to give you but a name. We "
    "live in the third house in the village of Sōkaze, north of "
    "the river. If you ever pass that way and need a bed, or a "
    "horse, or word carried, our door is yours.\"",
    [(425, "Help him up and walk on")])

passage(422,
    "You crouch in the brush. You set an arrow to your travel-bow "
    "(you have carried it for years; it is light and your master "
    "had you practise with it on autumn afternoons). You loose at "
    "the bandit leader. The arrow takes him in the throat.\n\n"
    "The others scatter — three back into the woods, two for the "
    "cart. You take one of the cart-runners with your second arrow "
    "and the other reaches the silk and runs with as much as he can "
    "carry.\n\n"
    "The merchant and his daughter are saved. They give you their "
    "name — the village of Sōkaze, third house, north of the river. "
    "\"Pass that way if ever you need a bed. Or a horse. Or word "
    "carried.\"",
    [(425, "Walk on")])

passage(423,
    "You step out into the road. The bandits straighten. The leader "
    "— a thick man with three days' beard — looks you up and down "
    "and laughs.\n\n"
    "\"A monk-boy with a sword. Walk on, monk-boy. We have already "
    "got more silk than we can carry; we do not need yours.\"\n\n"
    "\"Untie the merchant,\" you say.\n\n"
    "The leader's smile fades. He looks at his five men. He looks "
    "back at you. He sighs. \"A *talky* monk-boy. Alright, then.\" "
    "He spits, and draws.",
    [(421, "Fight them")])

passage(424,
    "You walk past. You hear the merchant beg, very softly. You "
    "hear the daughter weep. You walk on. You walk for half an "
    "hour. Then you stop. You turn around.\n\n"
    "You are too late. When you reach the road again, the cart is "
    "empty, the bandits are gone, the merchant lies face-down in "
    "the mud, and his daughter is — also gone. Either taken, or "
    "fled. You will never know which.\n\n"
    "You stand in the empty road a long time. A small bright "
    "thing in you dims.",
    [(426, "Walk on, colder than before")])

passage(425,
    "You walk on. The old merchant calls Sōkaze after you twice "
    "more, in case you have forgotten. You will not.",
    [(180, "Continue to the gathering")])

passage(426,
    "You walk on. You walk for three more days. Whatever you do "
    "next, the road remembers the merchant. The merchant remembers "
    "you. The merchant tells no one good things about a young "
    "samurai with a three-brushstroke token. Whatever doors might "
    "have opened to that token in the future, his will not.",
    [(180, "Continue to the gathering")])


# ---------------------------------------------------------------------------
# CHAPTER 2f — the kitsune
# ---------------------------------------------------------------------------

passage(440,
    "The bamboo road bends past a small wayside shrine. On the "
    "shrine steps sits a beautiful woman in a kimono the colour of "
    "autumn leaves. Her hair is unbound. She is eating a peach. She "
    "smiles at you as you pass.\n\n"
    "\"You walk wearily, samurai,\" she says. \"Sit a while. I have "
    "two peaches and only one mouth.\"\n\n"
    "Her smile is exactly the right amount of sad. Her shadow on "
    "the shrine steps has nine tails.",
    [(441, "Sit with her and take the peach"),
     (442, "Bow politely and walk on"),
     (443, "Comment on her shadow")])

passage(441,
    "You sit. You take the peach. The first bite is the best peach "
    "you have ever tasted in your life. The second bite is the "
    "second best. The third bite is the third best.\n\n"
    "You eat the peach in a kind of golden trance. When you are "
    "done, the woman is still smiling at you.\n\n"
    "\"I am called Kogane,\" she says. \"What is your name, "
    "samurai?\"",
    [(444, "Give your true name"),
     (445, "Give a false name"),
     (446, "Smile and say nothing")])

passage(442,
    "You bow politely. You walk on. A hundred paces up the road "
    "you realize you do not remember her face very clearly. Two "
    "hundred paces and you are not entirely sure she was there.\n\n"
    "But in your hand, somehow, is a single peach pit, polished "
    "smooth, warm as a coin held in someone's hand a long time.\n\n"
    "You keep it.",
    [(180, "Continue on the road")])

passage(443,
    "You stop. \"Your shadow has nine tails, lady.\"\n\n"
    "She freezes — only for a heartbeat. Then she laughs, a real "
    "laugh, low and delighted.\n\n"
    "\"You see *clearly*, samurai. Most do not.\" She pats the stone "
    "beside her. \"Sit. I will not eat you. I have eaten three "
    "samurai this month already and they all gave me indigestion.\"",
    [(447, "Sit with her")])

passage(444,
    "\"Takeshi,\" you say. \"Of Tōkin-ji.\"\n\n"
    "Her smile sharpens. \"Ah. *That* Takeshi. The boy with the "
    "three-brushstroke token and the broken sword-tang. I have "
    "heard your name three times this week, samurai. Once in the "
    "song of a thrush, once in the chatter of two ravens, once on "
    "the breath of a sleeping farmer.\"\n\n"
    "She tilts her head. \"You are well-known on the wind, "
    "Takeshi-san. The wind is mostly fond of you. Mostly.\"",
    [(447, "Ask what she means")])

passage(445,
    "\"Akira,\" you say. \"Of nowhere in particular.\"\n\n"
    "Her smile sharpens. \"A lie. The wind told me your name three "
    "days ago. *Takeshi.* Of Tōkin-ji. With a three-brushstroke "
    "token and a broken sword-tang at his belt. Tut, samurai. To "
    "lie to a kitsune at her own shrine. You are lucky I find it "
    "*charming*.\"\n\n"
    "She offers you the peach pit. \"Keep this. It will burn cold "
    "in your palm when something is lying to you. Consider it the "
    "fine for *your* lie. Now go.\"",
    [(180, "Walk on with the pit in your sleeve")])

passage(446,
    "You smile. You say nothing. She studies you a long moment. "
    "Then she laughs.\n\n"
    "\"Wise, samurai. The wisest answer at a kitsune's shrine is "
    "no answer at all. Here.\"\n\n"
    "She offers you the peach pit. \"Keep it. It will burn cold "
    "in your palm when something is lying to you. Consider it a "
    "gift. Walk on. The road will be kinder than it looks.\"",
    [(180, "Walk on with the pit in your sleeve")])

passage(447,
    "She tells you, as you sit on the shrine steps, that a man "
    "with a moon-shaped scar rode past this shrine three nights "
    "ago with a wrapped bundle across his saddle. She tells you "
    "the bundle *sang* as it passed her, and that her tails stood "
    "on end for an hour after.\n\n"
    "She tells you the road ahead splits four times and that on "
    "each split you should turn toward whichever direction smells "
    "of *salt* — even when there is no sea, even when there should "
    "be no salt. The wind has been telling her this for two days.\n\n"
    "She gives you the peach pit. \"It will burn cold when you are "
    "lied to. Keep it close. Even after the road ends — keep it.\"",
    [(180, "Walk on")])


# ---------------------------------------------------------------------------
# CHAPTER 5b — Black Crow approaches, expanded
# ---------------------------------------------------------------------------

passage(450,
    "The night before you reach Black Crow Castle, you make camp "
    "in a stand of pines above the salt lake. The lake is a black "
    "mirror under a half-moon. The castle, perhaps a ri off, is a "
    "dark tooth on the spur of the dead volcano.\n\n"
    "Around the fire your companions are quiet. Tetsu drinks. Kiri "
    "sharpens her tanto. Ayane, if she rode with you, hums the "
    "Water-mantra under her breath. Genshin's Fire is in your "
    "chest, a steady, terrible warmth.\n\n"
    "Tetsu speaks first. \"The boy should choose, brothers. Whose "
    "plan we use. He carries the three winds. He pays the bill.\"",
    [(250, "Choose your approach")])

passage(451,
    "You cannot sleep. You walk down to the lake's edge alone. The "
    "salt water laps against black pebbles. The moon is reflected "
    "perfectly, doubled, in the still surface.\n\n"
    "Behind you, soft as snow, a footstep. You turn. It is one of "
    "your companions — Kiri perhaps, or Ayane, or Tetsu, depending "
    "on the path you walked. You speak together a long time. You "
    "do not remember afterward exactly what was said. You remember "
    "that, by the time you walked back to the fire, you were no "
    "longer afraid of tomorrow. Not unafraid — but no longer "
    "*ruled* by the fear.\n\n"
    "It is the best gift the road has given you.",
    [(250, "Choose your approach")])

passage(452,
    "Before you sleep, you take out the peach pit the kitsune gave "
    "you (if you have it). It sits cold in your palm — not warm, "
    "not burning, but *cold*, the way a metal thing is cold on a "
    "winter morning.\n\n"
    "You think: *someone has lied to me today.*\n\n"
    "You go through the day. The innkeeper. The road-priest who "
    "blessed you. The hawker at the riverside. Tetsu.\n\n"
    "Tetsu.\n\n"
    "You sit up. You walk to the fire. Tetsu is asleep, snoring, "
    "his flask under his head. You watch him a long time. You do "
    "not wake him. But you remember.\n\n"
    "Tomorrow you will be more careful.",
    [(250, "Choose your approach")])


# ---------------------------------------------------------------------------
# CHAPTER 6b — Inside Black Crow, expanded sneaking path
# ---------------------------------------------------------------------------

passage(460,
    "You emerge in the cellar of Black Crow Castle. Empty lacquer "
    "barrels. A smell of old salt and older blood. A wooden "
    "stairway leads up to a curtained doorway, behind which the "
    "chanting grows louder.\n\n"
    "You can also see, in the corner, a small iron grate over a "
    "well-shaft. Wet rope is coiled beside it.",
    [(461, "Climb the stair toward the chanting"),
     (462, "Take the grate-and-rope route into the deeper castle"),
     (463, "Wait for a servant to come down for wine")])

passage(461,
    "You climb. At the curtain you pause. Beyond it, the chanting "
    "is in a language you do not know. You smell candle-wax and "
    "old iron and something like burning hair.\n\n"
    "Slowly, slowly, you part the curtain.",
    [(270, "Enter the chanting hall")])

passage(462,
    "You lower yourself by rope into the well-shaft. The shaft is "
    "wet and very cold. Twenty body-lengths down, the shaft opens "
    "into a horizontal tunnel, knee-deep in salt water. The tunnel "
    "leads — by your reckoning — directly under the high keep.\n\n"
    "You wade. After a long time the tunnel turns up. A ladder "
    "rises into shadow. You climb.\n\n"
    "You emerge in Hayabusa Mōri's *private chamber*. He is not "
    "there. The Yasha-no-Tachi is not there. But on his low desk "
    "sits a single open scroll, weighted by a black iron paperweight.",
    [(464, "Read the scroll"),
     (465, "Set the chamber on fire and ambush him when he returns"),
     (466, "Hide and wait")])

passage(463,
    "You wait. After perhaps a quarter hour, footsteps. A servant "
    "— a thin man in dull blue robes — comes down the stair for a "
    "jar of wine.\n\n"
    "You step out behind him with the wakizashi at his throat. He "
    "is too frightened even to call out.\n\n"
    "\"Where is the master?\" you whisper.\n\n"
    "\"High hall, sir. Always the high hall, these last six days. "
    "He does not eat. He does not sleep. He chants. He weeps. Sir, "
    "please.\"",
    [(467, "Let him live and proceed"),
     (468, "Bind him and proceed"),
     (469, "Cut his throat and proceed")])

passage(464,
    "You unroll the scroll. It is a letter, in a hand you have "
    "seen before — your master's own hand. The hand of Akiyama "
    "Ryūnosuke. Dated three years ago.\n\n"
    "*Brother Hayabusa,* it begins, *I have your last letter, and "
    "I weep over it. You ask me to come and end it for you. I "
    "cannot. The Yasha will not let me near enough. But I will "
    "train a student. I will send him to you when the seal "
    "breaks. He will be very young and very angry and he will "
    "have, perhaps, the fourth wind that I never had. Forgive me "
    "for not coming myself, brother. Forgive me for not coming "
    "thirty years ago. — A.*\n\n"
    "You sit down very suddenly on the floor.",
    [(470, "Carry this knowledge to Hayabusa")])

passage(465,
    "You set the chamber on fire. The paper screens go up at "
    "once. You hide in a cupboard.\n\n"
    "Hayabusa Mōri does not come back to the chamber. He sends "
    "guards. The guards find you in the cupboard, choking on "
    "smoke. You take three of them with you before the fourth "
    "puts a spear through your chest.\n\n"
    "The Yasha-no-Tachi will be re-forged on the full moon as "
    "planned. You will not see it. You will be ash in a burned "
    "chamber.",
    None)
P[465]["ending"] = "bad"
P[465]["title"] = "Smoke and Spear"

passage(466,
    "You hide behind a screen. You wait. After perhaps an hour, "
    "Hayabusa Mōri walks in alone, the Yasha-no-Tachi at his hip. "
    "He sits at his desk. He picks up the scroll you read (or did "
    "not read). He reads it. He weeps, silently, for a long time.\n\n"
    "Then he says, without turning: \"Boy. Come out from behind "
    "the screen. There is no point pretending I do not know you "
    "are there. The Yasha smelled you on the wind an hour ago.\"",
    [(280, "Step out")])

passage(467,
    "\"Run,\" you whisper. \"Off the castle grounds. Do not stop. "
    "Do not tell anyone what you saw.\"\n\n"
    "He nods, almost weeping with relief, and runs.\n\n"
    "(He will, in fact, escape and live a long quiet life as a "
    "boat-mender on the south coast. He will tell exactly one "
    "person — his granddaughter — that he once met a samurai with "
    "kind eyes who spared him in a cellar. The granddaughter will "
    "not believe him.)",
    [(461, "Climb toward the chanting")])

passage(468,
    "You bind him with his own sash, gag him with his own sleeve, "
    "and tuck him behind the lacquer barrels. He will be found in "
    "the morning. By then this will all be over, one way or "
    "another.",
    [(461, "Climb toward the chanting")])

passage(469,
    "You cut his throat. He sinks to the floor without a sound. "
    "His eyes go round and then go nothing.\n\n"
    "He was a servant. He was not a soldier. He was not, in any "
    "honest sense, your enemy.\n\n"
    "A small bright thing in you dims.",
    [(461, "Climb toward the chanting, a little colder")])

passage(470,
    "You roll the scroll up. You tuck it into your robe. You go to "
    "find Hayabusa Mōri.\n\n"
    "When you find him — in the high hall, alone, the Yasha-no-"
    "Tachi across his knees — you do not draw. You sit. You set "
    "the scroll on the floor between you.\n\n"
    "He looks at it. He looks at you. He weeps, silently.\n\n"
    "\"He sent you,\" he whispers. \"Three years ago. He *promised* "
    "me, three years ago, and I did not believe him.\"\n\n"
    "He bows — the deepest bow you have ever received.\n\n"
    "\"Then, Takeshi-san. Then let us begin.\"",
    [(330, "Begin the great fight together")])


# ---------------------------------------------------------------------------
# CHAPTER 6c — pilgrim approach, expanded
# ---------------------------------------------------------------------------

passage(480,
    "You walk the long causeway openly. The salt water laps the "
    "stones on both sides. Crows wheel overhead. A single guard "
    "stands at the inner gate; he watches you come the whole way.\n\n"
    "When you reach him, he bows. Bows. \"Takeshi-san. The master "
    "has been expecting you. The high hall, if you please. He "
    "asks that you take off your sandals at the inner door.\"\n\n"
    "He stands aside. He does not even ask for your sword.",
    [(481, "Walk in as he asks"),
     (482, "Ask him why he serves Hayabusa Mōri"),
     (483, "Cut him down at the gate")])

passage(481,
    "You walk in. The keep is strangely empty. Most of the rooms "
    "you pass are clean and bare, like rooms set aside for a "
    "memorial. The kitchens are cold.\n\n"
    "At the inner door you take off your sandals. The wood under "
    "your feet is old and good. You walk down a long corridor.\n\n"
    "At the end of the corridor is the high hall.",
    [(280, "Enter the high hall")])

passage(482,
    "\"Captain,\" you say. \"Why do you serve a man with a moon-"
    "shaped scar?\"\n\n"
    "The guard looks at you a long moment. Then, very quietly:\n\n"
    "\"Because thirty-one years ago he came down off Asahi "
    "mountain into a starving village with a strange new sword "
    "and he killed the bandits who had been raiding our rice for "
    "a year. He carried the bodies of three children out of the "
    "burned shed himself. He buried them himself. He was a good "
    "man, samurai. *Was.*\n\n"
    "\"He is not a good man now. But the village remembers. The "
    "village still feeds his men. And I, samurai, am from that "
    "village.\"\n\n"
    "He bows, very deep, and stands aside. \"Go in.\"",
    [(481, "Walk in")])

passage(483,
    "Your blade is faster than his. He drops. The salt water laps "
    "the stones.\n\n"
    "You walk into Black Crow Castle leaving a corpse at the "
    "gate. The corpse was a man who had been told to bow to you, "
    "not to fight you. The corpse was, in fact, the gentlest man "
    "who has served Hayabusa Mōri in twenty years.\n\n"
    "A small bright thing in you dims, on the threshold of the "
    "keep. You walk in, colder than you came.",
    [(481, "Walk in, dimmer than before")])


# ---------------------------------------------------------------------------
# CHAPTER 6d — assault, expanded
# ---------------------------------------------------------------------------

passage(500,
    "Tetsu of the Burnt Hill has, miraculously, raised forty-three "
    "old soldiers from his regiment in three days. They are "
    "middle-aged, scarred, and grim. They drink very steadily and "
    "they do not laugh. They do, however, salute Tetsu without "
    "irony.\n\n"
    "At dusk you form them up in the wood above the salt lake. "
    "Tetsu addresses them in a low voice. They do not cheer. They "
    "merely nod, one by one, and check their swords.\n\n"
    "Then, in the last of the light, you take the outer wall.",
    [(253, "Lead the assault")])

passage(501,
    "The outer wall is held by perhaps thirty of Hayabusa's men — "
    "and three of his lieutenants, who are not all entirely human. "
    "One of them is a *gaki* in lacquered armour. Another is "
    "something with too many fingers under his gauntlets. The "
    "third is merely a tall pale man who fights as if he has done "
    "it for a hundred years.\n\n"
    "Tetsu's old soldiers know how to break a wall. The outer wall "
    "falls in a quarter-hour. Twelve of Tetsu's men die taking it. "
    "Tetsu himself takes a cut across the ribs that is worse than "
    "he lets on.",
    [(266, "Press on toward the inner gate")])

passage(502,
    "Inside the broken outer wall the courtyard is a confusion of "
    "lantern-light and bodies. Kiri, somehow, is everywhere — her "
    "tanto opens throats in the dark. Ayane (if she rode with you) "
    "wields a naginata you did not know she could wield, and the "
    "tall pale lieutenant goes down beneath it before he has "
    "finished smiling.\n\n"
    "But the inner keep is harder. Its gate is iron-bound and held "
    "by twenty archers from above. You will not take it before "
    "dawn.",
    [(266, "Hold the courtyard until dawn")])


# ---------------------------------------------------------------------------
# CHAPTER 6e — waiting, expanded
# ---------------------------------------------------------------------------

passage(510,
    "On the second night Hayabusa Mōri does not come down alone. "
    "He comes with two figures who walk a little behind him on the "
    "causeway — and one of them moves wrong, jerkily, as if its "
    "joints are not arranged the way a person's joints are.\n\n"
    "The Yasha-no-Tachi is at his hip. The half-moon is bright on "
    "the salt.\n\n"
    "\"Takeshi-san,\" he calls. \"Akiyama's last. Will you not "
    "come speak with me before we kill each other?\"",
    [(254, "Walk out onto the causeway")])

passage(511,
    "You walk out alone onto the causeway. Behind you, your "
    "companions hold their breath. Before you, Hayabusa Mōri "
    "smiles, tired and old. The two figures behind him do not "
    "smile. One of them does not have a *face* in the conventional "
    "sense — it is a *gaki*, in armour, holding a long curved blade.\n\n"
    "Hayabusa lifts his hand. The *gaki* stops.\n\n"
    "\"They are not under my command,\" he says, quietly, with what "
    "might be apology. \"They came down from the keep behind me, "
    "uninvited. The blade summons them and the blade does not yet "
    "obey me entirely. We will both die tonight, Takeshi-san, if "
    "you wish to draw. Or we may, perhaps, attempt something "
    "harder.\"",
    [(280, "Sit on the causeway with him")])


# ---------------------------------------------------------------------------
# CHAPTER 7c — inner-keep exploration before the high hall
# ---------------------------------------------------------------------------

passage(520,
    "You move through the inner keep. The corridors are lit by "
    "guttering lanterns. You hear, far above you, the chanting. "
    "You hear, closer, the slow drip of water somewhere.\n\n"
    "You pass an open doorway. Inside, an old monk sits cross-"
    "legged on the floor, head bowed, hands folded. He is in chains.",
    [(521, "Free him"),
     (522, "Speak to him through the doorway"),
     (523, "Pass him by")])

passage(521,
    "You break his chains with the pommel of your wakizashi. He "
    "lifts his head slowly. His face is gaunt. His eyes are bright "
    "and entirely sane.\n\n"
    "\"Akiyama's last,\" he says — and you stiffen, because you "
    "did not say so. \"Yes, I know. He sent me word a year ago "
    "that you might come this way. I am Brother Donkō. I am one "
    "of your three winds that you were told was a fiction. He "
    "thought you might prefer to learn Fire from Genshin, but in "
    "case Genshin was already dead, he had me imprisoned here on "
    "purpose, so that you might find me.\"\n\n"
    "He smiles, faintly. \"Akiyama was a strange and patient old "
    "man. Sit. If you have not yet had the Fire — I will give it "
    "to you now.\"",
    [(524, "Receive the Fire from Brother Donkō")])

passage(522,
    "\"Brother,\" you whisper through the doorway. \"Who are you?\"\n\n"
    "His head lifts slowly. \"I am Brother Donkō. Hayabusa Mōri "
    "took me from my hermitage on Asahi mountain six months ago. "
    "He kept me alive because he thought I knew the Fire-wind. He "
    "was right. I do not intend to give it to him.\" He looks at "
    "you. \"Are you Akiyama's last?\"",
    [(521, "Free him")])

passage(523,
    "You pass him by. The chanting above is louder. You climb the "
    "next stair.\n\n"
    "(You will hear, eventually, that the old monk in chains died "
    "in his cell, of starvation, three weeks after the night you "
    "passed him by. You will hear it from a survivor of Black "
    "Crow Castle, years later, at a roadhouse in another province. "
    "You will not sleep that night.)",
    [(270, "Continue toward the high hall")])

passage(524,
    "Brother Donkō places one bony hand on your sternum. Fire — a "
    "warmth deeper than any fire you have known — kindles in your "
    "chest. He holds you a long, silent minute. Then he lowers "
    "his hand.\n\n"
    "\"You carry it now. Whether you can wield it tonight is yet "
    "to be seen. But you carry it. Go.\"\n\n"
    "He folds his hands again, closes his eyes. \"I will sit here "
    "and listen. If you fail, I will burn this keep down around "
    "Hayabusa before he can finish the re-forging. It will not "
    "save the country, but it will buy it another month.\"",
    [(270, "Climb toward the high hall, with Fire newly in you")])

passage(525,
    "You move past the chained monk's door (whether you freed him "
    "or did not). The corridor ends in a steep stair lit by a "
    "single lantern at the top. The chanting is now very loud.\n\n"
    "On the stair, halfway up, a figure in red lacquer sits with "
    "his back against the wall, head bowed. He is — perhaps — "
    "asleep. He is — perhaps — dead.\n\n"
    "You will have to step over him to climb.",
    [(526, "Step over him quietly"),
     (527, "Check whether he is alive first"),
     (528, "Cut his throat to be sure")])

passage(526,
    "You step over him. He does not stir. You climb. At the top "
    "of the stair the chanting is so loud it shakes the floor.",
    [(270, "Climb into the high hall")])

passage(527,
    "You crouch. He is breathing. He is asleep — drunk, perhaps, "
    "or simply spent. He is the burn-scarred captain from Karasu-"
    "juku.\n\n"
    "He stirs. His eyes open, just barely. He sees you. He says, "
    "very quietly: \"Akiyama's last. About time. Go up. I have "
    "not seen you. I have been asleep this whole watch.\"\n\n"
    "He closes his eyes again. He is, after all, from a village "
    "Hayabusa once saved from bandits. He has his own reasons.",
    [(270, "Climb past him")])

passage(528,
    "You cut his throat. He goes from sleep to nothing in a "
    "single breath, without a sound. You step over him.\n\n"
    "(He was a sleeping man. He was, also, the burn-scarred "
    "captain who had, once, threatened you in an inn in Karasu-"
    "juku. Whether that justifies the cut is between you and "
    "your master. A small bright thing in you dims a little "
    "further on the stair.)",
    [(270, "Climb into the high hall, colder still")])


# ---------------------------------------------------------------------------
# CHAPTER 8b — the great fight, deeper
# ---------------------------------------------------------------------------

passage(530,
    "You match Hayabusa Mōri stroke for stroke for a full minute. "
    "The hall echoes with steel. The Yasha-no-Tachi shrieks at "
    "every contact with Kōgetsumaru's stub and your wakizashi. "
    "Hayabusa's eyes — between the cuts — are *grateful*, in "
    "flashes.\n\n"
    "On the second minute, the demon takes over more fully. "
    "Hayabusa's cuts become faster, and crueler, and they no "
    "longer have the small fractional restraint they did before. "
    "His grip on the Yasha-no-Tachi has gone white.\n\n"
    "You have a heartbeat to decide.",
    [(531, "Strike at his grip — to disarm only"),
     (532, "Strike to wound — slow him, do not kill"),
     (533, "Strike to kill before the demon takes him fully")])

passage(531,
    "You strike at his grip. The cut of the willow, low and "
    "fast, takes the Yasha-no-Tachi at the guard. The guard "
    "snaps. The grip falls.\n\n"
    "Hayabusa staggers back, weeping with what looks like relief. "
    "The blade rings on the stones. The demon-steam begins to "
    "rise out of it.\n\n"
    "You have your opening for the True Sealing — *if* you have "
    "the fourth wind.",
    [(320, "Sing the full sealing")])

passage(532,
    "You strike to wound. Your blade scores Hayabusa across the "
    "thigh. He staggers, drops to one knee — but his grip on the "
    "Yasha-no-Tachi tightens, and the demon in it *howls*, and "
    "his next cut comes from the kneeling position faster than "
    "anything you have ever seen.\n\n"
    "It takes you across the chest. The wound is deep. You feel "
    "your strength leaving you.",
    [(534, "Sing the Water-mantra with your last breath"),
     (535, "Strike again to kill before you fall")])

passage(533,
    "You strike to kill. The cut of the falling pine. Your blade "
    "goes home. Hayabusa Mōri stiffens, eyes wide, and slowly "
    "topples. He smiles, faintly, as he falls.\n\n"
    "\"Thank you, Takeshi-san. Tell Genshin... tell Genshin he "
    "never could brew tea either.\"\n\n"
    "He dies on the stones of Black Crow Castle. The Yasha-no-"
    "Tachi falls from his hand and rings, and rings, and rings. "
    "The demon is still in it. The demon is not gone.",
    [(360, "Decide what to do with the blade")])

passage(534,
    "You sing. Bleeding badly, sinking to your knees, you sing "
    "the Water-mantra into the hall. The notes are weak. The "
    "song is whole.\n\n"
    "Hayabusa Mōri — kneeling, the Yasha-no-Tachi still in his "
    "hand — closes his eyes. The demon in the blade flinches. "
    "His grip loosens.\n\n"
    "The blade rings on the stones. Hayabusa whispers, \"Thank "
    "you, boy. Now — finish me. The demon will return to me "
    "otherwise.\"",
    [(536, "Finish him")])

passage(535,
    "You strike. Bleeding, sinking, you strike. Your blade takes "
    "Hayabusa Mōri high in the chest. He topples. The Yasha-no-"
    "Tachi falls.\n\n"
    "You drop to one knee. Your wound is bad. Your sight greys. "
    "But the demon in the blade is alone on the floor now, "
    "rising as steam, and you have just enough breath for one "
    "thing.",
    [(537, "Sing the Water-mantra with your last breath"),
     (538, "Break the blade with your last strength")])

passage(536,
    "You strike. Hayabusa Mōri dies smiling. You sink to your "
    "knees beside him on the bloody stones. The Yasha-no-Tachi "
    "rings beside you.\n\n"
    "You have a choice in the next breath: break the blade, "
    "carry it home, drop it in the lake, or take it up yourself.",
    [(360, "Decide")])

passage(537,
    "You sing. You sing with your last breath. The Water-mantra "
    "rises in the empty hall. The demon-steam thins. The Fire "
    "in your sternum gutters. The Earth under your feet "
    "loosens.\n\n"
    "You die singing. The demon, *almost* sealed, slips into the "
    "stones at the last possible note and escapes into the "
    "country. It will be back in a hundred years.\n\n"
    "But the country has a hundred years. And a song echoes in "
    "the stones of Black Crow Castle that will be heard, "
    "occasionally, on still nights, by travellers passing by.\n\n"
    "You are not famous. You are not remembered by name. You "
    "are, however, remembered.",
    None)
P[537]["ending"] = "ok"
P[537]["title"] = "The Singer in the Hall"

passage(538,
    "You raise your sword with your last strength. You bring it "
    "down on the Yasha-no-Tachi where it lies on the stones. The "
    "blade splinters. The demon-steam shrieks. The demon is "
    "loose.\n\n"
    "You die on the stones beside Hayabusa Mōri. The demon "
    "vanishes into the floor. It will be back in a hundred "
    "years. The country has a hundred years.\n\n"
    "Your companions will find you both at dawn. Your friends "
    "will bury you side by side, samurai and former samurai, "
    "the two of you who broke the blade together. It will "
    "become a *story*. The story will not be entirely correct, "
    "but the bones of it will be true.",
    None)
P[538]["ending"] = "good"
P[538]["title"] = "Two Brothers on the Stone"


# ---------------------------------------------------------------------------
# CHAPTER 9b — afterwards and small finishes
# ---------------------------------------------------------------------------

passage(540,
    "On the night of the True Sealing, the four winds in you "
    "speak together for the first time, and the small stoppered "
    "jar appears in your hand as if by no agency at all.\n\n"
    "Hayabusa Mōri kneels. He weeps. The demon is in the jar.\n\n"
    "Outside, the half-moon climbs above the salt lake. The "
    "fortress is silent for the first time in years. Your "
    "companions, on the causeway, hold their breath.\n\n"
    "You and Hayabusa walk out together, slowly. He bows to your "
    "friends. They bow back, uncertain. Tetsu — who has known "
    "Hayabusa longer than any of you, and who hated him longest "
    "— sets his hand on the old man's shoulder and says only, "
    "\"Brother.\"\n\n"
    "It is enough.",
    [(390, "Continue to the final passage")])

passage(541,
    "You ride south. The road is kinder coming home than it was "
    "going out. At every village the rumour has run ahead of "
    "you: *the Yasha-no-Tachi is in a jar; the Crimson Lord is a "
    "gentle old man now; the boy of Akiyama is coming home.* You "
    "do not enjoy the attention. You do not turn it away.",
    [(390, "Reach the final passage")])

passage(542,
    "Genshin meets you at the foot of Mount Suzaku. He is "
    "smoking, of course. He has aged a year for each day you "
    "were gone, by the look of him, but his eye is bright.\n\n"
    "\"You came back,\" he says. \"And you brought a jar.\" He "
    "looks at the stoppered jar in your hand. \"Akiyama would "
    "have rolled his eye at the *craftsmanship* of it. But he "
    "would have approved of the result.\"\n\n"
    "He embraces you, once, briefly, the way old monks embrace.",
    [(390, "Continue")])


# ---------------------------------------------------------------------------
# CHAPTER 5c — Karasu-juku to Mikuriya, if Ayane joins early
# ---------------------------------------------------------------------------

passage(550,
    "You ride east with Ayane through cold dawn. She does not "
    "speak for the first hour. Then she says, very quietly:\n\n"
    "\"My mother was a good singer, samurai. Better than I am. "
    "She gave me the mantra in one afternoon, on the steps of "
    "the tide-shrine, and she made me sing it back to her, line "
    "by line, until my voice was raw and the sun was setting. "
    "She knew. She knew exactly what was coming. She gave it to "
    "me anyway.\"\n\n"
    "She wipes her eyes once on her sleeve. \"That, samurai, is "
    "what mothers are.\"",
    [(551, "Ride with her in silence")])

passage(551,
    "You ride in silence. You reach the eastern shrine by "
    "noon, where Genshin and Kiri (and perhaps Tetsu) are "
    "already waiting.",
    [(180, "Join the gathering")])

passage(552,
    "Ayane sings the Water-mantra into you while you sit by a "
    "stream below the eastern shrine. It takes the whole "
    "afternoon. By dusk you can sing it back without error. "
    "Your voice is sore. Hers is shot. She laughs — really "
    "laughs — for the first time you have heard.\n\n"
    "\"You sing like a frog, samurai. But the song is whole. "
    "That is all the mantra cares about.\"",
    [(212, "Move on to Earth")])


# ---------------------------------------------------------------------------
# CHAPTER 1b — extra opening branches, returning to the temple
# ---------------------------------------------------------------------------

passage(560,
    "You return to the temple ruin once more before you leave "
    "Mount Suzaku. The crows have not come back. The rain has "
    "washed the blood off the stones. Your master's cairn looks "
    "very small under the empty sky.\n\n"
    "You stand a long time before it. You do not weep — you "
    "wept yourself dry the night you buried him. You merely "
    "stand. After a long time, you bow.\n\n"
    "Then you turn and walk down the mountain. You do not look "
    "back. There is no point in looking back.",
    [(31, "Descend to the fork in the road")])

passage(561,
    "Among the temple's ruined kitchens you find, half-burned, "
    "a small lacquered box that the killers missed. Inside is a "
    "second three-brushstroke token — identical to the one your "
    "master gave you with his last breath — and a folded note in "
    "your master's hand:\n\n"
    "*If you are reading this, my road has ended and yours has "
    "begun. The second token is for the one you find on the "
    "road who has earned your trust. Give it to them when you "
    "are certain. The wood is older than the temple. It knows "
    "its own.*",
    [(31, "Descend, carrying both tokens")])

passage(562,
    "In the rubble of the dōjō you find your old training-bow — "
    "scorched on one side, but the bamboo is sound. You shoulder "
    "it. Your master had you practise with it on autumn "
    "afternoons; you have not drawn it in two years. The string "
    "is rotten. You will replace it in the next village.\n\n"
    "Carrying a bow as well as a sword changes what kind of "
    "samurai you look like on the road. It also changes what "
    "kind of samurai you *are*.",
    [(31, "Descend")])


# ---------------------------------------------------------------------------
# CHAPTER 3b — small training-day finishes
# ---------------------------------------------------------------------------

passage(570,
    "On the night between Fire and Water, you cannot sleep. You "
    "sit outside Genshin's house in the cold, watching your "
    "breath, with the Fire newly kindled in your sternum like a "
    "small steady stove.\n\n"
    "Genshin's wife Hana comes out, wrapped in a quilt, and "
    "sits beside you without speaking. After a long time she "
    "says: \"He carried that Fire forty years, my husband. He "
    "never used it. He kept it for the day Akiyama would need "
    "it for someone else. It was lonely Fire, samurai. Use yours "
    "more kindly, if you can.\"",
    [(211, "Continue to the Water teaching")])

passage(571,
    "On the night between Water and Earth, your dreams are full "
    "of singing. You wake with the Water-mantra echoing in your "
    "throat. You go down to the stream and sing it, very softly, "
    "into the dark water. The stream does not respond. The "
    "stream does not need to.\n\n"
    "When you come back to the fire, Tetsu of the Burnt Hill is "
    "awake, watching you with his good eye. He says nothing. He "
    "passes you the flask. You take it. You drink.\n\n"
    "It is the closest he comes to telling you he is proud.",
    [(212, "Continue to the Earth teaching")])

passage(572,
    "On the morning you ride for Black Crow, Genshin walks you "
    "to the village gate. He does not bow. He does not embrace "
    "you. He merely puts one bony hand on your sternum, where "
    "the Fire sits.\n\n"
    "\"Akiyama's last,\" he says. \"Bring it back to me, the "
    "Fire. Or do not. But do not waste it.\"\n\n"
    "You bow. You ride.",
    [(213, "Ride")])


# ---------------------------------------------------------------------------
# CHAPTER 4b — small forest finishes
# ---------------------------------------------------------------------------

passage(580,
    "You sleep one night in the forest of Hōrai before walking "
    "out. You dream of the old bark-spirit. In the dream he is "
    "younger — middle-aged, with two eyes, dressed in the robes "
    "of a samurai. He tells you a story you do not entirely "
    "follow about a sword and a brother and a fire on a "
    "mountain, but the gist of it is *we have all carried this. "
    "Carry yours, boy.*\n\n"
    "You wake at dawn. The forest opens.",
    [(222, "Walk out")])


# ---------------------------------------------------------------------------
# OTHER ENDING — the lone-and-late path (passage 399 rehoming)
# ---------------------------------------------------------------------------

passage(590,
    "You leave Black Crow Castle alone. The Yasha-no-Tachi is "
    "broken on the floor of the high hall. Hayabusa Mōri lies "
    "dead beside it. The demon is loose, but loose into a hundred "
    "years of *somewhere else*.\n\n"
    "You ride south. You do not visit your master's cairn — you "
    "cannot make yourself. You ride past it on the river road "
    "and you cannot make yourself turn aside.\n\n"
    "You wander. You become a ronin. You die, eventually, in a "
    "village very far from where you began, of a small illness "
    "no one names. You are not famous. You are not remembered. "
    "But somewhere — under the prayer floor of a rebuilt "
    "Tōkin-ji you will never visit — a small stoppered jar "
    "would have sat, had things been a little different.",
    None)
P[590]["ending"] = "ok"
P[590]["title"] = "The Wandering"


# ---------------------------------------------------------------------------
# CHAPTER 2g — minor in-Karasu-juku flavour
# ---------------------------------------------------------------------------

passage(600,
    "You wake from a short sleep in the smaller inn to the smell "
    "of burning. Smoke under the door. Shouts in the alley.\n\n"
    "The inn is on fire. The fire was not your doing.",
    [(601, "Break out the window with your sword-hilt"),
     (602, "Wet your robe and try the main stair"),
     (603, "Climb up to the roof through the smoke-hatch")])

passage(601,
    "You break the window. You drop through, sword first, into "
    "the alley below. Three red-armoured soldiers wait for you in "
    "the alley. They have been waiting.\n\n"
    "Their captain — burn-scarred — smiles around his torch. "
    "\"There he is. Burn an inn down, lure a mouse out a window. "
    "Old trick. Always works on monk-boys.\"",
    [(190, "Fight")])

passage(602,
    "You wet your robe in the wash-bowl and pull it over your "
    "head. The stair is hot but passable. You stumble into the "
    "common room — and into the captain himself, sword drawn, "
    "waiting for you with three soldiers at his back.\n\n"
    "\"Wise, monk-boy,\" he murmurs. \"Most pick the window.\"",
    [(190, "Fight")])

passage(603,
    "You climb through the smoke-hatch onto the inn roof. The "
    "tile is hot under your hands. From up here you can see the "
    "whole town — and you can see five red-armoured soldiers "
    "ringing the inn at street level, and two more on the "
    "neighbouring rooftop, bows strung.\n\n"
    "But the inn next door is only an arm's-span away, and the "
    "rooftops beyond run unbroken for half the town.",
    [(187, "Run the rooftops")])


# ---------------------------------------------------------------------------
# CHAPTER 6f — extra waiting-day moments
# ---------------------------------------------------------------------------

passage(610,
    "On the day before Black Crow, your companions take a "
    "morning to rest in the pine wood. Tetsu has produced, from "
    "somewhere, a rice ball each and a strip of dried fish.\n\n"
    "Kiri tells you, over the fire, that her village was burned "
    "by Hayabusa's men eleven years ago. Her mother and her two "
    "younger brothers died in it. She was nine. The village had "
    "been hiding one of the three sealing scrolls; the soldiers "
    "had been told to retrieve it. They did. They burned the "
    "village afterward because their captain enjoyed burning "
    "villages.\n\n"
    "She tells you this in the same voice she uses to ask for "
    "more tea. She has not said the words aloud to anyone in "
    "eleven years.",
    [(611, "Sit with her")])

passage(611,
    "You sit with her. You do not say anything stupid. You do "
    "not promise her vengeance. You sit. After a long time, she "
    "leans her head briefly against your shoulder. Briefly. "
    "Then she straightens, wipes her eyes once on her sleeve, "
    "and goes to sharpen her tanto.\n\n"
    "It is the closest she has come, in eleven years, to "
    "letting someone in.",
    [(213, "Ride for Black Crow")])

passage(612,
    "Ayane, on the same day, tells you of her mother on the "
    "tide-shrine steps. She does not weep. She has been weeping "
    "for three weeks; she is, for the moment, dry. She tells "
    "you that her mother sang the Water-mantra into her ear so "
    "patiently, that afternoon, that Ayane only afterward "
    "understood her mother was teaching her in the same way she "
    "had taught her to swim, and to write her own name, and to "
    "tie a kimono.\n\n"
    "\"She was a *teacher*, my mother. Always. Even dying she "
    "was a teacher. I will spend the rest of my life trying to "
    "be that calm.\"",
    [(213, "Ride for Black Crow")])

passage(613,
    "Tetsu, on the same day, drinks. He talks about your "
    "master, Akiyama, when both of them were young. \"He was a "
    "*bad* swordsman in his youth, monk-boy. *Bad.* He held the "
    "blade like a farmer. We laughed at him. He did not stop "
    "training because we laughed. He became — he became — \" "
    "Tetsu wipes his eye. \"He became the swordsman who could "
    "have killed any of us in our sleep without us noticing. He "
    "did not. He went away and started a temple. He took you "
    "in. He died for you. You are a *lucky* young man, monk-"
    "boy, and the bill for that luck is the next two days. Pay "
    "it. Pay it well.\"",
    [(213, "Ride")])


# ---------------------------------------------------------------------------
# CHAPTER 2h — second meeting paths through Karasu-juku
# ---------------------------------------------------------------------------

passage(620,
    "The eastern shrine sits among black cedars an hour north of "
    "Karasu-juku. As you approach you see horses tied at the "
    "torii. On the shrine steps, a tall woman with grey at her "
    "temples and a longbow rises to meet you. Beside her sit a "
    "slighter young woman with eyes like flint, an old monk "
    "smoking a long pipe, and an enormous bearded man with one "
    "milky eye and a flask the size of a small child.\n\n"
    "Hana, Kiri, Genshin, Tetsu. All four. Already gathered. "
    "Already waiting.\n\n"
    "Hana stands. \"Takeshi-san. You are exactly on time. Sit. "
    "Eat. Tell us how he died, and then we will tell you what "
    "comes next.\"",
    [(180, "Sit and tell")])

passage(621,
    "An hour before dawn the back door of the larger inn opens "
    "without a sound. The innkeeper beckons. You slip out into a "
    "garden where a single horse is tied — a lean grey mare, "
    "saddled.\n\n"
    "\"The eastern shrine,\" the innkeeper murmurs. \"Genshin "
    "and the kunoichi are already there. Ride.\"\n\n"
    "You ride.",
    [(620, "Reach the shrine")])

# Final terminal: the bow-master ending if you carried the bow and chose
# certain paths.
passage(630,
    "On the night of the True Sealing, you stand with the bow "
    "scorched from your temple at your back. You do not need to "
    "draw it. You bow to Hayabusa Mōri as he kneels. He bows to "
    "you. The demon is in the jar.\n\n"
    "Years later, in the rebuilt Tōkin-ji, you will teach a "
    "small class of children — among them a freckle-faced boy "
    "who lives because, on a wet morning long ago, you lifted "
    "the beam in the burning temple instead of going to the "
    "garden first. You will hand him the bow you carried out of "
    "the ruin. He will, in time, hand it to his student. The "
    "bow will last a thousand years. So, somehow, will the "
    "peace.",
    None)
P[630]["ending"] = "best"
P[630]["title"] = "The Bow at Tōkin-ji"


# Final ending fallback for the "fled the reeds" path so it isn't a dead end:
passage(640,
    "You arrive at Black Crow on the seventh day with no winds "
    "and no companions and the memory of a girl in a tree-line "
    "still in your chest. You walk the causeway alone, sword "
    "drawn, half-mad with shame.\n\n"
    "Hayabusa Mōri meets you on the causeway. He does not need "
    "to draw the Yasha-no-Tachi. He looks at your face — really "
    "looks at it — and *sees* what you abandoned in the reeds. "
    "And the demon in the blade sees too. And the demon laughs.\n\n"
    "Hayabusa cuts you down with a single stroke. You die in "
    "the salt water at the lake's edge. The country burns on "
    "schedule. The demon walks.",
    None)
P[640]["ending"] = "bad"
P[640]["title"] = "Shame in the Salt Water"


# Re-route orphan 399 — small "walk away" ending — make it reachable from
# the alternative passage 282 path:

# Make sure 124 (the road-after-coward) eventually has a tougher fate:
P[124]["choices"] = [(640, "Continue toward Black Crow, friendless and ashamed")]


# Re-link some passages that had dangling pointers to old IDs:
# 165 had a single choice to 190 — already in place.
# 175 had a single choice to 190 — already in place.
# 200 had a single choice to 190 — already in place.


# Sprinkle some small extra story passages and link them via existing flavour
# spots:

passage(650,
    "On the first night below Mount Suzaku you sleep in a wood-"
    "cutter's empty hut. You dream of your master at the prayer "
    "stone — but in the dream he is whole, and very young, and "
    "he is laughing at something a one-eyed man has just said. "
    "You wake with the sound of the laugh in your ear and you "
    "do not move for a long time afterward.",
    [(31, "Wake and walk")])

passage(651,
    "You walk past a roadside Jizō shrine. You stop. You put one "
    "of your few coins on the stone before the small stone "
    "child. You do not pray; you have nothing left to pray *for* "
    "today.\n\n"
    "As you turn away, you could swear the Jizō's stone face has "
    "moved — a small, kind smile. You walk on. You are perhaps "
    "imagining things. You are perhaps not.",
    [(31, "Walk on")])

passage(652,
    "An old farmer on the road, hauling firewood, stops to "
    "study you. \"Young master,\" he says, \"you are walking "
    "toward something that is walking toward you. Be careful "
    "not to meet too suddenly.\"\n\n"
    "He bows. He shoulders his bundle. He walks on. You watch "
    "him go and you do not, in fact, ever see him again — "
    "though you will think of him, in the small hours, more "
    "often than you would expect.",
    [(31, "Walk on")])


# Re-link the descent so the new flavour passages are reachable.
# Replace the original passage(30) choice list:
P[30]["choices"] = [(650, "Sleep one night in the woodcutter's hut")]
P[650]["choices"] = [(651, "Walk on past the Jizō shrine")]
P[651]["choices"] = [(652, "Meet the old farmer")]
P[652]["choices"] = [(560, "Return to the temple one last time")]
P[560]["choices"] = [(561, "Search the ruined kitchens once more")]
P[561]["choices"] = [(562, "Find the old bow")]
P[562]["choices"] = [(31, "Descend to the fork in the road")]


# Re-link Karasu-juku flavour back to existing nodes:
P[600]["choices"] = [(601, "Break out the window with your sword-hilt"),
                     (602, "Wet your robe and try the main stair"),
                     (603, "Climb up to the roof through the smoke-hatch")]

# Tide-shrine alt-arc — reachable by adding a choice from the gathering:
P[180]["choices"] = [(210, "Begin the Fire teaching"),
                     (400, "Detour to Mikuriya to learn the Water directly")]


# Bandit road encounter — link from descent
P[31]["choices"] = [(40, "North, along the river"),
                    (60, "East, into the bamboo wood"),
                    (80, "West, to the hot spring"),
                    (420, "Take the north-river road but stop to investigate smoke")]

# Kitsune encounter — link from bamboo road
P[60]["choices"] = [(61, "Tell him: both"),
                    (62, "Tell him only of the grief"),
                    (63, "Ask who he is to bar your road"),
                    (440, "Pass the wayside shrine first")]
P[440]["choices"] = [(441, "Sit with her and take the peach"),
                     (442, "Bow politely and walk on"),
                     (443, "Comment on her shadow")]
P[447]["choices"] = [(61, "Walk on into Hisame, both wind and grief")]
P[446]["choices"] = [(61, "Walk on into Hisame")]
P[445]["choices"] = [(61, "Walk on into Hisame")]
P[444]["choices"] = [(447, "Ask what she means")]


# Pre-castle camp branch — link from 213 or 250 so the player gets the rest
P[213]["choices"] = [(450, "Camp the night before Black Crow")]
P[450]["choices"] = [(451, "Walk down to the lake alone"),
                     (452, "Test the kitsune's peach pit"),
                     (250, "Sleep, and choose at dawn")]
P[451]["choices"] = [(250, "Choose your approach in the morning")]
P[452]["choices"] = [(250, "Choose your approach in the morning")]


# Tide-shrine in-passage routing (already mostly OK; ensure 400 link)
# Already done above.


# Inner-keep exploration — link from the sneak passage
P[270]["choices"] = [(271, "Strike from behind the curtain"),
                     (272, "Step out and call his name"),
                     (273, "Wait — and sing the Water-mantra from cover"),
                     (520, "Slip aside through the keep first")]
P[520]["choices"] = [(521, "Free him"),
                     (522, "Speak to him through the doorway"),
                     (523, "Pass him by")]
P[521]["choices"] = [(524, "Receive the Fire from Brother Donkō")]
P[524]["choices"] = [(525, "Climb toward the high hall")]
P[525]["choices"] = [(526, "Step over him quietly"),
                     (527, "Check whether he is alive first"),
                     (528, "Cut his throat to be sure")]


# Pilgrim approach (252) — extended
P[252]["choices"] = [(480, "Walk up the causeway openly"),
                     (280, "Skip the pleasantries and go straight to the hall")]

# Storm/assault — extended
P[253]["choices"] = [(500, "Form up Tetsu's old soldiers in the wood")]
P[500]["choices"] = [(501, "Lead the assault on the outer wall")]
P[501]["choices"] = [(502, "Press into the courtyard"),
                     (266, "Hold the courtyard until dawn")]
P[502]["choices"] = [(266, "Hold the courtyard until dawn")]

# Wait — extended
P[254]["choices"] = [(510, "Wait — Hayabusa will come down on the second night")]
P[510]["choices"] = [(511, "Walk out onto the causeway alone")]

# Great-fight expansion
P[330]["choices"] = [(530, "Match him stroke for stroke")]
P[530]["choices"] = [(531, "Strike at his grip — to disarm only"),
                     (532, "Strike to wound — slow him, do not kill"),
                     (533, "Strike to kill before the demon takes him fully")]

# Ride-home passages
P[390]["choices"] = []  # ending stays terminal
# But we can branch *into* 390 via 540/541/542 to enrich the ending lead-in.
# 322 already goes to 390. We'll add a chain that flows 322 -> 540 -> 541 -> 542 -> 390:
P[322]["choices"] = [(540, "Walk out of Black Crow Castle with Hayabusa beside you")]
P[540]["choices"] = [(541, "Ride south")]
P[541]["choices"] = [(542, "Be met by Genshin at the foot of Mount Suzaku")]
P[542]["choices"] = [(390, "Continue to the final passage")]

# Best-bow ending path: if you took the bow at 562, give a chance after 390
# to swap to 630. We'll link 562 -> 31 normally, but add a flag-free shortcut:
# (simpler: link 542 also to 630 with a small choice)
P[542]["choices"] = [(390, "Reach the final passage"),
                     (630, "Return with the temple bow at your back, if you carried it")]

# 552 follow-up: link Ayane's water teaching back to Earth
P[211]["choices"] = [(552, "Sit by the stream with Ayane and learn"),
                     (212, "Skip ahead to Earth teaching")]
P[552]["choices"] = [(212, "Continue to Earth")]

# 611, 612, 613 — link from the camp scene
P[610]["choices"] = [(611, "Sit with Kiri"),
                     (612, "Sit with Ayane"),
                     (613, "Sit with Tetsu")]
P[612]["choices"] = [(213, "Ride for Black Crow")]
P[613]["choices"] = [(213, "Ride")]
P[611]["choices"] = [(213, "Ride for Black Crow")]

# Insert 610 into the lead-up: from 212 you go to 213; let's add a side-link
P[212]["choices"] = [(213, "Drink — and ride at dawn"),
                     (610, "Take one more morning to rest with your companions")]

# Smoke-out alt: from 125 add a smoke choice
P[125]["choices"] = [(163, "Slip out the window"),
                     (164, "Open the door with sword drawn"),
                     (600, "Wake to the smell of smoke")]

# Make a small change to 580 — exit forward
P[580]["choices"] = [(222, "Walk out of Hōrai")]

# Karasu-juku quick-meeting alt:
P[620]["choices"] = [(180, "Sit and tell")]

# Final: route some flavour passages forward
P[570]["choices"] = [(211, "Continue to the Water teaching")]
P[571]["choices"] = [(212, "Continue to the Earth teaching")]
P[572]["choices"] = [(213, "Ride")]
# Hook 570/571/572 in by adding them at the end of 210/211/212 instead:
P[210]["choices"] = [(570, "Sit with Hana for a while before sleep"),
                     (211, "Move on to the Water teaching")]
P[211]["choices"] = [(571, "Wake at midnight and sing the mantra to the stream"),
                     (552, "Sit by the stream with Ayane and learn"),
                     (212, "Skip ahead to Earth teaching")]
P[212]["choices"] = [(572, "Be walked to the village gate at dawn by Genshin"),
                     (213, "Drink — and ride at dawn"),
                     (610, "Take one more morning to rest with your companions")]

# Hook up the cellar-exploration path under the sneak-in route
P[251]["choices"] = [(460, "Surface in the cellar — and look around carefully"),
                     (270, "Climb straight toward the chanting")]

# Hook up the salt-gate alt-end paths (399, 590)
# 282 lets Hayabusa swing if Takeshi simply *walks away*:
P[282]["choices"] = [(285, "Strike him across the table"),
                     (286, "Drink the tea first"),
                     (399, "Sheathe your sword, bow, and walk away")]

# Hook up the lone wandering ending
P[321]["text"] = P[321]["text"]  # unchanged; but offer 590 as a darker alt
# Add 590 reachable via 323's "lord" path? No — 590 is a softer alt: link from 538
P[538]["text"] = P[538]["text"]
# Simpler: hook 590 from 360 as a fourth option
P[360]["choices"] = [(361, "Take the Yasha-no-Tachi back to Tōkin-ji for re-sealing"),
                     (362, "Drive your wakizashi through the Yasha-no-Tachi and break it"),
                     (363, "Carry the Yasha-no-Tachi to the salt lake and drop it in the deep water"),
                     (364, "Take up the Yasha-no-Tachi yourself"),
                     (590, "Leave the blade where it lies and walk away from all of it")]

# Hook 265 back: 253 -> 500 -> 501 -> (502, 266) ... but the keep-rush solo
# path 265 should be reachable from the assault branch too
P[502]["choices"] = [(266, "Hold the courtyard until dawn"),
                     (265, "Leave them; rush the keep alone before the moon climbs")]
P[265]["choices"] = [(280, "Face him alone in the high hall")]

# Hook 331 back: 330 -> 530 was added, but 331 is the "hold and wait" branch
P[330]["choices"] = [(530, "Match him stroke for stroke"),
                     (331, "Hold; sing; wait for an opening to give the fourth wind")]
P[331]["choices"] = [(322, "Speak the fourth wind")]

# Hook 550, 551 — these are an Ayane-ride detour from the Karasu-juku branch
P[177]["choices"] = [(550, "Ride east with Ayane through cold dawn"),
                     (180, "Go meet Tetsu and the others at the eastern shrine first")]
P[551]["choices"] = [(180, "Join the gathering")]

# Hook 580 — forest sleep before walking out of Hōrai
P[222]["choices"] = [(580, "Sleep one night in the forest first"),
                     (250, "Walk out and approach Black Crow alone")]

# Hook 620 / 621 — the "second meeting" alt route from Karasu-juku
P[143]["choices"] = [(141, "Follow him to the back room"),
                     (621, "Sneak out before dawn instead, to ride for the eastern shrine")]

# Fix small issue: 162 only goes one way; give a small "second thoughts" option
P[162]["choices"] = [(184, "Press on alone toward Black Crow"),
                     (185, "Turn aside into the forest of Hōrai to find Earth")]


# =============================================================================
# EXTRA STORY PASSAGES — push us toward 400
# =============================================================================

passage(700,
    "On the road north from Hisame, Kiri walks beside you. The "
    "morning fog clings to the cedars. After a long silence she "
    "says:\n\n"
    "\"Your master saved me from a snowfield when I was eleven. I "
    "had been left to die — my village had decided I was bad luck "
    "after the burning. He carried me three days to a temple. He "
    "stayed with me a week, until the fever broke, and then he "
    "left without telling me his name. I found it out years "
    "later. I have been waiting to repay him ever since.\"\n\n"
    "She looks at you. \"You are how I repay him, samurai. "
    "Forgive me if I am sometimes — more careful with you than "
    "you would like.\"",
    [(701, "Walk on beside her")])

passage(701,
    "You walk on. The fog thins. The road climbs out of the "
    "cedars into open hills. You do not speak for a long time.\n\n"
    "Then she says: \"Thank you for not saying anything stupid.\"\n\n"
    "And you nod. And you walk on.",
    [(180, "Continue toward the gathering")])

passage(702,
    "On the road north, Tetsu drinks. He always drinks. But on "
    "the second night around the fire he sets the flask down and "
    "says, almost shyly:\n\n"
    "\"Monk-boy. I was the soldier who held the Earth-stance "
    "the night your master broke the first seal on the Yasha. I "
    "was nineteen years old. I was so frightened my legs would "
    "not stop shaking. Akiyama set his hand on my shoulder and "
    "said, *Tetsu, the Earth does not require a man whose legs "
    "do not shake. It requires a man who is still standing when "
    "the shaking stops.* I have lived on that one sentence for "
    "forty years. I pass it on, monk-boy. Live on it too.\"\n\n"
    "He picks up the flask. He drinks. The fire pops.",
    [(180, "Travel on")])

passage(703,
    "Genshin, on the morning you ride out of Hisame, hands you "
    "a small paper bundle. \"Open it at Black Crow, not before. "
    "It is not a weapon. It is not a charm. It is — let us say "
    "— a *reminder*.\"\n\n"
    "You tuck it into your robe. You will, of course, forget it "
    "exists until the very last possible moment. That is what "
    "such bundles are for.",
    [(213, "Ride")])

passage(704,
    "At the gates of Black Crow, in the dawn cold, you remember "
    "Genshin's bundle. You unwrap it. Inside is a single white "
    "flower — pressed, dried, half a century old — and a paper "
    "note in your master's own hand.\n\n"
    "*Takeshi. If you are reading this, the road has carried "
    "you all the way. I knew, when I took you in, this day might "
    "come. I am sorry to have not been the master who could have "
    "spared you this. Carry the Fire kindly. Carry the song "
    "carefully. And remember — Hayabusa is, also, my student. "
    "Treat him as you would have treated yourself, had the "
    "blade found you instead. — A.*\n\n"
    "You close your fist around the flower. You walk in.",
    [(250, "Choose your approach")])

passage(705,
    "The morning of the True Sealing, your hand goes to the "
    "small dried flower Genshin gave you. It is in your fist as "
    "you sing the Water-mantra. It is in your fist when the "
    "fourth wind rises in you. It is in your fist when the "
    "demon-steam goes into the small stoppered jar.\n\n"
    "When you open your hand afterward, the flower has bloomed "
    "again — perfectly white, perfectly fresh, perfectly "
    "impossible. You will keep it for the rest of your life.",
    [(390, "Walk out")])

passage(706,
    "At the inner door of Black Crow's high hall you pause. You "
    "set the dried flower from your master on the threshold "
    "stone. You bow once, to a man not present.\n\n"
    "Then you walk in.",
    [(280, "Sit before Hayabusa Mōri")])

passage(707,
    "On the night before the assault on Black Crow, you cannot "
    "sleep. You walk down to where Tetsu's old soldiers have "
    "made their camp. They are quiet around the fire, oiling "
    "swords, checking armour, writing — some of them — small "
    "letters they will leave with Tetsu in the morning, in case.\n\n"
    "You sit with them. They make room. They do not ask who you "
    "are, because they already know. They pour you sake. You "
    "drink. You stay until the moon is half-down, and when you "
    "walk back to your own fire you have made forty-three "
    "promises in your heart that you cannot, possibly, all keep "
    "— and you are determined to keep every one.",
    [(213, "Ride for Black Crow")])

passage(708,
    "Above the salt lake, on the last evening before Black "
    "Crow, you sit alone with the broken sword-tang of "
    "Kōgetsumaru in your lap. You turn it over and over in your "
    "hands.\n\n"
    "It was your master's sword. It was the first sword you "
    "ever held — when you were six, when he sat you on his "
    "knee and let you hold it just for a moment under his "
    "hand. You were so afraid of dropping it that you started "
    "to cry. He laughed, gently, and said: *Takeshi, the "
    "sword is not afraid of you, and you should not be afraid "
    "of it. You should both be afraid of the same thing — "
    "doing wrong.*\n\n"
    "You wrap the broken tang in a clean cloth. You tuck it "
    "away. Tomorrow it will not help you. But it has helped "
    "you tonight.",
    [(213, "Sleep, and ride at dawn")])

passage(709,
    "On the second day's ride from Karasu-juku, you pass a "
    "small farm. A woman is hanging laundry. A baby cries from "
    "the house. A dog barks at your horses and is shushed.\n\n"
    "Tetsu reins in, very briefly. He watches the laundry for "
    "a long moment. Then he kicks his horse forward.\n\n"
    "\"Forty years ago,\" he says, when you have ridden out of "
    "sight, \"that was my farm. That was my wife. That was my "
    "boy. They are not there anymore. Other people live there "
    "now. I am glad of it. I do not stop.\" He drinks. \"I do "
    "not stop, monk-boy. Mind that you also keep moving "
    "past.\"",
    [(180, "Ride")])

passage(710,
    "On the road to Black Crow you pass a wandering monk going "
    "the other way. He carries a great-staff. He looks weary "
    "but kind.\n\n"
    "He stops in the road. He looks at you a long moment. He "
    "says: \"Akiyama's last? I am Brother Donkō. I escaped from "
    "Black Crow Castle three nights ago. The chains were not "
    "well-made, and the captain on the keep-stair was sleeping "
    "soundly. I bring word from inside.\"",
    [(711, "Listen")])

passage(711,
    "Donkō tells you: that the moon is nearly full, that "
    "Hayabusa Mōri is alone in the high hall, that his soldiers "
    "are uneasy and have been deserting since the last "
    "moon. That the inner gate is guarded by a *gaki* in red "
    "armour that must be fought with steel blessed at the "
    "tide-shrine, and by no other steel. That the salt-gate "
    "under the keep is unguarded.\n\n"
    "He gives you a small phial of black water — \"Take this. "
    "Pour it on your sword's edge before the *gaki*. The tide-"
    "shrine maiden made it for me before they took her.\"",
    [(250, "Choose your approach with all this knowledge")])

passage(712,
    "You ride. Three days. Four. By the fifth you can see, far "
    "ahead, the dark tooth of Black Crow Castle on the spur of "
    "the dead volcano. Tetsu reins in. \"Tonight,\" he says. "
    "\"Camp here. Tomorrow we ride at dawn and we are at the "
    "lake by noon. Sleep well, monk-boy. It is the last "
    "easy sleep.\"",
    [(450, "Camp")])

passage(713,
    "You cross a small wooden bridge above a fast stream. On "
    "the bridge, an old beggar sits with his back against the "
    "rail. He holds out a wooden bowl as you pass.\n\n"
    "His eyes are entirely black, no white at all.",
    [(714, "Drop a coin in the bowl"),
     (715, "Draw your blade"),
     (716, "Walk past without looking")])

passage(714,
    "You drop a coin. The beggar's blue-white face splits in a "
    "grin too wide for any human face.\n\n"
    "\"Bright,\" he whispers. \"Bright bright bright. Such a "
    "*bright* one. Coin will not feed me, samurai. Sit. Sit "
    "and let me have the bright thing in your chest. I will be "
    "so very gentle.\"\n\n"
    "His hand closes on your wrist. His grip is iron — colder "
    "than iron.",
    [(715, "Draw — better late than dead")])

passage(715,
    "You draw. The *gaki* — for that is what it is — lunges. "
    "If you have the phial of black tide-water from Brother "
    "Donkō, you have time to pour it on your edge. Otherwise "
    "your steel will pass through the thing with no resistance "
    "and the next minute will be the last minute of your life.",
    [(716, "Run, sword still drawn, before it touches you")])

passage(716,
    "You run. The *gaki* shrieks behind you but does not "
    "follow onto the road — it is bound to the bridge, perhaps, "
    "or to some old grief. You run for a long time. When you "
    "stop, your legs shake.\n\n"
    "(Steel will not bite a *gaki*. You knew this in theory. "
    "You know it now in practice. Mind the next bridge, "
    "samurai.)",
    [(180, "Continue with renewed caution")])

passage(720,
    "At the foot of Mount Suzaku, before you descend, you "
    "stand a long moment looking back up at the ruin of your "
    "temple. The smoke is gone. The crows have moved on. The "
    "rain has finally stopped.\n\n"
    "You think: *I do not know if I will see this place again. "
    "I do not know if I will be the same person if I do.*\n\n"
    "You bow once. You turn. You descend.",
    [(31, "The road forks below")])

passage(721,
    "At the river road, before the fork, you stop at an old "
    "stone well. You draw water. You wash the ash from your "
    "hands. You wash the blood from your sleeves. You wash "
    "your face.\n\n"
    "When you stand from the well, you are still tired and "
    "still grieving. But you are clean. You bow to the well. "
    "You move on.",
    [(31, "The fork")])

passage(722,
    "An old woman by the road offers you a rice ball wrapped "
    "in a leaf. \"Eat, young master. You are too thin. You "
    "have a long walk ahead.\"\n\n"
    "You eat. You thank her. She watches you go with a small, "
    "knowing smile that you do not entirely understand.\n\n"
    "(You will, much later, learn she was the kitsune Kogane "
    "in another shape. She has, in her own quiet way, blessed "
    "your road. The rice ball was real. The kindness, too.)",
    [(31, "Walk on")])

passage(723,
    "Down the river road from Karasu-juku, in a stretch of "
    "swampy ground, you see lanterns drifting at knee-height "
    "between the reeds. *Hitodama* — the souls of the recent "
    "dead, finding their way.\n\n"
    "You bow as you pass them. You count six. One of them, "
    "you are almost sure, has the curve of a child's small "
    "shoulder.",
    [(180, "Walk on, more quietly")])

passage(724,
    "On a stretch of road in the bamboo wood, you pass a small "
    "shrine to Hachiman, the god of war. Tetsu — who is "
    "riding beside you today — dismounts without comment. He "
    "walks to the shrine. He kneels. He puts a single old "
    "square coin on the offering stone. He bows. He stands.\n\n"
    "He does not explain. He never explains. He gets back on "
    "his horse and rides.",
    [(180, "Ride on")])

passage(725,
    "On the third day of your training with Genshin you ask "
    "him: \"Master, why did you not come down out of Hisame "
    "yourself? Why did you wait for me?\"\n\n"
    "He is quiet a long time. Then: \"Because, Takeshi, the "
    "Fire requires hands. *Two* hands. Mine are too old. They "
    "shake. They could not have held what needs to be held in "
    "Black Crow. And because — \" his single tea-coloured eye "
    "fixes on you, \" — because Akiyama would have been "
    "*livid* if I had set foot off this mountain before his "
    "student arrived. He always was a stubborn old man about "
    "his students.\"",
    [(210, "Continue training")])

passage(726,
    "Ayane, on a long ride east, sings a small old "
    "lullaby — not the Water-mantra, just a children's song. "
    "Her voice is rough with grief but the song is gentle.\n\n"
    "When she finishes, you ride beside her in silence for a "
    "long mile. Then she says, quietly: \"My mother used to "
    "sing me that one. I have not been able to make myself "
    "sing it since she died.\"\n\n"
    "She wipes her cheek with the back of her hand. She "
    "kicks her horse forward. The lullaby stays in your "
    "head.",
    [(180, "Ride after her")])

passage(727,
    "Kiri, on a still afternoon, teaches you something her "
    "old kunoichi-master taught *her*: how to walk so that you "
    "leave no track. It is not a technique of the body but of "
    "the attention. You have to *want*, deeply and without "
    "noise, to leave nothing behind. Most people cannot. Most "
    "people would rather be remembered.\n\n"
    "You practise for an hour. By the end you are leaving no "
    "track on the dust of the road. Kiri laughs — really "
    "laughs — for only the second time in your hearing.\n\n"
    "\"You will be very good at this, samurai. You may not "
    "thank me for it. But you will be very good at this.\"",
    [(180, "Travel on")])

passage(728,
    "In a small village three days from Black Crow, an old "
    "woman beckons you to her doorstep. She presses into your "
    "hand a small bundle of *senbon* — long iron needles, "
    "polished to a high shine.\n\n"
    "\"Take them, samurai. My son was a *gaki*-hunter on the "
    "north coast. He died last year. He left these. Iron from "
    "a struck temple bell, blessed at the tide-shrine. They "
    "bite hungry ghosts where ordinary steel will not. Take "
    "them. Use them well.\"\n\n"
    "She bows. She closes the door.",
    [(180, "Carry the needles on")])

passage(729,
    "On a small bridge two days from Black Crow you meet a "
    "young samurai going the other way. He bows. You bow. He "
    "is perhaps your age. His sword is good, his face is "
    "honest.\n\n"
    "\"Brother,\" he says. \"You go north. I would not. I came "
    "from Black Crow three days ago — I was foolish enough to "
    "approach it alone. The lord there is no longer a man. The "
    "blade he carries is no longer a blade. Turn aside. "
    "Whatever you came to do, it cannot be done.\"",
    [(730, "Thank him and ride on anyway"),
     (731, "Sit with him a while and learn what he saw")])

passage(730,
    "\"Thank you, brother,\" you say. \"But I am Akiyama's "
    "last, and I am going.\"\n\n"
    "His eyes widen. Then, slowly, he bows — deep, the bow "
    "you give to a teacher. \"Then you must. May the wind go "
    "with you.\" He rides on.",
    [(180, "Ride on")])

passage(731,
    "He tells you: that the high hall holds a forge re-lit "
    "after centuries; that Hayabusa Mōri kneels before it day "
    "and night; that the salt lake whispers; that the *gaki* "
    "at the inner gate must be fought with blessed steel; "
    "that the soldiers in red armour are good men who serve "
    "for old reasons and would, perhaps, lay down their arms "
    "if their captain told them to. \"Their captain is the "
    "burn-scarred one. He sleeps on the keep-stair. He is — \" "
    "the young samurai hesitates — \" — perhaps not entirely "
    "their master's man any longer.\"\n\n"
    "He bows. He rides on. You ride.",
    [(180, "Ride on with new knowledge")])


# =============================================================================
# Re-link the new flavour passages so they're reachable
# =============================================================================

# Add an opening choice from the descent for atmospherics:
P[30]["choices"] = [(720, "Look back up at the temple one last time"),
                    (650, "Sleep one night in the woodcutter's hut")]
P[720]["choices"] = [(721, "Wash at the old well at the river road"),
                     (31, "Walk straight on to the fork")]
P[721]["choices"] = [(722, "Take a rice ball from an old woman by the road"),
                     (31, "Walk on")]
P[722]["choices"] = [(31, "Walk on to the fork")]

# Add a hitodama passage as a north-road flavour:
P[40]["choices"] = [(41, "Try the larger inn"),
                    (42, "Try the smaller inn"),
                    (43, "Approach the girl on the steps"),
                    (44, "Slip past town entirely and follow the riders by night"),
                    (723, "Pass through the lantern-lit reeds first")]
P[723]["choices"] = [(40, "Walk on into Karasu-juku afterward")]

# Add the bridge gaki passage as a Hisame-area road flavour:
P[67]["choices"] = [(69, "Ask him to teach you the Fire wind"),
                    (70, "Ask why he hid this from you all your life"),
                    (71, "Ask if he will come with you"),
                    (713, "Tell him you crossed a bridge with an odd beggar")]
P[713]["choices"] = [(714, "Drop a coin in the bowl"),
                     (715, "Draw your blade"),
                     (716, "Walk past without looking")]
P[714]["choices"] = [(715, "Draw — better late than dead")]
P[715]["choices"] = [(716, "Run, sword still drawn, before it touches you")]
P[716]["choices"] = [(180, "Continue with renewed caution")]

# Hook Tetsu's farm scene & Hachiman scene
P[149]["choices"] = [(180, "Sleep and ride"),
                     (709, "Hear Tetsu speak of his lost farm in the morning"),
                     (724, "Stop at a Hachiman shrine in the bamboo wood")]
P[709]["choices"] = [(724, "Stop later at a Hachiman shrine"),
                     (180, "Ride on")]
P[724]["choices"] = [(180, "Ride on")]

# Hook the Brother Donkō encounter on the road
P[180]["choices"] = [(210, "Begin the Fire teaching"),
                     (400, "Detour to Mikuriya to learn the Water directly"),
                     (710, "Pass a wandering monk on the road")]
P[710]["choices"] = [(711, "Listen to Brother Donkō")]
P[711]["choices"] = [(250, "Choose your approach with all this knowledge")]

# Hook 712 (the camp before Black Crow) and 707/708 (camp atmospherics)
# Replace 450 fork:
P[450]["choices"] = [(451, "Walk down to the lake alone"),
                     (452, "Test the kitsune's peach pit"),
                     (707, "Sit with Tetsu's old soldiers tonight"),
                     (708, "Sit alone with your master's broken sword-tang"),
                     (250, "Sleep, and choose at dawn")]
P[707]["choices"] = [(213, "Ride for Black Crow"),
                     (250, "Choose your approach in the morning")]
P[708]["choices"] = [(213, "Sleep, and ride at dawn"),
                     (250, "Choose your approach in the morning")]
P[712]["choices"] = [(450, "Camp")]

# Hook 703, 704, 705, 706 — Genshin's bundle
P[572]["choices"] = [(703, "Take a paper bundle from Genshin"),
                     (213, "Ride")]
P[703]["choices"] = [(213, "Ride")]
P[704]["choices"] = [(250, "Choose your approach")]
P[705]["choices"] = [(390, "Walk out")]
P[706]["choices"] = [(280, "Sit before Hayabusa Mōri")]

# Hook the bundle into the approaches: from 250, give a "remember the bundle"
# option that goes to 704 first.
P[250]["choices"] = [(704, "Pause at the gate — remember the bundle"),
                     (251, "Sneak in by night, through the lake's salt-gate"),
                     (252, "Walk in openly at dawn, as a pilgrim"),
                     (253, "Storm the broken outer wall at dusk"),
                     (254, "Wait. Let Hayabusa come to you")]

# Hook 705 specifically into the sealing chain
P[391]["choices"] = [(705, "Open your fist on the flower"),
                     (390, "Walk out with him")]
P[706]["choices"] = [(280, "Sit before Hayabusa Mōri")]
# And let the pilgrim path optionally pause at the threshold:
P[481]["choices"] = [(706, "Pause at the inner door and set the flower down"),
                     (280, "Walk straight into the high hall")]

# Hook 725 — Genshin teaching reflection
P[210]["choices"] = [(570, "Sit with Hana for a while before sleep"),
                     (725, "Ask Genshin a question on the third night"),
                     (211, "Move on to the Water teaching")]
P[725]["choices"] = [(210, "Continue training"),
                     (211, "Move on to Water")]

# Hook 726 (Ayane lullaby)
P[550]["choices"] = [(551, "Ride with her in silence"),
                     (726, "Listen as she sings an old lullaby")]
P[726]["choices"] = [(551, "Ride on toward the shrine")]

# Hook 727 (Kiri's no-track lesson)
P[700]["choices"] = [(701, "Walk on beside her"),
                     (727, "Ask her to teach you something on the way")]
P[727]["choices"] = [(180, "Travel on")]

# Hook the kunoichi-passage chain: 159 -> 700 -> ...
P[159]["choices"] = [(700, "Travel north with her"),
                     (180, "Sit and tell her everything")]

# Tetsu's farm scene already linked. Add Donkō's chains alt-link:
# 461 -> 270 already. We've also got 520 from 270.
# Add a "stop at a village for needles" path before Black Crow:
P[712]["choices"] = [(450, "Camp"),
                     (728, "Pause at a village three days out")]
P[728]["choices"] = [(450, "Camp the next night at the lake")]

# Hook the wandering-samurai scene:
P[180]["choices"] = [(210, "Begin the Fire teaching"),
                     (400, "Detour to Mikuriya to learn the Water directly"),
                     (710, "Pass a wandering monk on the road"),
                     (729, "Cross paths with a young samurai coming the other way")]
P[729]["choices"] = [(730, "Thank him and ride on anyway"),
                     (731, "Sit with him a while and learn what he saw")]
P[730]["choices"] = [(180, "Ride on")]
P[731]["choices"] = [(180, "Ride on with new knowledge")]

# Hook 702 (Tetsu's earth-stance memory):
P[149]["choices"] = [(180, "Sleep and ride"),
                     (709, "Hear Tetsu speak of his lost farm in the morning"),
                     (702, "Hear Tetsu speak of your master in his youth"),
                     (724, "Stop at a Hachiman shrine in the bamboo wood")]
P[702]["choices"] = [(180, "Travel on")]


# =============================================================================
# Final padding for narrative — small descriptive passages used as bridges
# =============================================================================

passage(800,
    "The rain on the river road thins to mist. You walk in silence "
    "for a long time. Your sandals are wet. Your hands are cold. "
    "Your master's prayer beads click softly at your belt with "
    "every step.\n\n"
    "Once, far overhead, a heron flies north. You watch it until "
    "it is a speck. Then you walk on.",
    [(40, "Continue to Karasu-juku")])

passage(801,
    "The bamboo wood is darker than night has any right to make a "
    "forest. Your breath makes small clouds. Somewhere, a pheasant "
    "calls — short, sharp, surprised by your passage.\n\n"
    "You walk on.",
    [(60, "Continue toward Hisame")])

passage(802,
    "The west road climbs. The pines give way to cedar, the cedar "
    "to cloud. Your knees begin to ache before the third switch-"
    "back. You stop briefly at a small Jizō statue half-hidden in "
    "the moss. You bow. You walk on.",
    [(80, "Continue to Yumura")])

passage(803,
    "Somewhere on the road north, in a wayside teahouse, an old "
    "innkeeper refuses to take your coin. \"You have the look of "
    "Akiyama,\" she says — and she will say nothing more, but "
    "she presses an extra rice cake into your hand as you leave, "
    "and she watches the road behind you for an hour after you "
    "are gone.",
    [(180, "Continue")])

passage(804,
    "Beside a rice paddy at dusk, a farmer straightens to watch "
    "you pass. He says nothing. You nod. He nods. You walk on. "
    "Behind you, you hear him resume his work. The country goes "
    "about its business. The country always does, while the "
    "stories like yours move through it.",
    [(180, "Continue")])

passage(805,
    "A bell rings at a temple you cannot see. The sound is "
    "low and old. You stop on the road. You count six rings. "
    "After the sixth, the country is silent again. You walk on.",
    [(180, "Continue")])

passage(806,
    "On a clear morning, riding with your companions, you crest "
    "a ridge and see — far ahead, blue with distance — the "
    "outline of Black Crow Castle for the first time. It is "
    "smaller than you expected. Smaller and somehow worse for "
    "being smaller.\n\n"
    "Tetsu reins in beside you. \"There it is, monk-boy. The "
    "old place. Looks like nothing, does it not. The worst "
    "things always do.\"",
    [(180, "Ride on toward it")])

passage(807,
    "You stop briefly at a small mountain shrine that smells of "
    "incense and old wood. A single name is written on the "
    "offering box: *Akiyama Ryūnosuke*. It is your master's "
    "old name. He was here once, perhaps for a week, perhaps "
    "for a year, before he founded Tōkin-ji.\n\n"
    "You leave a coin. You leave a prayer. You walk on.",
    [(180, "Walk on")])

passage(808,
    "On the road, alone or with companions, you stop one "
    "afternoon at a wide, empty meadow. The grass is tall and "
    "green. The sky is impossibly clear. You stand a moment, "
    "and you think — for the first time since the temple "
    "burned — *the world is still very beautiful, in places. "
    "I had forgotten.*\n\n"
    "It is not a long thought. But it is enough.",
    [(180, "Continue")])

passage(809,
    "A small black cat crosses the road in front of you. It "
    "stops in the middle and looks at you, then continues on "
    "its way without hurry.\n\n"
    "Genshin, when you describe this to him later, will say "
    "only: \"Hmph. Good. A cat that does not hurry is a cat "
    "that is on its own business. Better than a cat that flees.\"",
    [(180, "Continue")])

passage(810,
    "You cross a small river by a rope bridge. The river runs "
    "fast and cold below. Halfway across, the bridge sways "
    "alarmingly. You stop. You take three slow breaths — the "
    "Fire-posture, used as Genshin meant it to be used, to "
    "steady you rather than to burn — and you finish the "
    "crossing. The bridge holds.\n\n"
    "On the far side, you bow back to the bridge. The bridge "
    "does not bow back, but neither does it complain.",
    [(180, "Continue")])

# Re-link the 180 hub to include the new flavour passages
P[180]["choices"] = [(210, "Begin the Fire teaching"),
                     (400, "Detour to Mikuriya to learn the Water directly"),
                     (710, "Pass a wandering monk on the road"),
                     (729, "Cross paths with a young samurai going the other way"),
                     (803, "Stop at a wayside teahouse"),
                     (804, "Pass a farmer at his paddy"),
                     (805, "Pause for a temple bell"),
                     (806, "Crest a ridge and see Black Crow for the first time"),
                     (807, "Stop at a small mountain shrine"),
                     (808, "Rest a moment in an empty meadow"),
                     (809, "Watch a black cat cross the road"),
                     (810, "Cross a rope bridge")]

P[803]["choices"] = [(180, "Continue")]
P[804]["choices"] = [(180, "Continue")]
P[805]["choices"] = [(180, "Continue")]
P[806]["choices"] = [(180, "Ride on toward it")]
P[807]["choices"] = [(180, "Walk on")]
P[808]["choices"] = [(180, "Continue")]
P[809]["choices"] = [(180, "Continue")]
P[810]["choices"] = [(180, "Continue")]


# Hook 800/801/802 into the fork
P[31]["choices"] = [(40, "North, along the river"),
                    (60, "East, into the bamboo wood"),
                    (80, "West, to the hot spring"),
                    (420, "Take the north-river road but stop to investigate smoke"),
                    (800, "Linger on the river road a while in the rain"),
                    (801, "Pause in the bamboo before going on"),
                    (802, "Sit a while at the foot of the climb to Yumura")]
P[800]["choices"] = [(40, "Continue to Karasu-juku")]
P[801]["choices"] = [(60, "Continue toward Hisame")]
P[802]["choices"] = [(80, "Continue to Yumura")]


# Make sure 399 has a satisfying outbound landing — it's an ending, so no
# outbound choices needed. But the rewind from it should be possible.

# Hook orphans 712 and 728 — second-to-last camp segment
P[806]["choices"] = [(712, "Ride toward the castle"),
                     (180, "Continue along the road")]


# =============================================================================
# Final 30+ passages — corridor of small encounters, ending touches
# =============================================================================

passage(820,
    "You wake one morning in the camp before Black Crow with your "
    "hand around the broken sword-tang of Kōgetsumaru. You do not "
    "remember reaching for it in the night. The metal is warm — "
    "warmer than the cold morning air should let it be.\n\n"
    "You think: *He is with me.* You do not believe it, exactly. "
    "But the thought helps.",
    [(450, "Get up and join the others at the fire")])

passage(821,
    "Tetsu, in the dawn, oils his sword with the slow patience of "
    "a man who has done this thousands of times. He does not look "
    "at you. He says quietly: \"You sleep noisily, monk-boy. Like a "
    "child. *Good*. That means you can still sleep at all. I have "
    "not slept properly in nineteen years. Sleep while you can.\"",
    [(450, "Sit at the fire")])

passage(822,
    "Kiri, in the dawn, has already been awake for hours. She "
    "sits cross-legged on a flat stone, watching the lake. When "
    "she hears you stir she does not turn.\n\n"
    "\"Look at the surface,\" she murmurs. \"Twice now since I sat "
    "down, the water has — *stilled*. Even when the wind was on it. "
    "He is doing something in there, samurai. Something is "
    "*listening*.\"",
    [(450, "Sit beside her")])

passage(823,
    "Ayane, in the dawn, has built up the fire. She is preparing "
    "tea. She glances up as you arrive. \"You did not eat last "
    "night. Eat now. My mother taught me — *do not let grief take "
    "your breakfast as well as your sleep.* The country runs on "
    "rice. Even endings.\"",
    [(450, "Eat and sit")])

passage(824,
    "Genshin, on the morning of your ride, sends a sealed letter "
    "ahead by pigeon to a friend at the imperial court. He does "
    "not say what is in it. He merely says: \"In case, monk-boy. "
    "In case.\"\n\n"
    "(You will, much later, learn that the letter was a full "
    "account of the road, the winds, and the four of you who "
    "rode for Black Crow. Genshin wanted, in case you all "
    "failed, the story written down somewhere. He was always a "
    "man who believed stories were a kind of seal.)",
    [(213, "Ride")])

passage(825,
    "On the causeway out from Black Crow, after the True Sealing, "
    "Hayabusa Mōri walks slowly. He is very old now. The Yasha-no-"
    "Tachi is iron at your hip; the demon is in a jar in your "
    "hand. He stops at the edge of the salt water. He bends, "
    "carefully, and washes his hands in the lake.\n\n"
    "\"There,\" he says quietly. \"Thirty years. Thirty *years*, "
    "boy. I have not been able to wash my hands since I was "
    "younger than you.\"",
    [(390, "Walk on with him to the final passage")])

passage(826,
    "The morning after the True Sealing, Hayabusa Mōri orders the "
    "soldiers of Black Crow to lay down their arms. They do, "
    "almost without protest — most of them have been waiting "
    "years for someone to give them permission. He releases them "
    "from his service.\n\n"
    "Forty-two of them ask to remain. Hayabusa, weeping, agrees. "
    "He will spend the rest of his days teaching them to be "
    "gardeners.\n\n"
    "The fortress becomes a hospice. The fortress becomes a "
    "kindness.",
    [(390, "Continue")])

passage(827,
    "On the road south, after Black Crow, Tetsu of the Burnt Hill "
    "develops a fever from his rib-wound. By the third day he "
    "cannot ride. You stop at a wayside inn. Kiri tends him for "
    "a week.\n\n"
    "On the seventh day he opens his eyes, weakly, and grins his "
    "lopsided one-eyed grin. \"Still here, monk-boy. Damn the "
    "old gods. I had been *hoping*.\" He laughs himself into a "
    "coughing fit. He survives. He will, in fact, live another "
    "fifteen years, and die in a sunny field with his boots off, "
    "which is more than most of his old regiment ever managed.",
    [(390, "Continue south")])

passage(828,
    "On the road south, after Black Crow, Kiri rides beside you "
    "for a long, silent afternoon. Then she says, very quietly:\n\n"
    "\"My village. The one Hayabusa's men burned eleven years "
    "ago. We will pass within a day's ride of it on the way back "
    "to Tōkin-ji. Would you — would you ride with me, when we "
    "do? I have not been back.\"\n\n"
    "You nod. \"Of course.\"\n\n"
    "She does not say thank you. She does not need to.",
    [(390, "Continue")])

passage(829,
    "On the road south, after Black Crow, Ayane sings the Water-"
    "mantra one last time — softly, just for herself — at a "
    "stream you stop at to water the horses. The mantra is no "
    "longer needed. The demon is in a jar. But the song was her "
    "mother's, and her mother's mother's, and the singing of it "
    "is its own kind of remembering.\n\n"
    "She finishes. She wipes her cheek with her sleeve. She "
    "mounts up. \"Ride on, samurai.\"",
    [(390, "Continue")])

passage(830,
    "Years later, you will sit on the steps of the rebuilt "
    "Tōkin-ji with a class of small children — eight of them, "
    "all freckled, all serious — and you will tell them a "
    "story about a young samurai who came down off a burning "
    "mountain a long time ago, and you will not, when you "
    "tell it, mention that the young samurai was you.\n\n"
    "They will guess, of course. Children always do.",
    [(390, "Continue to the final ending")])

passage(831,
    "Years later, you will receive a letter from Hayabusa Mōri "
    "in his hospice. *Dear Takeshi-san,* it will begin, *the "
    "gardens are doing well this autumn. The plum tree by the "
    "south wall has set fruit for the first time in twenty "
    "years. I think of you often, and of your master, and of "
    "the night you walked into the high hall with a song in "
    "your throat. The country has been good to me — better "
    "than I deserve. Thank you, again, brother. — H.*\n\n"
    "You will save it with the others.",
    [(390, "Continue to the final ending")])

passage(832,
    "Years later, you will sit at your master's cairn — now "
    "tended, with fresh moss, beneath a small wooden roof you "
    "built yourself — and you will tell him, aloud, in the "
    "long detail he would have wanted, about the road. About "
    "the four winds. About the boy named Jirō you carried to "
    "the spring. About the woman named Kiri you walk beside "
    "now in the rebuilt temple's courtyard.\n\n"
    "The cairn does not answer. But you know — in the way you "
    "*know* things that have no proof — that he hears.",
    [(390, "Continue to the final ending")])

passage(833,
    "You sit with little Jirō, in the rebuilt Tōkin-ji, on a "
    "winter afternoon. He is twelve again — no, he is "
    "fifteen now, and almost as tall as you. He has been your "
    "first novice for three years.\n\n"
    "\"Master,\" he says, \"why did you go back for me, that "
    "morning? You did not know me. I was only the rice-novice. "
    "You could have run straight to Master Akiyama.\"\n\n"
    "You think about this a long time.\n\n"
    "\"Because,\" you say at last, \"the cut of the willow is "
    "to lift the beam off the small thing pinned under it. That "
    "is the first lesson. The rest is footwork.\"\n\n"
    "He thinks about this. He nods. He goes off to chop wood.",
    [(390, "Continue")])

passage(834,
    "On a small mountain path one autumn, twenty years after "
    "Black Crow, you meet an old kitsune in the shape of a "
    "tea-stand seller. She offers you a cup. You take it. The "
    "tea is bitter and excellent.\n\n"
    "\"You did well, samurai,\" she says. \"The wind has been "
    "fond of you. I hear your name on it occasionally. *Mostly* "
    "fond.\"\n\n"
    "You smile. \"Only mostly?\"\n\n"
    "She winks. \"You were a *little* slow with the peach pit, "
    "samurai. The wind teases.\"",
    [(390, "Walk on, smiling")])

# Hook up the new passages
P[450]["choices"] = [(451, "Walk down to the lake alone"),
                     (452, "Test the kitsune's peach pit"),
                     (707, "Sit with Tetsu's old soldiers tonight"),
                     (708, "Sit alone with your master's broken sword-tang"),
                     (820, "Lie a while with your master's broken tang in your hand"),
                     (821, "Watch Tetsu oil his sword"),
                     (822, "Sit with Kiri above the still lake"),
                     (823, "Take Ayane's tea"),
                     (250, "Sleep, and choose at dawn")]
P[820]["choices"] = [(450, "Get up and join the others")]
P[821]["choices"] = [(450, "Sit at the fire")]
P[822]["choices"] = [(450, "Sit beside her")]
P[823]["choices"] = [(450, "Eat and sit")]

# Genshin's letter to court
P[572]["choices"] = [(703, "Take a paper bundle from Genshin"),
                     (824, "Watch Genshin send a pigeon south"),
                     (213, "Ride")]
P[824]["choices"] = [(213, "Ride")]

# Walk-out path: extend 390 with rich epilogue passages — but 390 is the
# ending, so insert epilogue passages *before* 390 in the chain.
P[540]["choices"] = [(825, "Walk slowly out to the causeway with Hayabusa"),
                     (541, "Ride south")]
P[825]["choices"] = [(826, "See the next morning's surrender of arms"),
                     (541, "Ride south")]
P[826]["choices"] = [(541, "Ride south the next day")]
P[541]["choices"] = [(827, "Tetsu falls ill on the road south"),
                     (828, "Kiri asks you to visit her ruined village"),
                     (829, "Ayane sings the mantra one last time at a stream"),
                     (542, "Be met by Genshin at the foot of Mount Suzaku")]
P[827]["choices"] = [(828, "Continue south"),
                     (542, "Reach Mount Suzaku")]
P[828]["choices"] = [(829, "Continue south"),
                     (542, "Reach Mount Suzaku")]
P[829]["choices"] = [(542, "Reach Mount Suzaku")]
P[542]["choices"] = [(830, "Tell the story to small children years later"),
                     (831, "Open a letter from Hayabusa Mōri years later"),
                     (832, "Sit at your master's cairn years later"),
                     (833, "Talk with little Jirō years later"),
                     (834, "Meet a kitsune as a tea-seller years later"),
                     (390, "Reach the final passage"),
                     (630, "Return with the temple bow at your back, if you carried it")]
for pid in (830, 831, 832, 833, 834):
    P[pid]["choices"] = [(390, "Continue to the final ending")]


# Confirm passages count
# (No code change needed; len(P) is the count.)

# ----- last fourteen passages to round out the road -----

passage(900,
    "On a wet afternoon at a wayside inn, you watch a small boy "
    "play knucklebones in the dirt. He is intent. He is happy. "
    "He has no idea who you are or where you have come from or "
    "where you are going.\n\n"
    "You think: *this is what the road is for.* Then you order "
    "another bowl of millet, and you eat slowly, and you let the "
    "afternoon pass without trying to make it serve anything.",
    [(180, "Travel on")])

passage(901,
    "A traveling priest at a roadside shrine asks if you would "
    "share his fire. You do. He boils tea. He asks no questions. "
    "After a long companionable silence he says, in the way of "
    "such priests, *Even the longest road is one step at a "
    "time, young master.* It is not an original thought. It is, "
    "tonight, the right one.",
    [(180, "Continue")])

passage(902,
    "On the road, you pass a wooden post nailed with a faded "
    "notice — a reward for the capture of a young samurai with "
    "a three-brushstroke token at his belt. The notice is "
    "three weeks old. The reward is generous.\n\n"
    "You remove it, fold it, and tuck it inside your robe. It "
    "will be useful, perhaps, as kindling. Or as a memento.",
    [(180, "Continue")])

passage(903,
    "A herd of deer crosses the road at dusk. The hind in the "
    "lead pauses, very briefly, to look at you. Her eyes are "
    "dark and entirely alive. Then she walks on, and the herd "
    "follows her, and the road is empty again.",
    [(180, "Continue")])

passage(904,
    "You sleep one night in an abandoned shrine where the "
    "thatch is mostly fallen in. The stars are bright through "
    "the broken roof. You count seven before you fall asleep. "
    "When you wake, your master's prayer beads have somehow "
    "found their way into your hand.",
    [(180, "Wake and walk")])

passage(905,
    "A small wandering child — perhaps six years old, perhaps "
    "seven — runs up to you on the road and presses a smooth "
    "river stone into your palm.\n\n"
    "\"For you, samurai!\"\n\n"
    "Before you can speak she has run off again, giggling, "
    "back toward a farmhouse you cannot see. You keep the "
    "stone. It is just a stone. It is also, somehow, exactly "
    "the gift you needed today.",
    [(180, "Walk on")])

passage(906,
    "On a hot afternoon, you sit in the shade of an old plum "
    "tree and watch your companions arguing — gently, "
    "ridiculously — about whose turn it is to brew the tea. "
    "Tetsu wins on the grounds of seniority. Tetsu's tea is "
    "terrible. Everyone drinks it. The plum tree's shadow moves "
    "across the road. The afternoon is, for one hour, "
    "blessedly ordinary.",
    [(180, "Travel on")])

passage(907,
    "An old soldier at a wayside inn recognizes Tetsu and "
    "stands to bow. Tetsu pretends not to see him. The old "
    "soldier sits back down with great patience and orders "
    "another flask, and as Tetsu leaves, he raises his cup in "
    "a small, silent salute. Tetsu does not turn back. But his "
    "shoulders shake very slightly. He is, you realize, "
    "laughing — or weeping — it is difficult to tell.",
    [(180, "Ride on")])

passage(908,
    "Kiri, on a still morning, teaches you the names of three "
    "birds you have never noticed before — the small grey one "
    "that calls at dawn, the green one in the bamboo, the "
    "white-throated one that nests near temples. \"My old "
    "master used to say: a kunoichi who does not know the "
    "birds of her road is a kunoichi who will be heard by them. "
    "Listen, samurai. They tell you who has just passed.\"",
    [(180, "Listen as you ride")])

passage(909,
    "Ayane, in a small town along the way, buys six rice cakes "
    "for the road. She gives you one before mounting up. \"My "
    "mother used to do this on every long road. She said — *a "
    "rice cake in the saddle-bag means you have a future to "
    "ride toward.* I keep doing it.\"\n\n"
    "You eat the rice cake later, on a cold afternoon, and it "
    "is the best one you have ever eaten.",
    [(180, "Ride on")])

passage(910,
    "At a wayside graveyard you stop briefly. None of the names "
    "are familiar. You bow to all of them anyway. Genshin, "
    "watching, says approvingly: \"Good. A samurai who does not "
    "bow to strangers' graves is a samurai who has forgotten "
    "how short the road is.\"",
    [(180, "Walk on")])

passage(911,
    "On the last leg of the journey to Black Crow, Genshin "
    "tells you a story about your master as a young man — a "
    "drunken night and a stolen horse and a long apology "
    "letter that took your master three days to write. \"He "
    "was so *embarrassed*,\" Genshin says, single eye "
    "twinkling. \"He never told you, of course. He never told "
    "*anyone*. But I was the one who held the brush while he "
    "dictated it through a terrible hangover. I have laughed "
    "about that letter for forty years.\"\n\n"
    "You laugh. Really laugh. It is — astonishing — the first "
    "laugh that has come out of you since the temple burned.",
    [(213, "Ride on")])

passage(912,
    "A small wandering kitten finds you at a wayside camp and "
    "refuses to leave. You feed it a strip of dried fish. It "
    "purrs. It rides on your shoulder for the next three days. "
    "When you reach the salt lake it leaps down and trots off "
    "into the reeds and is gone.\n\n"
    "(Genshin, when he hears about this later, will not be "
    "surprised. \"A small spirit, monk-boy. A small kindness "
    "sent ahead of you. Take it as such.\")",
    [(213, "Ride for Black Crow")])

passage(913,
    "On the morning of the ride to Black Crow, Tetsu's old "
    "soldiers form up in a long, ragged line beside the road. "
    "There are forty-three of them. As you and Tetsu ride past, "
    "each one bows — not to Tetsu, but to *you*. To the boy of "
    "Akiyama. To the one who carries the three winds.\n\n"
    "You are not used to being bowed to like this. You sit "
    "very straight on your horse. You do your best to look "
    "like a samurai who deserves it. Tetsu, beside you, smiles "
    "his lopsided one-eyed smile and says, very quietly: "
    "\"Good, monk-boy. *Good.* Carry it well today. They have "
    "all bet their lives on you.\"",
    [(500, "Ride to the wall")])

# Hook the last 14 into the road
P[180]["choices"] = [(210, "Begin the Fire teaching"),
                     (400, "Detour to Mikuriya to learn the Water directly"),
                     (710, "Pass a wandering monk on the road"),
                     (729, "Cross paths with a young samurai going the other way"),
                     (803, "Stop at a wayside teahouse"),
                     (804, "Pass a farmer at his paddy"),
                     (805, "Pause for a temple bell"),
                     (806, "Crest a ridge and see Black Crow for the first time"),
                     (807, "Stop at a small mountain shrine"),
                     (808, "Rest a moment in an empty meadow"),
                     (809, "Watch a black cat cross the road"),
                     (810, "Cross a rope bridge"),
                     (900, "Watch a small boy play knucklebones"),
                     (901, "Share a fire with a traveling priest"),
                     (902, "Find a wanted-poster of yourself"),
                     (903, "Watch deer cross the road at dusk"),
                     (904, "Sleep in an abandoned shrine under the stars"),
                     (905, "Be given a stone by a passing child"),
                     (906, "Drink Tetsu's terrible tea under a plum tree"),
                     (907, "Watch an old soldier salute Tetsu"),
                     (908, "Listen as Kiri teaches you the names of birds"),
                     (909, "Take a rice cake from Ayane in a small town"),
                     (910, "Bow at a wayside graveyard")]
for pid in (900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910):
    P[pid]["choices"] = [(180, "Continue")]

# Hook 911 and 912 into the final ride
P[213]["choices"] = [(450, "Camp the night before Black Crow"),
                     (911, "Hear Genshin tell a story about your master"),
                     (912, "Adopt a wayside kitten")]
P[911]["choices"] = [(450, "Camp the night before Black Crow")]
P[912]["choices"] = [(450, "Camp the night before Black Crow")]

# Hook 913 into the assault start
P[500]["choices"] = [(913, "Watch the old soldiers bow as you ride out"),
                     (501, "Lead the assault on the outer wall")]
P[913]["choices"] = [(501, "Lead the assault on the outer wall")]


# Final ending safety
for pid in (410, 465, 537, 538, 590, 630, 640):
    if pid in P and P[pid]["ending"] is None:
        P[pid]["ending"] = "bad"


# =============================================================================
# GAME ENGINE
# =============================================================================

ENDING_BANNERS = {
    "bad":      "*** AN ENDING — but not the only one. ***",
    "horrible": "*** AN ENDING — a dark one. ***",
    "ok":       "*** AN ENDING. ***",
    "good":     "*** AN ENDING. ***",
    "best":     "*** AN ENDING. ***",
}


def show_passage(pid):
    p = P[pid]
    _clear()
    print()
    if p.get("title"):
        print(f"  ~ {p['title']} ~".center(WIDTH))
        print()
    _slow(_wrap(p["text"]))
    print()
    if p["ending"]:
        print("-" * WIDTH)
        print(ENDING_BANNERS[p["ending"]].center(WIDTH))
        print("-" * WIDTH)
        print()


def choose(pid):
    p = P[pid]
    choices = p["choices"]
    if not choices:
        return None
    for i, (_, label) in enumerate(choices, 1):
        print(f"  {i}. {label}")
    print()
    while True:
        ans = _ask("Your choice (or 'q' to quit): ").lower()
        if ans in ("q", "quit", "exit"):
            print("\nThe wind carries your tale away unfinished.")
            sys.exit(0)
        if ans.isdigit():
            n = int(ans)
            if 1 <= n <= len(choices):
                return choices[n - 1][0]
        print(f"  (Enter 1-{len(choices)}.)")


def offer_rewind(history, rewinds_left):
    print()
    print("-" * WIDTH)
    if rewinds_left <= 0:
        print("  The spirits of your ancestors turn away. They have lifted")
        print("  you from death three times already. They will not do so a")
        print("  fourth.")
        print("-" * WIDTH)
        print()
        return False
    print(f"  A voice on the wind — your master's, perhaps — whispers:")
    print(f"  *Will you walk that path again, my student?*")
    print()
    print(f"  ({rewinds_left} rewind(s) remaining of three.)")
    print("-" * WIDTH)
    while True:
        ans = _ask("Rewind to your last choice? (y/n): ").lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no", "q", "quit"):
            return False


def title_screen():
    _clear()
    print()
    art = [
        "",
        "                  ~  T H E   C R I M S O N   B L A D E  ~",
        "                      a tale told in fragments",
        "",
        "                                |",
        "                                |",
        "                          ______|______",
        "                                |",
        "                                |",
        "                                *",
        "",
    ]
    for line in art:
        print(line.center(WIDTH))
    print()
    print("  A samurai-era choose-your-own-adventure.".center(WIDTH))
    print("  Many paths.  Many endings.  Only one is best.".center(WIDTH))
    print()
    print("  Your ancestors will lift you from death up to three times.".center(WIDTH))
    print("  After that, the wheel turns without you.".center(WIDTH))
    print()
    print("  (Type 'q' at any choice to leave the road.)".center(WIDTH))
    print()
    _ask("  Press ENTER to begin... ")


def play():
    title_screen()
    history = []          # stack of passage ids visited (for rewind)
    rewinds_left = 3
    current = 1

    while True:
        show_passage(current)
        p = P[current]

        # Terminal passage?
        if p["ending"]:
            tone = p["ending"]
            if tone in ("bad", "horrible"):
                if offer_rewind(history, rewinds_left) and history:
                    rewinds_left -= 1
                    # Pop the last *choice* node — i.e. the node we were at
                    # when we made the decision that led here.  We walk back
                    # one step.
                    current = history.pop()
                    continue
                else:
                    print()
                    print("  Press ENTER to end the tale.")
                    _ask("")
                    return
            else:
                # ok / good / best — let the player savour it
                print()
                _ask("  Press ENTER to end the tale.")
                return

        # Branching passage
        if not p["choices"]:
            print("  (The road ends here, untold.  Press ENTER.)")
            _ask("")
            return

        nxt = choose(current)
        if nxt is None:
            return
        history.append(current)
        current = nxt


# =============================================================================
# Self-check at import time — confirms every choice leads to a real passage.
# =============================================================================

def _validate():
    missing = []
    for pid, p in P.items():
        for nxt, _ in p["choices"]:
            if nxt not in P:
                missing.append((pid, nxt))
    if missing:
        print("WARNING: missing passage links detected:", missing, file=sys.stderr)


if __name__ == "__main__":
    _validate()
    play()
