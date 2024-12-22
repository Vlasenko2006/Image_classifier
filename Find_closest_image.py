#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:40:13 2024

@author: andreyvlasenko
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:43:40 2024

@author: andreyvlasenko
"""


from GUI import ProgressWindow
import cv2 
import os
from Similarity_metrics import compute_similarity
from Utilities import load_image 


def find_closest_image(num_images, 
                       path_to_samples,
                       SAR,
                       SNR,                            
                       log = True, 
                       resize = [1,1],
                       resize_n = [1,1],
                       SSIM = True):
    Js = []
    pass_storage = []
    counter = 0 
    progress_window = ProgressWindow(num_images)  
    
    image_files = [f for f in os.listdir(path_to_samples) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    for file_name in image_files:
        # Полный путь к исходному изображению
        input_path = os.path.join(path_to_samples, file_name)
        
        sample_image = load_image(input_path) 
        counter += 1 
        if sample_image is not None:
            J = 0
            Jn = 0
            c = 0
            cn = 0
            for reference_image in SAR:
                
                sample_image  = cv2.resize(sample_image , (resize[c][0], resize[c][1]))
                J = J + compute_similarity(reference_image, sample_image, SSIM = SSIM)
                c += 1

            for reference_image in SNR:
                sample_image  = cv2.resize(sample_image , (resize_n[cn][0], resize_n[cn][1]))
                Jn = Jn + compute_similarity(reference_image, sample_image, SSIM = SSIM)
                cn += 1
                
            if c == 0:
                c = 1
            else:
                J = J/c
                   
            if cn == 0:
                Jn = 0
            else:
                Jn = Jn/cn
                
            Js = Js + [(J - Jn)]
            pass_storage = pass_storage + [input_path]
            progress_window.update_progress(counter)
            if counter > num_images or progress_window.stop_now : break
        
    progress_window.close()
    
    return Js, pass_storage



def getscales(path,scaling_factor):
    grayscale_image = load_image(path)
    M,N  = grayscale_image.shape
    return [int(N/scaling_factor), int(M/scaling_factor)]



        


        
        
        
