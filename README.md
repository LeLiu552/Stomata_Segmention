# Mask-RCNN-Detectron2-FOR-Miaze-Stomata-Segmentation and Cell Profiler Pipeline to Perform parameter measurements in CellProfiller

### Description

Stomata are epidermal pores that facilitate plant gas exchange. Grasses have fast stomatal movements, which might be related to the plant's resistance to drought. The fast grass stomata are likely due to their dumbbell‐shaped guard cells and lateral subsidiary cells. Our previous work showed that subsidiary cells are necessary for the stomata function in corn. In this project, we want to explore what anatomy of the guard and subsidiary cells is important for stomatal efficiency.

Train on confocal images of the leaf epidermis to autometically segment the subsidiary cells and guard cells of maize inbred lines and measure the pixel areas, cell length and width of guard cells and subsidiary cells.

Code modified by Le Liu, Mask-RCNN written@ by Waleed Abdulla Copyright (c) 2018 Matterport, Inc.

### CZI2PNG.ipynb
Function to automatically read the .CZI files in the given folder and transfer into PNG files

### NDTOPNG.py
Function to automatically read the .nd files in the given folder and perform 3D projection with maximum stacks

### Train_setup.ipynb
This notebook provides detailed steps for training your model and validating its performance. 

### Model_usage.ipynb
The notebook provide the steps to apply the trained model to new images for inference and provide the options for display the images

![image](https://github.com/LeLiu552/Stomata_Segmention/assets/73537116/5303b18f-ee54-4a13-98dd-2d052fe3a34f)


### Example of application of the model:
![image](https://github.com/LeLiu552/Stomata_Segmention/assets/73537116/9b3f437a-ed68-45af-b136-aa26c0821476)

### There is NO significant difference in the area size of hand-traced and model-predicted Guard/Subsidiary cells 
![image](https://github.com/LeLiu552/Stomata_Segmention/assets/73537116/c1db10cf-482e-455a-9199-d17d89a12a03)




