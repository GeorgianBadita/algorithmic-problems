use std::cmp::max;

struct Solution;

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut sum = 0;
        let mut max_sum = std::i32::MIN;

        for &elem in nums.iter() {
            sum = max(sum + elem, elem);
            max_sum = max(max_sum, sum);
        }
        max_sum
    }
}

fn main() {
    println!("Hello, world!");
}
