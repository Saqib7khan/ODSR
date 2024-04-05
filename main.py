import cv2
import numpy as np
import speech_recognition as sr
import pyttsx3
import torch
import subprocess
engine = pyttsx3.init()
# Load pre-trained object detection model 
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  
# model = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel") 
# Function to perform object detection using YOLOv5
def detect_objects(image, target_classes, model):
    # Perform forward pass through the network to detect object
    results = model(image)

    # Extract detected object
    objects = results.names

    # Filter objects based on target classes
    detected_objects = [obj for obj in objects if obj in target_classes]

    return detected_objects

# Function to perform speech recognition
def recognize_speech():
    # Initializing the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""
    # Specify target classes for detection (e.g., person, chair, etc.)
target_classes = [
    "person",
    "chair",
    "table",
    "sofa",
    "table",
    "chair",
    "bed",
    "couch",
    "television",
    "lamp",
    "clock",
    "curtains",
    "rug",
    "bookshelf",
    "mirror",
    "dining table",
    "kitchen appliances (e.g., refrigerator, stove, microwave)",
    "dishes",
    "pots and pans",
    "cutlery",
    "kitchen utensils (e.g., spatula, ladle)",
    "glasses",
    "mugs",
    "plates",
    "bowls",
    "bedside table",
    "dresser",
    "wardrobe",
    "hangers",
    "ironing board",
    "iron",
    "vacuum cleaner",
    "broom",
    "mop",
    "trash can",
    "laundry basket",
    "towels",
    "bed sheets",
    "pillows",
    "blankets",
    "toiletries",
    "shower curtain",
    "toilet brush",
    "soap",
    "shampoo",
    "conditioner",
    "toilet paper",
    "tissues",
    "cleaning supplies (e.g., detergent, bleach, disinfectant)",
    "first aid kit",
    "flashlight",
    "batteries",
    "toolbox",
    "screws",
    "nails",
    "hammer",
    "screwdriver",
    "wrench",
    "tape measure",
    "scissors",
    "glue",
    "matches/lighter",
    "fire extinguisher",
    "smoke detectors",
    "carbon monoxide detector",
    "keys",
    "wallet/purse",
    "cell phone",
    "charging cables",
    "remote controls",
    "computers/laptops"
]
# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Perform object detection
    detected_objects = detect_objects(frame, target_classes, model)

    # Display detected objects
    for obj in detected_objects:
        cv2.putText(frame, obj, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (10, 30), (200, 60), (255, 0, 0), 2)

    # Launch camera app
    subprocess.Popen('start microsoft.windows.camera:', shell=True)

    # Perform speech recognition
    command = recognize_speech()

    if command:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()