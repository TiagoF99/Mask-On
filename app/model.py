import cv2
from tensorflow.keras.models import load_model
import numpy as np
import twilio_connect as twillio

def monitorMask(phone_number, maskAtDesk):
    # our tf model
    model_trained = load_model('saved_model/')

    face_clsfr = cv2.CascadeClassifier('saved_model/haarcascade_frontalface_default.xml')

    labels_dict = {0: 'no', 1: 'yes'}
    color_dict = {0: (0, 0, 255), 1: (0, 255, 0)}

    size = 4
    webcam = cv2.VideoCapture(0)  # Use camera 0

    # We load the xml file
    classifier = cv2.CascadeClassifier('saved_model/haarcascade_frontalface_default.xml')

    mask_off_count = 0

    if maskAtDesk == True:
        while True:
            (rval, im) = webcam.read()
            im = cv2.flip(im, 1, 1)  # Flip to act as a mirror
            frame = im
            (H, W) = im.shape[:2]

            # Resize the image to speed up detection
            mini = cv2.resize(im, (im.shape[1] // size, im.shape[0] // size))

            # detect MultiScale / faces
            faces = classifier.detectMultiScale(mini)

            # Draw rectangles around each face
            for f in faces:
                (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
                # Save just the rectangle faces in SubRecFaces
                face_img = im[y:y + h, x:x + w]
                resized = cv2.resize(face_img, (150, 150))
                normalized = resized / 255.0
                reshaped = np.reshape(normalized, (1, 150, 150, 3))
                reshaped = np.vstack([reshaped])
                result = model_trained.predict(reshaped)
                # print(result)

                label = np.argmax(result, axis=1)[0]

                if label == 0:
                    # mask is not on so we send a text message
                    # fill in number
                    mask_off_count += 1
                    if mask_off_count > 10:
                        twilio.send_message(phone_number, "You don't seem to be wearing a mask, did you mean to be wearing one?")
                        print("Text message sent")
                        mask_off_count = 0
            
                cv2.rectangle(im, (x, y), (x + w, y + h), color_dict[label], 2)
                cv2.rectangle(im, (x, y - 40), (x + w, y), color_dict[label], -1)
                cv2.putText(im, labels_dict[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            # Show the image
            cv2.imshow('LIVE', im)
            key = cv2.waitKey(10)
            # if Esc key is press then break out of the loop
            if key == 27:  # The Esc key
                break

    if maskAtDesk == False:

        faceFound = False
        tracker = None
        messageSent = False
        outOfFrameCount = 0 

        while True:
            (rval, im) = webcam.read()
            im = cv2.flip(im, 1, 1)  
            (H, W) = im.shape[:2]

            if faceFound:
                (faceFound, box) = tracker.update(im)

            if faceFound:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(im, (x, y), (x + w, y + h),
                    (0, 255, 0), 2)

            if not faceFound:
                outOfFrameCount += 1
                if outOfFrameCount > 45 and messageSent == False:
                    twilio.send_message(phone_number, "It seems like you've left your desk, did you remember to bring your mask with you?")
                    print("Text message sent")
                    messageSent = True
                    outOfFrameCount = 0

                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                detectedFaces = face_clsfr.detectMultiScale(gray, 1.1, 9)

                if len(detectedFaces) == 1:
                    tracker = tracker=cv2.TrackerKCF_create()
                    tracker.init(im, tuple(detectedFaces[0]))
                    faceFound = True
                    messageSent = False
                    outOfFrameCounter = 0

            text = "In Frame: {}".format(faceFound)
            cv2.putText(im, text, (10, H - ((20) + 20)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # Show the image
            cv2.imshow('LIVE', im)
            key = cv2.waitKey(10)
            # if Esc key is press then break out of the loop
            if key == 27:  # The Esc key
                break
        
    # Stop video
    webcam.release()

    # Close all started windows
    cv2.destroyAllWindows()
