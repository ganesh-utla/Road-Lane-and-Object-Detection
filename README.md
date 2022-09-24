<h1 align="center">Road Lane and Object Detection</h1>
<p align="center">The model for detecting the road lane and object detection</p>

## Prerequisites

Please make sure that you've already installed the following libraries:
- [``OpenCV``](https://r.search.yahoo.com/_ylt=Awr93tEJDi9jD8QbX3YM34lQ;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1664056969/RO=10/RU=https%3a%2f%2fpypi.org%2fproject%2fopencv-python%2f/RK=2/RS=66fj0VMlhtYnt6V98j1wtxaBjH8-)
```
pip install opencv-python
```
- [``Numpy``](https://r.search.yahoo.com/_ylt=AwrOqO9GES9jnfsbVlUM34lQ;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1664057798/RO=10/RU=https%3a%2f%2fnumpy.org%2f/RK=2/RS=OYq0vN.qDY0HVDDG7QrUh5arwsE-)
```
pip install numpy
```

## Description

- [Lane Line
detection](https://r.search.yahoo.com/_ylt=AwrOsas2FS9jFPsbDWcM34lQ;_ylu=Y29sbwNncTEEcG9zAzUEdnRpZAMEc2VjA3Ny/RV=2/RE=1664058807/RO=10/RU=https%3a%2f%2fmedium.com%2f%40avi.9006%2fsimple-lane-line-detection-8a2e18aa4adf/RK=2/RS=pWyUjqjXTLSwN_B3N3CblKetH8g-)
is a critical component for self driving cars and also for computer vision in general. This
concept is used to describe the path for self-driving cars and to avoid the risk of getting in another lane.

- Using [computer vision
techniques](https://r.search.yahoo.com/_ylt=AwrOo0OTFC9jjwAcw4EM34lQ;_ylu=Y29sbwNncTEEcG9zAzMEdnRpZAMEc2VjA3Ny/RV=2/RE=1664058644/RO=10/RU=https%3a%2f%2fpythonawesome.com%2fusing-computer-vision-techniques-in-opencv-we-will-identify-road-lane-lines-in-which-autonomous-cars-must-run%2f/RK=2/RS=SuKiodkNkwRsfeCZwSRnoj.yT78-)
in Python, we will identify road lane lines in which autonomous cars must run. This
will be a critical part of [``autonomous
cars``](https://r.search.yahoo.com/_ylt=AwrjaWPPFC9jeOwbsi8M34lQ;_ylu=Y29sbwNncTEEcG9zAzUEdnRpZAMEc2VjA3Ny/RV=2/RE=1664058704/RO=10/RU=https%3a%2f%2fwww.analyticsinsight.net%2fautonomous-cars-the-mystery-in-technology%2f/RK=2/RS=pr_qaz2_ccPdxbjmPZeMwZGnL50-),
as the self-driving cars should not cross it's lane and should not go in
opposite lane to avoid accidents.

- To detect white markings in the lane, first, we need to mask the rest part of the frame. We do this using [``frame
masking``](https://r.search.yahoo.com/_ylt=AwrO6y79FC9jXvMb25gM34lQ;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1664058750/RO=10/RU=https%3a%2f%2fpyimagesearch.com%2f2021%2f01%2f19%2fimage-masking-with-opencv%2f/RK=2/RS=DYO2bArRF4o7WUUSLKFeMfVutv0-).
The frame is nothing but a NumPy array of image pixel values. To mask the unnecessary pixel of the frame, we
simply update those pixel values to 0 in the NumPy array.

- After making we need to detect lane lines. The technique used to detect mathematical shapes like this is called Hough
Transform. [``Hough
transformation``](https://r.search.yahoo.com/_ylt=Awr9.5pRFC9jFngbGEIM34lQ;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Nj/RV=2/RE=1664058577/RO=10/RU=https%3a%2f%2fwww.educba.com%2fopencv-hough-transform%2f%23%3a~%3atext%3dWorking%2520of%2520Hough%2520Transform%2520in%2520OpenCV%2520Simple%2520shapes%2cusing%2520HoughLines%2520%2528%2529%2520function%2520and%2520HoughLinesP%2520%2528%2529%2520function./RK=2/RS=lxFJteA5RFZMoMfmHqTQnnHKDvI-)
can detect shapes like rectangles, circles, triangles, and lines.

- By using these functions/tools, we implemented this model.