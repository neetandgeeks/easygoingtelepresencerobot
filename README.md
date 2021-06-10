# ETRobo Project
This is a project of making an easy going [telepresence](https://en.wikipedia.org/wiki/Telepresence) robot.

# Showcase

a startup message sample.

![a startup message sample](https://raw.githubusercontent.com/neetandgeeks/easygoingtelepresencerobot/main/pictures/StartupMessageSample.gif)

Proof of Concept with [Sunfounder](https://github.com/sunfounder)'s [PiCar-X](https://www.sunfounder.com/products/picar-x).
![PoC](https://raw.githubusercontent.com/neetandgeeks/easygoingtelepresencerobot/main/pictures/ProofofConcept001.jpg)

By using [OpenTrack](https://github.com/opentrack/opentrack), It can be controlled with head tracking.

# the Client

## Python Packages / Modules

* [PyGame](https://www.pygame.org/docs/)
* * for GUI
* [pywin32](https://github.com/mhammond/pywin32)
* * for using Win32API

## Interface, etc.

* [OpenTrack](https://github.com/opentrack/opentrack)
* * for head tracking

# the Server

## Python Packages / Modules

* [PyGame](https://www.pygame.org/docs/)
* * for receiving commands and sending videos
* [ezblock](https://github.com/sunfounder-ezblock/ezb-pi)
* * for controlling Motors

## Interface, etc.

* Named pipe
* * for receiving commands and sending videos via SSH
* SSH
* * for communicating with client
