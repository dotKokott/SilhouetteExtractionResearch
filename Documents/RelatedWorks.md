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

There are approaches for videos that unfortunately dont apply because they analyze movement back and forth.

Pre-processing:
* RGB normalization to remove intensity variations

* Reference for pre processing background extraction and related works: https://arxiv.org/ftp/arxiv/papers/1408/1408.3814.pdf

Often background processing needs an empty frame without a human in the frame.

In case we are training there is a possiblity to synthesize data (https://arxiv.org/pdf/1604.02703v6.pdf) as well as using already existing datasets.

Human pose estimation is related however it usually relies on just finding "hot-points" like shoulders etc. to extract pose data. However these techniques should also be possible to get the whole shape depending on the training data. (https://www.robots.ox.ac.uk/~vgg/rg/papers/tompson2014.pdf)

Another approach could be to use the knowledge of human pose estimation and use another algo to go from pose data to silhouette. However until this works in realtime it could take a while. At least it could be used to make background removal and other techniques more robust by focusing only where there is a person already.

Some evidence that these joint techniques work: [3D Human Pose Estimation = 2D Pose Estimation + Matching](https://arxiv.org/pdf/1612.06524v1.pdf)

Visualization of feature maps: [A New Convolutional Network-in-Network Structure and Its Applications in Skin Detection, Semantic Segmentation, and Artifact Reduction](https://arxiv.org/pdf/1701.06190v1.pdf)

Most research is still focused on accuracy and not speed.

Fastest seems to be 0.09 seconds per frame (11 fps) which is not really fast enough for video games, however these are able to recognize all silhouettes in a frame. It should be possible to get a better speed trade-off to focus on only certain sizes or limited amount of silhouettes (assumption). [Fused DNN: A deep neural network fusion approach to fast and robust
pedestrian detection](https://arxiv.org/pdf/1610.03466v1.pdf) Also contains silhouette images for document.

There are already some that work faster (47 FPS) however it is still to be determined if the generated silhouettes can be extracted cleanly because this one is focusing only on region of interest. (Real-Time RGB-D based Template Matching Pedestrian Detection
)[https://arxiv.org/pdf/1610.00748v1.pdf]

All of them run on super graphic cards like the Titan X. Also possible that for my specific problem I need to use my own training data.

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

* [Unite the People: Closing the Loop Between 3D and 2D Human Representations](https://arxiv.org/pdf/1701.02468.pdf)

* [ROBUST STATISTICAL APPROACH FOR EXTRACTION OF MOVING HUMAN SILHOUETTES FROM VIDEOS](https://arxiv.org/ftp/arxiv/papers/1408/1408.3814.pdf)

* [Microsoft COCO](https://arxiv.org/pdf/1405.0312v3.pdf) Instance level segmentation

#### Code
* [PS4EYECam, GitHub](https://github.com/bigboss-ps3dev/PS4EYECam)

  PS4 driver for Linux/Mac, able to retrieve stereo image
  
* [Realtime Multi-person Pose Estimation](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation)
