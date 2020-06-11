Collager
=============

A Python script for generating a collage out of a set of PNG files. Compatible with Windows, OS X and Linux.

Installation:
------

To run the script, you need to install Pillow (a fork of the Python Imaging Library, or PIL). 
Installation guide here: https://pillow.readthedocs.io/en/stable/installation.html



Usage:
------

Below is a list of optional arguments. It is highly recommended to set up separate input and output folders.

```
optional arguments:
  -h, --help            show this help message and exit
  -w MAX_WIDTH, --maxwidth MAX_WIDTH
                        maximum output width 
						(default: 1304)
  -p PADDING, --padding PADDING
                        gap size between images and edges 
						(default: 4)
  -f FOLDERS, --folders FOLDERS
                        paths to images (separate multiple folders with a blank space)
						(default: current working folder)
  -o OUTPUT, --output OUTPUT
                        path to output
						(default: current working folder)
  -c COMP, --compression COMP
                        compression level (0-9) 
						(default: 6)
  -b BG_COLOR, --bgcolor BG_COLOR
						determines background color in RGBA (separate each channel with a blank space
						(default: 255 255 255 255)
```

Examples:
```
imagecollage.py -f imagefolder -o outputfolder
imagecollage.py -f imf1 imf2 imf3 -o outputfolder -w 1936 -p 8 -c 3 -b 0 0 0 255
imagecollage.py -f C:/path/to/image/folder -o C:/path/to/output/folder
```