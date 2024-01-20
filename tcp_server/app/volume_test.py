import sounddevice as sd
import numpy as np
from tuning import Tuning
import usb.core
import usb.util
import time
import numpy as np
import asyncio


past_sounds = np.zeros(50)
count = 0

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
Mic_tuning = None

def volume(indata, outdata, frames, time2, status):
	volume = np.linalg.norm(indata)*10
	global past_sounds
	past_sounds = np.append(past_sounds, volume)
	past_sounds = np.delete(past_sounds, 0)
	global Mic_tuning
	avg = np.average(past_sounds)
	std = np.std(past_sounds)
	voice = Mic_tuning.is_voice()
	# identify different noises:
	if volume > (avg + 2*std) and voice:
		print("LOUD HUMAN >:(")
	elif volume > avg and voice:
		print("KINDA MID HUMAN :(")
	elif volume > (avg + 2*std):
		print("LOUD THINGY :)")
	
	global count
	count = count + 1
	
	time.sleep(0.5)
	print(count)
	#print(np.average(past_sounds))
	

if dev:
	Mic_tuning = Tuning(dev)
	with sd.Stream(callback=volume, samplerate=16000):
		while True:
			#print(Mic_tuning.direction)
			time.sleep(1)
				

