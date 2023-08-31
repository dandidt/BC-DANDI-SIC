# import time
# import RPi.GPIO as GPIO
# import buzzer_on

# touch_pin = 23

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# def touch_det(pin):
#     touch = GPIO.input(pin)
#     return touch

# try:
#     while True:
#         if touch_det(touch_pin):
#             print('[' + time.ctime() + '] - ' + 'Touch Detected')
#             buzzer_on.main_buzzer()
#         time.sleep(0.5)
    
# except KeyboardInterrupt:
#     print('Interrupted!')
#     GPIO.cleanup()

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

touch_pin = 23
servo_pin = 17

GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(2.5)

def touch_det(pin):
    touch = GPIO.input(pin)
    return touch

def set_servo_position(angle):
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

try:
    while True:
        if touch_det(touch_pin):
            print('[' + time.ctime() + '] - ' + 'Touch Detected')

            # Mengatur posisi servo
            set_servo_position(30) # Servo Tertutup
            time.sleep(1)
            # set_servo_position(30) # Servo Tertutup
            # time.sleep(1)

except KeyboardInterrupt:
    print('Interrupted!')
    pwm.stop()
    GPIO.cleanup()
