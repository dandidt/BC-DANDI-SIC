import RPi.GPIO as GPIO

# Atur mode pin
def setup():
    GPIO.setmode(GPIO.BCM)

    # Daftar pin yang digunakan
    pin_solenoid1 = 24

    # Inisialisasi pin sebagai output
    GPIO.setup(pin_solenoid1, GPIO.OUT)

    # setup()
    while True:
        GPIO.output(pin_solenoid1, GPIO.HIGH)

        break
        # tutup = GPIO.output(pin_solenoid1, GPIO.LOW)
        # print("Solenoids are ON")
        # return buka
    # run_sele()
            # time.sleep(2)  # Tunggu 2 detik
# def close_sele():
#     setup()
#     GPIO.output(pin_solenoid1, GPIO.LOW)