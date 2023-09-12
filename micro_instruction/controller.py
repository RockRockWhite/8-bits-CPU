import os
import pin
import instruction

filename = os.path.join(os.path.dirname(__file__), "micro.bin")

micro = [pin.NOP for _ in range(0x10000)]
fetch_len = len(instruction.FETCH)

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

# fill instruction cycle for each instruction
for ia in instruction.instructions.keys():
    curr_instruction = instruction.instructions[ia]
    micro_instructions = curr_instruction["micro_instructions"]
    is_branch = curr_instruction["is_branch"]

    # fill for all possible PSW values
    for psw in range(0x10):
        if is_branch:
            # for branching instructions
            cf = psw & 1
            zf = (psw >> 1) & 1
            sf = (psw >> 2) & 1

            cond_handler_func = curr_instruction["cond_handler_func"]

            if cond_handler_func(cf, zf, sf):
                addr_base = (ia << 8) | (psw << 4)
                for cyc in range(len(micro_instructions)):
                    micro[addr_base | fetch_len + cyc] = micro_instructions[cyc]
            else:
                addr_base = (ia << 8) | (psw << 4)
                micro[addr_base | fetch_len] = pin.CYC_RS

        else:
            # for non-branching instructions
            addr_base = (ia << 8) | (psw << 4)
            for cyc in range(len(micro_instructions)):
                micro[addr_base | fetch_len + cyc] = micro_instructions[cyc]


with open(filename, "wb") as f:
    for val in micro:
        f.write(val.to_bytes(4, byteorder="little"))

print("Finished to compile micro instructions.")
