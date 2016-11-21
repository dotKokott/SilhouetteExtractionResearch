# Data collection
Before I can start developing any solution I will need to record some training and test data. This will allow me to train, test and compare my solutions. Additionally it will remove the need to get out of my chair for every test!  

I will record all relevant output data from the Kinect and PS4 camera. This data will be categorized by data type and stored frame by frame. The Kinect data will serve as training and testing data. I will consider it the ground truth example for my solution because I regard it as the optimal solution for now. The PS4 camera data will serve as input data for the algorithm I attempt to develop.

## Setup
During the recording session I will place the Kinect and PS4 camera on top of each other. This will help collecting comparable data for testing different solutions. The framerate will be capped at 30 FPS as the lowest common denominator between the two devices.

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

Please note that I have a working extraction library ([HTLIB](https://www.softkinetic.com/Products/HTLib/HTLib3)) for the PS4, provided by [SoftKinetic](https://www.softkinetic.com/). This implementation provides the current best silhouette extraction that is available on the PS4. It is not good enough for my use case, which is the motivation for developing another solution. I will use it as a competing solution that I want to beat, or at least match, with my implementation.

## Camera Differences
Related to our problem there is a major difference between the two cameras: **The method of depth sensing.**  
The Kinect is using an IR sensor to retrieve depth information. In comparison the PS4 relies on a stereo camera setup. This suggests that the PS4 is more susceptible to lighting and other ambient factors.

## Data collection
I do not know how much data I will need to develop the final solution. In any case I will start recording some relevant footage that I can use to begin working on the problem. It will be the most useful to record some footage that resembles a common living room setup. I will record scenarios that will be common in motion control interaction.


I will record the following scenarios in two different background variations (empty room / background furniture):
* Standing still
* Walking around
* Reaching for objects
* Holding real-life objects in hands
* Crouching / Lying on floor
* Second person walking behind / in front of user
