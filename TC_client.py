# -*- coding: utf-8 -*-

import sys
import time
import datetime
import paramiko
import pygame

# IP Address of a SSH Server to connect
ip = "192.168.11.17"

#Resolution
resolution = 640,480
#resolution = 320,240
#resolution = 160,120

# for shutdown
POWER=""

#Start PyGame:
pygame.init()
#screen = pygame.display.set_mode(resolution ,pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.OPENGL|pygame.NOFRAME)
#screen = pygame.display.set_mode(resolution ,pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.NOFRAME)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Tele Command Client')
clock = pygame.time.Clock()

# Mouse
pygame.mouse.set_visible(False)

# Joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Fonts
pygame.font.init()
font = pygame.font.SysFont("Arial",14)
dialogue_font = pygame.font.SysFont('Arial', 15)
alert_font = pygame.font.SysFont('notomono', 60)

# Connect SSH
client = paramiko.SSHClient()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.set_missing_host_key_policy(paramiko.WarningPolicy())
print("Connect to the server.")
client.connect(ip, username='pi', password='raspberry')
#stdin, stdout, stderr = client.exec_command('ps ax | grep TC_server.py | grep --invert-match grep')
#survive = stdout.channel.recv_exit_status()
#print(survive)
#if survive == 1:
#    print("Cannot connect. Aborted.")
#    pygame.display.quit()
#    sys.exit()

#Main program loop:
def main():
    previousImage = ""
    image = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                client.close() # Disconnect SSH
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    global POWER
                    POWER="OFF"
                    sys.exit()
            #Control Servo
            if event.type == pygame.MOUSEWHEEL:
                stdin, stdout, stderr = client.exec_command('ps ax | grep TC_server.py | grep --invert-match grep')
                survive = stdout.channel.recv_exit_status()
                if survive == 1:
#                    pygame.display.quit()
                    sys.exit()
                motor_both0 = "echo "
                motor_both1 = '"'
                motor_both2 = " > motor_both_fifo"
                motor_both = motor_both0 + motor_both1 + str(event.y) + motor_both1 + motor_both2
                stdin, stdout, stderr = client.exec_command(motor_both)

            if event.type == pygame.JOYAXISMOTION:
                stdin, stdout, stderr = client.exec_command('ps ax | grep TC_server.py | grep --invert-match grep')
                survive = stdout.channel.recv_exit_status()
                if survive == 1:
                    sys.exit()
                raw_axis3 = joystick.get_axis(3)
                str_axis3x200 = str(int(200 * raw_axis3))
                servo_pan0 = "echo "
                servo_pan1 = '"'
                servo_pan2 = " > servo_pwm00_fifo"
                servo_pan = servo_pan0 + servo_pan1 + str_axis3x200 + servo_pan1 + servo_pan2
                stdin, stdout, stderr = client.exec_command(servo_pan)
                raw_axis4 = joystick.get_axis(4)
                str_axis4x100 = str(int(100 * raw_axis4))
                servo_tilt0 = "echo "
                servo_tilt1 = '"'
                servo_tilt2 = " > servo_pwm01_fifo"
                servo_tilt = servo_tilt0 + servo_tilt1 + str_axis4x100 + servo_tilt1 + servo_tilt2
                stdin, stdout, stderr = client.exec_command(servo_tilt)
                raw_axis0 = joystick.get_axis(0)
                str_axis0x50 = str(int(50 * raw_axis0))
                servo_steer0 = "echo "
                servo_steer1 = '"'
                servo_steer2 = " > servo_pwm02_fifo"
                servo_steer = servo_steer0 + servo_steer1 + str_axis0x50 + servo_steer1 + servo_steer2
                stdin, stdout, stderr = client.exec_command(servo_steer)

        #Control Camera
        #Receive data
        stdin, stdout, stderr = client.exec_command('ps ax | grep TC_server.py | grep --invert-match grep')
        survive = stdout.channel.recv_exit_status()
        if survive == 1:
#            pygame.display.quit()
            sys.exit()
        stdin, stdout, stderr = client.exec_command('cat cam_fifo')
        data = stdout.read()
        previousImage = image

        #Convert image
        try:
            image = pygame.image.fromstring(data, resolution, "RGB", False)
        except:
            image = previousImage

        # Render image
        screen.blit(image, (0,0))

        # Render messages
        # Drop Shadow
        message00 = str(datetime.datetime.now())
        color00 = 0,0,0
        dialogue00 = dialogue_font.render(message00, True, color00)
        screen.blit(dialogue00, (11,11))
# Render article
#        message01 = str(datetime.datetime.now())
        color01 = 255,255,255
        dialogue01 = dialogue_font.render(message00, True, color01)
        screen.blit(dialogue01, (10,10))

# Render axes values of joystick
#        joystick = pygame.joystick.Joystick(0)
#        joystick.init()
        raw_axis3 = joystick.get_axis(3)
        message02 = str(int(200 * raw_axis3))
        dialogue02 = dialogue_font.render(message02, True, color01)
        screen.blit(dialogue02, (10,30))

        
        raw_axis4 = joystick.get_axis(4)
        message03 = str(int(100 * raw_axis4))
        dialogue03 = dialogue_font.render(message03, True, color01)
        screen.blit(dialogue03, (10,60))
        
        raw_axis0 = joystick.get_axis(0)
        message04 = str(int(50 * raw_axis0))
        dialogue04 = dialogue_font.render(message04, True, color01)
        screen.blit(dialogue04, (10,90))

#        clock.tick(120) # limit 120fps
        clock.tick(60) # limit 60fps

        pygame.display.flip()

while True:
    try:
        print("Client is started.")
        main()
    except:
        if POWER == "OFF":
            pygame.display.quit()
            client.close() # Disconnect SSH
            print("Client is stopped.")
            sys.exit()
        print("Exception!")
        print("Reconnect to the server.")
        print(str(datetime.datetime.now()))
        client.close()
        client.connect(ip, username='pi', password='raspberry')
        stdin, stdout, stderr = client.exec_command('ps ax | grep TC_server.py | grep --invert-match grep')
        survive = stdout.channel.recv_exit_status()
        if survive == 1:
            black = 0,0,0
            screen.fill(black)
            print("Cannot reconnect to the server. Aborted.")
            message041 = "Cannot connect"
            message042 = "to the server!"
            color04 = 255,0,0
            dialogue041 = alert_font.render(message041, True, color04)
            dialogue042 = alert_font.render(message042, True, color04)
            screen.blit(dialogue041, (60,120))
            screen.blit(dialogue042, (60,240))
            clock.tick(1)
            pygame.display.flip()
