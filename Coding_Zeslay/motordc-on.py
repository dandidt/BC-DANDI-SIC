# import RPi.GPIO as GPIO
# from time import sleep

# in1 = 6
# in2 = 5
# en = 27
# temp1 = 1

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
# GPIO.setup(en, GPIO.OUT)
# GPIO.output(in1, GPIO.LOW)
# GPIO.output(in2, GPIO.LOW)
# p = GPIO.PWM(en, 9)
# p.start(3)
# print("\n")
# print("Kecepatan & arah motor default adalah LOW & Maju.....")
# print("r-jalankan s-stop f-maju b-mundur l-lambat m-sedang h-cepat e-keluar")
# print("\n")

# while True:
#     x = input()

#     if x == 'r':
#         print("Jalankan")
#         if temp1 == 1:
#             GPIO.output(in1, GPIO.HIGH)
#             GPIO.output(in2, GPIO.LOW)
#             print("maju")
#             x = 'z'
#         else:
#             GPIO.output(in1, GPIO.LOW)
#             GPIO.output(in2, GPIO.HIGH)
#             print("mundur")
#             x = 'z'

#     elif x == 's':
#         print("Berhenti")
#         GPIO.output(in1, GPIO.LOW)
#         GPIO.output(in2, GPIO.LOW)
#         x = 'z'

#     elif x == 'f':
#         print("Maju")
#         GPIO.output(in1, GPIO.HIGH)
#         GPIO.output(in2, GPIO.LOW)
#         temp1 = 1
#         x = 'z'

#     elif x == 'b':
#         print("Mundur")
#         GPIO.output(in1, GPIO.LOW)
#         GPIO.output(in2, GPIO.HIGH)
#         temp1 = 0
#         x = 'z'

#     elif x == 'l':
#         print("Lambat")
#         p.ChangeDutyCycle(25)
#         x = 'z'

#     elif x == 'm':
#         print("Sedang")
#         p.ChangeDutyCycle(50)
#         x = 'z'

#     elif x == 'h':
#         print("Cepat")
#         p.ChangeDutyCycle(75)
#         x = 'z'

#     elif x == 'e':
#         GPIO.cleanup()
#         break

#     else:
#         print("<<<  data salah  >>>")
#         print("silakan masukkan data yang telah ditentukan untuk melanjutkan.....")
# import RPi.GPIO as GPIO
# from time import sleep

# in1 = 6
# in2 = 5
# en = 27
# temp1 = 1 

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
# GPIO.setup(en, GPIO.OUT)
# GPIO.output(in1, GPIO.LOW)
# GPIO.output(in2, GPIO.LOW)
# p = GPIO.PWM(en, 9)

# try:
#     while True: 
#         p.stop() 
#         GPIO.output(in1, GPIO.HIGH)
#         GPIO.output(in2, GPIO.LOW)
#         p.start(5)
#         print("Motor putar searah jarum jam")
#         sleep(2)  # Motor berputar selama 2 detik

#         p.stop()
#         GPIO.output(in1, GPIO.LOW)
#         GPIO.output(in2, GPIO.HIGH)
#         p.start(5)
#         print("Motor putar berlawanan jarum jam")
#         sleep(2)  # Motor berputar selama 2 detiki

#         p.stop()  # Berhenti mengirim sinyal PWM

#         sleep(2)  # Jeda 2 detik sebelum mengulang kembali
# except KeyboardInterrupt:
#     pass
# finally:
#     p.stop()
#     GPIO.cleanup()





import RPi.GPIO as GPIO
from time import sleep

in1 = 6
in2 = 5
en = 27
temp1 = 1 

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 9)

try:
    while True: 
        p.stop()

        # Motor berputar searah jarum jam
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        p.start(13)  # Kedua kaki H-bridge aktif
        print("Motor putar searah jarum jam")
        sleep(0.8)

        p.stop()
        sleep(2)
        p.stop()

        # Motor berputar berlawanan jarum jam
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        p.start(13)  # Kedua kaki H-bridge aktif
        print("Motor putar berlawanan jarum jam")
        sleep(1)

        p.stop()

        # Berhenti motor
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        p.start(0)  # Kedua kaki H-bridge nonaktif

        sleep(2)
except KeyboardInterrupt:
    pass
finally:
    p.stop()
    GPIO.cleanup()
