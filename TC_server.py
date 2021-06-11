# -*- coding: utf-8 -*-
# These codes are modified from the codes on the pages:
# https://stackoverflow.com/questions/27676637/stream-video-in-python-use-pygame-lib

# import modules
import os
import sys
import time
import threading
# pygame
import pygame
import pygame.camera
from pygame.locals import *
# ezblock
sys.path.append(r'/opt/ezblock')
import picarmini
# Servo
from ezblock import Servo
from ezblock import PWM
from ezblock import delay

# set variable
# setup FIFO
CAM_FIFO = 'cam_fifo'
if(os.path.exists(CAM_FIFO)):
    pass
else:
    os.mkfifo(CAM_FIFO)

SERVO_PWM00_FIFO = 'servo_pwm00_fifo'
if(os.path.exists(SERVO_PWM00_FIFO)):
    pass
else:
    os.mkfifo(SERVO_PWM00_FIFO)

SERVO_PWM01_FIFO = 'servo_pwm01_fifo'
if(os.path.exists(SERVO_PWM01_FIFO)):
    pass
else:
    os.mkfifo(SERVO_PWM01_FIFO)

SERVO_PWM02_FIFO = 'servo_pwm02_fifo'
if(os.path.exists(SERVO_PWM02_FIFO)):
    pass
else:
    os.mkfifo(SERVO_PWM02_FIFO)

MOTOR_BOTH_FIFO = 'motor_both_fifo'
if(os.path.exists(MOTOR_BOTH_FIFO )):
    pass
else:
    os.mkfifo(MOTOR_BOTH_FIFO )

#resolution
resolution = 640,480
#resolution = 320,240
#resolution = 160,120

def camserver():
#Start Pygame
    pygame.init()
    pygame.camera.init()

    cam = pygame.camera.Camera("/dev/video0",resolution,"RGB")
    cam.start()

#Send data
    while True:
        data = cam.get_raw()
#        image = cam.get_image()
#        data = pygame.image.tostring(image,"RGB",False)
        campipe = open(CAM_FIFO, 'wb')
        campipe.write(data)
        campipe.flush()
        campipe.close()
        time.sleep(0.008) #max 120fps (1/120=0.008333......)
#        time.sleep(0.04) #max 25fps (1/25=0.04)
#        time.sleep(0.1) #max 10fps (1/10=0.1)

#Interupt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def servoserver_pan():
    pwm_P0 = PWM("P0")
    while True:
        with open(SERVO_PWM00_FIFO) as pan:
            for line in pan:
                Servo(pwm_P0).angle(int(line))
                delay(100) # set delay of a servo (ms)

def servoserver_tilt():
    pwm_P1 = PWM("P1")
    while True:
        with open(SERVO_PWM01_FIFO) as tilt:
            for line in tilt:
                Servo(pwm_P1).angle(int(line))
                delay(100) # set delay of a servo (ms)

def servoserver_steer():
    pwm_P2 = PWM("P2")
    while True:
        with open(SERVO_PWM02_FIFO) as steer:
            for line in steer:
                Servo(pwm_P2).angle(int(line))
                delay(100) # set delay of a servo (ms)

def motorserver_both():
    count = int(0)
    while True:
        with open(MOTOR_BOTH_FIFO) as motor:
            zero = int(0)
            for line in motor:
                line = int(line) * int(100)
#                print(line)
# stop
                if  line == zero:
                    print("stop1")
                    picarmini.forward(zero)
# forward
                if line > count:
                    if count >= zero:
                        print("forward1")
                        picarmini.forward(line)
                    if count < zero:
                        if line > zero:
                            print("stop2")
                            picarmini.forward(zero)
                if line == count:
                    if count >= zero:
                        print("forward2")
                        picarmini.forward(line)
                if line < count:
                    if line > zero:
                        print("forward3")
                        picarmini.forward(line)
# backward
                if line < count:
                    if count <= zero:
                        print("backward1")
                        picarmini.forward(line)
                    if count > zero:
                        if line < zero:
                            print("stop3")
                            picarmini.forward(zero)
                if line == count:
                    if count <= zero:
                        print("backward2")
                        picarmini.forward(line)
                if line > count:
                    if line < zero:
                        print("backward3")
                        picarmini.forward(line)
# count
                count = line
#                print(count)

t1 = threading.Thread(target=camserver)
t2 = threading.Thread(target=servoserver_pan)
t3 = threading.Thread(target=servoserver_tilt)
t4 = threading.Thread(target=servoserver_steer)
t5 = threading.Thread(target=motorserver_both)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

print("Server is started.")
