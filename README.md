# Smart-Signal
Smart Signal is an openCV project integrated with IoT, in this case RaspberryPi4. 

Project Topic:
 Development of an intelligent pedestrian crossing system utilizing computer vision to enhance safety at road crossings.

Objective: 
To detect pedestrians and their intentions (e.g., raising hands) in real-time using a Raspberry Pi 4 and YOLOv8 model, activating red LED lights to signal vehicles to stop.
Test the system in various conditions to refine detection accuracy and responsiveness.

Expected Results:
A reliable and responsive system that automatically activates red lights upon detecting pedestrians or hand signals.
<img src="https://github.com/user-attachments/assets/4e720823-c4d4-451c-a6bc-086e2f202d29" width="480">


Methodology
Devices which were used in the project are :
 Raspberry Pi 4  
 Camera Module  
 Red LED Lights  
 Breadboard  
 Jumper Wires  
 Power Supply  
 MicroSD Card  
<img src="https://github.com/user-attachments/assets/cdfc0820-48c5-43e7-a44e-be8205be757c" width="480">




<img src="https://github.com/user-attachments/assets/b67243f9-0dd1-4046-9f42-98b5a4ec9cb9" width="480">


Special thanks to <img src="https://github.com/user-attachments/assets/0bc4e8fc-3d9e-4759-a940-9a9d79e26c1d" width="160"> library





Prototype/Experiment Details
The camera will capture real time video on which Raspberry Pi will act upon using the YoloV8 model.

<img src="https://github.com/user-attachments/assets/377e9c18-38e5-4066-b3ac-bb3b3ef591e3" width="480">


Red Light Pin is adjusted to Pin No. 18.

<img src="https://github.com/user-attachments/assets/5894312a-1842-42af-8fcb-8a06cfb09728" width="480">




FURTHER:
Red Light will turn on whenever a person is detected on the zebra-crossing.
Red Light will also turn on whenever a person, even when not on the road, but on the edge, raises hand, signaling the car to stop.
Power Supply is provided to Raspberry Pi from adapter.

Results & Discussion

<img src="https://github.com/user-attachments/assets/11cf81c7-1205-4464-89dc-c6ae0ec1001b" width="480">


The Red LEDs light up as intended. A box was drawn on zebra-crossing. The Yolo model lights up Red Light whenever a person is detected inside the box drawn.
Two boxes are drawn adjacent to the zebra-crossing. Whenever a person raises their hand, pose detection function lights up the red light.




<img src="https://github.com/user-attachments/assets/1f136c3b-a8c4-4a14-9b04-9a4ab4f087fe" width="480">





CONCLUSION:
 
This project demonstrates an ML-based pedestrian crossing system using computer vision to detect pedestrians and interpret hand gestures as crossing intent. By combining YOLOv8’s pose detection on a Raspberry Pi, the system can activate red LED signals to alert vehicles when pedestrians are detected on a crossing or are preparing to cross. This setup provides a  scalable solution for enhancing pedestrian safety in various urban settings. 

APPLICATIONS:
 
Urban Crosswalks in Smart Cities
School Zones
Railway Crossings
Industrial Facilities





