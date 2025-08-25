import cv2
import numpy as np
import imutils
import time

# Initialize video capture
cap = cv2.VideoCapture("traffic.mp4")  # Replace with 0 for webcam

# Background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Vehicle tracking dictionary {ID: (x, y, last_time)}
vehicles = {}
next_vehicle_id = 1  # Unique ID for tracking vehicles

# Speed calibration: Change based on real-world size
pixels_per_meter = 10  # Example: 10 pixels = 1 meter
fps = cap.get(cv2.CAP_PROP_FPS) or 30  # Fallback to 30 FPS if unavailable

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = imutils.resize(frame, width=800)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fg_mask = bg_subtractor.apply(gray)

    # Find contours of moving objects
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    current_time = time.time()
    new_vehicles = {}

    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Filter small objects 
            x, y, w, h = cv2.boundingRect(contour)
            center_x, center_y = x + w // 2, y + h // 2

            # Check if vehicle already exists
            matched_id = None
            for vid, (px, py, last_time) in vehicles.items():
                if abs(center_x - px) < 50 and abs(center_y - py) < 50:  # Close match
                    matched_id = vid
                    break

            if matched_id is None:  # New vehicle detected
                matched_id = next_vehicle_id
                next_vehicle_id += 1

            # Calculate speed if previous position exists
            if matched_id in vehicles:
                px, py, last_time = vehicles[matched_id]
                time_diff = current_time - last_time

                if time_diff > 0:  # Avoid division by zero
                    distance = np.sqrt((center_x - px) ** 2 + (center_y - py) ** 2)
                    speed_mps = (distance / pixels_per_meter) / time_diff
                    speed_kph = speed_mps * 3.6  # Convert m/s to km/h
                else:
                    speed_kph = 0  # Default to 0 if no movement

                # Display speed
                cv2.putText(frame, f"{int(speed_kph)} km/h", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            # Update vehicle tracking
            new_vehicles[matched_id] = (center_x, center_y, current_time)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    vehicles = new_vehicles  # Update vehicle tracking for the next frame

    # Display video
    cv2.imshow("Real-Time Vehicle Speed Detection", frame)

    if cv2.waitKey(30) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
