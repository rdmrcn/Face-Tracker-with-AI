# Face-Tracker-with-AI
made by Reha Demircan 08.2024
Face Tracker with Python Essentials This project is a face tracking application that uses OpenCV to detect and highlight faces in real-time video streams from a webcam. The application utilizes Haar Cascade Classifiers, specifically designed for face detection, to identify faces and outline them with rectangles on the video feed.
How It Works
Cascade Classifier: The project leverages a pre-trained Haar Cascade XML file (haarcascade_frontalface_default.xml) to detect facial features. OpenCV loads this classifier, which has been trained to identify faces using Haar features.

Face Detection and Tracking: Each frame from the webcam is converted to grayscale for more efficient processing. The classifier then scans the grayscale frame for faces, returning coordinates for each detected face. These coordinates are used to draw blue rectangles around the detected faces, marking them on the live video feed.

Real-Time Display: The application continuously displays the video feed with rectangles around detected faces. Users can exit the application by pressing the 'q' key.

Prerequisites
Python 3.x
OpenCV library
To install OpenCV, run:

bash
Kodu kopyala
pip install opencv-python
Usage
Clone the repository:

bash
Kodu kopyala
git clone https://github.com/your-username/FaceTracker.git
cd FaceTracker
Run the script:

bash
Kodu kopyala
python face_tracker.py
Press 'q' to stop the application.

Code Explanation
The main sections of the code:

Loading the Classifier: Loads the haarcascade_frontalface_default.xml file to detect faces.
Webcam Capture: Starts the webcam and reads frames in a loop.
Face Detection and Visualization: Detects faces and draws rectangles around them in each frame.
Exiting: The loop stops, and the window closes when 'q' is pressed.
Demo
The application runs a continuous real-time detection session, with all detected faces outlined by blue rectangles.
