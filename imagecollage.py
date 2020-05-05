# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:59:22 2020

@author: Aurelius
"""
import glob
from PIL import Image
import itertools
import sys
import subprocess
import time
import argparse
import os

def collager(max_width,padding,folder,output):
    ## Open output image
    def openImage(path):
        imageViewerFromCommandLine = {"win32":"explorer","darwin":"open"}[sys.platform]
        subprocess.run([imageViewerFromCommandLine, path])
    
    ## Setting up
    
    images = []
    images_height = []
    images_cumheight = []
    images_height.append(padding)
    
    ## Load images
    for image_path in glob.glob(os.path.join(folder,"*.png")):
        images.append(Image.open(image_path))
    
    ## Check for wide images
    for img in images:
        if (img.size[0]+padding*2)>max_width:
            print("Error: List contains images that are too wide!")
            return False
    
    ## Generate output height and row y-coordinates
    
    current_width = padding
    img_h = 0
    
    for index,image in enumerate(images):
        if (current_width + image.size[0]+padding) > max_width:
            images_height.append(img_h+padding)
            current_width = padding
            img_h = 0
        current_width += image.size[0]+padding
        if image.size[1]>img_h:
            img_h = image.size[1]
        if index == len(images)-1:
            images_height.append(img_h+padding)
    
    output_height = sum(images_height)
    images_cumheight = list(itertools.accumulate(images_height))
    
    ## Generating the collage
    
    current_width = padding
    current_height_index = 0
    
    background = Image.new("RGB",(max_width,output_height),(250,250,250,0))
    for index,image in enumerate(images):
        if (current_width + image.size[0]+padding) > max_width:
            current_height_index += 1
            current_width = padding
        background.paste(image,(current_width,images_cumheight[current_height_index]),image.convert("RGBA"))
        current_width += image.size[0]+padding
        
    if not os.path.exists(output):
        print("Output directory does not exist!")
        return False
    else:    
        background.save(os.path.join(output,"collage.png"))
        openImage(os.path.join(output,"collage.png"))
        return True


def main():
    ## Arguments
    parse = argparse.ArgumentParser(description="Collage maker.")
    parse.add_argument('-w','--maxwidth', dest='max_width',type=int, default=1044, help='maximum output width')
    parse.add_argument('-p','--padding', dest='padding',type=int, default=4, help='padding (gaps between images)')
    parse.add_argument('-f','--folder', dest='folder', type=str, default=".", help='path to images')
    parse.add_argument('-o','--output', dest='output', type=str, default=".", help='path to output')

    args = parse.parse_args()
    
    ## Running Collager function
    start = time.time()
    proc = collager(args.max_width,args.padding,args.folder,args.output)
    print("Processing images...")
    if not proc:
        print("Failed to create collage!")
        sys.exit(1)
    print("Collage created successfully!")
    print("The process took {0:0.1f} seconds." .format(time.time()-start))

if __name__ == "__main__":
    main()