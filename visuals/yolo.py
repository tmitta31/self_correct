import cv2
from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')
print("first step")
video_path = "test1.mp4"
print("second step")
cap = cv2.VideoCapture(video_path) # replace the input with a 0 for live webcam
print("third step")

while cap.isOpened():
    success, frame = cap.read()
    print("in for loop")
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO8 Inferance", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()