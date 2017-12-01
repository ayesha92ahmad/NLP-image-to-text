import cv2
import pytesseract
import os
from PIL import Image
import sys

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("thres.png"))
    os.remove("thres.png")

    return result

if __name__ == '__main__':
    from sys import argv

    if len(argv)<2:
        print("Usage: python image-to-text.py relative-filepath")
    else:
        print('--- Start recognize text from image ---')
        for i in range(1,len(argv)):
            print(argv[i])
            print(get_string(argv[i]))
            print()
            print()

        print('------ Done -------')
