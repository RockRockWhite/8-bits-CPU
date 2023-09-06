import pin

FETCH = [
    pin.PC_R | pin.MAR_W,
    pin.MC_R | pin.IR_W | pin.PC_INC | pin.PC_W,
    pin.PC_R | pin.MAR_W,
    pin.MC_R | pin.DST_W | pin.PC_INC | pin.PC_W,
    pin.PC_R | pin.MAR_W,
    pin.MC_R | pin.SRC_W | pin.PC_INC | pin.PC_W,
]
