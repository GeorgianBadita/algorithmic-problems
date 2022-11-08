use std::collections::{HashMap, VecDeque};

struct Solution;

impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut degree = vec![0; num_courses as usize];

        for pair in prerequisites {
            let (first, last) = (pair[0], pair[1]);
            if graph.contains_key(&first) {
                graph.get_mut(&first).unwrap().push(last);
            } else {
                graph.insert(first, vec![last]);
            }
            degree[last as usize] += 1;
        }

        let mut queue = VecDeque::new();
        let mut nodes_in_topo = 0;

        for course in 0..num_courses {
            if degree[course as usize] == 0 {
                queue.push_back(course);
            }
        }
        while !queue.is_empty() {
            let node = queue.pop_front().unwrap();
            nodes_in_topo += 1;
            for &neighbour in graph.get(&node).unwrap_or(&Vec::new()) {
                degree[neighbour as usize] -= 1;
                if degree[neighbour as usize] == 0 {
                    queue.push_back(neighbour);
                }
            }
        }
        nodes_in_topo == num_courses
    }
}

fn main() {
    println!("Hello, world!");
}
