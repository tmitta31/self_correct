import cv2
from ultralytics import YOLO


class Segmentation:

    def __init__(self, capture_index):

        self.capture_index = capture_index
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("using device: ", self.device)
        self.model = self.load_model()
    
    def load_model(self):

        model = YOLO('yolov8n-seg.pt')
        model.fuse()

        return model
    
    def predict(self, frame):
        cap = cv2.VideoCapture(frame) # replace the input with a 0 for live webcam

        while cap.isOpened():
            success, frame = cap.read()
            print("in for loop")
            if success:
                results = self.model(frame)
                annotated_frame = results[0].plot()
                cv2.imshow("YOLO8 Inferance", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

# model = YOLO('yolov8n-seg.pt')
# print("first step")
# video_path = "test1.mp4"
# print("second step")
# cap = cv2.VideoCapture(video_path) # replace the input with a 0 for live webcam
# print("third step")

# while cap.isOpened():
#     success, frame = cap.read()
#     print("in for loop")
#     if success:
#         results = model(frame)
#         annotated_frame = results[0].plot()
#         cv2.imshow("YOLO8 Inferance", annotated_frame)

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()