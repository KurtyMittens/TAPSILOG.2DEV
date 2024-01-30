import cv2
from thisIsHuck import HUCK
import mediapipe


cap = cv2.VideoCapture(0)
recognition = HUCK()
process_this_frame = 29

while 1 > 0:
    ret, frame = cap.read()
    if ret:
        # Different resizing options can be chosen based on desired program runtime.
        # Image resizing for more stable streaming
        img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        process_this_frame = process_this_frame + 1
        if process_this_frame % 30 == 0:
            predictions = recognition.huck_predicts(img, model_path="huck.clf")
        # frame = show_prediction_labels_on_image(frame, predictions)
        print(predictions)
        cv2.imshow('camera', frame)
        if ord('q') == cv2.waitKey(10):
            cap.release()
            cv2.destroyAllWindows()
            exit(0)
