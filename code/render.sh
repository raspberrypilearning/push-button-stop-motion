#!/bin/bash

avconv -y -f image2 -r 10 -i animation/frame%03d.jpg -c:v libxvid -aspect:v 16:9 -q:v 5 animation.mp4
