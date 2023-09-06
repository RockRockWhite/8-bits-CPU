MSR = 1
MAR = 2
MDR = 3
MC = 4
IR = 5
DST = 6
SRC = 7
R0 = 8
R1 = 9
R2 = 10
R3 = 11
R4 = 12
R5 = 13
R6 = 14
R7 = 15

MSR_R = MSR
MAR_R = MAR
MDR_R = MDR
MC_R = MC
IR_R = IR
DST_R = DST
SRC_R = SRC
R0_R = R0
R1_R = R1
R2_R = R2
R3_R = R3
R4_R = R4
R5_R = R5
R6_R = R6
R7_R = R7

MSR_W = MSR << 5
MAR_W = MAR << 5
MDR_W = MDR << 5
MC_W = MC << 5
IR_W = IR << 5
DST_W = DST << 5
SRC_W = SRC << 5
R0_W = R0 << 5
R1_W = R1 << 5
R2_W = R2 << 5
R3_W = R3 << 5
R4_W = R4 << 5
R5_W = R5 << 5
R6_W = R6 << 5
R7_W = R7 << 5


SRC_S = 2**10
DST_S = 2**11

PC_INC = 2**12
PC_W = 2**13
PC_R = 2**14

ALU_OP_ADD = 0 * (2**15)
ALU_OP_SUB = 1 * (2**15)
ALU_OP_AND = 2 * (2**15)
ALU_OP_OR = 3 * (2**15)
ALU_OP_XOR = 4 * (2**15)
ALU_OP_NOT = 5 * (2**15)

PSR_RS = 2**18
PSR_W = 2**19
PSR_R = 2**20

ALU_C_W = 2**21
ALU_C_R = 2**22
ALU_B_W = 2**23
ALU_A_W = 2**24

CYC_RS = 2**30
HLT = 2**31

NOP = 0
