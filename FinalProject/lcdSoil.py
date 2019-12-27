import time
import Adafruit_CharLCD as LCD
import spidev

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

#soil
delay = 3

spi = spidev.SpiDev()
spi.open(0,0)
 
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data

if __name__ == "__main__":
    lcd.message('Hello\nPlant!')
    # Wait 5 seconds
    time.sleep(3.0)
    lcd.clear()   
    
    try:
        while True:
            val = readChannel(0)
            lcd.clear()
            if (val != 0 and val < 700):
                print(val)
                lcd.message("wet")
            else:
                print("no water")
                lcd.message("dry")
            time.sleep(delay)
      
    except KeyboardInterrupt:
        lcd.clear()
        lcd.message("ByeBye")
        time.sleep(5.0)
        lcd.clear()
        print("Cancel.")

