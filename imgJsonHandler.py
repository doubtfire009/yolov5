import json
import cv2 as cv
import glob
import sys
import os

basePath = '/Users/liz187/Documents/miXing-campus/mixing-robot-platform/r-app/datasets/mixing-ball/'
imagesDir = basePath + 'images/'
labelsDir = basePath + 'labels/'
labelMeDir = basePath + 'labelmeJson/'

image_names = glob.glob(imagesDir + '*.jpg')
json_names = glob.glob(labelMeDir + '*.json')

def getFileName(file, end=-4):
    fileList = file.split('/')
    fileName = fileList[-1][0:end]
    return fileName

# del unused pics
for image in image_names:
    fileName = getFileName(image)
    corresAnnoFile = labelMeDir + fileName + '.json'
    if corresAnnoFile not in json_names:
        print(corresAnnoFile)
        os.remove(image)

for jsonItem in json_names:
    fileName = getFileName(jsonItem, -5)
    annotationFile = labelsDir + fileName + '.txt'

    with open(jsonItem, 'r') as j:
        jsonInfo = json.load(j)

    imageHeight = jsonInfo['imageHeight']
    imageWidth = jsonInfo['imageWidth']

    cont = ''
    for shape in jsonInfo['shapes']:
        width = format(abs(shape['points'][1][0] - shape['points'][0][0]) / imageWidth, '.4f')
        height = format(abs(shape['points'][1][1] - shape['points'][0][1]) / imageHeight, '.4f')
        x_center = format((shape['points'][1][0] + shape['points'][0][0])/2/imageWidth, '.4f')
        y_center = format((shape['points'][1][1] + shape['points'][0][1])/2/imageHeight, '.4f')
        contItem = '0 ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(height) + '\n'
        cont = cont + contItem

    with open(annotationFile, 'a') as f:
        f.write(cont)



