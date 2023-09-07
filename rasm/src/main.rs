use std::cell::RefCell;

mod rasm_lex;
pub mod rasm_parser;

fn main() {
    let r = rasm_lex::Rlex {
        tokens: RefCell::new(Vec::new()),
    };
    r.lex(
        r#"
li r0, 0x55 ; this is a comment
mv r1, r0
lb r3, 0x02
sb r3, 0x20
nop
hlt
     "#,
    );

    let mut tokens = r.tokens.borrow().clone();
    tokens.push(rasm_lex::LexToken::build(
        rasm_parser::RParser::END_SYMBOL.into(),
        "".into(),
    ));

    let parser = rasm_parser::RParser::new();
    let res = parser.parse(tokens).unwrap();
    dfs(&res, 0);
}

pub fn dfs(node: &rasm_parser::ParsingTreeNode, depth: usize) {
    for _ in 0..depth {
        print!("  ");
    }
    println!("{}: {}", node.symbol_type, node.data);
    for child in &node.children {
        dfs(child, depth + 1);
    }
}
