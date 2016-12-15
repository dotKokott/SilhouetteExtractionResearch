# Related works
Other names for "silhouette extraction" that I use to find related works are:
* Silhouette Detection
* Human Segmentation
* Silhouette Segmentation
* Semantic Segmentation (not restricted to humans but general object labeling in scenes)
* Pedestrian detection

  Pedestrian detection is a different use case but has the same requirement:  
  Detecting silhouettes in real-time

There are several different approaches to silhouette extraction and they use different kind of hardware configuration. So far I found:
* Silhouette from accurate depth data (Kinect)
* Silhouette from static single color image
* Silhouette from static stereo color image
* Silhouette from moving stereo color image

I am mostly interested in either static single color image or static stereo color image because that is what the PS4 camera supports.

#### Papers
* [Foreground silhouette extraction robust to sudden changes of background appearance, 2012](https://infoscience.epfl.ch/record/176268/files/2782.pdf)

 >Index Terms— Background subtraction, foreground silhouettes,
total variation, stereo camera, disparity map.

* [Robust Silhouette Extraction from Kinect Data, 2013](http://www.robots.ox.ac.uk/~lav/Papers/pirovano_etal_iciap2013/pirovano_etal_iciap2013.pdf)

  Aligning color and depth stream, smoothing segmentation

* [Labeled dataset for integral evaluation of moving object detection algorithms, 2016](http://www.sciencedirect.com/science/article/pii/S1077314216301138)

  Labeled silhouette datasets

* [SMPLify: 3D Human Pose and Shape from a Single Image, 2016](http://files.is.tue.mpg.de/black/papers/BogoECCV2016.pdf)

  Using CNN and human pose databases

* [Stereo-based region of interest generation for real-time pedestrian detection](http://link.springer.com/article/10.1007/s12083-013-0234-2)

  Using depth by stereo + color + SVM, K-means for depth clustering

* [ENet: A Deep Neural Network Architecture for Real-Time Semantic Segmentation](https://arxiv.org/pdf/1606.02147v1.pdf)

* [YOLO: Unified, Real-Time Object Detection](http://www.gitxiv.com/posts/wh64sGMfwegjHyHFq/you-only-look-once-unified-real-time-object-detection)
* [Human silhouette segmentation using discrete poisson equation and extended watershed algorithm](http://ieeexplore.ieee.org/document/7593830/figures)

#### Code
* [PS4EYECam, GitHub](https://github.com/bigboss-ps3dev/PS4EYECam)

  PS4 driver for Linux/Mac, able to retrieve stereo image
