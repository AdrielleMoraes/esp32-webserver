from AHT10 import AHT10
from machine import I2C
from machine import Pin
from ads1x15 import ADS1115

i2c = I2C(scl =Pin(22) , sda = Pin(21), freq=400000)

# use below for the aht10 sensor
# aht10_sensor = AHT10(i2c, 0)
# print(aht10_sensor.temperature())

# setup the ad converter
adc = ADS1115(i2c)
adc.read()