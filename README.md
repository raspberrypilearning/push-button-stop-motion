# Push Button Stop Motion

![Push Button Stop Motion](cover.png)

Make your own stop motion animation rig with a push button, using Python Picamera and GPIO.

You can use LEGO to animate a tower being built, figures acting out a scene, or anything else you can think of!

## Requirements

As well as a Raspberry Pi with an SD card loaded with Raspbian, you'll also need:

### Hardware

- 1 x [Raspberry Pi camera module](http://www.raspberrypi.org/product/camera-module/)
- 1 x Breadboard (e.g. from [Pimoroni](http://shop.pimoroni.com/products/colourful-mini-breadboard))
- 2 x Male-to-female jumper leads (e.g. from [Pimoroni](http://shop.pimoroni.com/products/jumper-jerky))
- 1 x Tactile button (e.g. from [RS Components](http://uk.rs-online.com/web/p/tactile-switches/7182443/))

### Software

- GPIO Zero for Python 3
- libav-tools

See more information on checking you have these packages installed, and how to install them on the [software installation](software.md) page.

### Extras

- Animation subject (e.g. LEGO)
- Camera mount (optional but useful)
    - Can be home-made (e.g. cardboard and/or Blu-Tack)
    - Can be bought (e.g. from [Pimoroni](http://shop.pimoroni.com/products/raspberry-pi-camera-mount) or [ModMyPi](https://www.modmypi.com/flexible-camera-mount))

## Worksheet & included files

You'll need the worksheet for the instructions and the GPIO diagram for the button setup. Optionally, you can download the final version of the code to save typing it out.

- [The worksheet](worksheet.md)
- [GPIO diagram](images/picamera-gpio-setup.png)
- (Optional) Final version of Python code [animation.py](code/animation.py)
    - Download to the home directory with `wget http://goo.gl/ZFsiyP -O animation.py --no-check-certificate`

## Licence

Unless otherwise specified, everything in this repository is covered by the following licence:

[![Creative Commons Licence](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

***Push Button Stop Motion*** by [Dave Jones](https://github.com/waveform80) and the [Raspberry Pi Foundation](http://www.raspberrypi.org) is licensed under a [Creative Commons Attribution 4.0 International Licence](http://creativecommons.org/licenses/by-sa/4.0/).

Based on a work at https://github.com/raspberrypilearning/push-button-stop-motion
