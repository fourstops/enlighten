#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
import smbus
from TCS34725 import TCS34725
import RPi.GPIO as GPIO
import Si1145 as Sensor
import veml6070

Sensor.Si1145_Init()
veml = veml6070.Veml6070()

ALL_INTEGRATION_TIMES = [
    veml6070.INTEGRATIONTIME_1_2T, veml6070.INTEGRATIONTIME_1T, veml6070.INTEGRATIONTIME_2T, veml6070.INTEGRATIONTIME_4T
]

def get_color():
    try:
        Light=TCS34725(0X29, debug=False)
        if(Light.TCS34725_init() == 1):
            print("TCS34725 initialization error!!")
        else:
            print("TCS34725 initialization success!!")
        time.sleep(3)
        while True:
            print("%d,"%Sensor.Si1145_readVisible()),
            print("%d,"%Sensor.Si1145_readIR()),
            UVindex = Sensor.Si1145_readUV()
            UVindex /= 100.0
            print("%s,"%UVindex),
            veml6070.INTEGRATIONTIME_2T
            print("%s,"%veml.get_uva_light_intensity_raw()),
            print("%s,"%veml.get_uva_light_intensity()),
            Light.Get_RGBData()
            Light.GetRGB888()
            Light.GetRGB565()
            print("%d,"%Light.RGB888_R), 
            print("%d,"%Light.RGB888_G), 
            print("%d,"%Light.RGB888_B), 
            print("%#x,"%Light.C),
            print("%#x,"%Light.RG565),
            print("%#x,"%Light.RGB888),    
            print("%d,"%Light.Get_Lux()),
            print("%dK,"%Light.Get_ColorTemp()),
            print("%d,"%Light.GetLux_Interrupt(0xff00, 0x00ff));
            time.sleep(3)
    except KeyboardInterrupt:
        print('Interrupted')
        GPIO.cleanup()
        print ("\nProgram end")
        exit()

while True:
    get_color()


#except:
 #   Sensor.Si1145_close()

    # Alternative constructors with parameters
    # uv = adafruit_veml6070.VEML6070(i2c, 'VEML6070_1_T')
    # uv = adafruit_veml6070.VEML6070(i2c, 'VEML6070_HALF_T', True)



#try:
 #   if(color.TCS34725_init() == 1):
 #       print("TCS34725 initialization error!!")
 #   else:
 #       print("TCS34725 initialization success!!")
 #   time.sleep(2)
#except:
 #   GPIO.cleanup()
  #  print "\nProgram end"
