
# Generated Info

## Base Info
- config_file: rasm.rparser
- output_file: ../src/rasm_parser.rs
- time: 2023-09-08 15:08:53.893140 +08:00

---

## DFA Graph
```mermaid
graph LR
0["instruction -> •hlt\nS -> •program\ninstruction -> •mv register comma register\nprogram -> •instructions\ninstruction -> •lb register comma number\ninstructions -> •\ninstruction -> •li register comma number\ninstructions -> •instruction instructions\n__DUMMY_START__ -> •S\ninstruction -> •nop\ninstruction -> •sb register comma number\n"]
1["instruction -> lb •register comma number\n"]
2["instruction -> lb register •comma number\n"]
3["instruction -> lb register comma •number\n"]
4["instruction -> lb register comma number•\n"]
5["instruction -> hlt•\n"]
6["__DUMMY_START__ -> S•\n"]
7["instruction -> nop•\n"]
8["program -> instructions•\n"]
9["instruction -> li •register comma number\n"]
10["instruction -> li register •comma number\n"]
11["instruction -> li register comma •number\n"]
12["instruction -> li register comma number•\n"]
13["instruction -> mv •register comma register\n"]
14["instruction -> mv register •comma register\n"]
15["instruction -> mv register comma •register\n"]
16["instruction -> mv register comma register•\n"]
17["instruction -> sb •register comma number\n"]
18["instruction -> sb register •comma number\n"]
19["instruction -> sb register comma •number\n"]
20["instruction -> sb register comma number•\n"]
21["instruction -> •li register comma number\ninstruction -> •lb register comma number\ninstructions -> •instruction instructions\ninstruction -> •mv register comma register\ninstruction -> •hlt\ninstructions -> instruction •instructions\ninstruction -> •nop\ninstructions -> •\ninstruction -> •sb register comma number\n"]
22["instructions -> instruction instructions•\n"]
23["S -> program•\n"]

3--"number"-->4
2--"comma"-->3
1--"register"-->2
0--"lb"-->1
0--"hlt"-->5
0--"S"-->6
0--"nop"-->7
0--"instructions"-->8
11--"number"-->12
10--"comma"-->11
9--"register"-->10
0--"li"-->9
15--"register"-->16
14--"comma"-->15
13--"register"-->14
0--"mv"-->13
19--"number"-->20
18--"comma"-->19
17--"register"-->18
0--"sb"-->17
21--"sb"-->17
21--"lb"-->1
21--"instructions"-->22
21--"instruction"-->21
21--"mv"-->13
21--"hlt"-->5
21--"nop"-->7
21--"li"-->9
0--"instruction"-->21
0--"program"-->23

```

---

## Follow Set
```txt
nop: ["sb", "nop", "hlt", "__$__", "lb", "mv", "li"]
__EPSILON__: ["__$__"]
sb: ["register"]
mv: ["register"]
comma: ["number", "register"]
instruction: ["li", "mv", "hlt", "nop", "sb", "lb", "__$__"]
register: ["sb", "lb", "__$__", "comma", "hlt", "li", "nop", "mv"]
li: ["register"]
program: ["__$__"]
lb: ["register"]
S: ["__$__"]
hlt: ["li", "hlt", "nop", "__$__", "mv", "sb", "lb"]
number: ["hlt", "nop", "__$__", "mv", "li", "sb", "lb"]
__DUMMY_START__: ["__$__"]
__$__: []
instructions: ["__$__"]
```

