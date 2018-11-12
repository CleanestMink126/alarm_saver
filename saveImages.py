import cv2
import numpy
import time

def show_cam():
    cap = cv2.VideoCapture(1)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        # cv2.imshow('frame',gray)
        now = time.time()
        cv2.imwrite('./../test.jpg', frame)
        print(time.time()-now)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
        exit()

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_cam()
