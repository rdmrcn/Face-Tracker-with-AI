#Face Tracker with python essentials
#one of python Reha Demircan  (R Projects) Projects

#Explanation
#When you create the CascadeClassifier object with this XML file,
#OpenCV loads the data required to detect faces based on the Haar features defined in the XML file.
#This classifier can then be used to scan images or video frames for faces.
#This loop iterates through each detected face's rectangle. cv2.rectangle draws a blue rectangle around each face on the frame, visualizing where the face was detected.


import cv2


def main():
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Start the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Face Tracker', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
