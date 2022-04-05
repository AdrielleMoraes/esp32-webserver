import time
from math import log
from machine import I2C
from machine import Pin


#CONSTANTS
AHT10_ADDRESS = 0x38 # 0111000 (7bit address)
AHT10_READ_DELAY_MS = 75 # Time it takes for AHT to collect data
AHT_TEMPERATURE_CONST = 200
AHT_TEMPERATURE_OFFSET = 50
KILOBYTE_CONST = 1048576
CMD_INITIALIZE = bytearray([0xE1, 0x08, 0x00])
CMD_MEASURE = bytearray([0xAC, 0x33, 0x00])
FARENHEIT_MULTIPLIER = 9/5
FARENHEIT_OFFSET = 32

class AHT10:
    def __init__(self, i2c, mode=0, address=AHT10_ADDRESS):
        if i2c is None:
            raise ValueError('I2C object required.')
        if mode is not (0 and 1):
            raise ValueError('Mode must be either 0 for Celsius or 1 Farenheit')
        self.i2c = i2c
        self.address = address
        self.i2c.writeto(address, CMD_INITIALIZE)
        self.readings_raw = bytearray(8)
        self.results_parsed = [0, 0]
        self.mode = mode # 0 for Celsius, 1 for Farenheit

    def read_raw(self):
        self.i2c.writeto(self.address, CMD_MEASURE)
        time.sleep_ms(AHT10_READ_DELAY_MS)
        self.readings_raw = self.i2c.readfrom(AHT10_ADDRESS, 6)
        self.results_parsed[0] = self.readings_raw[1] << 12 | self.readings_raw[2] << 4 | self.readings_raw[3] >> 4
        self.results_parsed[1] = (self.readings_raw[3] & 0x0F) << 16 | self.readings_raw[4] << 8 | self.readings_raw[5]

    def humidity(self):
        self.read_raw()
        return (self.results_parsed[0] / KILOBYTE_CONST) * 100 

    def temperature(self):
        self.read_raw()
        if self.mode is 0:
            return (self.results_parsed[1] / KILOBYTE_CONST) * AHT_TEMPERATURE_CONST - AHT_TEMPERATURE_OFFSET
        else:
            return ((self.results_parsed[1] / KILOBYTE_CONST) * AHT_TEMPERATURE_CONST - AHT_TEMPERATURE_OFFSET) * FARENHEIT_MULTIPLIER + FARENHEIT_OFFSET

    def set_mode(self, mode):
        if mode is not (0 or 1):
            raise ValueError('Mode must be either 0 for Celsius or 1 Farenheit')
        self.mode = mode

    def print(self):
        print("Temperature: " + str(self.temperature()) + ("C","F")[self.mode] + ", Humidity: " + str(self.humidity()))

    def dew_point(self):
        h = self.humidity()
        prev_mode = self.mode
        self.mode = 0
        h = (log(h, 10) - 2) / 0.4343 + (17.62 * t) / (243.12 + t)
        return 243.12 * h / (17.62 - h)




class readSensor:
    def __init__(self, slc_pin = 22, sda_pin =21):
        i2c = I2C(scl =Pin(slc_pin) , sda = Pin(sda_pin), freq=400000)

        # use below for the aht10 sensor
        self.aht10_sensor = AHT10(i2c, 0)

    def readTemp(self):
        value = 0
        # print data on screen
        try:   
            value = self.aht10_sensor.temperature()
            return value
        except:
            print('Error retrieving temperature from sensor')
    
    def readHumidity(self):
        value = 0
        # print data on screen
        try:   
            value = self.aht10_sensor.humidity()
            return value
        except:
            print('Error retrieving humidity from sensor')