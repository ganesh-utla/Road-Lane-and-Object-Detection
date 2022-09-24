# If you wish to convert the video to images for testing
import cv2
import os

cam = cv2.VideoCapture("./videofile.mp4") # reads the video file
path_for_images = 'path' # give the path for the images that you will convert from video


try:
	# If the directory doesn't exists, then it makes that directory
	if not os.path.exists(path_for_images):
		os.makedirs(path_for_images)

except OSError: 
	# It will raise error if there is any!
	print ('Error: Creating directory of data')

currentframe = 0 # initializing the variable for the name of the images

while(True):
	ret,frame = cam.read()

	if ret:
		# setting the path of the particular image
		img_name = path_for_images + '/' + str(currentframe) + '.jpg'
		print ('Creating...' + img_name)

		# downloading/writing the image 
		cv2.imwrite(img_name, frame)
		currentframe += 1
	else:
		break
print('Created!!')
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
