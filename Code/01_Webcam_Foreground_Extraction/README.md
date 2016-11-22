# Webcam Foreground Extraction
This is a simple Python + OpenCV example showing how to fetch the webcam image and apply some foreground/background extraction. Additionally we find the contours in the modified foreground and draw them on top of the image.

This shows that that the background extraction of OpenCV is quite powerful (using only a monocular camera setup). However it only works with moving images and loses all foreground information as soon as you stop moving. Here is a video demonstration:

[![OpenCV foreground extraction demonstration video](http://img.youtube.com/vi/qjDVPdYPtbo/0.jpg)](http://www.youtube.com/watch?v=qjDVPdYPtbo "OpenCV foreground extraction")

## References
* [Foreground Extraction and Contour Detection with OpenCV 3](http://www.erogol.com/foreground-extraction-and-contour-detection-with-opencv-3/)
* [Contours : Getting Started, OpenCV DOCS](http://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html)
* [Background Subtraction, OpenCV DOCS](http://docs.opencv.org/3.1.0/db/d5c/tutorial_py_bg_subtraction.html)
