struct Solution;

impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let nums_size = nums.len();
        let mut result = vec![0; 2 * nums_size];
        nums.into_iter().enumerate().for_each(|(idx, x)| {
            result[idx] = x;
            result[idx + nums_size] = x;
        });
        result
    }
}

fn main() {
    println!("Hello, world!");
}
