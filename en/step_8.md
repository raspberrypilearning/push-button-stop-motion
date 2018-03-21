## Take a selfie

If you want to take a photograph of yourself with the camera board, you are going to have to add in a delay to enable you to get into position. You can do this by modifying your program.

- Add a line to your code to tell the program to sleep briefly before capturing an image, as below:

 ```python
 camera.start_preview()
 button.wait_for_press()
 sleep(3)
 camera.capture('/home/pi/Desktop/image3.jpg')
 camera.stop_preview()
 ```

- Save and run your script.

- Press the button and try to take a selfie. Be sure to keep the camera still! Ideally, it should be mounted in position.

- Again, feel free to check the image in the file manager. You can run the program again to take another selfie.

