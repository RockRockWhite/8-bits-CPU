use serde::{Deserialize, Serialize};
use std::{collections::HashMap, error::Error, hash::Hash};

// declarations
// ======================

enum Instruction {
    MV = 0,
    LB = 1,
    LI = 2,
    SB = 3,

    ADD = 10,
    SUB = 11,
    AND = 12,
    OR = 13,
    XOR = 14,
    NOT = 15,

    NOP = 62,
    HLT = 63,
}

enum Register {
    R0 = 8,
    R1 = 9,
    R2 = 10,
    R3 = 11,
    R4 = 12,
    R5 = 13,
    R6 = 14,
    R7 = 15,
}

impl Register {
    pub fn from_str(s: &str) -> Option<Self> {
        match s {
            "r0" => Some(Register::R0),
            "r1" => Some(Register::R1),
            "r2" => Some(Register::R2),
            "r3" => Some(Register::R3),
            "r4" => Some(Register::R4),
            "r5" => Some(Register::R5),
            "r6" => Some(Register::R6),
            "r7" => Some(Register::R7),
            _ => None,
        }
    }
}

// ======================

/// Token
/// must implement Clone and Token trait
/// Token trait is used to convert a token to a tree node
pub trait Token: Clone {
    fn to_tree_node(&self) -> ParsingTreeNode;
}

pub struct ParsingTreeNode {
    pub symbol_type: String,
    pub data: String,
    pub children: Vec<ParsingTreeNode>,
}

impl ParsingTreeNode {
    pub fn build(symbol_type: String, data: String, children: Vec<ParsingTreeNode>) -> Self {
        ParsingTreeNode {
            symbol_type,
            data,
            children,
        }
    }
}

