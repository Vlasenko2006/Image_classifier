#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:49:11 2024

@author: andreyvlasenko
"""


import numpy as np
import os
from PIL import Image
import shutil
from tkinter import filedialog, messagebox, Toplevel




def load_image(image_path):
    try:
        image = Image.open(image_path)
        grayscale_image = image.convert("L")  # Convert to grayscale
        return np.array(grayscale_image)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
    
def copy_and_rename_file(src = None, dest = None, new_name = None):
    # Ensure the source file exists
    if not os.path.isfile(src):
  #      print(f"Source file {src} does not exist.")
        return
    
    # Ensure the destination directory exists
    if not os.path.isdir(dest):
  #      print(f"Destination directory {dest} does not exist.")
        return
    
    # Create the full path for the new file with the desired name
    destination_path = os.path.join(dest, new_name)
    
    # Copy the file and rename it in the process
    shutil.copy(src, destination_path)
  #  print(f"File copied and ren
  
  
  
def getscales(path,scaling_factor):
      grayscale_image = load_image(path)
      M,N  = grayscale_image.shape
      return [int(N/scaling_factor), int(M/scaling_factor)]
  
    
  