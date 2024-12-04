label intro:
    # Play background music.
    $ play_music(sad_emotional, loop=True, fadein=2.0, fadeout=2.00)

    scene intro_0 with fade
    $ renpy.pause()
    scene intro_1 with fade
    $ renpy.pause()
    scene intro_2 with dissolve
    $ renpy.pause()
    scene intro_3 with dissolve
    $ renpy.pause()
    scene intro_4 with fade
    $ renpy.pause()

    scene 11 with fade
    "{i}Aslan approaches the throne, confident yet respectful. Today your father, the Sultan, has summoned you into his presence to say something important.{/i}"
    scene 12 with fade
    "{i}Aslan approaches, his eyes meeting his father's. The Sultan observes him with a mix of pride and a hint of melancholy.{/i}"
    sul "Aslan."
    asl "Father. You summoned me?"
    scene 13 with dissolve
    sul "Indeed. There's much to discuss."
    scene 14 with dissolve
    asl "Is something amiss?  You seem troubled."
    scene 13 with dissolve
    sul "(a weary sigh) Troubled? Perhaps.  The weight of a kingdom rests heavily on these old shoulders, son."
    sul "The weight of the crown... it's heavier than you know."
    asl_ "Heavier than I know?  He makes it sound like a burden, not a privilege."
    scene 14 with dissolve
    asl "You've borne it well for many years, Father.  Your reign has brought peace and prosperity to our people."
    asl "I'm eager to learn, Father. To bear that weight alongside you."
    scene 15 with dissolve
    sul "Eagerness is a valuable trait, but it can also be a dangerous one.  Ambition unchecked can consume a man."
    asl_ "Is he warning me? Or testing me?"
    sul "And... peace is a fragile thing, Aslan. Easily shattered. And prosperity can breed complacency, weakening us from within."
    scene 14 with dissolve
    asl "I understand, Father. We must remain vigilant.  But our armies are strong, our defenses secure."
    asl "And... ambition is also what drives us forward.  What builds empires."
    scene 13 with dissolve
    sul "Empires are built on more than just ambition, Aslan. They're built on wisdom, strategy... and sometimes, sacrifice."
    asl_ "Sacrifice?  What does he mean by that?"
    scene 16 with dissolve
    asl "I believe I've learned those lessons well from you."
    scene 13 with dissolve
    sul "Have you?  Tell me, Aslan, what do you see as the greatest threat to our kingdom?"
    asl_ "Is this a test? What does he want me to say?"
    scene 16 with dissolve
    asl "Complacency, as you said.  And perhaps... the ambition of our neighbors.  They watch us, Father. They envy our strength."
    scene 13 with dissolve
    sul "And what of our own ambitions, Aslan?  Are they not a threat as well?  Unchecked ambition can be a dangerous fire, consuming all in its path."
    asl_ "He's probing me. Trying to gauge my intentions."
    scene 16 with dissolve
    asl "Ambition is a tool, Father.  A weapon to be wielded wisely.  It can build empires, but it can also destroy them.  I intend to wield it with caution."
    scene 17 with dissolve
    sul "Caution is wise. But sometimes, a ruler must be bold.  Must take risks to secure his kingdom's future."
    sul "There's something I wish to discuss with you, something of great importance. But it requires another's presence.  Wait here. I've sent for Minister Yazir."
    scene 18 with dissolve
    asl "As you wish, Father."
    "{i}The doors to the throne room open, and Minister Yazir enters, his face etched with concern.{/i}"
    scene 19 with dissolve
    $ renpy.pause()
    scene 20 with dissolve
    mya "Your Majesty. You requested my presence?"
    scene 17 with dissolve
    sul "Yazir. Good of you to come so quickly.  Aslan and I were just discussing matters of state.  Matters that concern you as well."
    scene 20 with dissolve
    mya "Indeed, Your Majesty. I am at your service."
    scene 17 with dissolve
    sul "Yazir, you have served me faithfully for many years.  You've been my confidante, my advisor, and a steadfast friend.  I trust your judgment implicitly."
    scene 20 with dissolve
    mya "You honor me, Your Majesty."
    scene 17 with dissolve
    sul "Aslan, Yazir has been privy to my thoughts, my plans, my fears... perhaps even more so than you."
    sul "He understands the burden of leadership, the sacrifices required to maintain peace and prosperity."
    asl_ "Why is he speaking like this? What's he getting at?"
    asl "Minister Yazir's wisdom is well known, Father."
    scene 21 with dissolve
    sul "(taking a deep breath, his voice now strained) Wisdom... yes. Wisdom will be crucial in the days to come.  For both of you."
    scene 20 with dissolve
    mya "Your Majesty?  Are you unwell?"
    scene 21 with dissolve
    sul "Unwell... yes.  More than unwell, I fear.  The truth is, my friends... I am dying."
    scene 22 with dissolve
    "{i}Aslan and Yazir are stunned into silence.  The guards shift uneasily. The air in the throne room grows heavy with the weight of the unspoken.{/i}"
    scene 23 with dissolve
    asl "Father! What are you saying?  This… this must be some kind of jest."
    scene 24 with dissolve
    mya "Your Majesty, are you certain?  Perhaps the royal physicians…?  Surely something can be done!"
    scene 25 with dissolve
    sul "Enough.  There’s no need for theatrics.  The physicians have done all they can."
    sul "It’s… it’s beyond their skill now."
    scene 23 with dissolve
    asl "No!  I refuse to believe it. You are strong, Father. You’ve overcome so much!"
    scene 22 with dissolve
    sul "Strength fades, Aslan. Even the mightiest oak eventually succumbs to the storm."
    sul "My storm has come."
    scene 24 with dissolve
    mya "But… but the kingdom!  What will become of us without your guidance?"
    scene 25 with dissolve
    sul "That, my friends, is precisely why I called you here.  There is little time left.  We must ensure a smooth transition of power."
    sul "We must protect our people from the chaos that inevitably follows a ruler’s death."
    scene 23 with dissolve
    asl "Tell me what I must do, Father.  I will do anything."
    scene 25 with dissolve
    sul "Yazir, you will assist Aslan in this. You will guide him, advise him.  You will be his rock in the turbulent times ahead."
    scene 26 with dissolve
    mya "I swear it, Your Majesty.  I will serve Aslan with the same loyalty and devotion I have always shown you."
    $ renpy.pause()
    scene 27 with fade
    nar_nvl "{i}{size=35}The sun sets on every reign, as surely as it rises.  A wise monarch does not lament the end, but celebrates the dawn.  For in the annals of history, it is not the length of one's rule that matters, but the mark it leaves upon the world.{/size}{/i}"
    nar_nvl "{i}{size=35}I penned these words not long ago, a reflection on the ephemeral nature of power.  A reminder to myself that regret should not be for what was done, but for what was left undone.  For the lands unconquered, the desires unfulfilled, the dreams that remained tethered to the earth.{/size}{/i}"
    nar_nvl "{i}{size=35}From the day I revealed my fate to my son and my most trusted advisor, to the day the flames claimed my mortal shell, the weight of my words pressed upon them both.  Aslan, my heir, with fire in his heart and ambition burning in his eyes...{/size}{/i}"
    nar_nvl "{i}{size=35}...and Yazir, the steady hand, the voice of caution, forever wrestling with the tempestuous nature of his future Sultan.{/size}{/i}"
    nar_nvl "{i}{size=35}The cycle continues.  The sun sets, and a new dawn breaks. What will be written in the next chapter of our story? Only time will tell...{/size}{/i}"
    nar_nvl "{size=35}--The Sultan{/size}"
    scene 28 with fade
    $ renpy.pause()
    asl_ "Father... I can scarcely believe you're gone."
    scene 29 with dissolve
    asl_ "The weight of your words... the weight of the crown... it's all on my shoulders now."
    asl_ "You spoke of ambition... of the dangers and the rewards."
    scene 30 with fade
    $ renpy.pause()
    scene 31 with fade
    $ renpy.pause()
    asl_ "You spoke of sacrifice.  What sacrifices will I be forced to make?"
    scene 32 with fade
    $ renpy.pause()
    scene 33 with fade
    asl_ "Yazir... you are my guide now. My counsel."
    asl_ "But can even your wisdom navigate the treacherous path ahead?"
    scene 34 with dissolve
    mya "Aslan..."
    asl "..."
    mya "My Sultan."
    scene 35 with dissolve
    asl "Sultan...?"
    mya "The title is yours now, Aslan.  The weight of the crown… it rests upon your head."
    mya "You must be strong.  Your people need you."
    asl "..."
    scene 37 with dissolve
    asl "Strong… yes."
    asl "Father spoke of strength.  Of ambition.  He warned of its dangers, but he also understood its power."
    scene 34 with dissolve
    mya "Indeed. Your father was a wise man. He knew that ambition, tempered with wisdom, can achieve great things."
    scene 36 with dissolve
    asl "He achieved much. He brought peace and unity to our lands."
    asl "But I… I will do more."
    scene 38 with dissolve
    mya "..."
    mya "More?"
    asl "I will build an empire greater than he ever imagined!"
    asl "Our banners will fly over distant lands! Our name will be whispered in awe and fear across the world!"
    mya "..."
    mya "Such ambition… I pray you can control it, Aslan.  For your sake, and for the sake of us all."
    scene 39 with dissolve
    asl_ "I will not fail you, Father."
    asl_ "I will build the empire you dreamed of.  I will make our name known throughout the world."
    scene 40 with dissolve
    asl_ "Even if it means embracing the darkness you warned me against."
    asl_ "The sun has set on your reign, Father.  But my dawn is just breaking."
    nvl clear
    $ play_music(wide_sky, loop=True, fadein=2.0, fadeout=2.00)
    scene 41 with fade
    nar_nvl "{size=35}The days between the Sultan’s funeral and Aslan’s coronation were a whirlwind of ritual and preparation, a strange dichotomy of grief and burgeoning expectation.{/size}"
    nar_nvl "{size=35}The scent of incense still clung to the air, a lingering reminder of the late Sultan's passing, yet the halls of the palace now echoed with the hurried footsteps of servants and the clatter of armor as the royal guard prepared for the ceremony.{/size}"
    nar_nvl "{size=35}Whispers, like shadows, danced through the corridors. Some spoke of Aslan’s youth, questioning his readiness to rule. Others recalled his fiery pronouncements at his father’s funeral pyre, the bold declaration of a future empire echoing in their ears.{/size}"
    nar_nvl "{size=35}Would he be a wise and just ruler like his father, or a reckless conqueror driven by ambition? The court seethed with speculation, each faction vying for position, eager to curry favor with the soon-to-be Sultan.{/size}"
    nar_nvl "{size=35}The throne room, so recently draped in black for the funeral rites, was transformed. Banners of crimson and gold now adorned the walls, proclaiming the arrival of a new reign.{/size}"
    nar_nvl "{size=35}The throne room, once a space of mourning, now pulsed with a different kind of energy – the electric hum of expectation, crackling with the promise of what was to come. The dawn of Aslan’s reign was at hand.{/size}"
    scene 43 with fade
    mya "Nobles of the realm, honored guests, loyal subjects… we gather today to witness a momentous occasion."
    mya "The passing of our beloved Sultan has left a void in our hearts, but also a space for new beginnings."
    scene 42 with dissolve
    kad "The cycle of life and death is eternal."
    kad "Just as the sun sets to give way to the moon, so too does one reign end to make way for another."
    scene 44 with dissolve
    far "The legacy of the late Sultan will forever be etched in the annals of our history."
    far "His wisdom and strength guided us through times of turmoil and brought us to an era of peace and prosperity."
    scene 46 with dissolve
    mya "And now, that legacy falls upon the shoulders of his son, Aslan."
    mya "He stands before you today, ready to embrace the mantle of leadership, ready to guide us into a new age."
    mya "Yazir: Aslan, do you swear before the assembled court to uphold the laws of our land, to protect our people, and to rule with wisdom, justice, and strength?"
    scene 45 with dissolve
    asl "I swear to honor my father's memory, but I will not be bound by the past. "
    asl "I swear to protect our people, but I will not shy away from conquest.  I swear to rule with justice, but I will not hesitate to crush those who defy my authority."
    scene 49 with dissolve
    asl "But... before we proceed, I have a question for my esteemed advisors."
    asl "Tell me… the people… do they truly accept me as their Sultan?  Or do they simply see the son of their former ruler, a boy playing at being a man?"
    scene 48 with dissolve
    kad "Your Majesty, the people respect the bloodline."
    kad "They remember your father's wisdom and strength.  They see in you the promise of a continuation of his legacy."
    scene 47 with dissolve
    far "More than a continuation, Your Majesty."
    far "They see in you the potential for even greater things.  Your youth is not a weakness, but a strength. It signifies a new era, a time of boldness and expansion."
    scene 49 with dissolve
    asl "Boldness and expansion…  I like the sound of that."
    asl "But words are wind.  Tell me, is there any… resistance? Any dissent among our subjects?  Any who question my right to rule?"
    scene 52 with dissolve
    far "There are always those who cling to the old ways, Your Majesty."
    far "Those who resist change.  A few minor grumblings, nothing more.  Easily dealt with."
    scene 50 with dissolve
    kad "There is… one matter, Your Majesty."
    kad "A small village to the east, Karakaya. They have refused to send emissaries to acknowledge your ascension.  They have also, pointedly, withheld the customary tribute."
    scene 53 with dissolve
    asl "Karakaya…  I’ve heard of this village.  Nestled in the mountains, difficult to access.  They believe themselves untouchable."
    scene 54 with dissolve
    kad "A minor inconvenience, Your Majesty."
    kad "A show of force will quickly remind them of their place.  A few troops dispatched to… persuade them."
    scene 53 with dissolve
    asl "Persuasion is for diplomats, Farid.  I prefer action.  This defiance… it cannot be tolerated. It will be a test. A first test of my rule."
    scene 51 with dissolve
    mya "Your Majesty, I implore you to reconsider."
    scene 57 with dissolve
    asl "This Karakaya… they test my patience. They test the strength of my rule."
    asl "I will not tolerate such insolence.  We will march on this village and show them what happens to those who defy their Sultan."
    scene 55 with dissolve
    mya "A show of force so early in your reign could be… destabilizing.  Perhaps a diplomatic solution…?  Send emissaries, offer terms…"
    scene 57 with dissolve
    asl "Diplomacy is for the weak, Yazir. I will not negotiate with rebels.  I will crush them.  I will make them an example."
    scene 59 with dissolve
    far "Wise words, Your Majesty."
    far "A swift and decisive strike will send a clear message to any who would dare question your authority.  These mountain villagers… they need to be reminded of their place."
    scene 53 with dissolve
    asl "Indeed, Farid.  They need to learn that defiance has a price.  A steep price."
    scene 56 with dissolve
    kad "Your Majesty, while I understand your desire to demonstrate strength, I urge caution."
    kad "This Roxelana… the woman who leads Karakaya… she is not to be underestimated.  She is cunning, resourceful, and fiercely protective of her people."
    kad "She has defied the rule of Sultans before you, and she has always emerged victorious.  She commands the loyalty of her people, and they are skilled warriors, accustomed to the harsh terrain of the mountains."
    kad "A direct assault could prove… challenging.  They have little to lose, and everything to gain by defying you. They see your youth as a weakness to exploit."
    scene 49 with dissolve
    asl "A challenge…  Good.  I welcome a challenge.  Let this Roxelana and her villagers test their strength against mine."
    asl "Let them see what it means to face the wrath of a Sultan.  Prepare the army.  We march on Karakaya at dawn."
    scene 58 with dissolve
    mya "Your Majesty… is this truly your decision?  To unleash war upon your own people, so soon after ascending to the throne?"
    scene 60 with dissolve
    asl "My decision?  It is the Sultan's decision!  And I *am* the Sultan!  Do you question my authority, Yazir?"
    scene 61 with dissolve
    mya "Forgive me, Your Majesty. I only… I only wished to offer counsel."
    scene 62 with dissolve
    asl "Your counsel is valued, Yazir. But my mind is made up.  Karakaya will fall.  And in its fall, a new era will begin."
    asl "An era of strength, of expansion, of absolute obedience. Now… enough of this.  Place the crown upon my head, Yazir.  Let us begin my reign."
    scene 63 with dissolve
    "{i}Yazir hesitates for a moment, his hand trembling slightly as he holds the crown.{/i}"
    scene 64 with dissolve
    "{i}He looks at Kadir, then at Farid, seeking some sign of support or dissent.  But both men remain impassive, their faces betraying nothing.{/i}"
    scene 65 with dissolve
    "{i}With a sigh of resignation, Yazir places the crown upon Aslan's head.{/i}"
    scene 66 with dissolve
    "{i}Aslan sits upon the throne, the weight of the crown pressing down upon him, a tangible symbol of the burden he has chosen to bear.{/i}"
    scene 67 with dissolve
    mya "All hail Sultan Aslan."
    scene 68 with dissolve
    asl "Assemble the armies!  Prepare for war!  We march on Karakaya at dawn! I will raze that village to the ground!  And this Roxelana…"
    asl "if she is as cunning and resourceful as they say… if she is… beautiful… perhaps I will find a use for her.  Perhaps she will serve to… satisfy my desires.  Perhaps she will become… my wife...or my slave. We'll see."

    nvl clear
    scene harem1 with fade
    nar_nvl "{size=35}A murmur of shock ripples through the crowd.  Yazir closes his eyes, a silent prayer escaping his lips. Farid smiles, a predatory gleam in his eyes.{/size}"
    nar_nvl "{size=35}Kadir remains stoic, but a deep unease settles upon him.  He knows that Aslan's reign will be one of blood and conquest.  And he fears what the future holds.  The scene fades to black.{/size}"
    nar_nvl "{size=35}The die is cast. Aslan's ambition has been unleashed, and the fate of Karakaya hangs in the balance.{/size}"
    nar_nvl "{size=35}Will his thirst for power consume him, or will he find something more amidst the chaos of conquest?{/size}"
    nar_nvl "{size=35}The story continues in Part Two of The Sultan and his Harem!  Prepare for war.  Prepare for desire.  Prepare for… The Sultan and his Harem - Part Two!{/size}"
    
    return