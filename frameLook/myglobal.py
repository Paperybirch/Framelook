import cv2 as cv
###########################################################
## EDIT THIS VARIBLE TO YOUR OPENPOSE FILE PATH WHICH CONTAINS BIN AND LIB FOLDERS
opath = r'C:/Users/callahanm5/Openpose/openpose/'
## EDIT THIS VARIABLE TO YOUR FRAMELOOK FILE PATH WHICH CONTAINS PSEUDOMAIN.PY
framelookpath = 'C:/Users/callahanm5/source/repos/frameLookdemotest/frameLook/'
###########################################################
 
opathbin = opath+'bin/OpenPoseDemo.exe'
outjson_path = opath+'output_jsons'
opathoutput = opath+'output'
workingdir = "./framelook/outmasks/"

#framelookpath = 'C:/Users/Micheal/source/repos/frameLook/frameLook/'



clicklist = []

