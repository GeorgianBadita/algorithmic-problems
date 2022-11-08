struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let palindrome = compute_palindrome(&x);
        x == palindrome
    }
}

fn main() {
    println!("Hello, world!");
}

fn compute_palindrome(number: &i32) -> i32 {
    let mut result = 0;
    let mut copy = number.clone();

    while copy != 0 {
        result = result * 10 + copy % 10;
        copy = copy / 10;
    }
    result
}
