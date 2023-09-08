use rasm::*;
use std::{cell::RefCell, env, error::Error, fs::File, io::Read};

fn main() {
    // read args
    let args = Args::build(env::args().collect()).unwrap_or_else(|err| {
        println!("{}", err);
        std::process::exit(1);
    });

    run(args).unwrap_or_else(|err| {
        println!("{}", err);
        std::process::exit(1);
    });

    println!("Done.");
}

fn run(args: Args) -> Result<(), Box<dyn Error>> {
    // read source code
    let mut f = File::open(args.source_file)?;
    let mut buf = String::new();
    f.read_to_string(&mut buf)?;

    // lexical analysis
    let rlex = Rlex {
        tokens: RefCell::new(Vec::new()),
    };
    rlex.lex(&buf);
    let mut tokens = rlex.tokens.borrow().clone();

    // parsing
    tokens.push(LexToken::build(RParser::END_SYMBOL.into(), "".into()));
    let parse_tree = RParser::new().parse(tokens).unwrap();

    // get code bytes
    let code_str = parse_tree.children[0].children[0].children[0].data.clone();
    let bytes = &mut Vec::new();
    let hex_parts: Vec<&str> = code_str.split_whitespace().collect();
    for hex_part in hex_parts {
        let byte = u8::from_str_radix(hex_part, 16).unwrap();
        bytes.push(byte);
    }

    // write to output file
    std::fs::write(&args.output_file, bytes)?;

    Ok(())
}

struct Args {
    source_file: String,
    output_file: String,
}

impl Args {
    fn build(args: Vec<String>) -> Result<Args, &'static str> {
        if args.len() != 3 {
            return Err("Usage: rlex <config_file> <output_file>");
        }

        Ok(Args {
            source_file: args[1].clone(),
            output_file: args[2].clone(),
        })
    }
}
