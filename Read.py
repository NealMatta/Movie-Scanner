from time import sleep
import RPi.GPIO as GPIO
import sys
from mfrc522 import SimpleMFRC522
import cv2

reader = SimpleMFRC522()


def playMovie(movieSrc):
    cap = cv2.VideoCapture(movieSrc)
    
    if (cap.isOpened() == False):
        print ("Error Opening Video Stream of File")
    
    while(cap.isOpened()):
        ret, frame = cap.read()
                
        if ret == True:
            cv2.imshow('frame', frame)    
            if cv2.waitKey(25) == ord('q'):
                 break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    try:
        #while True:
        print("Hold a tag near the reader")
        print("Press Ctrl-C to stop.")
        id, text = reader.read()
        cleanDirectory = text.strip()
        playMovie(cleanDirectory)
        sleep(0.5)
        print("====================" * 3)
    except KeyboardInterrupt:
        print("Quitting")
        GPIO.cleanup()
        raise
    
main()

