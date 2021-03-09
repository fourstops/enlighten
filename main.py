#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
import Si1145 as Sensor
import RPi.GPIO as GPIO
from TCS34725 import TCS34725

Sensor.Si1145_Init()

try:
    while True:
        print "==================="
        print "Vis: ", Sensor.Si1145_readVisible()
        print "IR: ", Sensor.Si1145_readIR()
    
        UVindex = Sensor.Si1145_readUV()
        UVindex /= 100.0
        print "UV: ", UVindex
        
        Light.Get_RGBData()
        Light.GetRGB888()
        Light.GetRGB565()
        print("R: %d "%Light.RGB888_R), 
        print("G: %d "%Light.RGB888_G), 
        print("B: %d "%Light.RGB888_B), 
        print("C: %#x "%Light.C),
        print("RGB565: %#x "%Light.RG565),
        print("RGB888: %#x "%Light.RGB888),    
        print("LUX: %d "%Light.Get_Lux()),
        print("CT: %dK "%Light.Get_ColorTemp()),
        print("INT: %d "%Light.GetLux_Interrupt(0xff00, 0x00ff));
        time.sleep(2)

except:
    Sensor.Si1145_close()
    GPIO.cleanup()
    print "\nProgram end"
    exit()
