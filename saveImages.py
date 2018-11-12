import cv2
import numpy
import datetime
import time

def show_cam():
    cap = cv2.VideoCapture(0)

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

def save_images():
    print('into function')
    time.sleep(20)
    cap = cv2.VideoCapture(0)
    capture = False

    last = datetime.datetime.now()
    while(True):
        # Capture frame-by-frame
        current = datetime.datetime.now()
        if 3 < current.hour < 7:
            print('asleep')
            path = './../Asleep/'
        elif 12 < current.hour < 23:
            print('awake')
            path = './../Awake/'
        else:
            time.sleep(5)
            continue

        if capture:
            print('save image---------')
            capture = False
            ret, frame = cap.read()
            cv2.imwrite(path + str(time.time())+ '.jpg', frame)
        else:
            print('waiting for image')
            diff = current - last
            if diff.days != 0 or diff.seconds > 30:
                capture = True
                last = current
        time.sleep(5)
if __name__ == '__main__':
    save_images()
