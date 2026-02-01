# Real-Time Vehicle Speed Detection Using Computer Vision

## Overview
This project implements a real-time vehicle speed detection system using classical computer vision techniques.  
It detects moving vehicles from video input, tracks their motion across frames, and estimates speed based on pixel displacement over time.

The system supports both:
- Local video processing using OpenCV
- Real-time web streaming using a Flask backend

---

## Key Features
- Real-time vehicle detection using background subtraction
- Vehicle tracking across frames with unique IDs
- Speed estimation in km/h using distance–time calculation
- Bounding box visualization with live speed overlay
- Flask-based web interface for live video streaming

---

## Tech Stack
- Python
- OpenCV
- NumPy
- Imutils
- Flask

---

## Project Structure
```
Real-Time-Vehicle-Speed-Detection/
│
├── src/
│   ├── speed_detection.py     # Core CV logic
│   ├── web_app.py             # Flask streaming app
│
├── data/
│   └── traffic.mp4            # Input video
│
├── assets/
│   └── output_sample.png      # Screenshot of detection
│
├── requirements.txt
├── README.md
├── .gitignore
```
---

## How It Works
1. Video frames are captured using OpenCV.
2. Background subtraction identifies moving vehicles.
3. Contours are filtered to detect valid vehicles.
4. Vehicles are tracked using centroid matching.
5. Speed is calculated using:
   - Pixel distance moved
   - Time difference between frames
6. Speed is converted from m/s to km/h and displayed on screen.

---

## Sample Output
![Speed Detection Result](output_sample.jpg)

## Installation

```bash
git clone https://github.com/your-username/Real-Time-Vehicle-Speed-Detection.git
cd Real-Time-Vehicle-Speed-Detection
pip install -r requirements.txt
```
## Author: Kersoan P
## Description: Detects and estimates vehicle speed from video input.
