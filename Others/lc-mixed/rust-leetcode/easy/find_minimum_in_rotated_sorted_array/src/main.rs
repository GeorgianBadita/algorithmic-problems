struct Solution;

impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;

        if nums.len() == 1 {
            return nums[left];
        }

        if nums[left] <= nums[right] {
            return nums[left];
        }

        // nums = [4,5,6,7,0,1,2]
        while left <= right {
            let mid = (left + right) / 2;

            if nums[mid] > nums[mid + 1] {
                return nums[mid + 1];
            }
            if nums[mid - 1] > nums[mid] {
                return nums[mid];
            }

            if nums[mid] >= nums[0] {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        nums[0]
    }
}

fn main() {
    println!("Hello, world!");
}
