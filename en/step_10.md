## Generate the video

- To generate the video, begin by returning to the terminal window.

- Run the video rendering command:

 ```bash
 avconv -r 10 -i animation/frame%03d.jpg -qscale 2 animation.h264
 ```

 *Note you're using `%03d` again - this is a common format which both Python and `avconv` understand, and means the photos will be passed in to the video in order.*

- You can adjust the frame rate by editing the rendering command. Try changing `-r 10` (10 frames per second) to another number.

 ```bash
 omxplayer animation.h264
 ```

- You can also change the filename of the rendered video to stop it from overwriting your first attempt. To do this, change `animation.mp4` to something else.

