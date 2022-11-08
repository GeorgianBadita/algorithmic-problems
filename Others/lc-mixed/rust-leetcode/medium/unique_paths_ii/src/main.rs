use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        if obstacle_grid[0][0] == 1 {
            return 0;
        }

        let mut obstacle_grid = obstacle_grid;
        let (m, n) = (obstacle_grid.len(), obstacle_grid.last().unwrap().len());
        obstacle_grid[0][0] = 1;

        for idx in 1..m {
            if obstacle_grid[idx][0] == 0 && obstacle_grid[idx - 1][0] == 1 {
                obstacle_grid[idx][0] = 1;
            } else {
                obstacle_grid[idx][0] = 0;
            }
        }

        for idx in 1..n {
            if obstacle_grid[0][idx] == 0 && obstacle_grid[0][idx - 1] == 1 {
                obstacle_grid[0][idx] = 1;
            } else {
                obstacle_grid[0][idx] = 0;
            }
        }

        for idx in 1..m {
            for jdx in 1..n {
                if obstacle_grid[idx][jdx] == 0 {
                    obstacle_grid[idx][jdx] =
                        obstacle_grid[idx - 1][jdx] + obstacle_grid[idx][jdx - 1];
                } else {
                    obstacle_grid[idx][jdx] = 0;
                }
            }
        }
        obstacle_grid[m - 1][n - 1]
    }
}

fn main() {
    println!("Hello, world!");
}
