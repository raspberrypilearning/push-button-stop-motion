## Connect the camera

Before booting your Pi, you'll need to connect the camera.

[[[rpi-picamera-connect-camera]]]

### Test the camera

--- task ---

Open a terminal window from the application menu. Enter the following command:

```bash
rpicam-hello
```

--- /task ---

You should see a preview appear on the screen. It doesn't matter if the picture is upside-down; you can configure this later. Press `Ctrl + C` to exit the preview.

--- task ---

To save an image you can use the following command:

```bash
rpicam-still -o test.jpg
```

---/task ---

--- task ---

Run the command `ls` to see the files in your home directory; you should see `test.jpg` listed.

--- /task ---

--- task ---

Click the file manager icon in the taskbar and you should see some folders and files. Double-click `test.jpg` to preview it.

--- /task ---
