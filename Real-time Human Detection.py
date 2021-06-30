# import numpy as np
# import cv2

# cv2.startWindowThread()
# cap = cv2.VideoCapture(0)

# while(True):
#     # reading the frame
#     ret, frame = cap.read()
#     # displaying the frame
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         # breaking the loop if the user types q
#         # note that the video window must be highlighted!
#         break

# cap.release()
# cv2.destroyAllWindows()
# # the following is necessary on the mac,
# # maybe not on other platforms:
# cv2.waitKey(1)

#     # turn to greyscale:
#     frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#     # apply threshold. all pixels with a level larger than 80 are shown in white. the others are shown in black:
#     ret,frame = cv2.threshold(frame,80,255,cv2.THRESH_BINARY)

#     # import the necessary packages
import numpy as np
import cv2
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,    (1080,720))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    
    # Write the output video 
    out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)