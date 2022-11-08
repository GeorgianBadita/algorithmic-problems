use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();

        for elem in nums {
            if seen.contains(&elem) {
                return true;
            }
            seen.insert(elem);
        }
        false
    }
}
fn main() {
    println!("Hello, world!");
}
