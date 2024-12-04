## Setup Label

label map_event_setup:
    $ actions["harem"] = Act(name = _("HAREM"),  picture_in_background = "pre map harem", label_name = "harem_event", room_ids=['empire_capital'],
        xalign = 640/1920, yalign = 63/1080)
    
    $ actions["ministery"] = Act(name = _("MINISTERY"),  picture_in_background = "pre map ministery", label_name = "ministery_event", room_ids=['empire_capital'],
        xalign = 200/1920, yalign = 200/1080)
    
    $ actions["wife"] = Act(name = _("WIFE"),  picture_in_background = "pre map wife", label_name = "wife_event", room_ids=['empire_capital'],
        xalign = 920/1920, yalign = 440/1080)
    return