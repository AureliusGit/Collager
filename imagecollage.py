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

def collager(max_width,padding,folders,output,comp,bg_color):
    
    ## Open output image
    def openImage(path):
        try:
            imageViewerFromCommandLine = {"win32":"explorer","darwin":"open","linux":"xdg-open"}[sys.platform]
            subprocess.run([imageViewerFromCommandLine, path])
        except KeyError:
            return
    
    ## Setting up
    images = []
    images_height = []
    images_cumul_height = []
    images_height.append(padding)

    ## Load images
    image_index = 1
    
    for folder_index in folders:
        for image_path in glob.glob(os.path.join(folder_index,"*.png")):
            image = Image.open(image_path)
            images.append((image_index,image_path,image.size[0],image.size[1]))
            image_index += 1
            image.close()
    
    ## Check for wide images
    for _,_,width,_ in images:
        if (width+padding*2)>max_width:
            print("Error: List contains images that are too wide!")
            return False
    
    ## Check for proper compression value
    if comp not in range(0,10):
        print("Error: Invalid compression value!")
        return False

    ## Generate output height and row y-coordinates
    current_width = padding
    img_h = 0

    for index,_,width,height in images:
        if (current_width + width+padding) > max_width:
            images_height.append(img_h+padding)
            current_width = padding
            img_h = 0
        current_width += width+padding
        if height > img_h:
            img_h = height
        if index == len(images)-1:
            images_height.append(img_h+padding)
    
    output_height = sum(images_height)
    images_cumul_height = list(itertools.accumulate(images_height))

    ## Generating the collage
    current_width = padding
    current_height_index = 0
    current_image_index = 0
    
    print("Processing images...")
    
    background = Image.new("RGBA",(max_width,output_height),(bg_color[0],bg_color[1],bg_color[2],bg_color[3]))
    for index,path,width,_ in images:
        if (current_width + width+padding) > max_width:
            current_height_index += 1
            current_width = padding
        image = Image.open(path)
        background.paste(image,(current_width,images_cumul_height[current_height_index]),image.convert("RGBA"))
        image.close()
        current_image_index += 1
        current_width += width+padding
        
    print("Saving collage...")
    if not os.path.exists(output):
        print("Error: Output directory does not exist!")
        return False
    else:    
        background.save(os.path.join(output,"collage.png"), compress_level=comp)
        openImage(os.path.join(output,"collage.png"))
        return True


def main():
    ## Arguments
    parse = argparse.ArgumentParser(description="Collage maker.")
    parse.add_argument('-w','--maxwidth', dest='max_width',type=int, default=1304, help='maximum output width')
    parse.add_argument('-p','--padding', dest='padding',type=int, default=4, help='gap size between images and edges')
    parse.add_argument('-f','--folders', nargs='+', dest='folders', type=str, default=".", help='paths to images')
    parse.add_argument('-o','--output', dest='output', type=str, default=".", help='path to output')
    parse.add_argument('-c','--compression', dest='comp', type=int, default=6, help='compression level (0-9)')
    parse.add_argument('-b','--bgcolor', nargs='+', dest='bg_color', type=int, default=(255,255,255,255), help='background color in RGBA')

    args = parse.parse_args()
    
    ## Running Collager function
    start = time.time()
    proc = collager(args.max_width,args.padding,args.folders,args.output,args.comp,args.bg_color)
    if not proc:
        print("Failed to create collage!")
        sys.exit(1)
    print("Collage created successfully! The process took {0:0.1f} seconds." .format(time.time()-start))

if __name__ == "__main__":
    main()