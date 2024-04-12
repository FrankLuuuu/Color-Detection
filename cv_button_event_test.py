import cv2

def function1(event, x, y, flags, param):

    if event==cv2.EVENT_LBUTTONDOWN:


        print(input_img[x, y])


input_img = cv2.imread(r'colorpic.jpg') # get image
# named window
cv2.namedWindow('new window')
# show the image in the window
cv2.imshow('new window', input_img)

# call setMouseCallback()
cv2.setMouseCallback('new window', function1)

while True:

    if cv2.waitKey(1) and 0xFF==ord('q'):

        break


cv2.detroyAllWindows()