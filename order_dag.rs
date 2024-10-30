use std::collections::{HashMap, HashSet, VecDeque};
use std::io;

fn topological_sort() -> Result<Vec<u8>, String> {
    // parse file into adjacency list
    let lines = io::stdin().lines();
    let mut adj_list: HashMap<u8, Vec<u8>> = HashMap::new();
    let mut indegree_count: HashMap<u8, u8> = HashMap::new();
    let mut all_nodes: HashSet<u8> = HashSet::new();

    for line in lines {
        let l = line.expect("cannot get line");
        let temp: Vec<&str> = l.split("->").map(str::trim).collect();
        let start = temp[0].parse::<u8>().expect("cannot get start");
        all_nodes.insert(start);
        let mut ends: Vec<u8> = temp[1].split(",").map(|x| x.parse::<u8>().unwrap()).collect();
        let mut ends_dup: Vec<u8> = ends.iter().copied().collect();
        adj_list.entry(start).or_default().append(&mut ends_dup);
        for end in ends {
            *indegree_count.entry(end).or_default() += 1; // if v has zero incoming edges from the start, it doesn't get into indegree_count
            all_nodes.insert(end);
        }
    }

    let mut sorted: Vec<u8> = Vec::new();
    // initialized queue contains all nodes with indegree_count == 0
    let mut queue: VecDeque<u8> = all_nodes.into_iter().filter(|x| !indegree_count.contains_key(x)).collect();
    while let Some(node) = queue.pop_front() {
        sorted.push(node);
        // update indegree count
        if let Some(connected_nodes) = adj_list.get(&node) {
            for v in connected_nodes.iter() {
                *indegree_count.get_mut(v).unwrap() -= 1;
                if indegree_count.get(v).unwrap() == &0 {
                    queue.push_back(v.clone());
                    indegree_count.remove(v);
                }
            }
        }
    }
    Ok(sorted)
}

fn main() {
    match topological_sort() {
        Ok(sorted) => println!("{sorted:?}"),
        Err(e) => eprintln!("Error: {}", e)
    }
}
