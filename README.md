# Capacitor_RAM_memory_for_raspberry_pi_pico
diy capacitor ram with driver writed in micropython for raspberry pi pico

This repo contains 2-bit RAM electronics project.
But you can easily expand its capaticy by adding
more circuits responsible for 1 bit, connecting
read, write and clear wires to the pico, and finally
you have to add bits in capacitor_ram.py in class __init__:
self.bits = [{"read": Pin(NEW_BIT_READ_PIN_NUMBER, Pin.IN), "write": Pin(NEW_BIT_WRITE_PIN_NUMBER, Pin.OUT), "clear": Pin(NEW_BIT_CLEAR_PIN_NUMBER, Pin.OUT)}, ...]
If you want to use example code on more bits, you  aslo need to add more leds.

Example script uses capacitor RAM to count in binary.
and shows current binary number on leds.

Instructions:
1. Open schematics.png and build your circuit
2. Download driver - capacitor_ram.py
3. Download aslo example.py
4. Export those scripts to your raspberry pi pico
5. Run example.py

Remember, if you are making your
own script using my driver, you
have to call refresh_bits() method in the
fast loop to avoid data disappearing from capacitors.
