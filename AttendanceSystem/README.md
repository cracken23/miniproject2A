Attendance System
Overview
This Attendance System uses facial recognition and YOLO object detection to automatically register student attendance. It captures real-time video feed, detects faces, recognizes them, and logs attendance data into an SQLite database. The system features a web interface to view and manage attendance records.

Project Structure
graphql
Copy code
AttendanceSystem/
│
├── client.py                 # Main script for capturing video, detecting faces, and sending attendance data
├── face_recognition_module.py # Module for handling face recognition and loading known faces
├── train_faces.py            # Script for training the face recognition model with known faces
├── database_setup.py         # Script for setting up the SQLite database
├── clear_db.py               # Script for clearing the SQLite database
│
├── models/                   # Directory for model files
│   ├── yolov10s.pt           # YOLOv10 model file
│
├── dataset/                  # Directory containing folders with student images for training
│   ├── student1/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   ├── student2/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   └── ...
│
├── templates/                # Directory for HTML templates
│   └── attendance.html       # HTML file for displaying attendance records
│
├── attendance.db             # SQLite database file for storing attendance records
│
└── requirements.txt          # File listing the required Python packages
Setup
Install Dependencies: Ensure you have Python installed, then install the required packages using:

sh
Copy code
pip install -r requirements.txt
Set Up Database: Run the database_setup.py script to set up the SQLite database:

sh
Copy code
python database_setup.py
Train Face Recognition Model: Run the train_faces.py script to train the face recognition model with known faces:

sh
Copy code
python train_faces.py
Run the Client: Start the client script to begin capturing video and logging attendance:

sh
Copy code
python client.py
View Attendance Records: Start the Flask web server and navigate to http://127.0.0.1:5000/ to view attendance records:

sh
Copy code
flask run
Scripts
client.py: Main script for capturing video feed, detecting faces using YOLO, recognizing faces using the face recognition model, and sending attendance data to the server.
face_recognition_module.py: Module for handling face recognition, including loading known face encodings and recognizing faces.
train_faces.py: Script for loading images from the dataset directory and training the face recognition model.
database_setup.py: Script to create the SQLite database and initialize the attendance table.
clear_db.py: Script to clear all records from the SQLite database.
Database
The SQLite database attendance.db stores attendance records with the following schema:

id: Auto-incremented primary key
student_name: Name of the student
timestamp: Time when the attendance was recorded (in seconds since epoch)
HTML Template
The attendance.html file in the templates directory is used to display attendance records. It fetches records from the Flask server and updates the table every 5 seconds.

Requirements
Python 3.x
Required Python packages listed in requirements.txt
Sample requirements.txt
txt
Copy code
flask
face_recognition
opencv-python
requests
torch
ultralytics
Notes
Ensure that the YOLO model file yolov10s.pt is placed in the models directory.
The dataset directory should contain subfolders for each student with their images for training.