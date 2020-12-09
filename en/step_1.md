## What you will make

Make your own stop motion animation video using a Raspberry Pi, Python and a camera module to take pictures, controlled by a push button connected to the Pi's GPIO pins.

You can use LEGO to animate a tower being built, figures acting out a scene, or anything else you can think of!

![showcase](images/showcase.gif)

--- collapse ---
---
title: What you will learn
---

By creating a push button stop motion machine with your Raspberry Pi you will learn:

- How to set up and use the Raspberry Pi camera module
- How to use the Python picamera library to capture photographs
- How to connect a button to the GPIO pins on a Raspberry Pi
- How to control the camera with a button using GPIO Zero
- How to generate a video from the command line using `avconv`

This resource covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](https://www.raspberrypi.org/curriculum/):

- [Combine programming constructs to solve a problem](https://www.raspberrypi.org/curriculum/programming/builder)
- [Combine inputs and/or outputs to create projects or solve a problem](https://www.raspberrypi.org/curriculum/physical-computing/builder)
--- /collapse ---

--- collapse ---
---
title: What you will need
---

### Hardware

* Raspberry Pi camera module
* 1 x Full size breadboard
* 2 x Male-to-female jumper leads
* 1 x Tactile button

### Software

ffmpeg should be preinstalled on the latest version of Raspberry Pi OS. If it is not installed, open a terminal and type:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt install ffmpeg
```

--- /collapse ---

--- collapse ---
---
title: Additional information for educators
---
If you need to print this project, please use the [printer-friendly version](https://projects.raspberrypi.org/en/projects/push-button-stop-motion/print){:target="_blank"}.

You can find the finished code for this project [here](https://rpf.io/p/en/push-button-stop-motion-get){:target="_blank"}.

--- /collapse ---
