import time
import board
import busio
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint

# ---------- LED SETUP ----------
led_red = DigitalInOut(board.GP0)
led_red.direction = Direction.OUTPUT

led_green = DigitalInOut(board.GP1)
led_green.direction = Direction.OUTPUT

def led_ok():
    led_green.value = True
    led_red.value = False

def led_fail():
    led_green.value = False
    led_red.value = True

def led_off():
    led_green.value = False
    led_red.value = False


# ---------- UART & SENSOR ----------
uart = busio.UART(tx=board.GP16, rx=board.GP17, baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)


def scan_and_check():
    print("Leg vinger op sensor...")

    # Wachten op beeld
    while finger.get_image() != adafruit_fingerprint.OK:
        pass

    # Template maken
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        print("Slechte scan")
        led_fail()
        return

    # Zoeken in opgeslagen prints
    if finger.finger_fast_search() == adafruit_fingerprint.OK:
        print("MATCH! ID:", finger.finger_id,
              " confidence:", finger.confidence)
        led_ok()
    else:
        print("Geen match")
        led_fail()


# ---------- HOOFDPROGRAMMA ----------
print("Aantal opgeslagen prints laden...")
if finger.read_templates() == adafruit_fingerprint.OK:
    print("Templates:", finger.templates)
else:
    print("Kon templates niet lezen!")

led_off()

while True:
    scan_and_check()
    time.sleep(2)
    led_off()

