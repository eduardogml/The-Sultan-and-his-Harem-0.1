#a very simple gallery

init python:

    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0

    class GalleryItem:
        def __init__(self, name, images, locked="locked"):
            self.name = name
            self.images = images
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme

    gallery_items = []
    gallery_items.append(GalleryItem("Image 1", ["img1"] ))
    gallery_items.append(GalleryItem("Image 2", ["img2"] ))



#gallery background
image gray = "#777"

#gallery images
image img1 = ("images/gallery/gallery1.jpg")
image img2 = ("images/gallery/gallery2.jpg")
