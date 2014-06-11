# Push Button Stop Motion

Make your own stop motion animation rig with a push button, using Python Picamera and GPIO.

You can use LEGO to animate a tower being built, or figures acting out a scene! Or anything else you can think of...

## Requirements

As well as a Raspberry Pi with an SD card with Raspbian, you'll also need:

### Hardware

- 1 x [Raspberry Pi Camera Module](http://www.raspberrypi.org/product/camera-module/)
- 1 x Solderless breadboard (e.g. from [Pimoroni](http://shop.pimoroni.com/products/colourful-mini-breadboard))
- 2 x male-to-female jumper leads (e.g. from [Pimoroni](http://shop.pimoroni.com/products/jumper-jerky))
- 1 x tactile button (e.g. from [RS Components](http://uk.rs-online.com/web/p/tactile-switches/7182443/))

### Software

- python-picamera
- python-rpi.gpio
- ffmpeg

Install these with the following command:

```bash
sudo apt-get install python-picamera python-rpi.gpio ffmpeg
```

Alternatively using Python 3, the following command will install the required packages:

```bash
sudo apt-get install python3-picamera python3-rpi.gpio ffmpeg
```

### Extras

- Animation subject (e.g. LEGO)
- Camera mount (optional but useful)
    - Can be home-made / makeshift (e.g. cardboard and/or blu tack)
    - Can be bought (e.g. from [Pimoroni](http://shop.pimoroni.com/products/raspberry-pi-camera-mount) or [ModMyPi](https://www.modmypi.com/flexible-camera-mount))

## Steps

1. Setup the Pi and camera board
1. Test the camera
1. Take a picture with Python
1. Connect a hardware button
1. Take a selfie
1. Stop motion animation
1. Render the video

## Worksheet & included files

You'll need the worksheet for the instructions and the GPIO diagram for the button setup. You will also need to download the Optionally you could use a copy of the final version of the code to save typing it out.

- [The worksheet](worksheet.md)
- [GPIO diagram](images/picamera-gpio-setup.png)
- Video Rendering Bash script [render.sh](code/render.sh)
    - Download to the home directory with `wget http://goo.gl/V8b2FQ -O render.sh --no-check-certificate`
    - Make executable with `chmod +x render.sh`
- (Optional) Final version of Python Code [animation.py](code/animation.py)
    - Download to the home directory with `wget http://goo.gl/ZFsiyP -O animation.py --no-check-certificate`

## Licence

Unless otherwise specified, everything in this repository is covered by the following licence:

[![Creative Commons License](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

***Push Button Stop Motion*** by [Dave Jones](https://github.com/waveform80) and the [Raspberry Pi Foundation](http://www.raspberrypi.org) is licenced under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

Based on a work at https://github.com/raspberrypilearning/push-button-stop-motion
