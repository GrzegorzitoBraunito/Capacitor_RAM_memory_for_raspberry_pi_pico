from machine import Pin
from time import sleep

class Capacitor_RAM():
    def __init__(self):
        self.bits = [{"read": Pin(28, Pin.IN), "write": Pin(27, Pin.OUT), "clear": Pin(26, Pin.OUT)},
                     {"read": Pin(22, Pin.IN), "write": Pin(21, Pin.OUT), "clear": Pin(20, Pin.OUT)}]
        self.clear()
        
    def write(self, val):
        self.clear()
        bin_val = self.zfill(bin(val)[2:])
        for i in range(len(bin_val)):
            bit = int(bin_val[i])
            if bit:
                self.bits[i]["write"].value(1)
        sleep(0.01)
        for b in self.bits:
            b["write"].value(0)
        
    def read(self):
        bin_val = ""
        for b in self.bits:
            if b["read"].value():
                bin_val += "1"
            else:
                bin_val += "0"
                
        return bin_val
    
    def clear(self):
        for b in self.bits:
            b["clear"].value(1)
            sleep(0.01)
            b["clear"].value(0)

    def refresh_bits(self):
        for b in self.bits:
            if b["read"].value():
                b["write"].value(1)
        sleep(0.05)
        for b in self.bits:
            b["write"].value(0)

    def zfill(self, val):
        new_val = ""
        new_val += "0"*(len(self.bits)-len(val))
        new_val += val
        return new_val