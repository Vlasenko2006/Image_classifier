#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:43:40 2024

@author: andreyvlasenko
"""


from Find_closest_image import find_closest_image
from GUI import get_user_inputs, ProgressWindow, ImageAreaSelector
import numpy as np
import os
from Similarity_metrics import sort_array_with_indices
from Utilities import getscales, copy_and_rename_file



def main():
        
    SAR = []
    SNR = []
    scaling_ref = []
    scaling_anti = []
    Exit_gui_status = False
    
    
    user_inputs = get_user_inputs()

    
    while not Exit_gui_status:
        selector = ImageAreaSelector(gui_name="Select pattern you WANT to see in your set")
        selector.run()
        coordinates, scaling_factor, ref_image_path, selected_area_array, Exit_gui_status = selector.get_results()
        if not Exit_gui_status:
            scaling_ref = scaling_ref + [getscales(ref_image_path,scaling_factor)]
            SAR = SAR + [(selected_area_array)]
        
      
    Exit_gui_status = False
    
    while not Exit_gui_status:   
        selector = ImageAreaSelector(gui_name="Select pattern you DO NOT WANT to see in your set")
        selector.exit_text = "Start matching procedure"
        selector.run()
        _, scaling_factor, ref_image_path, selected_area_array2, Exit_gui_status = selector.get_results()
        if not Exit_gui_status: 
            scaling_anti = scaling_anti + [getscales(ref_image_path,scaling_factor)]
            SNR = SNR + [(selected_area_array2)]
    


    
    image_save = user_inputs['output_path']


    log = True
    SSIM = False
    
    print("Start Searching!")
    

    passf = image_save + '/sorted'
    if not os.path.exists(passf):
        print("Creating directory " + passf)
        os.mkdir(passf)
        
    path_to_samples = user_inputs['sample_path'] +  "/"

    Js, pass_storage = find_closest_image(user_inputs['samples_to_process'], 
                                              path_to_samples,
                                              SAR, 
                                              SNR, log = log,  
                                              resize = scaling_ref,
                                              resize_n = scaling_anti,
                                              SSIM = SSIM)


    vals, ind = sort_array_with_indices(np.asarray(Js))

    progress_window = ProgressWindow(len(ind), Title = "Recorded images")
    for i in range(0,len(ind)):
        new_name = str(i) +".jpg"
        orig_file = pass_storage[ind[i]] #image_path + str(ind[i] + start) +".jpg"   
        copy_and_rename_file(src = orig_file, dest = passf, new_name = new_name) 
        progress_window.update_progress(i)
        if progress_window.stop_now : break
        
    progress_window.close()
        
        


        
        
        


if __name__ == "__main__":
    main()
