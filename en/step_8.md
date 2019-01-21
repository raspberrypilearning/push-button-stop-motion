## Generate the video

--- task ---

To generate the video, begin by returning to the terminal window.

--- /task ---

--- task ---

Run the video rendering command:

```bash
avconv -r 10 -i animation/frame%03d.jpg -qscale 2 animation.h264
```

*Note you're using `%03d` again - this is a common format which both Python and `avconv` understand, and means the photos will be passed in to the video in order.*

--- /task ---

--- task ---

Play your video using `omxplayer`.

```bash
omxplayer animation.h264
```

--- /task ---

You can adjust the frame rate by editing the rendering command. Try changing `-r 10` (10 frames per second) to another number.

You can also change the filename of the rendered video to stop it from overwriting your first attempt. To do this, change `animation.h264` to something else.

