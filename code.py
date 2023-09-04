import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Motor configurations
motor_pins = [17, 18, 5, 6] # actual GPIO pins
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Ultrasonic sensor configurations
trigger_pin = 22  #   trigger GPIO pin
echo_pin = 23     #   echo GPIO pin
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def move_forward():
    GPIO.output(motor_pins[0], GPIO.HIGH)
    GPIO.output(motor_pins[1], GPIO.LOW)
    GPIO.output(motor_pins[2], GPIO.LOW)
    GPIO.output(motor_pins[3], GPIO.HIGH)

def move_backward():
    GPIO.output(motor_pins[0], GPIO.LOW)
    GPIO.output(motor_pins[1], GPIO.HIGH)
    GPIO.output(motor_pins[2], GPIO.HIGH)
    GPIO.output(motor_pins[3], GPIO.LOW)

def turn_left():
    GPIO.output(motor_pins[0], GPIO.LOW)
    GPIO.output(motor_pins[1], GPIO.HIGH)
    GPIO.output(motor_pins[2], GPIO.LOW)
    GPIO.output(motor_pins[3], GPIO.HIGH)

def turn_right():
    GPIO.output(motor_pins[0], GPIO.HIGH)
    GPIO.output(motor_pins[1], GPIO.LOW)
    GPIO.output(motor_pins[2], GPIO.HIGH)
    GPIO.output(motor_pins[3], GPIO.LOW)

def stop_motors():
    for pin in motor_pins:
        GPIO.output(pin, GPIO.LOW)

def measure_distance():
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound (343 meters per second) / 2
    distance = round(distance, 2)
    print(distance)
    return distance



try:
    GPIO.setmode(GPIO.BCM)
    while True:
        distance = measure_distance()
        if distance<=25:
            while distance <=30:
                move_backward()
                distance = measure_distance()
        if distance <=40:
            for i in range(100000):
                turn_right()
        
        move_forward()
        
except KeyboardInterrupt:
    GPIO.cleanup()
