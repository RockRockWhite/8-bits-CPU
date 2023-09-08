import os
import pin
import instruction

filename = os.path.join(os.path.dirname(__file__), "micro.bin")

micro = [pin.NOP for _ in range(0x10000)]

# fill the microcode with the beginning of the fetch cycle
for addr in range(0x10000):
    micro[addr] = pin.HLT
    ia = addr >> 8
    # get the 4 bits of the address
    psw = addr >> 4 & 0xF
    cyc = addr & 0xF

    # fill the microcode with
    # the beginning of the fetch cycle
    fetch_len = len(instruction.FETCH)
    if cyc < fetch_len:
        micro[addr] = instruction.FETCH[cyc]

    # fill instruction cycle if the instruction exists
    if ia in instruction.instructions:
        if cyc >= fetch_len and cyc < fetch_len + len(instruction.instructions[ia]):
            micro[addr] = instruction.instructions[ia][cyc - fetch_len]

with open(filename, "wb") as f:
    for val in micro:
        f.write(val.to_bytes(4, byteorder="little"))

print("Finished to compile micro instructions.")
