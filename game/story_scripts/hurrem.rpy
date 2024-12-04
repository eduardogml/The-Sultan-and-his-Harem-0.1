label hurrem_1:
    scene wife_1 with dissolve
    $ renpy.pause()
    "Stage 1 completed."
    $ sth = number_stages_completed_in_quest["wife"]
    "Stage current: [sth]"
    call new_day
    return

label hurrem_2:
    scene wife_2 with dissolve
    $ renpy.pause()
    "Stage 2 completed."    
    $ sth = number_stages_completed_in_quest["wife"]
    "Stage current: [sth]"
    call new_day
    return

label hurrem_3:
    scene wife_3 with dissolve
    $ renpy.pause()
    "Stage 3 completed."
    $ sth = number_stages_completed_in_quest["wife"]
    "Stage current: [sth]"
    call new_day
    return