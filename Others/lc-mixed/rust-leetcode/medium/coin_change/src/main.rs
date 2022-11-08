

struct Solution;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut dp = vec![amount + 1; amount as usize + 1];
        dp[0] = 0;
        for value in 1..(amount + 1) {
            for coin in coins.iter() {
                if value - coin >= 0 {
                    dp[value as usize] = i32::min(1 + dp[value as usize - *coin as usize ], dp[value as usize]);
                }
            }
        }
        if dp[amount as usize] == amount + 1 {-1} else {dp[amount as usize]}
    }
}

// [2,5,10,1]
// 27

fn main() {
    println!("{}", Solution::coin_change(vec![2, 5, 10, 1], 27));
}
