# ODSR
  Object detection and Speech recognition 
To run this project install necessary pacakages and libraries .
pip install opencv-python numpy speechrecognition torch pyttsx3
Create an environment in the same folder .
This project can run both online and offline 
#To run this offline 
remove the below line from from comment 
# model = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel") 
{check the correct location of the file }
