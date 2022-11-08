struct Solution;

impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        if grid.is_empty() {
           return 0;
        }

        let mut grid = grid;
        let mut num_islands = 0;
        for row in 0..grid.len() {
            for col in 0..grid[row].len() {
                if grid[row][col] == '1' {
                    num_islands += 1;
                    Self::mark_island(&mut grid, row, col);
                }
            }
        }
        num_islands
    }

    fn mark_island(grid: &mut Vec<Vec<char>>, row: usize, col: usize) {
        grid[row][col] = '-';
        let dx: Vec<i32> = vec![-1, 1, 0, 0];
        let dy: Vec<i32> = vec![0, 0, -1, 1];

        let valid_coords = |grid: &Vec<Vec<char>>, row: i32, col: i32| {
            row >= 0 && row < grid.len() as i32 && col >= 0 && col < grid[0].len() as i32
        };

        for dir in 0..dx.len() {
            let (new_row, new_col) = (row as i32 + dx[dir], col as i32 + dy[dir]);
            if valid_coords(&grid, new_row, new_col) && grid[new_row as usize][new_col as usize] == '1' {
                Self::mark_island(grid, new_row as usize, new_col as usize);
            }
        }
    }
}

fn main() {
    println!("Hello, world!");
}
