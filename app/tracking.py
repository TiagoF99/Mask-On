from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

faceFound = False
tracker = None

face_cascade = cv2.CascadeClassifier('saved_model/haarcascade_frontalface_default.xml')
vs = VideoStream(src=0).start()
time.sleep(1.0)

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=500)

	(H, W) = frame.shape[:2]

	if faceFound:
		(faceFound, box) = tracker.update(frame)
	
	if faceFound:
		(x, y, w, h) = [int(v) for v in box]
		cv2.rectangle(frame, (x, y), (x + w, y + h),
			(0, 255, 0), 2)

	if not faceFound:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.1, 7)
		if len(faces) == 1:
			tracker = tracker=cv2.TrackerKCF_create()
			tracker.init(frame, tuple(faces[0]))
			faceFound = True
	
	text = "In Frame: {}".format(faceFound)
	cv2.putText(frame, text, (10, H - ((20) + 20)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

	cv2.imshow("Frame", frame)

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

vs.stop()
cv2.destroyAllWindows()
