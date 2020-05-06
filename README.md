Collager
=============

A Python script for generating collages from PNG files.

Usage:
------
```
optional arguments:
  -h, --help            show this help message and exit
  -w MAX_WIDTH, --maxwidth MAX_WIDTH
                        maximum output width 
						(default 1304)
  -p PADDING, --padding PADDING
                        gap size between images and edges 
						(default 4)
  -f FOLDERS, --folders FOLDERS
                        paths to images (separate with ",")
  -o OUTPUT, --output OUTPUT
                        path to output
  -c COMP, --compression COMP
                        compression level (0-9) 
						(default 6)
```

Examples:
```
imagecollage.py -f imagefolder -o outputfolder
imagecollage.py -f imf1,imf2,imf3 -o outputfolder -w 1936 -p 8 -c 3
imagecollage.py -f C:/path/to/image/folder -o C:/path/to/output/folder
```