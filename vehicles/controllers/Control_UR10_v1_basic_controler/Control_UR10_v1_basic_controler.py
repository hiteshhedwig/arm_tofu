#!/usr/bin/env python3.8
from controller import Robot, Keyboard, Camera
import cv2
import numpy as np

# Create the Robot instance
robot = Robot()

# Get the time step of the current world
timestep = int(robot.getBasicTimeStep())

# Enable the keyboard device
keyboard = Keyboard()
keyboard.enable(timestep)

# Define joints
joints = [
    robot.getDevice('shoulder_pan_joint'),
    robot.getDevice('shoulder_lift_joint'),
    robot.getDevice('elbow_joint'),
    robot.getDevice('wrist_1_joint'),
    robot.getDevice('wrist_2_joint'),
    robot.getDevice('wrist_3_joint')
]


# Enable position sensors on all joints
position_sensors = [robot.getDevice('shoulder_pan_joint_sensor'),
                    robot.getDevice('shoulder_lift_joint_sensor'),
                    robot.getDevice('elbow_joint_sensor'),
                    robot.getDevice('wrist_1_joint_sensor'),
                    robot.getDevice('wrist_2_joint_sensor'),
                    robot.getDevice('wrist_3_joint_sensor')]

for sensor in position_sensors:
    sensor.enable(timestep)

# Initialize the camera
camera = robot.getDevice('camera')
camera.enable(timestep)

INCREMENT = 0.01

# Simulation step
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    if key != -1:
        print(f"Key pressed: {key}")

    if key == ord('A'):
        print("A key pressed")
        joints[0].setPosition(joints[0].getTargetPosition() + INCREMENT)  # Increase shoulder_pan_joint position
    elif key == ord('D'):
        print("D key pressed")
        joints[0].setPosition(joints[0].getTargetPosition() - INCREMENT)  # Decrease shoulder_pan_joint position
    elif key == ord("W"):
        print("W key pressed")
        joints[1].setPosition(joints[1].getTargetPosition() + INCREMENT)  # Increase shoulder_lift_joint position
    elif key == ord("S"):
        print("S key pressed")
        joints[1].setPosition(joints[1].getTargetPosition() - INCREMENT)  # Decrease shoulder_lift_joint position
    elif key == ord("X"):
        print("X key pressed")
        joints[2].setPosition(joints[2].getTargetPosition() + INCREMENT)  # Increase elbow_joint position
    elif key == ord("Z"):
        print("Z key pressed")
        joints[2].setPosition(joints[2].getTargetPosition() - INCREMENT)  # Decrease elbow_joint position
    elif key == ord("O"):
        print("O key pressed")
        joints[3].setPosition(joints[3].getTargetPosition() + INCREMENT)  # Increase elbow_joint position
    elif key == ord("P"):
        print("P key pressed")
        joints[3].setPosition(joints[3].getTargetPosition() - INCREMENT)  # Decrease elbow_joint position


    # Get image from the camera
    image = camera.getImage()

    # Convert the image to a format OpenCV can use
    width = camera.getWidth()
    height = camera.getHeight()
    image_array = np.frombuffer(image, np.uint8).reshape((height, width, 4))
    
    # Convert RGBA image to BGR (OpenCV format)
    image_bgr = cv2.cvtColor(image_array, cv2.COLOR_BGRA2BGR)
    
    # cv2.imshow('Camera', image_bgr)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break

# Release resources
cv2.destroyAllWindows()
