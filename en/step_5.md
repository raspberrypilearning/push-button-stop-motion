## Connect a hardware button

--- task ---

Using your breadboard and jumper leads, connect the Pi to the button as shown in the diagram below:

![](images/picamera-gpio-setup.png)

--- /task ---

--- task ---

Import `Button` from the `gpiozero` module at the top of the code, create up a `Button` connected to pin 17, and change the `sleep` line to use `button.wait_for_press` like so:

```python
from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/image.jpg')
camera.stop_preview()
```

--- /task ---

--- task ---

Save and run your program.

--- /task ---

--- task ---

Once the preview has started, press the button connected to your Pi to capture an image.

--- /task ---

--- task ---

Return to the file manager window and you should see your `image.jpg`. Again, double-click to view.

--- /task ---
