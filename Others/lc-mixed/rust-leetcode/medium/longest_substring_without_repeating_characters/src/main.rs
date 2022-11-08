use std::{cmp::max, collections::HashMap};

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        if s.len() < 2 {
            s.len() as i32
        } else {
            let mut char_freq = HashMap::new();
            let mut max_freq: i32 = 0;
            let mut freq: i32 = 0;
            let mut idx = 0;

            while idx < s.len() {
                let char = s.as_bytes()[idx] as char;
                if !char_freq.contains_key(&char) {
                    freq += 1;
                    char_freq.insert(char, idx);
                    idx += 1
                } else {
                    max_freq = max(max_freq, freq);
                    idx = *char_freq.get(&char).unwrap() + 1;
                    freq = 0;
                    char_freq = HashMap::new();
                }
            }
            max(max_freq, freq)
        }
    }
}

fn main() {
    print!(
        "Res: {}",
        Solution::length_of_longest_substring(String::from("dvdf"))
    );
}
