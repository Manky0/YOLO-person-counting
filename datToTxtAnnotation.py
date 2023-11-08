import os
import cv2

def yolobbox2bbox(x,y,w,h, img):
    print(f'Processing {img}...')
    # imgData = cv2.imread(img)
    # (imgH, imgW, s) = imgData.shape
    imgH = 480
    imgW = 640
    x = x+w/2
    x = x/imgW
    w = w/imgW
    y = y+h/2
    y = y/imgH
    h = h/imgH
    return f'0 {x} {y} {w} {h}'

pathToImages = '../micc_crowd_counting/Queue/RGB/'
pathToDat = '../micc_crowd_counting/Queue/GT_dat/'
pathToSave = './txt/Queue/'

files = os.listdir(pathToDat)

for file in files:
    if(file.split('.')[1] == 'dat'):
        datFile = open(pathToDat + '/' + file, 'r')
        data = datFile.read()
        datFile.close()

        linesData = data.split('\n')

        newTxtName = file.split('.')[0] + '.txt'
        newTxtFile = pathToSave + newTxtName
        
        imgPath = pathToImages + file.split('.')[0] + '.png'
        
        with open(newTxtFile, 'w') as txtFile:
            for line in linesData:
                # txtFile.write('0 ')
                # txtFile.write(line)

                lineData = line.split(' ')
                if(len(lineData) > 1):
                    lineData = yolobbox2bbox(int(lineData[0]), int(lineData[1]), int(lineData[2]), int(lineData[3]), imgPath)
                    txtFile.write(lineData + '\n')
            
    

    
