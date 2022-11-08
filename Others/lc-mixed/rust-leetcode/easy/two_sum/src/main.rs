use std::collections::HashMap;
use std::vec::Vec;

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, usize> = HashMap::new();
        for (idx, elem) in nums.into_iter().enumerate() {
            let diff = target - elem;
            match seen.get(&diff) {
                Some(prev_idx) => return vec![*prev_idx as i32, idx as i32],
                _ => {
                    seen.insert(elem, idx);
                }
            }
        }
        unreachable!();
    }
}

fn main() {
    println!("{:?}", Solution::two_sum(vec![2, 7, 11, 15], 9));
}
