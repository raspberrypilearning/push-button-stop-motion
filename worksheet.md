# Push Button Stop Motion

Make your own stop motion animation rig with a push button, using Python Picamera and GPIO.

You can use LEGO to animate a tower being built, figures acting out a scene, or anything else you can think of!

## Step 1: Test the camera

Before booting your Pi, you'll need to connect the camera.

### Connecting the camera

1. Locate the camera port next to the Ethernet port.
1. Lift the tab on the top.
1. Place the strip in the connector, with the blue side facing the Ethernet port.
1. While holding the strip in place, push down the tab.
1. Turn the power on to boot the Pi.

### Log in and take a test picture

1. Log in with username `pi` and password `raspberry`.
1. Adjust the camera to point at yourself or an object.
1. At the command prompt, enter `raspistill -o image1.jpg`.
1. You should see a preview appear on the screen for a few seconds, and then change briefly while the image is captured. It doesn't matter if the picture is upside-down; we'll come to that later.
1. Run the command `ls` to see the files in your home directory; you should see `image1.jpg` listed.
1. Enter `startx` to start the graphical desktop environment.
1. Once the desktop icons appear, the graphical interface has loaded. Click the file manager icon in the taskbar and you should see some folders and files.
1. Double-click `image1.jpg` to preview it.

## Step 2: Take a picture with Python

1. Double-click on `LXTerminal` to open a terminal window, and enter `sudo idle3 &` to start the Python environment.
1. Select `File > New Window` from the menu to open a Python file editor.
1. Carefully enter the following code (case is important!):

    ```python
    import picamera
    from time import sleep

    with picamera.PiCamera() as camera:
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/image2.jpg')
        camera.stop_preview()
    ```

1. Select `File > Save` from the menu (or press `Ctrl + S`) and save as `animation.py`.
1. Press `F5` to run the script.
1. Without closing the Python window, return to the file manager window and you'll see the new file `image2.jpg`. Double-click to view the picture.
1. If the picture is upside-down you can either reposition your camera using a mount, or leave it as it is and tell Python to flip the image. To do this, add the following lines:

    ```python
    camera.vflip = True
    camera.hflip = True
    ```

    inside the `with` loop, so it becomes:

    ```python
    import picamera
    from time import sleep

    with picamera.PiCamera() as camera:
        camera.vflip = True
        camera.hflip = True
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/image2.jpg')
        camera.stop_preview()
    ```

1. Run the file again and it will overwrite `image2.jpg` with a new image in the correct orientation. Remember to keep these lines in your code while you alter it in the next few steps.

## Step 3: Connect a hardware button

1. Connect the Pi to the button as shown in the diagram below:

    ![](images/picamera-gpio-setup.png)

1. Import the `RPi.GPIO` module at the top of the code, set up GPIO pin 11, and change the `sleep` line to use `GPIO.wait_for_edge` like so:

    ```python
    import picamera
    from time import sleep
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        GPIO.wait_for_edge(11, GPIO.FALLING)
        camera.capture('/home/pi/image3.jpg')
        camera.stop_preview()
    ```

1. Save and run your script.
1. Once the preview has started, press the button connected to your Pi to capture an image.
1. Return to the file manager window and you should see your `image3.jpg`. Again, double-click to view.

## Step 4: Take a selfie

1. Modify your program to include a delay after the button wait, as follows:

    ```python
    import picamera
    from time import sleep
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        GPIO.wait_for_edge(11, GPIO.FALLING)
        sleep(5)
        camera.capture('/home/pi/image4.jpg')
        camera.stop_preview()
    ```

1. Save and run your script.
1. Press the button and try to take a selfie. Be sure to keep the camera still! Ideally, it should be mounted in position.
1. Again, feel free to check the image in the file manager. Run the program again to take another selfie!

## Step 5: Stop motion animation

1. **IMPORTANT:** Create a new folder to store your stills. In the terminal window, enter `mkdir animation`.
1. Modify your code to add a loop to keep taking pictures every time the button is pressed:

    ```python
    import picamera
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        frame = 1
        while True:
            GPIO.wait_for_edge(11, GPIO.FALLING)
            camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
            frame += 1
        camera.stop_preview()
    ```

1. Now set up your animation subject (e.g. LEGO), ready to start the stop motion animation.
1. **IMPORTANT** This time, do not run the program from IDLE as it will be impossible to break out of the loop. Instead, return to the terminal window and enter `sudo python3 animation.py`.
1. Press the button to capture the first frame, then rearrange the animation subject and press the button again to capture each subsequent frame.
1. Once all the frames have been captured, press `Ctrl + C` which will terminate the program.
1. Open the `animation` folder in the file manager to see your stills collection.

## Step 6: Render the video

1. Now return to the terminal window.
1. Run the video rendering command:

    ```bash
    avconv -r 10 -i animation/frame%03d.jpg -vcodec libx264 animation.mp4
    ```

1. With 10 frames this will take about 5 minutes. Once complete, you can play the video with the following command:

    ```bash
    omxplayer animation.mp4
    ```

1. Optionally, you can adjust the frame rate by editing the rendering command. Try changing `-r 10` (10 frames per second) to another number.
1. You can also change the filename of the rendered video to stop it from overwriting your first attempt. To do this, change `animation.mp4` to something else.
