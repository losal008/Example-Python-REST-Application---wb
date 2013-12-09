import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

key = '8b00ba67a7938706'
ApiUrl = 'http://api.wunderground.com/api/' + key + '/forecast/q/CA/San_Francisco.json'

while True:
        r = requests.get(ApiUrl)
        forecast = r.json
        popValue = forecast['forecast']['txt_forecast']['forecastday'][0]['pop']
        popValue = int(popValue)
        print popValue

        if popValue <= 8:
                GPIO.output(25, GPIO.HIGH)
        else:
                GPIO.output(25, GPIO.LOW)

        time.sleep(180) # 3 minutes
