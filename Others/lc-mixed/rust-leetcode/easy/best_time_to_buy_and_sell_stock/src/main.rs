use std::cmp::max;

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.is_empty() {
            return 0;
        }
        let mut max_profit = 0;
        let mut current_min_idx = 0;
        for (idx, value) in prices.iter().enumerate() {
            if *value < prices[current_min_idx] {
                current_min_idx = idx;
            }
            max_profit = max(max_profit, prices[idx] - prices[current_min_idx]);
        }
        max_profit
    }
}

fn main() {
    println!("Hello, world!");
}
