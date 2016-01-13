# Software installation

You'll need to make sure you have the following packages installed to proceed with the workshop.

- GPIO Zero for Python 3
- libav-tools

You'll need to be online to install packages.

First update and upgrade your system. Enter the following commands in to the terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Now install the packages you'll need:

```bash
sudo apt-get install python3-gpiozero libav-tools
```

- Test you have `gpiozero` installed by entering `python3 -c "import gpiozero"` at the command line. You should see no error.
- Test you have `libav-tools` installed by entering `avconv` at the command line. You should see some information about the `avconv` version.
