import os

filename = os.path.join(os.path.dirname(__file__), "ins.bin")

ALU_ADD = 0
ALU_SUB = 1

WE_REG_RES = 2**4
RE_REG_RES = 2**5

WE_REG_A = 2**6
RE_REG_A = 2**7

WE_REG_B = 2**8
RE_REG_B = 2**9

PC_INC = 2**10
PC_WE = 2**11
PC_RE = 2**12

RE_MC = 2**13
WE_MC = 2**14

HLT = 2**15

micro = [
    RE_MC | WE_REG_A | PC_RE,
    PC_RE | PC_INC,
    RE_MC | WE_REG_B | PC_RE,
    PC_RE | PC_INC,
    RE_REG_A | RE_REG_B | WE_REG_RES | ALU_ADD,
    RE_REG_RES | WE_MC | PC_RE,
    HLT,
]

with open(filename, "wb") as f:
    for val in micro:
        f.write(val.to_bytes(2, byteorder="little"))

print((RE_MC | WE_REG_A).to_bytes(2, byteorder="big").hex(" "))
