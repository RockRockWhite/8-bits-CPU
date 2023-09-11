import pin

MV = 0
LB = 1
LI = 2
SB = 3

ADD = 10
ADDI = 11
SUB = 12
AND = 13
ANDI = 14
OR = 15
ORI = 16
XOR = 17
XORI = 18
NOT = 19

CMP = 32
JAL = 33
JALR = 34
BE = 35
BNE = 36
BGE = 37
BLT = 38

NOP = 62
HLT = 63

FETCH = [
    pin.PC_R | pin.MAR_W,
    pin.MC_R | pin.IR_W | pin.PC_INC | pin.PC_W,
    pin.PC_R | pin.MAR_W,
    pin.MC_R | pin.DST_W | pin.PC_INC | pin.PC_W,
    pin.PC_R | pin.MAR_W,
    pin.MC_R | pin.SRC_W | pin.PC_INC | pin.PC_W,
]


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
    # add r0, r1
    ADD: [
        pin.SRC_S | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_ADD | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    # addi r0, 0x55
    ADDI: [
        pin.SRC_R | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_ADD | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    SUB: [
        pin.SRC_S | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_SUB | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    AND: [
        pin.SRC_S | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_AND | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    ANDI: [
        pin.SRC_R | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_AND | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    OR: [
        pin.SRC_S | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_OR | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    ORI: [
        pin.SRC_R | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_OR | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    XOR: [
        pin.SRC_S | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_XOR | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    XORI: [
        pin.SRC_R | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_XOR | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    # not r0
    NOT: [
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_NOT | pin.ALU_C_W | pin.PSR_W,
        pin.ALU_C_R | pin.DST_S,
        pin.CYC_RS,
    ],
    # cmp r0, r1
    CMP: [
        pin.SRC_S | pin.ALU_B_W,
        pin.DST_R | pin.SRC_W,
        pin.SRC_S | pin.ALU_A_W,
        pin.ALU_OP_SUB | pin.ALU_C_W | pin.PSR_W,
        pin.CYC_RS,
    ],
    # jal r0, 0x55
    JAL: [
        pin.PC_R | pin.DST_S,
        pin.SRC_R | pin.PC_W,
        pin.CYC_RS,
    ],
    NOP: [pin.CYC_RS],
    HLT: [pin.HLT],
}
