# Image Sorting Script: Overview and Functionality

This script processes a set of images and assigns integer-based similarity scores based on user-specified patterns and antipatterns. It also allows the user to exclude images matching certain criteria (antipatterns). Below is a detailed explanation of the script's components and workflow.

## Key Features

1. **Similarity-Based Sorting**:  
   - Images are sorted based on their similarity to a user-selected pattern.
   - The similarity score is computed using methods such as Structural Similarity Index (SSIM) or Mean Squared Error (MSE).

2. **Antipattern Exclusion**:  
   - Users can specify "antipatterns" that represent unwanted features.
   - Images matching the antipatterns are assigned the maximum score and can be excluded from further analysis.

3. **Interactive GUI for Pattern Selection**:  
   - The script provides an interactive GUI to select patterns and antipatterns from image samples.
   - Users can crop regions of interest and specify rescaling factors.

4. **Custom Matching Methods**:  
   - Users can choose between SSIM, MSE, or FFT-based similarity metrics.
   - FFT (Fast Fourier Transform) is used for frequency-based image analysis.

## Workflow

### 1. **User Input via GUI**

- The GUI allows users to:
  - Select a directory containing image samples.
  - Define patterns to focus on and antipatterns to avoid.
  - Specify the number of images to process and the output directory.
  - Choose a similarity matching method (default: MSE).

### 2. **Pattern and Antipattern Selection**

- **Pattern Selection**:  
  Users interactively select regions of interest from images. These regions define the patterns they want to identify in the dataset.
- **Antipattern Selection**:  
  Similar to pattern selection, users define unwanted features using a separate GUI step.

### 3. **Similarity Computation**

- The script compares each image in the dataset to the selected patterns and antipatterns.
- Similarity scores are calculated using:
  - **SSIM**: Measures perceptual similarity between two images.
  - **MSE**: Measures pixel-wise differences.
  - **FFT**: Analyzes frequency-domain features.
- The computed scores determine the image rankings:
  - **Perfect match**: Assigned a score of `0`.
  - **Partial match**: Assigned intermediate scores.
  - **Antipattern match**: Assigned the maximum score.

### 4. **Image Sorting and Output**

- Images are sorted by their scores.  
- The script can rename images for easier identification:
  - Small integers (e.g., `1`, `2`, `3`) are assigned to images closely matching the patterns.
  - High integers are assigned to images dissimilar to patterns or matching antipatterns.
- The sorted images are saved to the user-specified output directory.

### 5. **Progress Tracking**

- A progress window displays real-time updates on the sorting process.
- Users can stop the process at any time.

## Code Components

1. **Image Area Selector**:  
   Allows users to select patterns or antipatterns interactively.

2. **Similarity Metrics**:
   - **SSIM**: Calculates structural similarity (coded, but not implemented yet).
   - **MSE**: Calculates mean squared error between image patches (set by default).
   - **FFT**: Provides a frequency-domain representation of images (coded, but not implemented yet).

3. **Sorting Mechanism**:
   - Images are scored based on their similarity to patterns and antipatterns.
   - The scores are used to sort and rename images.

4. **GUI Framework**:  
   The script uses `tkinter` for GUI components such as file dialogs, progress windows, and selection tools.

### Example Output
- Images closely matching the user-specified pattern:
  - Renamed as `1.jpg`, `2.jpg`, etc.
- Images matching the antipattern:
  - Renamed with high integers or excluded altogether.

# How to install 

## 1. Clone the code

Run in the terminal either:

`git@github.com:Vlasenko2006/Image_classifier.git`

or 

`https://github.com/Vlasenko2006/Image_classifier.git`

Congrats! You've downloaded the code. 



### 2. Install the Environment

Open your terminal or Anaconda Prompt, navigate to the directory containing env.yaml, and execute:
`conda env create -f env.yaml`
you will create a "myenv" that contains all necessary packages. If you whant to name it differntly, change the environment name in the `env.yaml` file.

After you installed the script you can process your images running the comand int bash shell `python Image_classifier.py`  or run the file `Image_classifier.py` in the python IDE tool.


