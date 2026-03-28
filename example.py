from capacitor_ram import Capacitor_RAM
from machine import Pin
from time import ticks_ms

COUNTER_DELAY = 250 #[ms]
counter_timer = ticks_ms()

leds = [Pin(14, Pin.OUT), Pin(15, Pin.OUT)]
for l in leds:
    l.value(0)

capacitor_ram = Capacitor_RAM()
if len(leds) != len(capacitor_ram.bits):
    raise ValueError("the number of LEDs is not the same as the number of bit cells")

def binary_count_on_ram():
    readed_val = capacitor_ram.read()
    for i in range(len(readed_val)):
        leds[i].value(int(readed_val[i]))
            
    if int(readed_val, 2)+1 <= 3:
        capacitor_ram.write(int(readed_val, 2)+1)
    else:
        capacitor_ram.write(0)

while True:
    if ticks_ms() - counter_timer > COUNTER_DELAY:
        binary_count_on_ram()
        counter_timer = ticks_ms()
    capacitor_ram.refresh_bits()
