init python:
    from pythonpackages.nqtr.quest import Stage
    from pythonpackages.nqtr.quest import Quest

default quests_descriptions = {
    # "quest_id"  : "description",
}

define quests = {
    "wife"  : Quest(id = "wife", title = _("Hurrem"), info_image ="pre map wife",
        stage_ids = ["hurrem_start_quest", "hurrem1", "hurrem2", "hurrem3"],
        description = _("Long Description"),
        development = True
    ),
    "ministery"  : Quest(id = "ministery", title = _("Ministery"), info_image ="pre map ministery",
        stage_ids = ["ministery_start_quest", "ministery1", "ministery2", "ministery3"],
        description = _("Long Description"),
        development = True
    ),
}

define quest_stages = {
    # Quest "wife"
    "hurrem_start_quest" : Stage(quest_id = "wife", title = _("Talk a Hurrem Start"), description = _("Talk a Hurrem 0 time.")),
    "hurrem1" : Stage(quest_id = "wife", title = _("Talk a Hurrem part 1"), description = _("Talk a Hurrem 1 time."), start_label_name="hurrem_1"),
    "hurrem2" : Stage(quest_id = "wife", title = _("Talk a Hurrem part 2"), description = _("Talk a Hurrem 2 time."), start_label_name="hurrem_2"),
    "hurrem3" : Stage(quest_id = "wife", title = _("Talk a Hurrem part 3"), description = _("Talk a Hurrem 3 time."), start_label_name="hurrem_3"),
    "ministery_start_quest" : Stage(quest_id = "ministery", title = _("Talk The Ministery Start"), description = _("Talk The Ministery 0 time.")),
    "ministery1" : Stage(quest_id = "ministery", title = _("Talk The Ministery part 1"), description = _("Talk The Ministery 1 time."), start_label_name="ministery_1"),
    "ministery2" : Stage(quest_id = "ministery", title = _("Talk The Ministery part 2"), description = _("Talk The Ministery 2 time."), start_label_name="ministery_2"),
    "ministery3" : Stage(quest_id = "ministery", title = _("Talk The Ministery part 3"), description = _("Talk The Ministery3 time."), start_label_name="ministery_3"),
}

label harem_event:
    call harem1
    return

label ministery_event:
    $ quest_next_stage(id = "ministery")
    return

label wife_event:
    $ quest_next_stage(id = "wife")
    return

label quest_setup:
    if(not quest_start(id = "wife")):
        $ log_error("The quest hurrem has not started", renpy.get_filename_line())
    if(not quest_start(id = "ministery")):
        $ log_error("The quest ministery has not started", renpy.get_filename_line())
    return