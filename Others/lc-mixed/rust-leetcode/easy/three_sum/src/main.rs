use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn two_sum(nums: &Vec<i32>, l: usize, r: usize, target: i32) -> Vec<Vec<i32>> {
            let mut result = Vec::new();
            let mut left = l;
            let mut right = r;

            while left < right {
                if nums[left] + nums[right] == target {
                    result.push(vec![nums[left], nums[right]]);
                    left += 1;
                    right -= 1;
                } else if nums[left] + nums[right] < target {
                    left += 1;
                } else {
                    right -= 1;
                }
                while left + 1 < nums.len() && nums[left] == nums[left + 1] {
                    left += 1;
                }
                while right > 0 && nums[right] == nums[right - 1] {
                    right -= 1;
                }
            }
            result
        }

        let mut result: HashSet<(i32, i32, i32)> = HashSet::new();
        let mut nums = nums;
        nums.sort();

        for (idx, &num) in nums.iter().enumerate() {
            let two_sum_sol = two_sum(&nums, idx + 1, nums.len() - 1, -num);
            two_sum_sol
                .iter()
                .map(|pair| (num, pair[0], pair[1]))
                .for_each(|x| {
                    result.insert(x);
                });
        }
        result.iter().map(|(x, y, z)| vec![*x, *y, *z]).collect()
    }
}

fn main() {
    println!("Hello, world!");
}
