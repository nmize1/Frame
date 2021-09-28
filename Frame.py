import tkinter as tk
from PIL import Image
from PIL import ImageTk
import random
import os
import sys
import HEICHandler.py

# Slideshow is the object that handles cycling images
class Slideshow():
    def __init__(self, delay, images, w, h):
        self.delay = delay
        self.images = images
        self.w = w
        self.h = h

    # Function to cycle images
    # Choose a random image from the opened images and transition to it
    # After delay seconds, recurse to keep the cycle going
    def chooseImage(self):
        img = random.choice(self.images)
        self.transitionImages(img)
        root.after(1000 * self.delay, self.chooseImage)

    # Handles creating the new image and removing the old one
    def transitionImages(self, img):

        #ADD IMAGE TRANSITIONS HERE


        new = canvas.create_image(self.w / 2, self.h / 2, image = img, tags = "new")
        canvas.delete("old")
        canvas.itemconfig(new, tag = "old")

# Initialize lists to append to later
images = []
opened = []

# Initialize root window properties
root = tk.Tk()
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

# Initialize canvas
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
canvas = tk.Canvas(root, bg = "Black", height = h, width = w)

# Set curr_dir and delay based on command args or print usage message
if len(sys.argv) == 3:
    curr_dir = sys.argv[2]
elif len(sys.argv) == 2:
    curr_dir = '.'
else:
    print("Usage: Frame.py delay [path_to_images]\ndelay is seconds between image changes\nif path_to_images is not specified, Frame will look for images in current directory\n")
    exit()

delay = int(sys.argv[1])

# Find all valid images in path
for rt, dirs, files in os.walk(curr_dir):
    for f in files:
        if f.endswith(".png") or f.endswith(".jpg") or f.endswith(".JPG") or f.endswith(".HEIC"):
            img_path = os.path.join(rt, f)
            print(img_path)
            images.append(img_path)


# Open all found images in Pillow and resize them to fit on the screen
# Then convert them to a tkinter friendly image
for image in images:
    if(image.endswith(".HEIC")):
        if(sys.platform.startswith("win")):
            print("Sorry, HEIC files not supported on Windows.")
        else:
            tmp = openHEIC(image)
    else:
        tmp = Image.open(image)
    imgWidth, imgHeight = tmp.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        tmp = tmp.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    open = ImageTk.PhotoImage(tmp)
    opened.append(open)

# Pass the list of tkinter friendly images to the Slideshow class along with needed parameters
# Start cycling....forever
ss = Slideshow(delay, opened, w, h)
ss.chooseImage()

canvas.pack()
root.mainloop()
