# Software installation

You'll need to make sure you have the following packages installed to proceed with the workshop.

You'll need to be online to install packages.

First update and upgrade your system. Enter the following commands in to the terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Now install the packages you'll need:

```bash
sudo apt-get install python3-picamera ffmpeg
```

Test you have everything you need by entering the following command:

```bash
sudo python3 -c "import picamera"
```

This should bring you back to the command prompt with no errors. If you get an error saying `No module named picamera` then check you entered the commands above correctly.

Also test you have `ffmpeg` installed by entering `avconv` at the command line. You should see some information about the `avconv` tool. If you see the error

```
The program 'avconv' is currently not installed.
```

then make sure you enter the `ffmpeg` package properly by checking the command above.
