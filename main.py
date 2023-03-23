
# Wiring details
# SDA -> GP0
# SCL -> GP1
# VCC -> 3V3_EN 3.3 Volts
# GND -> GND


from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

boardled = machine.Pin(25, machine.Pin.OUT) # Defines the green LED which is on the PICO Board.

WIDTH = 128 # oled display width
HEIGHT = 64 # oled display height

i2c = I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) # Init I2C using , SCL=Pin(GP1), SDA=Pin(GP0), freq=400000
print("I2C Address 0X3C : "+hex(i2c.scan()[0]).upper()) # Display device address - should be 0X3C for a SSD1306 display, look at the ssd1306 driver
print("I2C Configuration: "+str(i2c)) # Display I2C config
devices = i2c.scan()

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c) # Init oled display
# BeetleboxCI logo as 64x64 bytearray
buffer =bytearray(b'\x00\x0e\x00\x00\x00\x00`\x00\x00\x0e\x00\x00\x00\x00`\x00\x00\x0e\x00\x00\x00\x00`\x00\x00\x0e\x00\x00\x00\x00`\x00\x00\x0e\x00\x00\x00\x00`\x00\x00\x0e\x00\x00\x00\x00`\x00\x00\x0e\x00\x00\x00\x00`\x00\x00\x0f\x00\x00\x00\x01\xe0\x00\x00\x0f\xc0\x00\x00\x07\xe0\x00\x00\x03\xf0\x03\x80\x1f\xc0\x00\x00\x00\xfc\x07\xe0>\x00\x00\x00\x00<\x1f\xf08\x00\x00\x00\x00\x1c~\xfc0\x00\x00\x00\x00\x1d\xf8?0\x00\x00\x00\x00\x1b\xf0\x1f\xb0\x00\x00\x00\x00\x0f\xc0\x07\xe0\x00\x00\x00\x00?\x00\x01\xf8\x00\x00\x00\x00\xfc\x00\x00~\x00\x00\x00\x01\xf8\x00\x00?\x00\x00\x00\x07\xe0\x00\x00\x0f\xc0\x00\x00\x1f\x80\x00\x00\x03\xf0\x00\x00>\x00\x00\x00\x00\xfc\x00\x00|\x00\x00\x00\x00|\x00\x00~\x00\x00\x00\x00\xfc\x00\x00\x7f\x80\x00\x00\x03\xfc\x00\x00w\xe0\x00\x00\x0f\xdc\x00\x01\xf1\xf8\x00\x00\x1f\x1f\x00\x03\xf0\xfc\x00\x00~\x1f\x80\x07\xf0?\x00\x01\xf8\x1f\xe0\x1f\xf0\x0f\xc0\x07\xe0\x1f\xf0>p\x03\xf0\x0f\xc0\x1c\xf8\xfcp\x01\xf8?\x00\x1c~\xf8p\x00~\xfc\x00\x1c\x1e\xe0p\x00\x1f\xf0\x00\x1c\x0e\xf0p\x00\x0f\xe0\x00\x1c\x1epp\x00\x03\x80\x00\x1c\x1cxp\x00\x00\x00\x00\x1c<8p\x00\x00\x00\x00\x1c8<p\x00\x00\x00\x00\x1cx\x18p\x00\x00\x00\x00\x1c0\x18\xf0\x00\x00\x00\x00\x1e0\x03\xf0\x00\x00\x00\x00\x1f\x80\x07\xf0\x00\x00\x00\x00\x1f\xc0\x0f\xf0\x00\x00\x00\x00\x1f\xe0\x1fp\x00\x00\x00\x00\x1d\xf8~p\x00\x00\x00\x00\x1c\xfc\xf8p\x00\x00\x00\x00\x1c>\xf0p\x00\x00\x00\x00\x1c\x1epp\x00\x00\x00\x00\x1c\x1exx\x00\x00\x00\x00<<8|\x00\x00\x00\x00|<<?\x00\x00\x00\x01\xf8x\x1c\x0f\xc0\x00\x00\x07\xe0p\x1e\x03\xf0\x00\x00\x0f\xc0\xf0\x0e\x01\xf8\x00\x00?\x00\xe0\x0f\x00~\x00\x00\xfc\x01\xe0\x07\x00\x1f\x80\x03\xf0\x01\xc0\x07\x00\x07\xc0\x07\xe0\x01\xc0\x03\x00\x03\xf0\x1f\x80\x01\x80\x02\x00\x00\xfc~\x00\x00\x80\x00\x00\x00?\xf8\x00\x00\x00\x00\x00\x00\x1f\xf0\x00\x00\x00\x00\x00\x00\x07\xc0\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00')
fb = framebuf.FrameBuffer(buffer, 64, 64, framebuf.MONO_HLSB)

# Clear the oled display in case it has junk on it.
oled.fill(0)

# Blit the image from the framebuffer to the oled display
oled.blit(fb, 0, 0)

# Add some text
oled.text("I can",64,10)
oled.text("automate",64,25)
oled.text("Picos!",64,40)

# Finally update the oled display so the image & text is displayed
oled.show()
