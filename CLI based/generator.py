import qrcode
import time
import sys


def slow_type(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


name = input("Kindly enter the name for the file -> ")
url = input("Please the URL -> ").strip()
filePath = f"output\\{name}.png"
time.sleep(1)
print(f"Your file --> {name} is getting processed")
time.sleep(1)

qr = qrcode.QRCode()
qr.add_data(url)
slow_type("===========================", speed=0.5)
image = qr.make_image()
image.save(filePath)

print(f"Your QRcode | {name}.png | is now generated \n-- Kindly check the output folder. ")
