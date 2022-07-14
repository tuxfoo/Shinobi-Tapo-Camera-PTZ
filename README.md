# PTZ Shinobi/AgentDVR/HomeAssistant Tapo Camera controls

A simple web API to enable use of pan/tilt from third party software such as shinobi, agentdvr and home assistant

Currently, this software is a proof of concept and is by no means secure; so if you want to use it in production make sure to set up your network firewall so that only the app that needs to make API calls can access it.

# Requirements

* python
* pytapo
* flask

# How to run

On your shinobi server install the required python libraries

```
python3 -m pip install pytapo flask
```

Make sure to add the username and password for your tapo camera's in ptz-tapo.py
If you want to leave it running, you can use a program like screen

```
screen python3 ptz-tapo.py
```

As long as all your tapo camera's have the same username and password, you can make API calls to all of them.

At the Moment, this app enables you to use Pan and Tilt, Save and goto presets, start and stop the alarm.

Check out ptz-tapo.py for which api calls you can make.

Example (Save a preset at current position on camera with ip address 192.168.1.155 called "my_second_preset"):
```
http://127.0.0.1:8092/save-preset/192.168.1.155/my_second_preset
```

Example (Start the alarm on camera with ip address 192.168.1.156)
```
http://127.0.0.1:8092/start-alarm/192.168.1.156
```

Shinobi and AgentDVR should have a file called PTZ2.xml, we can add our camera controls to it.

eg (Will need to do this for each camera);

```
  <Camera id="270">
    <Makes>
      <Make Name="TP-Link" Model="Tapo Camera 1" />
    </Makes>
        <CommandURL>/</CommandURL>
    <Commands>
      <Left>pan-left/192.168.1.155</Left>
      <Right>pan-right/192.168.1.155</Right>
      <Up>pan-up/192.168.1.155</Up>
      <Down>pan-down/192.168.1.155</Down>
    </Commands>
    <ExtendedCommands>
      <Command Name="Go Preset 1">goto-preset/192.168.1.155/one</Command>
      <Command Name="Go Preset 2">goto-preset/192.168.1.155/two</Command>
      <Command Name="Go Preset 3">goto-preset/192.168.1.155/three</Command>
      <Command Name="Set Preset 1">save-preset/192.168.1.155/one</Command>
      <Command Name="Set Preset 2">save-preset/192.168.1.155/two</Command>
      <Command Name="Set Preset 3">save-preset/192.168.1.155/three</Command>
      <Command Name="Start Alarm">start-alarm/192.168.1.155</Command>
      <Command Name="Stop Alarm">stop-alarm/192.168.1.155</Command>
    </ExtendedCommands>
  </Camera>
```

In Home Assistant we can add a shell service to make api calls

eg;

```
shell_command:
  first_preset: 'curl http://tuxfoo01:8099/goto-preset/192.168.1.155/one'
  second_preset: 'curl http://tuxfoo01:8099/goto-preset/192.168.1.155/two'
  start_cam1_alarm: 'curl http://tuxfoo01:8099/start-alarm/192.168.1.155'
  stop_cam1_alarm: 'curl http://tuxfoo01:8099/stop-alarm/192.168.1.155'
```