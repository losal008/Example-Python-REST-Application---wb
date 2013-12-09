import os
import glob
import requests
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template
import datetime

key = '8b00ba67a7938706'
ApiUrl = 'http://api.wunderground.com/api/' + key + '/forecast/q/CA/San_Francisco.json'

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(25,GPIO.OUT)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


app = Flask(__name__)

@app.route("/")

def hello():
        r = requests.get(ApiUrl)
        forecast = r.json
        popValue = forecast['forecast']['txt_forecast']['forecastday'][0]['pop']
        popValue = int(popValue)
        #print popValue

        if popValue <= 8:
                #GPIO.output(25, GPIO.HIGH)
                led = 1
        else:
                #GPIO.output(25, GPIO.LOW)
                led = 0

        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        temp = read_temp()
        templateData = {
                'title' : 'HELLO!',
                'time' : timeString,
                'percentage' : popValue,
                'led'  : led,
                'temp' : temp
                }
        return render_template('main.html', **templateData)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug=True)
