# Motionmatics

Motionmatics is a project that uses hand gestures, detected with OpenCV, to interact with Gemini AI to solve problems represented by the drawings. Users can draw a problem using hand gestures, and the system leverages the Gemini API to provide a solution.

## Features

*   **Real-time Hand Gesture Recognition:** Uses OpenCV to detect and track hand movements.
*   **Drawing Interface:** Allows users to draw on a canvas using hand gestures.
*   **Gemini AI Integration:** Sends the drawn content to Gemini AI, which interprets the drawing and provides a relevant solution.
*   **Problem Solving:** Solves mathematical or other visual problems based on the hand-drawn input.

## Technologies Used

*   Python
*   OpenCV
*   Gemini AI (using the Gemini API)
*   NumPy

## Interacting with the Application

*   The application will display a live feed from your webcam [2].
*   Use the following hand gestures:
    *   **Draw:** Use index finger to draw on the canvas.
    *   **Clear:** Use a specific gesture (thumb and pinky finger extended) to clear the canvas.
    *   **Solve:** Use a specific gesture (all fingers but thumb extended) to submit the drawing for solving.
