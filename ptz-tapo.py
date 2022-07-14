import sys
from pytapo import Tapo
from flask import Flask

user = "admin" # Camera Username
password = "somepassword" # Camera password
port = 8099 # The port this camera API will run on
app = Flask(__name__)

#Simple PTZ TAPO Camera API for Shinobi
#This APP is not secure, be sure to setup firewall correctly.

@app.route('/pan-left/<camera>')
def pan_left(camera):
    tapo = Tapo(camera, user, password)
    tapo.moveMotor(-5,0)
    return 'pan left'

@app.route('/pan-right/<camera>')
def pan_right(camera):
    tapo = Tapo(camera, user, password)
    tapo.moveMotor(5,0)
    return 'pan right'

@app.route('/tilt-up/<camera>')
def tilt_up(camera):
    tapo = Tapo(camera, user, password)
    tapo.moveMotor(0,5)
    return 'tilt up'

@app.route('/tilt-down/<camera>')
def tilt_down(camera):
    tapo = Tapo(camera, user, password)
    tapo.moveMotor(0,-5)
    return 'tilt down'

@app.route('/get-presets/<camera>')
def get_presets(camera):
    tapo = Tapo(camera, user, password)
    presets = tapo.getPresets()
    return str(presets)

@app.route('/goto-preset/<camera>/<preset>')
def setPreset1(camera, preset):
    tapo = Tapo(camera, user, password)
    preset_id = search_preset(camera, preset)
    if preset_id is not None:
        tapo.setPreset(preset_id)
        return 'Changed to preset {preset}'.format(preset=preset)
    else:
        return 'Preset not found'

@app.route('/save-preset/<camera>/<preset>')
def savePreset3(camera, preset):
    tapo = Tapo(camera, user, password)
    tapo.savePreset(preset)
    return 'Saved to preset {preset}'.format(preset=preset)

@app.route('/start-alarm/<camera>')
def startAlarm(camera):
    tapo = Tapo(camera, user, password)
    tapo.startManualAlarm()
    return 'Alarm started'

@app.route('/stop-alarm/<camera>')
def stopAlarm(camera):
    tapo = Tapo(camera, user, password)
    tapo.stopManualAlarm()
    return 'Alarm stopped'

def search_preset(camera, name):
    tapo = Tapo(camera, user, password)
    presets = tapo.getPresets()
    for id, value in presets.items():
        if value == name:
            return id
    return None

if __name__ == '__main__':
    # Change host to 0.0.0.0 to enable for external access such as shinobi in a docker container
    # but if you do change the host, make sure your network firewall blocks access for everything except your shinobi server.
    app.run(host='0.0.0.0',port=port)
