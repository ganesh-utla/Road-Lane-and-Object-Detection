import matplotlib.pylab as plt
import cv2
import numpy as np


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def drow_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

def process(image):
    # print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width/2, height/2),
        (width, height)
    ]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32),)
    lines = cv2.HoughLinesP(cropped_image,
                            rho=2,
                            theta=np.pi/180,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)
    image_with_lines = drow_the_lines(image, lines)
    return image_with_lines

THRESHOLD = 0.5

cap = cv2.VideoCapture('./object-detection.mp4')
# cap = cv2.VideoCapture('C:/Users/ganes/Downloads/lane-line-detection-project-code/demo/test_video.mp4')
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)

classNames = []
classFile = './coco.names'
with open(classFile) as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = './ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = './frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)


# Detection for the image
img = cv2.imread('./roadlane.jpg')
classIds, confs, bbox = net.detect(img, confThreshold=THRESHOLD)
# print(classIds, bbox)
if len(classIds)!=0:
    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        cv2.rectangle(img, box, color=(0,255,0), thickness=2)
        cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
frame = process(img)
cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()



# Detection for the video

while cap.isOpened():
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=THRESHOLD)
    # print(classIds, bbox)
    if len(classIds)!=0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0,255,0), thickness=2)
            cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    frame = process(img)
    cv2.imshow('frame', frame)
    # cv2.imshow('Output', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

