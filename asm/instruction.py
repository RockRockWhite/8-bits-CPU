import pin

MV = 0
LA = 1
LI = 2

ADD = 10
SUB = 11
AND = 12
OR = 13
XOR = 14
NOT = 15

NOP = 62
HLT = 63

instructions = {
    MV: [pin.SRC_R | pin.DST_S, pin.CYC_RS],
    LA: [],
    # li r0, 0x55aa
    LI: [pin.SRC_R | pin.DST_S, pin.CYC_RS],
    ADD: [],
    SUB: [],
    AND: [],
    OR: [],
    XOR: [],
    NOT: [],
    NOP: [pin.CYC_RS],
    HLT: [pin.HLT],
}
