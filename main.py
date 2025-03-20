import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")
st.image('Motionmatics.jpg')

col1,col2=st.columns([2,1])

with col1:
    run =st.checkbox('Run',value=True)
    FRAME_WINDOW=st.image([])

with col2:
    output_text_area=st.title("Answer")
    output_text_area=st.subheader("")



genai.configure(api_key="AIzaSyAdzaGJSkNX55cjpKWeUJdzvgYNJN65gG8")
model = genai.GenerativeModel("gemini-1.5-flash")
# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 450)

# Initialize the HandDetector class
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)


def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)  # Set draw to False to remove hand markers
    if hands:
        hand1 = hands[0]  # Get the first hand detected
        lmList = hand1["lmList"]  # List of 21 landmarks for the first hand

        # Count the number of fingers up
        fingers = detector.fingersUp(hand1)
        return fingers, lmList
    return None


def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:  # Check if index finger is up
        current_pos = lmList[8][0:2]  # Get position of index finger (landmark 8)

        if prev_pos is None:
            prev_pos = current_pos

        # Draw line from previous position to current position
        cv2.line(canvas, tuple(prev_pos), tuple(current_pos), (88, 219,255), 10)
    elif fingers==[1,0,0,0,1]:
        canvas = np.zeros_like(img)
    return current_pos , canvas

def sendToAI(model,canvas,fingers):
    if fingers == [1,1,1,1,0]:
        pil_image=Image.fromarray(canvas)
        response = model.generate_content(["If its solvable then give solution else try your best to describe the image",pil_image])
        return response.text


prev_pos = None
canvas = None
image_combined = None
output_text= ""
# Continuously get frames from the webcam
while True:
    success, img = cap.read()  # Capture frame
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)



    info = getHandInfo(img)

    if info:
        fingers, lmList = info
        prev_pos, canvas = draw(info, prev_pos, canvas)  # Draw line and update prev_pos
        output_text=sendToAI(model, canvas, fingers)
    image_combined= cv2.addWeighted(img,0.7,canvas,0.3,8)
    FRAME_WINDOW.image(image_combined,channels="BGR")

    output_text_area.text(output_text)

    # Display the image in a window
    #cv2.imshow("Image", img)
    #cv2.imshow("Canvas", canvas)
    #cv2.imshow("Image_combined", image_combined)
    # Wait for 1 millisecond and update the frame
    cv2.waitKey(1)
