import requests
import time
import usb.core
import usb.util
from tuning import Tuning
import numpy as np
import sounddevice as sd

past_sounds = np.zeros(50)
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
Mic_tuning = None
message = ""

if dev:
    Mic_tuning = Tuning(dev)
url = "https://ecae-137-110-116-189.ngrok-free.app/sounds"

def volume(indata, outdata, frames, time2, status):
    volume = np.linalg.norm(indata)*10
    print(volume)
    global past_sounds
    past_sounds = np.append(past_sounds, volume)
    past_sounds = np.delete(past_sounds, 0)
    global Mic_tuning
    global message
    avg = np.average(past_sounds)
    std = np.std(past_sounds)
    voice = Mic_tuning.is_voice()
    direction = Mic_tuning.direction
    direc_str = ""
    if(direction >= 45 and direction < 135):
        direc_str = "BACK"
    elif(direction >= 135 and direction <225):
        direc_str = "RIGHT"
    elif(direction >= 255 and direction < 315):
        direc_str = "FRONT"
    else:
        direc_str = "LEFT"
	# identify different noises:
    if volume > (avg + 1.5*std) and Mic_tuning.is_voice() and message == "":
        message = "HUMAN," + "LOUD," + direc_str
    elif volume > avg and Mic_tuning.is_voice() and message == "":
        message = "HUMAN," + "QUIET," + direc_str
    elif volume > (avg + 2*std) and not Mic_tuning.is_voice() and message == "":
        message = "THING," + "LOUD," + direc_str

with sd.Stream(callback=volume, samplerate=16000):
	while True:
		time.sleep(1)
		#global message
		post_response = requests.post(url, json={"description": message})
		message = ""
