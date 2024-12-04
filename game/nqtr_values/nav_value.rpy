init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
    Room(id="empire_capital", location_id="empire", name=_("Empire Capital"), background ="bg empire_capital"),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
    Location(id = "empire", map_id="world_map", external_room_id="empire_capital", name=_("Empire")),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define maps = {
    "world_map": Map(
        name = _("World Map"), background = "bg world_map",
    ),
}