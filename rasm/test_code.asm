# li r0, 0xff ; this is a comment
# mv r1, r0
# lb r2, 0x02
# sb r2, 0x20

# L1:
#     addi r0, 1
#     jal r1, L1

# not r0
# not r1

# li r0, 24
# li r1, 24
# cmp r0, r1
# be r0, L1

beg:
    li r0, 2
    li r1, 1

    cmp r0, r1
    be r0, beg

# sub r0, r1
# and r0, r1
# andi r0, 0x01
# or r0, r1
# ori r0, 0x01
# xor r0, r1
# xori r0, 0x01
# not r0
# cmp r0, r1

end:
    nop
    hlt