## Take a picture with Python

--- task ---

Open **Python 3 (IDLE)** from the main menu:

![Open Python 3](images/python3-app-menu.png)

--- /task ---

--- task ---

Select `File > New Window` from the menu to open a Python file editor.

--- /task ---

--- task ---

Carefully enter the following code into the new window (case is important!):

```python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
```

--- /task ---

--- task ---

Select `File > Save` from the menu (or press `Ctrl + S`) and save as `animation.py`.

--- /task ---

--- task ---

Press `F5` to run your program.

--- /task ---

--- task ---

You should see `image.jpg` saved on your Desktop. Double-click the icon to open the image.

--- /task ---

--- task ---

If the picture is upside-down you can either reposition your camera using a mount, or leave it as it is and tell Python to flip the image. To do this, add the following lines:

```python
camera.rotation = 180
```

after `camera = PiCamera()`, so it becomes:

```python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
```

--- /task ---

--- task ---

Run the file again and it will overwrite `image.jpg` with a new image in the correct orientation. Remember to keep these lines in your code while you alter it in the next few steps.

--- /task ---

