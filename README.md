# ETRobo Project
This is a project of making an easy going [telepresence](https://en.wikipedia.org/wiki/Telepresence) robot.

# References
https://docs.python.org/3.8/tutorial/index.html

https://docs.python.org/ja/3.8/tutorial/index.html

https://www.python.org/dev/peps/pep-0008/

https://pep8-ja.readthedocs.io/ja/latest/

https://stackoverflow.com/help/licensing

https://ja.stackoverflow.com/help/licensing

https://stackoverflow.com/questions/45508213/using-channels-with-paramiko

https://stackoverflow.com/questions/550001/fully-transparent-windows-in-pygame

https://stackoverflow.com/questions/27676637/stream-video-in-python-use-pygame-lib

https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python

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
* [paramiko](https://www.paramiko.org/)
* * for communicating with server

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
