// Recursive Rust program to calculate the factorial of a given number.
//
// @File = factorial.rs
// @Date = 2022-12-28
// @Author = Jannis Metrikat
// @Version = 1.0

use std::env;

// calculate the factorial of a given number
fn factorial(n: i64) -> i64 {
    if n == 0 {
        1
    } else {
        n * factorial(n - 1)
    }
}

// main function
fn main() {
    let args: Vec<String> = env::args().collect();
    let n: i64 = args[1].parse().unwrap();

    if n < 0 {
        println!("Number must be positive.");
        std::process::exit(1);
    }

    println!("{}", factorial(n));
}
