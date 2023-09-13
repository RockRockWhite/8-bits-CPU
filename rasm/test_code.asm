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

# li Zero, 0xff
# li ra, 1
# li sp, 2
# li r3, 3
# li r4, 4
# li r5, 5
# li r6, 6
# li r7, 7
# li r8, 8
# li r9, 9
# li r10, 10
# li r11, 11
# li r12, 12
# li r13, 13
# li r14, 14
# li r15, 15

# # test branch
#     li r3, 0
#     li r4, 10
# loop:
#     addi r3, 1
#     cmp r3, r4
#     blt Zero, loop

# test stack
li sp, stack_top
addi sp, -3


mv r8, sp
lb r3, (r8)

addi r8, 1
li r4, 6
sb r4, (r8)

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

stack_bottom:
    .byte 0x1
    .byte 0x2
    .byte 0x3
stack_top: