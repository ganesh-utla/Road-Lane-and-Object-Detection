import cv2

THRESHOLD = 0.5

cap = cv2.VideoCapture('../../media/videos/detection.mp4') # reads the video file
# setting the constraints
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)


classNames = []
classFile = '../other/coco.names' # taking file that contains the names of the object that will help during the object detection 
with open(classFile) as f:
    # appending all the names in the classFile to the classNames list
    classNames = f.read().rstrip('\n').split('\n')

configPath = '../other/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = '../other/frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=THRESHOLD)
    # print(classIds, bbox)
    if len(classIds)!=0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0,255,0), thickness=2)
            cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow('Output', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

