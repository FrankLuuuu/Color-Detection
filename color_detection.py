import cv2 # openCV
import numpy as np 
import pandas as pd
import argparse 

# create argument parser to take image path from user via command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = "Image Path")
args = vars(ap.parse_args())
imgPath = args['image']

# read image with openCV
img = cv2.imread(imgPath)

# declare global necessary variables 
clicked = False
r = g = b = x = y = 0

# read csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names = index, header = None)

# calculate distance from all colors and get closest color
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if(d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname
    
# get x, y coordinates of mouse double click
def drawFunction(event, xPos, yPos, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, x, y, clicked
        clicked = True
        x = xPos
        y = yPos
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('Color Detection')
cv2.setMouseCallback('Color Detection', drawFunction)

while(1):
    cv2.imshow("Color Detection", img)

    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r + g + b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            
        clicked = False

    # break loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()