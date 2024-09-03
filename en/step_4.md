## Connect a hardware button

--- task ---

Using your breadboard and jumper leads, connect the Pi to the button as shown in the diagram below:

![The image depicts a Raspberry Pi connected to a breadboard via jumper wires. The Raspberry Pi's GPIO pins are connected to a red button on the breadboard. Specifically, two wires are shown: one black wire connected to a ground (GND) pin on the Raspberry Pi and to the breadboard, and one yellow wire connected to a GPIO pin (likely GP17) and the breadboard. The breadboard is labeled with rows and columns, where the button is placed in the middle section.](images/picamera-gpio-setup.png)

--- /task ---

--- task ---

Import `Button` from the `gpiozero` module at the top of the code, create up a `Button` connected to pin 17, and change the `sleep` line to use `button.wait_for_press` like so:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3, 5, 9
---
from picamzero import Camera
from time import sleep
from gpiozero import Button

button = Button(17)
cam = Camera()

cam.start_preview()
button.wait_for_press()
cam.take_photo("image.jpg")
cam.stop_preview()
--- /code ---

--- /task ---

--- task ---

Save and run your program.

--- /task ---

--- task ---

Once the preview has started, press the button connected to your Pi to capture an image.

--- /task ---

--- task ---

Return to the desktop and you should see your `image.jpg`. Again, double-click to view.

--- /task ---
