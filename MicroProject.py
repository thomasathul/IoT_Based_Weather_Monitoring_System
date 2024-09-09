import time
import board
import digitalio
import thingspeak
import busio
import Adafruit_DHT
import bmpsensor
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn

#Thingspeak Credentials
channel_id = 2571640
write_key="2LPV4J63J5Q19J3N"

#Channel Ids
channel = thingspeak.Channel(id=channel_id, api_key = write_key)


# Set up SPI
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)  # Chip select on GPIO5 (Pin 29)
mcp = MCP3008(spi, cs)

# Create analog input channel on pin 0
chan = AnalogIn(mcp, 0)

#DHT11 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def read_gas_concentration():
    # Read the analog value
    adc_value = chan.value
    voltage = chan.voltage

    gas_concentration = (voltage / 3.3) * 100.0

    return gas_concentration

while True:
    #MQ135
    gas_concentration = read_gas_concentration()
    print("Gas Concentration: {:.2f}%".format(gas_concentration))
    
    #BMP180
    pressure = bmpsensor.readBmp180()
    print("Pressure is ",pressure) # Pressure in Pa 
   
    #DHT11 
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    print("Temperature is ",temperature, "C") #Temperature is in degree Celcius
    print("Humidity is ",humidity, "%") 
    
    #Thingspeak channel update
    reponse = channel.update({
        'field1' : pressure,
        'field2' : temperature,
        'field3' : humidity,
        'field4' : gas_concentration
        })

    time.sleep(0.5)