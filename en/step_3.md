## Take a picture with Python

--- task ---

Open **Thonny** from the **Programming** menu:

![The image shows a part of a desktop interface from a Raspberry Pi OS. The "Programming" menu is expanded, displaying two options: "Geany Programmer's Editor" with an icon of a yellow teapot, and "Thonny," a Python IDE, listed underneath. The "Internet" menu option is also partially visible below the "Programming" menu.](images/thonny_menu.png)

--- /task ---

--- task ---

Carefully enter the following code into the new window (case is important!):

--- code ---
---
language: python
line_numbers: true
---
from picamzero import Camera
from time import sleep

cam = Camera()

cam.start_preview()
sleep(3)
cam.take_photo("image.jpg")
cam.stop_preview()

--- /code ---

--- /task ---

--- task ---

Select `Save` from the menu (or press `Ctrl + S`) and save as `animation.py`.

--- /task ---

--- task ---

Press `Run` to run your program.

--- /task ---

--- task ---

You should see `image.jpg` saved in the same folder as you saved your program. Double-click the icon to open the image.

--- /task ---

--- collapse ---
---
title: My picture is upside down
---

If the picture is upside-down you can either reposition your camera using a mount, or leave it as it is and tell Python to flip the image. To do this, add the following line of code:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from picamzero import Camera
from time import sleep

cam = Camera()
cam.flip_camera(vflip=True)
cam.start_preview()
sleep(3)
cam.take_photo("image.jpg")
--- /code ---

Run the file again and it will overwrite `image.jpg` with a new image in the correct orientation. Remember to keep these lines in your code while you alter it in the next few steps.

--- /collapse ---

