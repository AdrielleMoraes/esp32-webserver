# function to collect data via the I2c protocol

def readValue(scl_pin=5, sda_pin=4):
    import machine
    i2c = machine.I2C(scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
    byte_data = bytearray(2)
    i2c.readfrom_mem_into(24, 5, byte_data)
    value = byte_data[0] << 8 | byte_data[1]
    return (value & 0xFFF) / 16.0