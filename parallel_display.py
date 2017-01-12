''' PARALLEL_DISPLAY - Inerits display class from display.py '''

'''
Written by Luka Žgur

ParallelDisplay uses adafruit char LCD library for communication with display.
https://github.com/adafruit/Adafruit_Python_CharLCD
'''

# WARNING: For all overrided methods see display.py for documentation

import display
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
from time import *

''' COMMANDS FOR LCD DISPLAY '''
# GPIO numbering mode
GPIO_NUMBERING_MODE = GPIO.BCM

# pins indexes
LCD_RS_INDEX = 0
LCD_EN_INDEX = 1
LCD_D4_INDEX = 2
LCD_D5_INDEX = 3
LCD_D6_INDEX = 4
LCD_D7_INDEX = 5
LCD_BL_INDEX = 6

class ParallelDisplay(display.Display):
    
    # Method for LCD initialization
    ''' OVERRIDED FROM DISPLAY '''
    def lcd_initialize(self):
        # Initialize parallel_Device
        GPIO.setmode(GPIO_NUMBERING_MODE)
        GPIO.setwarnings(False)
        #self.lcd_bl_pin = self.pins[LCD_BL_INDEX]
        

        self.lcd = LCD.Adafruit_CharLCD(self.pins[LCD_RS_INDEX], self.pins[LCD_EN_INDEX], self.pins[LCD_D4_INDEX], self.pins[LCD_D5_INDEX], self.pins[LCD_D6_INDEX], self.pins[LCD_D7_INDEX], self.columns, self.rows, None)
        sleep(0.2)
        self.lcd_backlight(True)
        
    # Toggle backlight on/off, it uses a variable with stored data
    ''' OVERRIDED FROM DISPLAY '''
    def lcd_backlight(self, state):
        GPIO.setup(16, GPIO.OUT)
        if state == True:
            GPIO.output(16, True)
            
        elif state == False:
            GPIO.output(16, False)

    # Write whole message to LCD
    ''' OVERRIDED FROM DISPLAY '''
    def lcd_message(self, text):
        self.lcd.set_cursor(0,0)
        self.lcd.message(text)

    # Load custom characters into display CGRAM (0 - 7)
    ''' OVERRIDED FROM DISPLAY '''
    def lcd_load_custom_chars(self, fontdata):
        index = 0
        for char in fontdata:
            self.lcd.create_char(index, char)
            index += 1