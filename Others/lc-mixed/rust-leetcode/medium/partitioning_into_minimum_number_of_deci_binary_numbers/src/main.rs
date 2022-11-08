struct Solution;

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        n.chars().into_iter().fold(0, |accum, item| {
            i32::max(accum, item.to_digit(10).unwrap() as i32)
        })
    }
}

fn main() {
    println!("Hello, world!");
}
