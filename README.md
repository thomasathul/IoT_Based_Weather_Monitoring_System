# 🌦️ IoT-Based Weather Monitoring System

A project designed to monitor environmental conditions in real-time using sensors and a Raspberry Pi. The system collects temperature, humidity, pressure, and air quality data and uploads it to the ThingSpeak cloud platform for visualization and analysis.

---

## 🧠 Features

- 📡 Real-time weather data acquisition
- 🌐 Wireless transmission via WiFi (ThingSpeak API)
- 🌡️ Measures Temperature, Humidity, Air Quality, Pressure
- 📊 Cloud-based data logging and visualization using ThingSpeak
- 🧰 Built with Python and Raspberry Pi (ARM Cortex-A53)

---

## 🛠️ Components

| Component          | Function                          |
|--------------------|-----------------------------------|
| Raspberry Pi 3 B   | Microcontroller and WiFi module   |
| DHT11              | Temperature and Humidity Sensor   |
| BMP180             | Barometric Pressure Sensor        |
| MQ135              | Gas Sensor (Air Quality)          |
| MCP3008            | ADC for analog sensor (MQ135)     |

---

## 🖥️ Software & Tools

- Raspbian OS
- Python (Thonny IDE)
- ThingSpeak API (MathWorks)
- Libraries: Adafruit_DHT, bmpsensor, thingspeak, adafruit_mcp3xxx

---

## 🔐 ThingSpeak Integration

1. Sign in to [ThingSpeak](https://thingspeak.com/)
2. Create a new channel with 4 fields:
   - Field 1: Pressure
   - Field 2: Temperature
   - Field 3: Humidity
   - Field 4: Gas Concentration
3. Copy your **Write API Key**
4. Replace it in `MicroProject.py`:
   ```python
   write_key = "YOUR_WRITE_KEY"
   ```

---

## 🔧 Setup Instructions

### ⚙️ Hardware Wiring

- DHT11 connected to GPIO4
- BMP180 connected via I2C (SDA: GPIO2, SCL: GPIO3)
- MQ135 analog output to MCP3008 Channel 0
- MCP3008 SPI connections:
  - CLK: GPIO11
  - MISO: GPIO9
  - MOSI: GPIO10
  - CS: GPIO8

### 🧪 Enable Interfaces

```bash
sudo raspi-config
# Enable I2C and SPI
```

### 📦 Install Python Libraries

```bash
pip install Adafruit_DHT bmpsensor thingspeak adafruit-circuitpython-mcp3xxx
```

---


## 🧾 Code Overview

Main logic in `MicroProject.py`:

- Reads gas concentration via ADC
- Reads pressure using BMP180
- Reads temperature & humidity via DHT11
- Updates ThingSpeak every 0.5 seconds

---

## 📊 Results

- Visualized via real-time graphs on ThingSpeak
- Nighttime shows higher humidity and lower pressure
- CO₂ levels fluctuate between 10–16% indoors
- Morning vs night comparison identifies rain likelihood

---


## Future Improvements:

- Add sensors (e.g., rain gauge, light sensor)
- Predictive analytics with ML (LSTM models)
- Long-term statistical forecasting

---

