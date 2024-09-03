## Stop motion animation

Now that you have successfully taken individual photographs with your camera, it's time to try combining a series of still images to make a stop motion animation.

--- task ---

**IMPORTANT** You must create a new folder to store your stills. In the folder where you saved your Python code, create a folder called `animation`. 

--- /task ---

--- task ---

Modify your code to add a loop to keep taking pictures every time the button is pressed:

--- code ---
---
language: python
line_numbers: true
---
cam.start_preview()
frame = 1
while True: 
    try:
        button.wait_for_press()
        cam.take_photo('/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
--- /code ---

*Because `while True` goes on forever, you have to be able to make it exit gracefully. Using `try` and `except` means it can deal with an exceptional circumstance - if you force it to stop with `Ctrl + C` it will close the camera preview and exit the loop*

*`frame%03d` means the file will be saved as the name "frame" followed by a 3-digit number with leading zeroes - 001, 002, 003, etc. This allows them to be easily sorted into the correct order for the video.*

--- /task ---

--- task ---

Now set up your animation subject (e.g. LEGO), ready to start the stop motion animation.

--- /task ---

--- task ---

Press the button to capture the first frame, then rearrange the animation subject and press the button again to capture each subsequent frame.

--- /task ---

--- task ---

Once all the frames have been captured, press `Ctrl + C` to terminate the program.

--- /task ---

--- task ---

Open the `animation` folder in the file manager to see your stills collection.

--- /task ---
