# NLP-image-to-text

Code to extract text from images

```
pip install -r requirements.txt
```


If you encounter file not found error as below:
```
FileNotFoundError: [Errno 2] No such file or directory: 'tesseract'
```

Run the following command
```
brew install tesseract
```

Then run the image-to-text.py as below:
```
 python image-to-text.py <relative filepaths separated by spaces>

```

We observe that for clean inputs the accuracy is high. See input 2.
Noisy input may not have the same effect!
 
Some sample inputs and outputs:

Input:

![Don't watch the clock; Do what it does. keep going. Sam Levenson](https://github.com/ayesha92ahmad/NLP-image-to-text/blob/master/data/test1.jpg)

Output:
```
DON’T
WATCH THE
CLOCK;



KEEP GOING.

SAM LEVENSON

/
/

7 J .- - ﬂCESScom
```
Input:

![How to recognize text from image with Python OpenCv OCR?](https://github.com/ayesha92ahmad/NLP-image-to-text/blob/master/data/test1.png)

Output:
```
How to recognize text from image with Python OpenCv OCR ?
```

Input:

![A negative mind will never give you a positive life.](https://github.com/ayesha92ahmad/NLP-image-to-text/blob/master/data/test2.jpg)

Output:
```
A negative mind
will nevergive you
a positivevli‘fe.
```

Credit: Base code has been taken from [Tram Vo Minh's blog](http://www.tramvm.com/2017/05/recognize-text-from-image-with-python.html). And modifications have been performed on that!
