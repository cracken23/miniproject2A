import cv2
import torch
from ultralytics import YOLO

# Load the YOLOv10x model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('yolov10s.pt').to(device)  # Load model to GPU if available

# Function to perform object detection on frames from the webcam
def detect_objects_from_webcam():
    cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from webcam.")
            break

        # Resize the frame for inference
        frame = cv2.resize(frame, (320, 320))  # Resize to 640x640 or another size

        # Convert frame to a tensor and move to device
        frame_tensor = torch.from_numpy(frame).permute(2, 0, 1).float().to(device) / 255.0
        frame_tensor = frame_tensor.unsqueeze(0)  # Add batch dimension

        # Perform inference
        results = model(frame_tensor)

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
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_objects_from_webcam()
