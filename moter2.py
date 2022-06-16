#coding:utf-8
#tojiru
import RPi.GPIO as gpio
import json
from time import sleep

a=open("/home/pi/ドキュメント/Python_tests/moter.json","r",encoding="utf-8")
cond=json.load(a)
if cond==0:
    with open("/home/pi/ドキュメント/Python_tests/moter.json","w") as f:
        json.dump(1,f)
    gpio.setmode(gpio.BOARD)

    AIN1=13
    AIN2=15
    PWMA=12


    gpio.setup(AIN1, gpio.OUT, initial=gpio.LOW)
    gpio.setup(AIN2, gpio.OUT, initial=gpio.LOW)
    gpio.setup(PWMA, gpio.OUT, initial=gpio.LOW)

    p=gpio.PWM(PWMA,100)
    p.start(100)
    gpio.output(AIN2,gpio.HIGH)#2.2
    sleep(2)
    gpio.output(AIN2, gpio.LOW)

    p.stop()

    gpio.cleanup()

