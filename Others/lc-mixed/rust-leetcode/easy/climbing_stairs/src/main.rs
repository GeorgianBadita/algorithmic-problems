struct Solution;

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 3 {
            return n
        }
        let (mut a, mut b, mut c) = (2, 3, 0);
        for _ in 3..n {
            c = a + b;
            a = b;
            b = c;
        }
        c
    }
}

fn main() {
    println!("Hello, world!");
}
