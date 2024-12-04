screen gallery():

    tag menu

    add "gray"

    $start = gallery_page * maxperpage
    $end = min(start + maxperpage - 1, len(gallery_items) - 1)

    #grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
                    at imageThumb
            else:
                imagebutton: 
                    idle gallery_items[i].images
                    style "gallery_button" #delete this line to remove hover
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5
                    at imageThumb

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #grid for info
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                style_prefix "name"
                spacing maxthumbx - 20
                xalign 0.5
                yalign 0.1
                text gallery_items[i].name
        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #previous, next, and return buttons
    if gallery_page > 0:
        textbutton "{color=#000}Previous{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.98
            background "#fff8"
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "{color=#000}Next{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98
            background "#fff8"
    textbutton "{color=#000}Return{/color}":
        action Return() 
        xalign 0.5
        yalign 0.98
        background "#fff8"

screen gallery_closeup(images): #shows full sized image as a button on top of everything!
    zorder 10
    imagebutton idle images[closeup_page]:
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
        xalign 0.5
        yalign 0.98
        background "#fff8"

