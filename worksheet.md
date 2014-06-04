# Push Button Stop Motion

Make your own stop motion animation rig with a push button, using Python Picamera and GPIO.

You can use LEGO to animate a tower being built, or figures acting out a scene! Or anything else you can think of...

## Step 1: Setup the Pi and camera board

Before booting your Pi, you'll need to connect the camera and enable it.

### Connecting the camera

1. Locate the camera port next to the ethernet port
1. Lift the tab on the top
1. Place the strip in the connector (blue side facing the ethernet port)
1. While holding the strip in place, push down the tab

### Activate the camera

1. Connect a USB cable to the power
1. Login with username `pi` and password `raspberry`
1. At the command prompt enter `sudo raspi-config`
1. At the menu, navigate to `Enable Camera`
1. Select `Enable`
1. Select `Finish`
1. Select `Yes` to reboot

## Step 2: Test the camera

1. Login again with username `pi` and password `raspberry`.
1. Adjust the camera to point at yourself or some object.
1. At the command prompt enter `raspistill -o image1.jpg`.
1. On the screen you should see a preview appear for a few seconds, and then change briefly while the image is captured (it doesn't matter if the picture is upside-down, we'll come to that later).
1. Run the command `ls` to see the files in your home directory, and you should see `image1.jpg` listed.
1. Enter `startx` to start the graphical desktop environment.
1. Once the desktop icons appear, the graphical interface has loaded. Click the file manager icon in the taskbar and you should see some folders and files.
1. Double click `image1.jpg` to preview it.

## Step 3: Take a picture with Python

1. Double click on `LXTerminal` to open a terminal window, and enter `sudo idle &` to start the Python environment.
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

1. Select `File > Save` from the menu (or hit `Ctrl + S`) and give your script a name, e.g. `workshop.py`.
1. Press `F5` to run the script.
1. Without closing the Python window, return to the file manager window and you'll see the new file `image2.jpg`. Double click to view the picture.
1. If the picture is upside-down, you can either reposition your camera using a mount, or leave it as it is and tell Python to flip the image. To do this, add the following lines:

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
    
1. Run the file again and it will overwrite `image2.jpg` with a new one in the correct orientation. Remember to keep these lines in your code as you alter it in the next few steps.

## Step 4: Connect a hardware button

1. Connect the Pi to the button as shown in the diagram below:

    ![](images/picamera-gpio-setup.png)

1. In the text editor, import the `RPi.GPIO` module, set up GPIO pin 17 and change the `sleep` line to use `GPIO.wait_for_edge` like so:

    ```python
    import picamera
    from time import sleep
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        GPIO.wait_for_edge(17, GPIO.FALLING)
        camera.capture('/home/pi/image3.jpg')
        camera.stop_preview()
    ```

1. Save and run your script.
1. Once the preview has started, press the button connected to your Pi to capture an image.

## Step 5: Take a selfie

1. Modify your program to include the delay after the button wait:

    ```python
    import picamera
    from time import sleep
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        GPIO.wait_for_edge(17, GPIO.FALLING)
        sleep(5)
        camera.capture('/home/pi/image4.jpg')
        camera.stop_preview()
    ```

1. Save and run your script.
1. Press the button and try to take a selfie.

## Step 6: Stop motion animation

1. First create a new folder to store your stills. In the terminal, enter `mkdir animation`.
1. Modify your code to add a loop to keep taking pictures every time the button is pressed:

    ```python
    import picamera
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        frame = 1
        while True:
            GPIO.wait_for_edge(17, GPIO.FALLING)
            camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
            frame += 1
        camera.stop_preview()
    ```

1. Now set up your animation subject (e.g. LEGO) and run the Python script to begin.
1. Press the button to capture the first frame, then rearrange the animation subject and press the button again to capture each subsequent frame.
1. Once all the frames have been captured, hit `Ctrl + C` in the IDLE prompt (not the code window) which will terminate the program.

## Step 7: Compile the video

1. Now use the `avconf` command to compile each frame in to a video. Enter the following line in to the terminal window.

    ```bash
    avconv -y -f image2 -r 10 -i animation/frame%02d.jpg -c:v libxvid -aspect:v 16:9 -q:v 5 animation.mp4
    ```

1. With 20 frames this will take about 30 seconds. Once complete, you can play the video with the following command:

    ```bash
    omxplayer animation.mp4
    ```
