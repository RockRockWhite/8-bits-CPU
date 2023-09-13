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
    MV: {
        "micro_instructions": [pin.SRC_S | pin.DST_S, pin.CYC_RS],
        "is_branch": False,
    },
    # lb r0, (0xaa)
    # load byte from memory
    LB: {
        "micro_instructions": [
            pin.SRC_S | pin.MAR_W,
            pin.MC_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    # li r0, 0xaa
    LI: {
        "micro_instructions": [pin.SRC_R | pin.DST_S, pin.CYC_RS],
        "is_branch": False,
    },
    # sb r0, (0x5a)
    # store byte to memory
    SB: {
        "micro_instructions": [
            pin.SRC_S | pin.MAR_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.MDR_W,
            pin.MC_W,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    # add r0, r1
    ADD: {
        "micro_instructions": [
            pin.SRC_S | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_ADD | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    # addi r0, 0x55
    ADDI: {
        "micro_instructions": [
            pin.SRC_R | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_ADD | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    SUB: {
        "micro_instructions": [
            pin.SRC_S | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_SUB | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    AND: {
        "micro_instructions": [
            pin.SRC_S | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_AND | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    ANDI: {
        "micro_instructions": [
            pin.SRC_R | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_AND | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    OR: {
        "micro_instructions": [
            pin.SRC_S | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_OR | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    ORI: {
        "micro_instructions": [
            pin.SRC_R | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_OR | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    XOR: {
        "micro_instructions": [
            pin.SRC_S | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_XOR | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    XORI: {
        "micro_instructions": [
            pin.SRC_R | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_XOR | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    # not r0
    NOT: {
        "micro_instructions": [
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_NOT | pin.ALU_C_W | pin.PSR_W,
            pin.ALU_C_R | pin.DST_S,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    # cmp r0, r1
    CMP: {
        "micro_instructions": [
            pin.SRC_S | pin.ALU_B_W,
            pin.DST_R | pin.SRC_W,
            pin.SRC_S | pin.ALU_A_W,
            pin.ALU_OP_SUB | pin.ALU_C_W | pin.PSR_W,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    # jal r0, 0x55
    JAL: {
        "micro_instructions": [
            pin.PC_R | pin.DST_S,
            pin.SRC_R | pin.PC_W,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    # jalr r0, r1
    JALR: {
        "micro_instructions": [
            pin.PC_R | pin.DST_S,
            pin.SRC_S | pin.PC_W,
            pin.CYC_RS,
        ],
        "is_branch": False,
    },
    BE: {
        "micro_instructions": [
            pin.PC_R | pin.DST_S,
            pin.SRC_R | pin.PC_W,
            pin.CYC_RS,
        ],
        "is_branch": True,
        "cond_handler_func": lambda cf, zf, sf: ((zf == 1) and (cf == 0)),
    },
    BNE: {
        "micro_instructions": [
            pin.PC_R | pin.DST_S,
            pin.SRC_R | pin.PC_W,
            pin.CYC_RS,
        ],
        "is_branch": True,
        "cond_handler_func": lambda cf, zf, sf: (zf != 1),
    },
    BGE: {
        "micro_instructions": [
            pin.PC_R | pin.DST_S,
            pin.SRC_R | pin.PC_W,
            pin.CYC_RS,
        ],
        "is_branch": True,
        # a - b, get a >= b
        # if not overflow
        # then sf = 0, cf = 0
        #
        # if overflow
        # then sf = 1, cf = 1
        #
        # so, the condition is (sf == cf)
        "cond_handler_func": lambda cf, zf, sf: (cf == sf),
    },
    BLT: {
        "micro_instructions": [
            pin.PC_R | pin.DST_S,
            pin.SRC_R | pin.PC_W,
            pin.CYC_RS,
        ],
        "is_branch": True,
        # a - b, get a < b
        # if not overflow
        # then sf = 1, cf = 0
        #
        # if overflow
        # then sf = 0, cf = 1
        #
        # so, the condition is (sf == cf)
        "cond_handler_func": lambda cf, zf, sf: (cf != sf),
    },
    NOP: {
        "micro_instructions": [pin.CYC_RS],
        "is_branch": False,
    },
    HLT: {
        "micro_instructions": [pin.HLT],
        "is_branch": False,
    },
}
