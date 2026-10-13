extern crate tracker;
use tracker::*;
#[test] fn legacy_boundary_and_state_machine() {
 assert_eq!(parse_legacy("usr_1","ord_1","alpha",true,None),Err("inconsistent legacy status"));
 assert_eq!(parse_legacy("usr_1","ord_1","alpha",false,Some("5")),Err("inconsistent legacy status"));
 assert_eq!(Timestamp::parse("bad"),Err("invalid timestamp"));
 assert_eq!(UserId::parse("ord_1"),Err("invalid user id"));
 assert_eq!(status_label(&parse_legacy("usr_1","ord_1","alpha",false,None).unwrap().status),"open");
 assert_eq!(status_label(&parse_legacy("usr_1","ord_1","alpha",true,Some("5")).unwrap().status),"done");
}
#[test] fn total_and_partial_result_operations() {
 assert_eq!(sum(&[]),0); assert_eq!(sum(&[3,4,-2]),5);
 assert_eq!(*head(&NonEmpty{first:7,rest:vec![9,11]}),7);
}
#[test] fn search_absence_and_presence() {
 let jobs=vec![Job::new(UserId::parse("usr_1").unwrap(),OrderId::parse("ord_1").unwrap(),"alpha".into()),Job::new(UserId::parse("usr_2").unwrap(),OrderId::parse("ord_2").unwrap(),"beta".into())];
 assert_eq!(search(&jobs,"missing"),Vec::<&Job>::new());
 assert_eq!(search(&jobs,"alpha").iter().map(|j|j.title.as_str()).collect::<Vec<_>>(),vec!["alpha"]);
}
#[test] fn revoke_after_parsing_then_reauthorize() {
 let user=UserId::parse("usr_1").unwrap(); let job=parse_legacy("usr_1","ord_1","alpha",false,None).unwrap();
 let mut tracker=Tracker::default(); tracker.grant(user.clone()); tracker.revoke(&user);
 assert_eq!(tracker.execute(job.clone()),Err("permission denied")); assert_eq!(tracker.jobs(),&[]);
 tracker.grant(user); assert_eq!(tracker.execute(job),Ok(()));
 assert_eq!(tracker.jobs().iter().map(|j|j.title.as_str()).collect::<Vec<_>>(),vec!["alpha"]);
}
#[test] fn concurrent_independent_publishers() {
 let root=std::path::Path::new("state"); std::fs::create_dir_all(root).unwrap(); let (mut indexer,mut metrics)=publishers(root);
 std::thread::scope(|s| { s.spawn(||{for i in 1..=1000 {indexer.publish(i).unwrap();}}); s.spawn(||{for i in 1..=700 {metrics.publish(i).unwrap();}}); });
 assert_eq!(report(root).unwrap(),"{\"indexer\":{\"indexed\":1000},\"metrics\":{\"processed\":700}}");
}