---
## Action Table
```txt
State 0:
hlt: Shift(5)
nop: Shift(7)
S: Shift(6)
mv: Shift(13)
instructions: Shift(8)
program: Shift(23)
li: Shift(9)
__$__: Accept
instruction: Shift(21)
sb: Shift(17)
lb: Shift(1)
===================
State 1:
register: Shift(2)
===================
State 2:
comma: Shift(3)
===================
State 3:
number: Shift(4)
===================
State 4:
lb: Reduce(ReduceDerivation { left: "instruction", right: ["lb", "register", "comma", "number"] })
__$__: Reduce(ReduceDerivation { left: "instruction", right: ["lb", "register", "comma", "number"] })
li: Reduce(ReduceDerivation { left: "instruction", right: ["lb", "register", "comma", "number"] })
hlt: Reduce(ReduceDerivation { left: "instruction", right: ["lb", "register", "comma", "number"] })
nop: Reduce(ReduceDerivation { left: "instruction", right: ["lb", "register", "comma", "number"] })
sb: Reduce(ReduceDerivation { left: "instruction", right: ["lb", "register", "comma", "number"] })
mv: Reduce(ReduceDerivation { left: "instruction", right: ["lb", "register", "comma", "number"] })
===================
State 5:
lb: Reduce(ReduceDerivation { left: "instruction", right: ["hlt"] })
li: Reduce(ReduceDerivation { left: "instruction", right: ["hlt"] })
hlt: Reduce(ReduceDerivation { left: "instruction", right: ["hlt"] })
sb: Reduce(ReduceDerivation { left: "instruction", right: ["hlt"] })
__$__: Reduce(ReduceDerivation { left: "instruction", right: ["hlt"] })
mv: Reduce(ReduceDerivation { left: "instruction", right: ["hlt"] })
nop: Reduce(ReduceDerivation { left: "instruction", right: ["hlt"] })
===================
State 6:
__$__: Reduce(ReduceDerivation { left: "__DUMMY_START__", right: ["S"] })
===================
State 7:
li: Reduce(ReduceDerivation { left: "instruction", right: ["nop"] })
mv: Reduce(ReduceDerivation { left: "instruction", right: ["nop"] })
hlt: Reduce(ReduceDerivation { left: "instruction", right: ["nop"] })
sb: Reduce(ReduceDerivation { left: "instruction", right: ["nop"] })
nop: Reduce(ReduceDerivation { left: "instruction", right: ["nop"] })
lb: Reduce(ReduceDerivation { left: "instruction", right: ["nop"] })
__$__: Reduce(ReduceDerivation { left: "instruction", right: ["nop"] })
===================
State 8:
__$__: Reduce(ReduceDerivation { left: "program", right: ["instructions"] })
===================
State 9:
register: Shift(10)
===================
State 10:
comma: Shift(11)
===================
State 11:
number: Shift(12)
===================
State 12:
nop: Reduce(ReduceDerivation { left: "instruction", right: ["li", "register", "comma", "number"] })
lb: Reduce(ReduceDerivation { left: "instruction", right: ["li", "register", "comma", "number"] })
mv: Reduce(ReduceDerivation { left: "instruction", right: ["li", "register", "comma", "number"] })
__$__: Reduce(ReduceDerivation { left: "instruction", right: ["li", "register", "comma", "number"] })
hlt: Reduce(ReduceDerivation { left: "instruction", right: ["li", "register", "comma", "number"] })
li: Reduce(ReduceDerivation { left: "instruction", right: ["li", "register", "comma", "number"] })
sb: Reduce(ReduceDerivation { left: "instruction", right: ["li", "register", "comma", "number"] })
===================
State 13:
register: Shift(14)
===================
State 14:
comma: Shift(15)
===================
State 15:
register: Shift(16)
===================
State 16:
nop: Reduce(ReduceDerivation { left: "instruction", right: ["mv", "register", "comma", "register"] })
sb: Reduce(ReduceDerivation { left: "instruction", right: ["mv", "register", "comma", "register"] })
hlt: Reduce(ReduceDerivation { left: "instruction", right: ["mv", "register", "comma", "register"] })
__$__: Reduce(ReduceDerivation { left: "instruction", right: ["mv", "register", "comma", "register"] })
lb: Reduce(ReduceDerivation { left: "instruction", right: ["mv", "register", "comma", "register"] })
li: Reduce(ReduceDerivation { left: "instruction", right: ["mv", "register", "comma", "register"] })
mv: Reduce(ReduceDerivation { left: "instruction", right: ["mv", "register", "comma", "register"] })
===================
State 17:
register: Shift(18)
===================
State 18:
comma: Shift(19)
===================
State 19:
number: Shift(20)
===================
State 20:
li: Reduce(ReduceDerivation { left: "instruction", right: ["sb", "register", "comma", "number"] })
hlt: Reduce(ReduceDerivation { left: "instruction", right: ["sb", "register", "comma", "number"] })
lb: Reduce(ReduceDerivation { left: "instruction", right: ["sb", "register", "comma", "number"] })
__$__: Reduce(ReduceDerivation { left: "instruction", right: ["sb", "register", "comma", "number"] })
nop: Reduce(ReduceDerivation { left: "instruction", right: ["sb", "register", "comma", "number"] })
sb: Reduce(ReduceDerivation { left: "instruction", right: ["sb", "register", "comma", "number"] })
mv: Reduce(ReduceDerivation { left: "instruction", right: ["sb", "register", "comma", "number"] })
===================
State 21:
sb: Shift(17)
li: Shift(9)
lb: Shift(1)
mv: Shift(13)
hlt: Shift(5)
instructions: Shift(22)
instruction: Shift(21)
nop: Shift(7)
__$__: Reduce(ReduceDerivation { left: "instructions", right: [] })
===================
State 22:
__$__: Reduce(ReduceDerivation { left: "instructions", right: ["instruction", "instructions"] })
===================
State 23:
__$__: Reduce(ReduceDerivation { left: "S", right: ["program"] })
===================

```
---
generated by rparser
RockRockWhite 2023
    