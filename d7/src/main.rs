use std::{cmp::Ordering, collections::HashMap};

#[derive(Debug, Copy, Clone)]
enum Hand {
    HighCard([u8; 5]),
    Pair([u8; 5]),
    TwoPair([u8; 5]),
    ThreeOfAKind([u8; 5]),
    FullHouse([u8; 5]),
    FourOfAKind([u8; 5]),
    FiveOfAKind([u8; 5]),
}

impl Hand {
    fn type_(self) -> &'static str {
        match self {
            Hand::HighCard(_) => "high card",
            Hand::Pair(_) => "pair",
            Hand::TwoPair(_) => "two pair",
            Hand::ThreeOfAKind(_) => "three of a kind",
            Hand::FullHouse(_) => "full house",
            Hand::FourOfAKind(_) => "four of a kind",
            Hand::FiveOfAKind(_) => "five of a kind",
        }
    }

    fn rank(self) -> u8 {
        match self {
            Hand::HighCard(_) => 0,
            Hand::Pair(_) => 1,
            Hand::TwoPair(_) => 2,
            Hand::ThreeOfAKind(_) => 3,
            Hand::FullHouse(_) => 4,
            Hand::FourOfAKind(_) => 5,
            Hand::FiveOfAKind(_) => 6,
        }
    }

    fn cards(self) -> [u8; 5] {
        match self {
            Hand::HighCard(cards) => cards,
            Hand::Pair(cards) => cards,
            Hand::TwoPair(cards) => cards,
            Hand::ThreeOfAKind(cards) => cards,
            Hand::FullHouse(cards) => cards,
            Hand::FourOfAKind(cards) => cards,
            Hand::FiveOfAKind(cards) => cards,
        }
    }

    fn compare(self, other: Hand) -> bool {
        if &self.type_() != &other.type_() {
            self.rank() > other.rank()
        } else {
            let self_cards = self.cards();
            let other_cards = other.cards();

            if self_cards[1 - 1] != other_cards[1 - 1] {
                self_cards[1 - 1] > other_cards[1 - 1]
            } else if self_cards[2 - 1] != other_cards[2 - 1] {
                self_cards[2 - 1] > other_cards[2 - 1]
            } else if self_cards[3 - 1] != other_cards[3 - 1] {
                self_cards[3 - 1] > other_cards[3 - 1]
            } else if self_cards[4 - 1] != other_cards[4 - 1] {
                self_cards[4 - 1] > other_cards[4 - 1]
            } else {
                self_cards[5 - 1] > other_cards[5 - 1]
            }
        }
    }

    fn from_str(s: &str) -> Hand {
        println!("{}", s);
        let mut cards: Vec<u8> = s
            .chars()
            .map(|x| match x {
                'A' => 14,
                'T' => 10,
                'J' => 1,
                'Q' => 12,
                'K' => 13,
                _ => x.to_digit(10).unwrap() as u8,
            })
            .collect();
        let mut counts: HashMap<u8, u8> = HashMap::new();
        for card in cards.iter() {
            if card != &1 {
                let count = counts.entry(*card).or_insert(0);
                *count += 1;
            }
        }
        let max = cards.iter().max().unwrap();
        if *max == 1 {
            return Hand::FiveOfAKind(cards.as_slice().try_into().unwrap());
        } 

        println!("{:?}", max);

        let maximum_count = counts.iter().max_by_key(|x| x.1).unwrap();

        counts.insert(*maximum_count.0, maximum_count.1 + cards.iter().filter(|x| x == &&1).count() as u8);
        let counts: Vec<(u8, u8)> = counts.into_iter().collect();
        println!("{:?}", counts);
        match counts.len() {
            1 => Hand::FiveOfAKind(cards.as_slice().try_into().unwrap()),
            2 => {
                if counts.iter().any(|x| x.1 == 4) {
                    Hand::FourOfAKind(cards.as_slice().try_into().unwrap())
                } else {
                    Hand::FullHouse(cards.as_slice().try_into().unwrap())
                }
            }
            3 => {
                if counts.iter().any(|x| x.1 == 3) {
                    Hand::ThreeOfAKind(cards.as_slice().try_into().unwrap())
                } else {
                    Hand::TwoPair(cards.as_slice().try_into().unwrap())
                }
            }
            4 => Hand::Pair(cards.as_slice().try_into().unwrap()),
            5 => Hand::HighCard(cards.as_slice().try_into().unwrap()),
            _ => panic!("Invalid hand"),
        }
    }
}

fn main() {
    let filecontents = std::fs::read_to_string("../d7.real.input").expect("error reading file");
    let mut hands: Vec<(Hand, u32)> = filecontents
        .lines()
        .map(|line| {
            let mut cards = line.split_whitespace();
            let hand = Hand::from_str(cards.next().unwrap());
            let bid = cards.next().unwrap().parse::<u32>().unwrap();
            (hand, bid)
        })
        .collect();

    // let mut hands = vec![
    //     (Hand::from_str("KKKKK"), 10),
    //     (Hand::from_str("AAAAA"), 9),
    //     (Hand::from_str("KKKKA"), 8),
    //     (Hand::from_str("KAAAA"), 7),
    //     (Hand::from_str("KKKAA"), 6),
    //     (Hand::from_str("KKAAA"), 5),
    //     (Hand::from_str("KKAAT"), 4),
    //     (Hand::from_str("KKTTA"), 3),
    // ];

    hands.sort_by(|a, b| {
        if b.0.compare(a.0) {
            Ordering::Greater
        } else {
            Ordering::Less
        }
    });
    println!("{:?}", hands);
    let len = *(&hands.len()) as u32;
    let mut total = 0;
    for (i, hand) in hands.iter().enumerate() {
        total += hand.1 * (len - (i as u32));
        println!("{} * {} = ", hand.1, len - (i as u32));
    }
    println!("{}", total);

    // println!("KKKAA: {:?}", Hand::from_str("KKKAA").rank());
    // println!("KKKKA: {:?}", Hand::from_str("KKKKA").rank());
    println!(
        "A555J vs AJAA3: {:?}",
        Hand::from_str("A555J").compare(Hand::from_str("AJAA3"))
    );
}
