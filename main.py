import network
import socket
import time
from machine import Pin, I2C

# --- WiFi credentials ---
SSID = "Millie5 2.4"
PASSWORD = "BAM$alcetti.1981"

# --- I2C setup for BH1750 light sensor ---
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
BH1750_ADDR = 0x23

def read_light():
    i2c.writeto(BH1750_ADDR, b'\x10')  # continuous high-res mode
    time.sleep(0.2)
    data = i2c.readfrom(BH1750_ADDR, 2)
    lux = (data[0] << 8 | data[1]) / 1.2
    return lux

# --- Connect to WiFi ---
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Connecting to WiFi...")
while not wlan.isconnected():
    time.sleep(1)
print("Connected:", wlan.ifconfig())

start_time = time.time()

# --- Web server ---
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on", addr)

while True:
    cl, addr = s.accept()
    lux = read_light()
    uptime = time.time() - start_time

    html = f"""<!DOCTYPE html>
<html><head><title>Sunnode</title></head>
<body style="font-family:sans-serif; text-align:center; margin-top:50px;">
<h1>☀️ Sunnode</h1>
<p>Light level: {lux:.1f} lux</p>
<p>Uptime: {int(uptime)} seconds</p>
<p>Status: online, running on solar/battery</p>
</body></html>"""

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
    cl.send(response)
    cl.close()
