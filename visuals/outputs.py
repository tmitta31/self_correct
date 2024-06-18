# import torch
# import numpy as np
# import cv2
# from time import time
# from ultralytics import YOLO

# class ObjectDetection:

#     def __init__(self, capture_index):

#         self.capture_index = capture_index

#         self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
#         print("using device: ", self.device)
#         self.model = self.load_model()

#     def load_model(self):

#         model = YOLO("yolov8m.pt")
#         model.fuse()

#         return model
    
#     def predict(self, frame):

#         results = self.model(frame)
#         return results
    
#     def plot_bboxes(self, results, frame):

#         xyxys = []
#         confidences = []
#         class_ids = []

#         for result in results:
#             boxes = result.boxes.cpu().numpy()

#             print(boxes)

#             print(boxes)

#         return frame

# object = ObjectDetection("index")
# output = object.predict("test1.mp4")
# object.plot_bboxes(output, "test1.mp4")
