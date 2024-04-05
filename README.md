# ODSR
  ***Object detection and Speech recognition*** <br><br>
To run this project install necessary pacakages and libraries . <br>
`pip install opencv-python numpy speechrecognition torch pyttsx3` <br>
Create an environment in the same folder . <br>
This project can run both online and offline <br>
#To run this offline <Br>
Add the below line <br>
`model = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")` <br>
{check the correct location of the file } <br>
In place of <br>
`model = torch.hub.load('ultralytics/yolov5', 'yolov5s') `
