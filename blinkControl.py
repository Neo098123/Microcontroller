import RPi.GPIO as GPIO
import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)  # Set up GPIO pins as outputs
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

try:
    print("Press 'r', 'g', 'b' or 'w'")
    while True:
        x = getch()
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        x = x.lower()
        if (x == 'r'):
            GPIO.output(11, GPIO.HIGH)
        elif (x == 'b'):
            GPIO.output(12, GPIO.HIGH)
        elif(x == 'w'):
            GPIO.output(13, GPIO.HIGH)
        elif(x == 'g'):
            GPIO.output(15, GPIO.HIGH)
        elif(x == 'p'):
            raise KeyboardInterrupt
        
        
        
except KeyboardInterrupt:
    print("\nA keyboard interrupt has been detected!")

except:
    print("\nAn error or exception has occurred!")

finally:
    GPIO.cleanup()
