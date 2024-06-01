#!/usr/bin/env python3.8
from controller import Robot, Keyboard

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

# for joint in joints:
    # joint.setPosition(0.0)  # Initial position
    # joint.setVelocity(1.0)  # Initial velocity

print("Robot initialized and ready to receive inputs.")


INCREAMENT = 0.01

# Simulation step
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    # print("key ", key)
    if key != -1:
        print(f"Key pressed: {key}")

    if key == ord('A'):
        print("A key pressed")
        joints[0].setPosition(joints[0].getTargetPosition() + INCREAMENT)  # Increase shoulder_pan_joint position
    elif key == ord('D'):
        print("D key pressed")
        joints[0].setPosition(joints[0].getTargetPosition() - INCREAMENT)  # Decrease shoulder_pan_joint position
    elif key == ord("W") :
        print("W key pressed")
        joints[1].setPosition(joints[1].getTargetPosition() + INCREAMENT)  # Decrease shoulder_pan_joint position
    elif key == ord("S"):
        print("S key pressed")
        joints[1].setPosition(joints[1].getTargetPosition() - INCREAMENT)  # Decrease shoulder_pan_joint position
    elif key == ord("X"):
        print("X key pressed")
        joints[2].setPosition(joints[2].getTargetPosition() + INCREAMENT)  # Decrease shoulder_pan_joint position
    elif key == ord("Z"):
        print("Z key pressed")
        joints[2].setPosition(joints[2].getTargetPosition() - INCREAMENT)  # Decrease shoulder_pan_joint position

    # Add more key bindings for other joints as needed
    pass
