import os
import pin

filename = os.path.join(os.path.dirname(__file__), "ins.bin")

micro = [
    pin.NOP,
]

with open(filename, "wb") as f:
    for val in micro:
        f.write(val.to_bytes(2, byteorder="little"))
