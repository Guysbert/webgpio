import time
import RPi.GPIO as GPIO
from flask import Flask, render_template, request, jsonify
from threading import Thread

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

app = Flask(__name__)

blink = False
frequency = 1.0
threadstarted = False
thread = Thread()

@app.route("/")
def hello():
    return render_template('ledsetter.html')

@app.route("/on")
def on():
    GPIO.output(3, GPIO.HIGH)
    global blink
    blink = False
    return "On"

@app.route("/off")
def off():
    GPIO.output(3, GPIO.LOW)
    global blink
    blink = False
    return "Off"

@app.route("/setfrequency", methods=['POST'])
def setfrequency():
    global blink
    global frequency
    global threadstarted
    global thread
    blink = False
    if threadstarted:
        thread.join()
    thread = Thread(target = blinkled)
    json = request.get_json()
    frequency = json['value'] / 1000
    thread.start()
    return "ok"

def blinkled():
    global blink
    global frequency
    global thread_started
    blink = True
    threadstarted = True
    print("repeat")
    while blink:
        print(blink)
        print(off)
        GPIO.output(3, GPIO.LOW)
        time.sleep(frequency)
        print(on)
        GPIO.output(3, GPIO.HIGH)
        time.sleep(frequency)
    threadstarted = False


if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True)
