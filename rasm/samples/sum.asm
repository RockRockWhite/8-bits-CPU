# calculate the sum of 5 bytes started from stack_bottom
# and store result to res

li sp, stack_top
addi sp, -6

# r3 store sum
li r3, 0
# r4 for loop
li r4, 4
# r5 for stack
mv r5, sp

loop:
    lb r6, (r5)
    add r3, r6

    addi r4, -1
    addi r5, 1

    # r7 for cmp
    li r7, 0
    cmp r4, r7
    bge Zero, loop

# store result to res
# r8 for store
li r8, res
sb r3, (r8)

stack_bottom:
    .byte 0x1
    .byte 0x2
    .byte 0x3
    .byte 0x4
    .byte 0x5
res:
    .byte 0x0
stack_top: