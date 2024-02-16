import smbus2
import bme280
import sys

## By Trey, Brett

port = 1
address = 0x77 # BME DEFAULT ADRESS 
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# read data funct

def read_bme280():
    data = bme280.sample(bus, address, calibration_params)
    temperature = data.temperature
    humidity = data.humidity
    pressure = data.pressure
    print(f"Temperature: {temperature:.2f}C")
    print(f"Humidity: {humidity:.2f}%")
    print(f"Pressure: {pressure:.2f}hPa")
    return temperature , humidity , pressure

#read data

read_bme280()






