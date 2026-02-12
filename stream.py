import cv2
import numpy as np

from ultralytics import YOLO

# Loading the YOLO11 model
model = YOLO("yolo11n.pt")

# Openning the video file
#video_path = "path/to/video.mp4"
cap = cv2.VideoCapture(0)

# Loopping through the video frames
while cap.isOpened():
    # Reading a frame from the video
    success, frame = cap.read()

    if success:
        # Running YOLO11 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, tracker="bytetrack.yaml")

        # Visualizing the results on the frame
        annotated_frame = results[0].plot()

        # Displaying the annotated frame
        cv2.imshow("YOLO11 Tracking", annotated_frame)

        # Breaking the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Breaking the loop if the end of the video is reached
        break

# Releasing the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()