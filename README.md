# panorama
image stitching using python 
Author : Rohith Agaram
Date   : 30-10-2017



                     PANORAMA - IMAGE STITCHING 
This package contains source code for image stiching

#Contents
sift.py : It gives the sift features and descriptors which are matched in two images
homography.py: It estimates the homography matrix between image planes
ransac.py : It provides roboust estimation for points to calculate homography
warp.py : It warps the all the images in to one image

#Prerequisites
1.sift:https://anaconda.org/menpo/cyvlfeat
2.scipy:https://www.scipy.org/install.html


#Compiling and Running
1.put the images in the "out" folder with the names 1.jpg,2.jpg,3.jpg so on from left to right in panorama.
2.cd ~/panorama/
3.python panorama.py
