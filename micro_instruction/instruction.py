import pin

MV = 0
LB = 1
LI = 2
SB = 3

ADD = 10
SUB = 11
AND = 12
OR = 13
XOR = 14
NOT = 15

NOP = 62
HLT = 63

instructions = {
    # mv r0, r1
    MV: [pin.SRC_S | pin.DST_S, pin.CYC_RS],
    # lb r0, 0x55aa
    # load byte from memory
    LB: [
        pin.SRC_R | pin.MAR_W,
        pin.MC_R | pin.DST_S,
        pin.CYC_RS,
    ],
    # li r0, 0x55aa
    LI: [pin.SRC_R | pin.DST_S, pin.CYC_RS],
    # sb r0, 0x55aa
    # sb srt, dst
    # revert in asm!!!
    SB: [
        pin.SRC_S | pin.MDR_W,
        pin.DST_R | pin.MAR_W,
        pin.MC_W,
        pin.CYC_RS,
    ],
    ADD: [],
    SUB: [],
    AND: [],
    OR: [],
    XOR: [],
    NOT: [],
    NOP: [pin.CYC_RS],
    HLT: [pin.HLT],
}
