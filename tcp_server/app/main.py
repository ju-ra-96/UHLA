from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from dumm_data import generate_data
#import RPi.GPIO as GPIO
import time
import asyncio
#import usb.core
#import usb.util
#from tuning import Tuning
import numpy as np
import sounddevice as sd
from pydantic import BaseModel

class Sound(BaseModel):
    description: str


past_sounds = np.zeros(50)
#dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
message = None
#Mic_tuning = None
message = ""

#if dev:
#    Mic_tuning = Tuning(dev)
    
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
    #print("message: ", message)
    # count
    #count = count + 1
	
    #time.sleep(0.5)
    #print(count)
	#print(np.average(past_sounds))
	
#sensorL = 17
#sensorR = 23
#fake_data = "NONE"

#buzzerL = 22
#buzzerR = 12

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(sensorL, GPIO.IN)
#GPIO.setup(sensorR, GPIO.IN)
#GPIO.setup(buzzerL, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(buzzerR, GPIO.OUT, initial=GPIO.LOW)

#def detectL(sensorL):
#    print("LEFT")
#    global fake_data
#    fake_data = "LEFT"

#def detectR(sensorR):
#    print("RIGHT")
#    global fake_data
#    fake_data = "RIGHT"

#GPIO.add_event_detect(sensorL, GPIO.RISING, bouncetime=300)
#GPIO.add_event_callback(sensorL, detectL)
#GPIO.add_event_detect(sensorR, GPIO.RISING, bouncetime=300)
#GPIO.add_event_callback(sensorR, detectR)
        
app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("wss://ecae-137-110-116-189.ngrok-free.app/ws"); // //bfd9-69-196-47-69.ngrok-free.app/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
                ws.send('OK')
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
        #with sd.Stream(callback=volume, samplerate=16000):
        #    while True:
        #        #print(Mic_tuning.direction)
        #        data = await websocket.receive_text()
        #        time.sleep(2)
        #        global message
        #        print("MESSAGE:" + message)
        #        await websocket.send_text(f"{message}")
        #while True:
        #    await asyncio.sleep(0.5)
        #    data = await websocket.receive_text()
        #    print(data)
        #    print("hello")
        #    #await websocket.send_text(f"Message text was: {data}")
        #    #fake_data = generate_data()
        #    if(Mic_tuning.is_voice()):
        #        print("voice")
        #        direction = Mic_tuning.direction
        #        if(direction >= 45 and direction < 135):
        #            message = "BOTH"
        #        elif(direction >= 135 and direction <225):
        #            message = "RIGHT"
        #        elif(direction >= 255 and direction < 315):
        #            message = "FRONT"
        #        else:
        #            message = "LEFT"
        #        print(message)
        #        await websocket.send_text(f"{message}")
        #    else:
        #        await websocket.send_text("nothing detected")
        #    #print(Mic_tuning.read('AGCGAIN'))
            global message
            data = await websocket.receive_text()
            await asyncio.sleep(0.5)
            print(data)
            #await websocket.send_text(f"Message text was: {data}")
            print("outgoing msg ", message)
            await websocket.send_text(f"{message}")
    except Exception as error:
        print(error, type(error).__name__)
    
@app.post("/sounds")
async def update_sounds(sound: Sound):
    global message
    message = sound.description
    print(message)
    return "thanks"
    
    
