# Software installation

You'll need to make sure you have the following packages installed to proceed with the workshop.

You'll need to be online to install packages.

## python3-rpi.gpio

The `python3-rpi.gpio` package has been installed by default in Raspbian since mid-2012 so unless you're using an old image, you'll have it already. To test this, enter the following command in a terminal:

```bash
python3 -c "import RPi.GPIO"
```

If you get no errors, you have `rpi.gpio` installed. If you get an error, install with the following command:

```bash
sudo apt-get install python3-rpi.gpio
```

## python3-picamera

The `python3-picamera` package has been installed by default in Raspbian since June 2014 so unless you're using an old image, you'll have it already. To test this, enter the following command:

```bash
python3 -c "import picamera"
```

If you get no errors, you have `picamera` installed. If you get an error, install with the following command:

```bash
sudo apt-get install python3-picamera
```

## ffmpeg

You'll also need the `ffmpeg` package for the video rendering. Install this with:

```bash
sudo apt-get install ffmpeg
```

## Python 2 compatibility

This worksheet works fine in both Python 2 and Python 3. Python 3 is recommended but if you require Python 2 for an extension of the worksheet, simply use the equivalent Python 2 packages when installing, i.e.

```bash
sudo apt-get install python-rpi.gpio python-picamera
```

The usage is exactly the same, except using `IDLE` instead of `IDLE3` and using `python` instead of `python3` in the terminal.
