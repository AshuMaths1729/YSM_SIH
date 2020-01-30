# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:24:38 2020

@author: yashi
"""
import encodings
import cv2 
from imageai.Detection import ObjectDetection
import dlib
import face_recognition as fr
from PIL import Image
def clickSnap(pic_id):    
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    file = pic_id + str(".jpg") 
    cv2.imwrite(filename = file, img=frame)
    webcam.release()
    return check

def scaleSnap(pic_id):
    file = pic_id + str(".jpg")
    snap = cv2.imread(file, cv2.IMREAD_ANYCOLOR)
    print("Resizing image to 140x140 scale...")
    snap = cv2.resize(snap, (140, 140))
    print("Resized...")
    new_file = "scaled" + pic_id + ".jpg"
    cv2.imwrite(filename = new_file, img = snap)
    print("Image saved!")

def detectObjects(pic_id):
    file = "scaled" + pic_id + ".jpg"
    out_file = "out" + pic_id + ".jpg"
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image = file, output_image_path = out_file)
    return detections

def onlyOneFace(detections):
    count = 0
    for eachObject in detections:
        if eachObject["name"] == "person" and eachObject["percentage_probability"] > 0.5:
            count += 1
    return count == 1

def isGadgetPresent(detections):
    gadgets = ["cell phone", "laptop", "tv"]
    for eachObject in detections:
        if eachObject["name"] in gadgets and eachObject["percentage_probability"] > 0.5:
            return True
    return False

def headGaze(pic_id):
    return 0

def reauthenticateUser(known_image, new_image):
    known_encode = fr.face_encodings(known_image)[0]
    new_encode = fr.face_encodings(new_image)[0]
    return fr.compare_faces([known_encode], new_encode)[0]
    

def process():
    pic_id = "i1"
    clickSnap(pic_id)
    scaleSnap(pic_id)
    user = fr.load_image_file("scaledi1.jpg")
    count = 3
    pic_id = "i2"
    while pic_id != "i10":
        if clickSnap(pic_id):
            scaleSnap(pic_id)
            det = detectObjects(pic_id)
            path = "scaled" + pic_id + ".jpg"
            new_pic = fr.load_image_file(path)
            if onlyOneFace(det):
                print("Faces ", onlyOneFace(det))
                if not reauthenticateUser(user, new_pic):
                    print("User Identity violated")
                    break
                print("User authentic : ", reauthenticateUser(user, new_pic))
                print("Gadget : ", isGadgetPresent(det))
            else:    
            
                print("Faces Detected are not 1 ", onlyOneFace(det))
                break
        pic_id = "i" + str(count)
        count += 1

process()