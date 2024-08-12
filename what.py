import cv2
import torch
import threading
from ultralytics import YOLO
import time

# Load the YOLOv10x model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('yolov10x.pt').to(device)

# Global variables
frame = None
lock = threading.Lock()
capturing = True

def capture_frames():
    global frame, capturing
    cap = cv2.VideoCapture(0)
    while capturing:
        ret, f = cap.read()
        if ret:
            with lock:
                frame = f
    cap.release()

# Function to perform object detection
def detect_objects_from_webcam():
    global frame, capturing
    thread = threading.Thread(target=capture_frames)
    thread.daemon = True
    thread.start()

    while True:
        with lock:
            if frame is None:
                continue

            # Resize the frame for inference
            resized_frame = cv2.resize(frame, (320, 320))

            # Convert to tensor and move to device
            frame_tensor = torch.from_numpy(resized_frame).permute(2, 0, 1).float().to(device) / 255.0
            frame_tensor = frame_tensor.unsqueeze(0)  # Add batch dimension

            # Perform inference and measure inference time
            start_time = time.time()
            results = model(frame_tensor)
            inference_time = time.time() - start_time

            # Process results
            for box in results[0].boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = box.conf[0]
                cls = box.cls[0]
                print(f'Detected: {model.names[int(cls)]} with confidence: {conf:.2f}')

            # Render results on the original frame
            annotated_frame = results[0].plot()

            # Display the resulting frame
            cv2.imshow('Webcam Object Detection', annotated_frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                capturing = False
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_objects_from_webcam()
