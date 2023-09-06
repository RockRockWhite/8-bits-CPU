import os
import pin
import assembly

filename = os.path.join(os.path.dirname(__file__), "micro.bin")

micro = [pin.NOP for _ in range(0x10000)]

# fill hlt
for addr in range(0x10000):
    micro[addr] = pin.HLT
    ia = addr >> 8
    # get the 4 bits of the address
    psw = addr >> 4 & 0xF
    cyc = addr & 0xF

    # fill the microcode with
    # the beginning of the fetch cycle
    if cyc < len(assembly.FETCH):
        micro[addr] = assembly.FETCH[cyc]


with open(filename, "wb") as f:
    for val in micro:
        f.write(val.to_bytes(4, byteorder="little"))

print("Finished to compile micro instructions.")
