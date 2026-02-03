# We importeren modules (bibliotheken) die we nodig hebben

import board        # Bevat de namen van de pinnen op de Pico (zoals LED, GP0, ...)
import digitalio    # Nodig om pinnen als digitale in- of output te gebruiken
import time         # Voor tijdsfuncties zoals sleep()

# We maken een LED-object dat verbonden is met de ingebouwde LED van de Pico
led = digitalio.DigitalInOut(board.LED)

# We zeggen dat deze pin een OUTPUT is (we sturen iets aan)
led.direction = digitalio.Direction.OUTPUT

# Oneindige lus: de code hieronder blijft zich herhalen
while True:
    
    # LED aanzetten (True = spanning op de pin)
    led.value = True
    
    # 1 seconde wachten
    time.sleep(1)
    
    # LED uitzetten (False = geen spanning)
    led.value = False
    
    # Opnieuw 1 seconde wachten
    time.sleep(1)
