struct Solution;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        // [1,2,3,4]
        // left: [1, 1, 2, 6]
        // right: [24, 12, 4, 1]
        //product = [24, 12, 8, 6]
        let mut left = vec![1; nums.len()];
        let mut right = vec![1; nums.len()];

        for idx in 1..nums.len() {
            left[idx] = left[idx - 1] * nums[idx - 1];
        }
        for idx in (0..(nums.len() - 1)).rev() {
            right[idx] = right[idx + 1] * nums[idx + 1];
        }
        left.iter()
            .zip(right.iter())
            .map(|(x, y)| *x * (*y))
            .collect()
    }
}

fn main() {
    println!("Hello, world!");
}
