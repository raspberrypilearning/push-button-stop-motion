## Take a picture with Python

[[[camera-bullseye]]]

--- task ---

Open **Thonny** from the **Programming** menu:

![The image shows a part of a desktop interface from a Raspberry Pi OS. The "Programming" menu is expanded, displaying two options: "Geany Programmer's Editor" with an icon of a yellow teapot, and "Thonny," a Python IDE, listed underneath. The "Internet" menu option is also partially visible below the "Programming" menu.](images/thonny_menu.png)

--- /task ---

--- task ---

Carefully enter the following code into the new window (case is important!):

```python
from picamzero import Camera
from time import sleep

camera = Camera()

camera.start_preview()
sleep(3)
camera.take_photo("/home/pi/Desktop/image.jpg")
```

--- /task ---

--- task ---

Select `Save` from the menu (or press `Ctrl + S`) and save as `animation.py`.

--- /task ---

--- task ---

Press `Run` to run your program.

--- /task ---

--- task ---

You should see `image.jpg` saved on your Desktop. Double-click the icon to open the image.

--- /task ---

--- task ---

If the picture is upside-down you can either reposition your camera using a mount, or leave it as it is and tell Python to flip the image. To do this, add the following lines:

```python
camera.pc2.rotation = 180
```

after `camera = Camera()`, so it becomes:

```python
from picamzero import Camera
from time import sleep

camera = Camera()

camera.pc2.rotation = 180
camera.start_preview()
sleep(3)
camera.take_photo("/home/pi/Desktop/image.jpg")
```

--- /task ---

--- task ---

Run the file again and it will overwrite `image.jpg` with a new image in the correct orientation. Remember to keep these lines in your code while you alter it in the next few steps.

--- /task ---

