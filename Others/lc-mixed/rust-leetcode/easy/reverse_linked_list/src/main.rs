use std::mem::replace;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
      let (mut prev, mut head) = (None, head.clone());
      while let Some(mut node) = head {
          head = replace(&mut node.next, prev);
          prev = Some(node);
      }
      prev
    }
}

fn main() {
    println!("Hello, world!");
}
