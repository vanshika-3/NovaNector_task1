import cv2
import os

# Initialize video capture
video = cv2.VideoCapture(0)

# Check if the video capture was successfully initialized
if not video.isOpened():
    print("Error: Could not open video device.")
    exit()

# Load the Haar cascade for face detection
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0

# Get the name ID from the user
nameID = str(input("Enter Your Name: ")).lower()

# Create the path for saving images
path = 'images/' + nameID

# Check if the path already exists
if os.path.exists(path):
    print("Name Already Taken")
    nameID = str(input("Enter Your Name Again: ")).lower()
    path = 'images/' + nameID
    if os.path.exists(path):
        print("Error: Name already taken. Please choose a different name.")
        exit()
else:
    os.makedirs(path)

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture image")
        break

    faces = facedetect.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        count += 1
        name = os.path.join(path, str(count) + '.jpg')
        print("Creating Images........." + name)
        cv2.imwrite(name, frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("WindowFrame", frame)
    
    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if count >= 500:
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()
