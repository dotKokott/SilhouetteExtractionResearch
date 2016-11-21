# Data collection


## Introduction
I am writing a silhouette extraction algorithm for the PS4 camera. I want to collect all the data I can get from the PS4. Additionally I would like to collect labeled data from the Kinect as well to be able to compare solutions and eventually even be able to use the Kinect data as training data for a Machine Learning solution. The labeled Kinect data is hereby used as the ground truth data, because we consider the Kinect silhouette extraction as “good enough”.
Setup
I want to place the Kinect and the PS4 camera on top of each other and record all the different data frames that could be useful for my further research. I will be capping both recording devices at 30 FPS so the data is more comparable.


#### Kinect
| Stream Type                                  	| Resolution 	| Framerate 	|
|----------------------------------------------	|------------	|-----------	|
| Color                                        	| 1920x1080  	| 30 FPS    	|
| Depth                                        	| 512x424    	| 30 FPS    	|
| BodyIndex (Player segmentation / Silhouette) 	| 512x424    	| 30 FPS    	|


#### PS4 Camera
| Stream Type                                  	| Resolution 	| Framerate 	|
|----------------------------------------------	|------------	|-----------	|
| Color Left                                  	| 1280x720  	| 30/60 FPS   |
| Color Right                                  	| 1280x720  	| 30/60 FPS   |
| Depth                                        	| ??x??    	  | 30/60 FPS   |
| BodyIndex (Example implementation in HTLIB) 	| ??x??    	  | 30/60 FPS   |

Please note that I have a reference implementation for silhouette extraction on the PS4 provided by the [HTLIB](https://www.softkinetic.com/Products/HTLib/HTLib3) from [SoftKinetic](https://www.softkinetic.com/). This implementation provides the current best silhouette extraction that is available on the PS4. It is not good enough for my particular use case but can be used as a reference implementation that I want to beat, quality wise, with my implementation.

## Camera Differences
Besides the framerate, resolution and stream availability there is a major difference between these two cameras:  
**The method of depth sensing.** The Kinect is using an IR sensor to retrieve depth information whereas the PS4 camera relies on a stereo camera setup.

## Data collection
I do not know how much data I will need in the end but I would like to start recording some example and reference footage that I can use to debug my solutions and start working on the problem. I think it will be useful to record some footage that would resemble a common living room setup. I will record some movements that will be common in motion control gameplay.


I will record sample footage for:
* Standing still
* Walking around
* Reaching for objects
* Holding real-life objects in hands
* Crouching / Lying on floor
* Second person walking behind / in front of player


I will record this footage in two variations:
* with a clean background
* with normal living room furniture in the background


## Retrieval of data
To retrieve this data I will have to write a recording application for all the necessary data streams for the PC (Kinect) and the PS4 (PS4 camera). I will lock the framerate to 30 fps and save the data frame by frame and divided by input category. For example: Kinect/Color/frame_001.png
