import sys
from pytapo import Tapo
from flask import Flask

user = "admin" # Camera Username
password = "password" # Camera password
host = "192.168.1.50" # ip of the camera
port = 8092 # The port this camera API will run on
app = Flask(__name__)
tapo = Tapo(host, user, password)

#Simple PTZ TAPO Camera API for Shinobi
#This APP is not secure, be sure to setup firewall correctly.

@app.route('/pan-left')
def pan_left():
    tapo.moveMotor(-5,0)
    return 'pan left'

@app.route('/pan-right')
def pan_right():
    tapo.moveMotor(5,0)
    return 'pan right'

@app.route('/tilt-up')
def tilt_up():
    tapo.moveMotor(0,5)
    return 'tilt up'

@app.route('/tilt-down')
def tilt_down():
    tapo.moveMotor(0,-5)
    return 'tilt down'

if __name__ == '__main__':
    # Change host to 0.0.0.0 to enable for external access such as shinobi in a docker container
    # but if you do change the host, make sure your network firewall blocks access for everything except your shinobi server.
    app.run(host='127.0.0.1',port=port)
