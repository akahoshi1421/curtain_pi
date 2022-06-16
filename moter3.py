#coding:utf-8
#hiraku
import RPi.GPIO as gpio
import json
from time import sleep

a=open("/home/pi/ドキュメント/Python_tests/moter.json","r",encoding="utf-8")
cond=json.load(a)
if cond==1:
    with open("/home/pi/ドキュメント/Python_tests/moter.json","w") as f:
        json.dump(0,f)
    gpio.setmode(gpio.BOARD)

    AIN1=13
    AIN2=15
    PWMA=12


    gpio.setup(AIN1, gpio.OUT, initial=gpio.LOW)
    gpio.setup(AIN2, gpio.OUT, initial=gpio.LOW)
    gpio.setup(PWMA, gpio.OUT, initial=gpio.LOW)

    #p=gpio.PWM(PWMA,100)
    #p.start(100)#2.4
    gpio.output(PWMA, gpio.HIGH)
    gpio.output(AIN1,gpio.HIGH)
    sleep(2)#2.5
    gpio.output(AIN1, gpio.LOW)
    
    gpio.output(PWMA, gpio.LOW)
    #p.stop()

    gpio.cleanup()
