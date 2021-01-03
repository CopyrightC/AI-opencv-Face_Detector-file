import cv2, sys
from tkinter import *
from tkinter import messagebox
window_msg = Tk()
window_msg.eval('tk::PlaceWindow %s center' % window_msg.winfo_toplevel())
window_msg.withdraw()
faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
webcam_cap = cv2.VideoCapture(0)
messagebox.showinfo("Guide","Welcome to the Face Detector app, to quit the programme at any instance press 'Spacebar'")

while True:

    boolxval, frame = webcam_cap.read()
    imgGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
    cv2.imshow("Face detector", frame)
    key_press = cv2.waitKey(1)
    if key_press == 32:
        if messagebox.askyesno("Do you want to quit?","Are you sure that you want to quit the app?") == True:
            sys.exit()
        else:
            continue
  
