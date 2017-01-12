import RPi.GPIO as GPIO
import time

# This class will send commands to MPD client from buttons
class buttons():
	# Class constructor
	# Buttons pins is a dictionary with button_name=>pin_number format
	def __init__(self, button_pins, bounce_time):
		# Set bounce time
		self.bounce_time = bounce_time
		
		# Set buttons
		self.buttons = button_pins

		# Initialize display client
		self.display = False
	
		# We don't need warnings from GPIO
		GPIO.setwarnings(False)
		
		# Set button GPIO pins as inputs and enable interrupts
		for button in button_pins:
			if (button_pins[button] != False):
				GPIO.setup(button_pins[button], GPIO.IN, pull_up_down = GPIO.PUD_UP)
				GPIO.add_event_detect(button_pins[button], GPIO.FALLING, callback=self.button_pressed, bouncetime=self.bounce_time)
			
		# Initalize MPD
		self.mpd = False
			
	# Register MPD client to send it commands
	def register(self, mpd):
		self.mpd = mpd

	# Register display client so this thread can send commands to it
	def register_display(self, display):
		self.display = display
			
	def button_pressed(self, channel):
		# Debouncing
		time.sleep(0.05)
		if (GPIO.input(channel) == 0):
			# Find out which button was pressed
			for button in self.buttons:
				if (channel == self.buttons[button]):
					# Change screen
					if (button == 'MODE_BUTTON'):
						if (self.display != False):
							self.display.change_screen()
					# Toggle backlight
					elif (button == 'PAUSE_BUTTON'):
                        if (self.display != False):
							self.display.toggle_backlight()
					# Send command to MPD client
					elif (self.mpd != False):
						self.mpd.commands(button.replace('_BUTTON', ''))