import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO

class ObjectDetection:

    def __init__(self, capture_index):

        self.capture_index = capture_index

        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("using device: ", self.device)
        self.model = self.load_model()

    def load_model(self):

        model = YOLO("yolov8m.pt")
        model.fuse()

        return model
    
    def predict(self, frame):
        results = self.model(frame)
        # results = self.model(frame, show = True, conf = 0.4, save = True)
        return results
    
    def plot_bboxes(self, results, frame):

        xyxys = []
        confidences = []
        class_ids = []

        for result in results:
            boxes = result.boxes.cpu().numpy()
            box2 = result.boxes.cpu()
            # print(boxes)
            # xyxys = boxes.xyxy
            # for xyxy in xyxys:
            #     cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])), (0, 255,0), 2)
            xyxys.append(boxes.xyxy)
            confidences.append(boxes.conf)
            class_ids.append(box2.cls)
            
        
        return results[0].plot(), xyxys, confidences, class_ids

frame = "camera_recording.mp4"
object = ObjectDetection("index")
output = object.predict(frame)
ans = object.plot_bboxes(output, frame)
print(ans[3][0:5])
