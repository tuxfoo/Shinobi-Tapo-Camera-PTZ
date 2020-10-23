# PTZ Shinobi Tapo Camera controls

A simple web API to control enable use of pan/tilt from Shinobi
Currently, this software is a proof of concept and is by no means secure; so if you want to use it in production make sure to set up your network firewall so that only shinobi can access it.

# Requirements

* python
* pytapo
* flask

# How to run

On your shinobi server install the required python libraries

```
python3 -m pip install pytapo flask
```

Make sure to add the IP and password for your tapo camera in ptz-tapo.py
If you want to leave it running, you can use a program like screen

```
screen python3 ptz-tapo.py
```

In Shinobi, go into the camera settings and find the control settings and add http://127.0.0.1:8092 as your host.

Then set up the correct URL's for pan and tilt which you can find in ptz-tapo.py
