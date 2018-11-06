import numpy as np
import cv2
import imutils
#import skvideo.io

#videogen = skvideo.io.vread('/Users/mfstech/PROJECT/unknown_face/test.mp4')

cap = cv2.VideoCapture('/Users/mfstech/PROJECT/unknown_face/test.mp4')

while(cap.isOpened()):  # check !
    # capture frame-by-frame
    ret, frame = cap.read()

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        #cv2.rotate(frame, rotateCode=cv2.ROTATE_90_CLOCKWISE)
        frame = imutils.rotate(frame, -90)
        cv2.imshow('frame', cv2.flip( frame , -1 ))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done release the capture
cap.release()
cv2.destroyAllWindows()
