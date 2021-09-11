import cv2

trained_faced_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

x = input('Press "1" for detecting face in Picture. \nPress "2" for detecting face in Video.\nyour input:')
if (x == "1"):
     pName = input("type your file including with format like example.PNG .\n Your file's name:")
     img = cv2.imread(pName)
     grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     face_coordinates = trained_faced_data.detectMultiScale(grayscaled_img)
     print(face_coordinates)
     for (x, y, w, h) in face_coordinates:
         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
     cv2.imshow('Mohammad Mahdi Baloochnejad Face Detector', img)
     cv2.waitKey()
     print("Code Completed")

elif (x == '2'):
     videoChoice = input('Press "W" for detecting face in webcam. \n'
                         'Press "V" for detecting face in Chosen Video.\nyour input:')
     if (videoChoice == "V" or videoChoice == "v" ):
          vName =input("type your file including with format like example.MP4 .\n Your file's name:")
     elif (videoChoice == "W" or videoChoice == "w"):
          vName = 0
     webcam = cv2.VideoCapture(vName)

     while True:
          successful_frame_read, frame = webcam.read()
          grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          face_coordinates = trained_faced_data.detectMultiScale(grayscaled_img)
          for (x, y, w, h) in face_coordinates:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
          cv2.imshow('Mohammad Mahdi Baloochnejad Face Detector', frame)
          key = cv2.waitKey(1)
          if key == 81 or key == 113:
               break
     webcam.release()
     print("Code Completed")


