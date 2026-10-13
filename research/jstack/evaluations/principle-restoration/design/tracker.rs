use std::{collections::HashSet, fs, path::Path};
#[derive(Clone, Debug, PartialEq, Eq, Hash)] pub struct UserId(String);
#[derive(Clone, Debug, PartialEq, Eq)] pub struct OrderId(String);
impl UserId { pub fn parse(s: &str) -> Result<Self, &'static str> { if s.starts_with("usr_") && s.len()>4 { Ok(Self(s.into())) } else { Err("invalid user id") } } }
impl OrderId { pub fn parse(s: &str) -> Result<Self, &'static str> { if s.starts_with("ord_") && s.len()>4 { Ok(Self(s.into())) } else { Err("invalid order id") } } }
#[derive(Clone, Debug, PartialEq, Eq)] pub struct Timestamp(u64);
impl Timestamp { pub fn parse(s: &str) -> Result<Self, &'static str> { s.parse::<u64>().map(Self).map_err(|_| "invalid timestamp") } }
#[derive(Clone, Debug, PartialEq, Eq)] pub enum Status { Open, Done { at: Timestamp } }
#[derive(Clone, Debug, PartialEq, Eq)] pub struct Job { pub owner: UserId, pub order: OrderId, pub title: String, pub status: Status, pub result: i64 }
impl Job {
 pub fn new(owner: UserId, order: OrderId, title: String) -> Self { Self { owner, order, title, status: Status::Open, result: 0 } }
}
pub fn parse_legacy(owner: &str, order: &str, title: &str, completed: bool, at: Option<&str>) -> Result<Job, &'static str> {
 let status = match (completed, at) { (false,None)=>Status::Open, (true,Some(s))=>Status::Done { at:Timestamp::parse(s)? }, _=>return Err("inconsistent legacy status") };
 Ok(Job { owner:UserId::parse(owner)?, order:OrderId::parse(order)?, title:title.into(), status, result:0 })
}
pub fn status_label(s:&Status)-> &'static str { match s { Status::Open=>"open", Status::Done {..}=>"done" } }
pub struct NonEmpty<T> { pub first:T, pub rest:Vec<T> }
pub fn head<T>(xs:&NonEmpty<T>)->&T { &xs.first }
pub fn sum(xs:&[i64])->i64 { xs.iter().sum() }
pub fn search<'a>(jobs:&'a [Job], query:&str)->Vec<&'a Job> { jobs.iter().filter(|j|j.title.contains(query)).collect() }
// Permissions are live authority state, not a timeless property of parsed input.
// &mut self makes this single-process operation exclusive across checking and mutation.
#[derive(Default)] pub struct Tracker { allowed: HashSet<UserId>, jobs: Vec<Job> }
impl Tracker {
 pub fn grant(&mut self, user:UserId) { self.allowed.insert(user); }
 pub fn revoke(&mut self, user:&UserId) { self.allowed.remove(user); }
 pub fn execute(&mut self, job:Job)->Result<(), &'static str> { if !self.allowed.contains(&job.owner) { return Err("permission denied"); } self.jobs.push(job); Ok(()) }
 pub fn jobs(&self)->&[Job] { &self.jobs }
}
pub struct IndexerPublisher<'a> { root: &'a Path }
pub struct MetricsPublisher<'a> { root: &'a Path }
// Split ownership once. Each actor's public interface writes only its own artifact.
pub fn publishers(root:&Path)->(IndexerPublisher<'_>, MetricsPublisher<'_>) { (IndexerPublisher{root},MetricsPublisher{root}) }
impl IndexerPublisher<'_> { pub fn publish(&mut self, n:u64)->std::io::Result<()> { fs::write(self.root.join("indexer.tmp"),format!("{{\"indexed\":{n}}}"))?; fs::rename(self.root.join("indexer.tmp"),self.root.join("indexer.json")) } }
impl MetricsPublisher<'_> { pub fn publish(&mut self, n:u64)->std::io::Result<()> { fs::write(self.root.join("metrics.tmp"),format!("{{\"processed\":{n}}}"))?; fs::rename(self.root.join("metrics.tmp"),self.root.join("metrics.json")) } }
pub fn report(root:&Path)->std::io::Result<String> { Ok(format!("{{\"indexer\":{},\"metrics\":{}}}",fs::read_to_string(root.join("indexer.json"))?,fs::read_to_string(root.join("metrics.json"))?)) }
