#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:40:13 2024

@author: andreyvlasenko
"""

import numpy as np
from skimage.metrics import structural_similarity as ssim




def sort_array_with_indices(arr):
    # Создаем список пар (значение, индекс)
    indexed_array = list(enumerate(arr))
    
    # Сортируем список по значениям (вторым элементам кортежей)
    indexed_array.sort(key=lambda x: x[1])
    
    # Извлекаем отсортированные значения и индексы
    sorted_values = [x[1] for x in indexed_array]
    sorted_indices = [x[0] for x in indexed_array]
    
    return sorted_values, sorted_indices


def compare_ssim(imageA, imageB):
    # Ensure the images have the same size
    assert imageA.shape == imageB.shape, "Images must be the same size."
    
    # Compute SSIM between two images
    score, diff = ssim(imageA, imageB, full=True)
    return score

def compute_similarity(reference_image, sample_image, SSIM = True):
    """
    Compute similarity between the reference image and the sample image using convolution.
    
    Parameters:
        reference_image (numpy.ndarray): The reference image (pattern).
        sample_image (numpy.ndarray): The sample image to compare with the reference.
    
    Returns:
        float: The highest convolution score.
    """
    ref_height, ref_width = reference_image.shape
    sample_height, sample_width = sample_image.shape

    # Ensure the reference image fits inside the sample image
    if ref_height > sample_height or ref_width > sample_width:
        raise ValueError("Reference image must be smaller than or equal to the sample image.")

    min_score = float('inf')  # Initialize the max score as negative infinity

    # Slide the reference image across the sample image
    for y in range(sample_height - ref_height + 1):
        for x in range(sample_width - ref_width + 1):
            # Extract the current region in the sample image
            
            region = sample_image[y:y + ref_height, x:x + ref_width]
            if SSIM:
                score = compare_ssim(region,reference_image)
            else:
                score = np.mean((((region -  reference_image)) ** 2)) 

            # Update the maximum score
            min_score = min(min_score, score)

    return min_score


# Compute the FFT of the image
def compute_fft(image, log = True):
    fft_image = np.fft.fft2(image)  # 2D FFT
    fft_shifted = np.fft.fftshift(fft_image)  # Shift the zero-frequency component to the center
    if log:
        magnitude_spectrum = np.log(np.abs(fft_shifted) + 1)  # Compute magnitude spectrum
    else: 
        magnitude_spectrum = fft_shifted  # Compute magnitude spectrum
        
    return  magnitude_spectrum











        


        
        
        
