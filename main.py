import torch
import cv2
from message import send_whatsapp_message
from mobile_msg import forward
from sqlite3_queries import insert_record_values
from PIL import Image
from datetime import datetime as dt

# loads the model with given weights, custom is for custom model
detector = torch.hub.load("yolov5", path= "yolov5/runs/train/exp2/weights/best.pt", model= "custom", source= "local")
# local mean local storage we can also give GitHub directory link

# for a video let's split it into frames
video = cv2.VideoCapture("rtsp://192.168.147.231:8080/h264_ulaw.sdp")
# video = cv2.VideoCapture("videoplayback.mp4")
frame_exists, frame = video.read()

can_message: bool = True # to control flow

while frame_exists:

    # It accepts only image no mp4
    results = detector(frame)

    boxes, classes, scores = [], ["Elephant"], []

    for detection in results.xyxy[0]:
        print(detection)
        *bbox, confidence, label = detection
        if confidence >= 0.8 and can_message:
            # storing frame(ndarray)
            img = Image.fromarray(obj= frame)
            img.save(fp= "captured.jpg")

            print("found")
            scores.append(float(confidence))

            # # send message
            # send_whatsapp_message(confidence= float(confidence),
            #                        label= classes[int(label)], # label is in float
            #                        image_file= "objfoufna.jpg")

            # mobile message offline
            forward(confidence= float(confidence))

            # store it in database
            date, time = str(dt.now()).split()
            time = time.split('.')[0] # filtering micro seconds
            now = f"{date} {time}"
                                            # label is in float
            insert_record_values(animal_name= classes[int(label)],
                                 time_of_incident= now,
                                 confidence= float(confidence),
                                 image= frame)

            can_message = False


    if not can_message:
        break

        # elif confidence < 0.8:
        #     can_message = True

    frame_exists, frame = video.read()
