# Face_Detection

This particular project is based on ```Haar Cascade Algorithm```, also known as ```Voila-Jones Algorithm``` to 
detect faces.

In OpenCV, There are several trained  Haar Cascade models which are saved as XML files.

**scaleFactor** – Parameter specifying how much the image size is reduced at each image scale. By rescaling the input image, you can resize a larger 
face to a smaller one, making it detectable by the algorithm. 1.05 is a good possible value for this, which means you use a small step for resizing, 
i.e. reduce the size by 5%, you increase the chance of a matching size with the model for detection is found.

**minNeighbors** – Parameter specifying how many neighbors each candidate rectangle should have to retain. This parameter will affect the quality of 
the detected faces. Higher value results in fewer detections but with higher quality. 3~6 is a good value for it.

**flags** –Mode of operation

**minSize** – Minimum possible object size. Objects smaller than that are ignored.