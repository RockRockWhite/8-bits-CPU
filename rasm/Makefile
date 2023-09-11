BUILD:=./target
SRC:=./src
CONF:=./conf
TOOLS:=./tools
SYS:=linux

RLEX:=$(TOOLS)/$(SYS)/rlex
PRARSER:=$(TOOLS)/$(SYS)/rparser

$(SRC)/rasm_lex.rs:
	$(RLEX) $(CONF)/rasm.rlex $@

$(SRC)/rasm_parser.rs:
	$(PRARSER) $(CONF)/rasm.rparser $@

.PHONY: build
build: clean_rs $(SRC)/rasm_lex.rs $(SRC)/rasm_parser.rs
	cargo build --release

.PHONY: debug
debug: clean_rs $(SRC)/rasm_lex.rs $(SRC)/rasm_parser.rs
	cargo run -- test_code.asm test.bin
	
.PHONY: clean_rs
clean_rs:
	rm -f $(SRC)/rasm_lex.rs
	rm -f $(SRC)/rasm_parser.rs

.PHONY: clean
clean: clean_rs
	cargo clean