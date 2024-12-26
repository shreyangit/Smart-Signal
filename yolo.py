import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
from gpiozero import LED, Buzzer
from time import sleep

# Initialize the GPIO pin for the LED and buzzer
output = LED(17)
buzzer = Buzzer(18)

# Set up the camera with Picam
picam2 = Picamera2()
picam2.preview_configuration.main.size = (320, 640)
picam2.preview_configuration.main.format = "BGR888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
picam2.awb_mode = 'auto'

# Load the YOLOv8 pose model
model = YOLO("yolov8n-pose.pt")

def check_wrist_above_head(results):
    """
    Check if either wrist is above the head
    Returns True if either wrist is above head, False otherwise
    """
    try:
        # Check if we have any detections
        if len(results) == 0:
            print("No detections found")
            return False

        # Get the first detection result
        result = results[0]
        
        # Print the shape and content of keypoints for debugging
        print("Keypoints shape:", result.keypoints.shape)
        print("Keypoints data:", result.keypoints.data)
        
        # Get keypoints tensor
        keypoints = result.keypoints.data[0]  # Get keypoints for first person
        
        # Define keypoint indices
        NOSE_IDX = 0
        LEFT_WRIST_IDX = 9
        RIGHT_WRIST_IDX = 10
        
        # Extract coordinates
        nose_y = float(keypoints[NOSE_IDX][1])
        left_wrist_y = float(keypoints[LEFT_WRIST_IDX][1])
        right_wrist_y = float(keypoints[RIGHT_WRIST_IDX][1])
        
        # Get confidence scores
        nose_conf = float(keypoints[NOSE_IDX][2])
        left_wrist_conf = float(keypoints[LEFT_WRIST_IDX][2])
        right_wrist_conf = float(keypoints[RIGHT_WRIST_IDX][2])
        
        # Debug print
        print(f"Nose Y: {nose_y:.2f} (conf: {nose_conf:.2f})")
        print(f"Left Wrist Y: {left_wrist_y:.2f} (conf: {left_wrist_conf:.2f})")
        print(f"Right Wrist Y: {right_wrist_y:.2f} (conf: {right_wrist_conf:.2f})")
        
        # Check if keypoints are valid (confidence > 0.5)
        if nose_conf < 0.5:
            print("Nose detection not confident enough")
            return False
            
        # Check if either wrist is above nose with good confidence
        left_wrist_raised = (left_wrist_conf > 0.5) and (left_wrist_y < nose_y)
        right_wrist_raised = (right_wrist_conf > 0.5) and (right_wrist_y < nose_y)
        
        if left_wrist_raised or right_wrist_raised:
            print("Wrist raised above head detected!")
            return True
            
        return False
        
    except Exception as e:
        print(f"Error in check_wrist_above_head: {str(e)}")
        return False

try:
    print("Starting pose detection...")
    while True:
        # Capture a frame from the camera
        frame = picam2.capture_array()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Run YOLO pose model on the captured frame
        results = model.predict(frame_rgb, imgsz=320, conf=0.5)
        
        # Check if wrist is above head and control LED
        wrist_raised = check_wrist_above_head(results)
        if wrist_raised:
            output.on()
            print("LED ON")
        else:
            output.off()
            print("LED OFF")
        
        # Visualize the results
        annotated_frame = results[0].plot()
        
        # Add FPS counter
        inference_time = results[0].speed['inference']
        fps = 1000 / inference_time
        text = f'FPS: {fps:.1f}'
        
        # Draw FPS on frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize(text, font, 1, 2)[0]
        text_x = annotated_frame.shape[1] - text_size[0] - 10
        text_y = text_size[1] + 10
        cv2.putText(annotated_frame, text, (text_x, text_y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Display the frame
        cv2.imshow("Camera", annotated_frame)
        
        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program stopped by user")
except Exception as e:
    print(f"Error in main loop: {str(e)}")
finally:
    # Cleanup
    output.off()
    buzzer.off()
    cv2.destroyAllWindows()
    picam2.stop()
    print("Cleanup completed")
