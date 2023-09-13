# 8-bits-CPU

PC MC and bus

![image-20230829223915458](README.assets/image-20230829223915458.png)

微程序控制器与微命令编程

![image-20230831122257095](README.assets/image-20230831122257095.png)

> 记一个踩过的坑：
>
> POW打开时，有可能会立即带来上升沿，而部分总线上的数据还未准备好造成莫名其妙的错误
>
> 因此需要增加一个nop来解决此问题

ALU

![image-20230901232840102](README.assets/image-20230901232840102.png)

## 8 bits CPU

![image-20230906215101512](README.assets/image-20230906215101512.png)

## 指令系统

### 指令格式
一条指令3个Byte，分别为OP，DST，SRC
| 23    16 | 15    8 | 7   0 |
| -------- | ------- | ----- |
| OP       | DST     | SRC   |

### 支持指令集：
![34c1fce01d5562639efa913a79fdb389](README.assets/34c1fce01d5562639efa913a79fdb389.png)

### 寄存器：
| Register | Alias | Description                   |
| -------- | ----- | ----------------------------- |
| r0       | Zero  | Always be 0.                  |
| r1       | ra    | Return address.               |
| r2       | sp    | Stack pointer.Return address. |
| r3-r15   | -     | -                             |

### 汇编器rasm
> ./rasm 下实现了简单的汇编器

> ./rasm/test_code.asm 为汇编示例代码

```asm
li r0, 0xff ; this is a comment
mv r1, r0
lb r2, 0x02
sb r2, 0x20
nop
hlt
```

> ./rasm/test.bin 为生成的二进制文件

本汇编器基于我自己写的 rlex 和 rparsr 实现  
[RockRockWhite/RLex: lexical analyis by rust (github.com)](https://github.com/RockRockWhite/RLex)  
[RockRockWhite/RParser: a parser tools by rust (github.com)](https://github.com/RockRockWhite/RParser)  

## 最终完成CPU硬件图

![83798c141f607bd17ed8bc51fcc52f56](README.assets/83798c141f607bd17ed8bc51fcc52f56.png)

## 汇编sample
下面这段代码的功能是计算栈底开始的5个字节的和，并将结果存储到res中。

```asm
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
```

运行结果:

![d7c2646fb21293b08ed2f6bdc87ef8b9](README.assets/d7c2646fb21293b08ed2f6bdc87ef8b9.png)