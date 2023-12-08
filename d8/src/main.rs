use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;
use num::Integer;
use num::integer::lcm;
fn main() {
    let filecontents = std::fs::read_to_string("./d8.real.input").expect("error reading file");
    let lines = filecontents
        .lines()
        .map(|s| s.to_string())
        .collect::<Vec<String>>();
    let directions = &lines[0].chars().collect::<Vec<char>>();
    let maps: Vec<(String, String, String)> = lines[2..]
        .iter()
        .map(|s| {
            (
                s[0..3].to_string(),
                s[7..10].to_string(),
                s[12..15].to_string(),
            )
        })
        .collect::<Vec<(String, String, String)>>();

    

    let forward_map = HashMap::<String, (String, String)>::from(
        maps.iter()
            .map(|(a, b, c)| (a.to_string(), (b.to_string(), c.to_string())))
            .collect::<HashMap<String, (String, String)>>(),
    );

    let all_a = forward_map
        .keys()
        .filter(|k| k.ends_with("A"))
        .collect::<Vec<&String>>();

    let mut lowest_common_multiple = 1;
    for mut a in all_a {
        let mut dist = 0;
        let mut total_dist = 0;
        loop {
            if a.ends_with('Z') {
                break;
            }
            let (b, c) = &forward_map.get(a).unwrap();
            // println!("{} {} {}", a, b, c);
            if directions[dist] == 'L' {
                a = b;
            } else {
                a = c;
            }
            // println!("{}", a);
            total_dist = total_dist + 1;
            dist = total_dist % directions.len();
        }

        lowest_common_multiple = lowest_common_multiple.lcm(&(total_dist as i64));

        println!("{:?}", total_dist);
    }

    println!("{:?}", lowest_common_multiple);


    // loop {
    //     if a == "ZZZ" {
    //         break;
    //     }
    //     let (b, c) = &forward_map.get(&a).unwrap();
    //     println!("{} {} {}", a, b, c);
    //     if directions[dist] == 'L' {
    //         a = b.to_string();
    //     } else {
    //         a = c.to_string();
    //     }
    //     println!("{}", a);
    //     total_dist = total_dist + 1;
    //     dist = total_dist % directions.len();
    // }

}
