// Recursive Rust program to calculate the factorial of a given number.
//
// @File = factorial.rs
// @Date = 2022-12-28
// @Author = Jannis Metrikat
// @Version = 1.0

use std::env;

// calculates the factorial of a given number
fn factorial(n: u64) -> u64 {
    if n == 0 {
        1
    } else {
        n * factorial(n - 1)
    }
}

// main function
fn main() {
    let args: Vec<String> = env::args().collect();
    let n: u64 = args[1].parse().unwrap();
    println!("{}", factorial(n));
}