/// NodePair
/// a pair of a node and a state.
/// (TreeNode, state)
pub struct NodePair(ParsingTreeNode, usize);
impl NodePair {
    pub fn new(node: ParsingTreeNode, state: usize) -> Self {
        NodePair(node, state)
    }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ReduceDerivation {
    pub left: String,
    pub right: Vec<String>,
}

impl PartialEq for ReduceDerivation {
    fn eq(&self, other: &Self) -> bool {
        self.left == other.left && self.right == other.right
    }
}

impl Eq for ReduceDerivation {}

impl Hash for ReduceDerivation {
    fn hash<H: std::hash::Hasher>(&self, state: &mut H) {
        self.left.hash(state);
        self.right.hash(state);
    }
}

impl ReduceDerivation {
    pub fn build(left: String, right: Vec<String>) -> Self {
        ReduceDerivation { left, right }
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub enum Action {
    Shift(usize),
    Reduce(ReduceDerivation),
    Accept,
    Error,
}

#[derive(Serialize, Deserialize)]
pub struct State {
    pub actions: HashMap<String, Action>,
}

impl State {
    pub fn new() -> Self {
        State {
            actions: HashMap::new(),
        }
    }
}

#[derive(Serialize, Deserialize, Default)]
pub struct ActionTable {
    pub states: Vec<State>,
}

impl ActionTable {
    pub fn get_action(&self, state: usize, symbol: &str) -> Option<&Action> {
        self.states[state].actions.get(symbol)
    }
}

#[derive(Default)]
pub struct RParser {
    action_table: ActionTable,
    handlers: HashMap<ReduceDerivation, Box<dyn Fn(Vec<String>) -> String>>,
    // variables
    // ======================
    pub gen_code: Vec<u8>,
    // ======================
}

impl RParser {
    pub const END_SYMBOL: &'static str = "__$__";
    pub const EPSILON_SYMBOL: &'static str = "__EPSILON__";
    pub const DUMMY_START_SYMBOL: &'static str = "__DUMMY_START__";

    pub fn new() -> Self {
        // action table generated by rparser
        // ======================
        let action_table: ActionTable =  serde_json::from_str(r#"{"states":[{"actions":{"hlt":{"Shift":5},"nop":{"Shift":7},"S":{"Shift":6},"mv":{"Shift":13},"instructions":{"Shift":8},"program":{"Shift":23},"li":{"Shift":9},"__$__":"Accept","instruction":{"Shift":21},"sb":{"Shift":17},"lb":{"Shift":1}}},{"actions":{"register":{"Shift":2}}},{"actions":{"comma":{"Shift":3}}},{"actions":{"number":{"Shift":4}}},{"actions":{"lb":{"Reduce":{"left":"instruction","right":["lb","register","comma","number"]}},"__$__":{"Reduce":{"left":"instruction","right":["lb","register","comma","number"]}},"li":{"Reduce":{"left":"instruction","right":["lb","register","comma","number"]}},"hlt":{"Reduce":{"left":"instruction","right":["lb","register","comma","number"]}},"nop":{"Reduce":{"left":"instruction","right":["lb","register","comma","number"]}},"sb":{"Reduce":{"left":"instruction","right":["lb","register","comma","number"]}},"mv":{"Reduce":{"left":"instruction","right":["lb","register","comma","number"]}}}},{"actions":{"lb":{"Reduce":{"left":"instruction","right":["hlt"]}},"li":{"Reduce":{"left":"instruction","right":["hlt"]}},"hlt":{"Reduce":{"left":"instruction","right":["hlt"]}},"sb":{"Reduce":{"left":"instruction","right":["hlt"]}},"__$__":{"Reduce":{"left":"instruction","right":["hlt"]}},"mv":{"Reduce":{"left":"instruction","right":["hlt"]}},"nop":{"Reduce":{"left":"instruction","right":["hlt"]}}}},{"actions":{"__$__":{"Reduce":{"left":"__DUMMY_START__","right":["S"]}}}},{"actions":{"li":{"Reduce":{"left":"instruction","right":["nop"]}},"mv":{"Reduce":{"left":"instruction","right":["nop"]}},"hlt":{"Reduce":{"left":"instruction","right":["nop"]}},"sb":{"Reduce":{"left":"instruction","right":["nop"]}},"nop":{"Reduce":{"left":"instruction","right":["nop"]}},"lb":{"Reduce":{"left":"instruction","right":["nop"]}},"__$__":{"Reduce":{"left":"instruction","right":["nop"]}}}},{"actions":{"__$__":{"Reduce":{"left":"program","right":["instructions"]}}}},{"actions":{"register":{"Shift":10}}},{"actions":{"comma":{"Shift":11}}},{"actions":{"number":{"Shift":12}}},{"actions":{"nop":{"Reduce":{"left":"instruction","right":["li","register","comma","number"]}},"lb":{"Reduce":{"left":"instruction","right":["li","register","comma","number"]}},"mv":{"Reduce":{"left":"instruction","right":["li","register","comma","number"]}},"__$__":{"Reduce":{"left":"instruction","right":["li","register","comma","number"]}},"hlt":{"Reduce":{"left":"instruction","right":["li","register","comma","number"]}},"li":{"Reduce":{"left":"instruction","right":["li","register","comma","number"]}},"sb":{"Reduce":{"left":"instruction","right":["li","register","comma","number"]}}}},{"actions":{"register":{"Shift":14}}},{"actions":{"comma":{"Shift":15}}},{"actions":{"register":{"Shift":16}}},{"actions":{"nop":{"Reduce":{"left":"instruction","right":["mv","register","comma","register"]}},"sb":{"Reduce":{"left":"instruction","right":["mv","register","comma","register"]}},"hlt":{"Reduce":{"left":"instruction","right":["mv","register","comma","register"]}},"__$__":{"Reduce":{"left":"instruction","right":["mv","register","comma","register"]}},"lb":{"Reduce":{"left":"instruction","right":["mv","register","comma","register"]}},"li":{"Reduce":{"left":"instruction","right":["mv","register","comma","register"]}},"mv":{"Reduce":{"left":"instruction","right":["mv","register","comma","register"]}}}},{"actions":{"register":{"Shift":18}}},{"actions":{"comma":{"Shift":19}}},{"actions":{"number":{"Shift":20}}},{"actions":{"li":{"Reduce":{"left":"instruction","right":["sb","register","comma","number"]}},"hlt":{"Reduce":{"left":"instruction","right":["sb","register","comma","number"]}},"lb":{"Reduce":{"left":"instruction","right":["sb","register","comma","number"]}},"__$__":{"Reduce":{"left":"instruction","right":["sb","register","comma","number"]}},"nop":{"Reduce":{"left":"instruction","right":["sb","register","comma","number"]}},"sb":{"Reduce":{"left":"instruction","right":["sb","register","comma","number"]}},"mv":{"Reduce":{"left":"instruction","right":["sb","register","comma","number"]}}}},{"actions":{"sb":{"Shift":17},"li":{"Shift":9},"lb":{"Shift":1},"mv":{"Shift":13},"hlt":{"Shift":5},"instructions":{"Shift":22},"instruction":{"Shift":21},"nop":{"Shift":7},"__$__":{"Reduce":{"left":"instructions","right":[]}}}},{"actions":{"__$__":{"Reduce":{"left":"instructions","right":["instruction","instructions"]}}}},{"actions":{"__$__":{"Reduce":{"left":"S","right":["program"]}}}}]}"#).unwrap();
        // ======================

        let mut handlers: HashMap<ReduceDerivation, Box<dyn Fn(Vec<String>) -> String>> =
            HashMap::new();

        // handlers generated by rparser
        // ======================
        handlers.insert(
            ReduceDerivation::build("S".into(), vec!["program".into()]),
            Box::new(|datas| {
                println!("S -> program");
                "".to_string()
            }),
        );
        handlers.insert(
            ReduceDerivation::build("program".into(), vec!["instructions".into()]),
            Box::new(|datas| {
                println!("program -> instructions");
                "".to_string()
            }),
        );
        handlers.insert(
            ReduceDerivation::build(
                "instructions".into(),
                vec!["instruction".into(), "instructions".into()],
            ),
            Box::new(|datas| {
                println!("instructions -> instruction instructions");
                format!("{} {}", datas[0], datas[1])
            }),
        );
        handlers.insert(
            ReduceDerivation::build("instructions".into(), vec![]),
            Box::new(|datas| {
                println!("instructions -> ε");
                "".to_string()
            }),
        );
        handlers.insert(
            ReduceDerivation::build(
                "instruction".into(),
                vec![
                    "li".into(),
                    "register".into(),
                    "comma".into(),
                    "number".into(),
                ],
            ),
            Box::new(|datas| {
                println!("instruction -> li register comma number");

                let dst = Register::from_str(&datas[1]).unwrap() as u8;
                let src = u8::from_str_radix(&datas[3], 10).unwrap();
                format!("{:02X} {:02X} {:02X}", Instruction::LI as u8, dst, src)
            }),
        );
        handlers.insert(
            ReduceDerivation::build(
                "instruction".into(),
                vec![
                    "mv".into(),
                    "register".into(),
                    "comma".into(),
                    "register".into(),
                ],
            ),
            Box::new(|datas| {
                println!("instruction -> li register comma register");

                let dst = Register::from_str(&datas[1]).unwrap() as u8;
                let src = Register::from_str(&datas[3]).unwrap() as u8;
                format!("{:02X} {:02X} {:02X}", Instruction::MV as u8, dst, src)
            }),
        );
        handlers.insert(
            ReduceDerivation::build(
                "instruction".into(),
                vec![
                    "lb".into(),
                    "register".into(),
                    "comma".into(),
                    "number".into(),
                ],
            ),
            Box::new(|datas| {
                println!("instruction -> lb register comma number");

                let dst = Register::from_str(&datas[1]).unwrap() as u8;
                let src = u8::from_str_radix(&datas[3], 10).unwrap();
                format!("{:02X} {:02X} {:02X}", Instruction::LB as u8, dst, src)
            }),
        );
        handlers.insert(
            ReduceDerivation::build(
                "instruction".into(),
                vec![
                    "sb".into(),
                    "register".into(),
                    "comma".into(),
                    "number".into(),
                ],
            ),
            Box::new(|datas| {
                println!("instruction -> sb register comma number");

                let src = Register::from_str(&datas[1]).unwrap() as u8;
                let dst = u8::from_str_radix(&datas[3], 10).unwrap();
                format!("{:02X} {:02X} {:02X}", Instruction::SB as u8, dst, src)
            }),
        );
        handlers.insert(
            ReduceDerivation::build("instruction".into(), vec!["nop".into()]),
            Box::new(|datas| {
                println!("instruction -> nop");
                format!("{:02X} 00 00", Instruction::NOP as u8)
            }),
        );
        handlers.insert(
            ReduceDerivation::build("instruction".into(), vec!["hlt".into()]),
            Box::new(|datas| {
                println!("instruction -> hlt");
                format!("{:02X} 00 00", Instruction::HLT as u8)
            }),
        );
        // ======================

        handlers.insert(
            ReduceDerivation::build(Self::DUMMY_START_SYMBOL.into(), vec!["S".into()]),
            Box::new(|vals| vals[0].clone()),
        );

        let mut res: RParser = RParser::default();
        res.action_table = action_table;
        res.handlers = handlers;
        res
    }

    // do shift-reduce parsing
    pub fn parse<T>(&self, tokens: Vec<T>) -> Result<ParsingTreeNode, Box<dyn Error>>
    where
        T: Token,
    {
        let mut shift_index = 0;
        let mut stack: Vec<NodePair> = Vec::new();

        stack.push(NodePair::new(
            ParsingTreeNode::build(Self::DUMMY_START_SYMBOL.into(), String::new(), Vec::new()),
            0,
        ));

        loop {
            let token_node = &tokens[shift_index].to_tree_node();

            let action = self
                .action_table
                .get_action(stack.last().unwrap().1, &token_node.symbol_type);

            match action {
                Some(Action::Shift(next_state)) => {
                    // shift
                    stack.push(NodePair::new(
                        tokens[shift_index].to_tree_node(),
                        *next_state,
                    ));
                    shift_index += 1;
                }
                Some(Action::Reduce(derivation)) => {
                    // pop right hand
                    let mut children: Vec<ParsingTreeNode> = Vec::new();
                    let mut datas = Vec::new();
                    for _ in 0..derivation.right.len() {
                        if let Some(top) = stack.pop() {
                            datas.push(top.0.data.clone());
                            children.push(top.0);
                        } else {
                            Err("parsing error: stack is empty.")?;
                        }
                    }

                    let children: Vec<_> = children.into_iter().rev().collect();
                    let datas: Vec<_> = datas.into_iter().rev().collect();
                    let handler = self.handlers.get(&derivation).unwrap();

                    // if the left hand side is dummy start symbol
                    // do nothing
                    if derivation.left == Self::DUMMY_START_SYMBOL {
                        stack.push(NodePair(
                            ParsingTreeNode::build(
                                derivation.left.to_string(),
                                handler(datas),
                                children,
                            ),
                            0,
                        ));
                        continue;
                    }

                    // goto[top_state(stack), X]
                    if let Action::Shift(next_state) = self
                        .action_table
                        .get_action(stack.last().unwrap().1, &derivation.left)
                        .unwrap()
                    {
                        stack.push(NodePair(
                            ParsingTreeNode::build(
                                derivation.left.to_string(),
                                handler(datas),
                                children,
                            ),
                            *next_state,
                        ));
                    } else {
                        Err("parsing error: invalid Shift action.")?;
                    }
                }
                Some(Action::Accept) => {
                    let res = stack.pop().unwrap().0;
                    return Ok(res);
                }
                _ => {
                    Err("parsing error: unknown.")?;
                }
            }
        }
    }
}
