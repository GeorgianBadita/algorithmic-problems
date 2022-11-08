use std::cmp::max;

struct Solution;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        fn get_max_prod(nums: &Vec<i32>) -> i32 {
            let mut curr_mul = 1;
            let mut max_val = *nums.iter().max().unwrap();
            nums.iter().for_each(|num| {
                curr_mul *= *num;
                max_val = max(max_val, curr_mul);
                if curr_mul == 0 {
                    curr_mul = 1;
                }
            });
            max_val
        }

        max(
            get_max_prod(&nums),
            get_max_prod(&nums.into_iter().rev().collect()),
        )
    }
}

fn main() {
    println!("Hello, world!");
}
