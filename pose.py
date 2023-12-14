import cv2
import time
import mediapipe as mp

#this is software 1.0 way scuffed for counting repetitions on pushups squats curls

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

pose_dict = {
0 : "nose",
1 : "left eye (inner)",
2 : "left eye",
3 : "left eye (outer)",
4 : "right eye (inner)",
5 : "right eye",
6 : "right eye (outer)",
7 : "left ear",
8 : "right ear",
9 : "mouth (left)",
10 : "mouth (right)",
11 : "left shoulder",
12 : "right shoulder",
13 : "left elbow",
14 : "right elbow",
15 : "left wrist",
16 : "right wrist",
17 : "left pinky",
18 : "right pinky",
19 : "left index",
20 : "right index",
21 : "left thumb",
22 : "right thumb",
23 : "left hip",
24 : "right hip",
25 : "left knee",
26 : "right knee",
27 : "left ankle",
28 : "right ankle",
29 : "left heel",
30 : "right heel",
31 : "left foot index",
32 : "right foot index"
}

#TODO: make a menu for picking what exercise to do 
#TODO: make a class?
#TODO: make angle calc
#TODO: check if stuff is visible
#TODO: check if angles for reps
#TODO: add reps to display
# Capture video
cap = cv2.VideoCapture(0) # 0 for webcam, replace with video file path for a video file

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB and process it with MediaPipe Pose.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw landmarks
    if results.pose_landmarks:
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    #display landmark positions
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            print(f"pose: {pose_dict[id]}\n x: {lm.x}\n y: {lm.y}\n z: {lm.z}\n visibility: {lm.visibility}\n")




    # Display the image
    cv2.imshow('MediaPipe Pose', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
