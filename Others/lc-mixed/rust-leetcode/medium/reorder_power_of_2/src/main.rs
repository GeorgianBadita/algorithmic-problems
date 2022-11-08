struct Solution;

impl Solution {
    pub fn reordered_power_of2(n: i32) -> bool {
        let cmp_digits = |mut x: u32, mut y: u32| -> bool {
            let mut x_digs = Vec::new();
            let mut y_digs = Vec::new();
            while x > 0 && y > 0 {
                x_digs.push(x % 10);
                y_digs.push(y % 10);
                x /= 10;
                y /= 10;
            }
            x_digs.sort();
            y_digs.sort();
            return x == y && x == 0 && x_digs == y_digs;
        };
        let n = n as u32;
        let powers = (0..30).map(|x| u32::pow(2, x as u32)).collect::<Vec<u32>>();

        for power in powers {
            if cmp_digits(power, n) {
                return true;
            }
        }
        false
    }
}

fn main() {
    println!("Hello, world!");
}
