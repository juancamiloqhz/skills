extern crate tracker;
use tracker::*;
fn main() { Job::new(OrderId::parse("ord_1").unwrap(),UserId::parse("usr_1").unwrap(),"bad".into()); }
