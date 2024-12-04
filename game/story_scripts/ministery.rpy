label ministery_1:
    scene ministery1 with dissolve
    $ renpy.pause()
    "Stage 1 completed."
    $ sth = number_stages_completed_in_quest["ministery"]
    "Stage current: [sth]"
    call new_day
    return

label ministery_2:
    scene ministery2 with dissolve
    $ renpy.pause()
    "Stage 2 completed."    
    $ sth = number_stages_completed_in_quest["ministery"]
    "Stage current: [sth]"
    call new_day
    return

label ministery_3:
    scene ministery3 with dissolve
    $ renpy.pause()
    "Stage 3 completed."
    $ sth = number_stages_completed_in_quest["ministery"]
    "Stage current: [sth]"
    call new_day
    return