import RPi.GPIO as GPIO

# Atur mode pin
def close_sele():
    GPIO.setmode(GPIO.BCM)

    # Daftar pin yang digunakan
    pin_solenoid1 = 24

    # Inisialisasi pin sebagai output
    GPIO.setup(pin_solenoid1, GPIO.OUT)

    
    while True:
        GPIO.output(pin_solenoid1, GPIO.LOW)

        break
        # tutup = GPIO.output(pin_solenoid1, GPIO.LOW)
        # print("Solenoids are ON")
        # return buka
            # time.sleep(2)  # Tunggu 2 detik