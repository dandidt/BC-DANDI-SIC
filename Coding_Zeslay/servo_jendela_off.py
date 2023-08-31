import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo_pin = 17
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)

pwm.start(2.5)

def set_servo_position(angle):
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    try:
        set_servo_position(30)
        time.sleep(1)

    except KeyboardInterrupt:

        pwm.stop()
        GPIO.cleanup()
