from pyfirmata import Arduino
import time

board = Arduino("COM4")
ledverde = board.get_pin('d:11:o')
ledamarillo = board.get_pin('d:10:o')
ledrojo = board.get_pin('d:9:o')

while True:
    ledverde.write(1)
    time.sleep(5)
    ledverde.write(0)
    ledamarillo.write(1)
    time.sleep(3)
    ledamarillo.write(0)
    ledrojo.write(1)
    time.sleep(5)
    ledrojo.write(0)