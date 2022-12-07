use phf::phf_map;

static ITEMS: phf::Map<&str, i8> = phf_map! {
    "A" => 1,
    "B" => 2,
    "C" => 3,
};

fn main() {
    let val: i32 = std::fs::read_to_string("input.txt")
        .unwrap()
        .split('\n')
        .map(|r| {
            let (opponent, outcome) = r.split_once(' ').unwrap();
            let opponent_score = ITEMS.get(opponent).unwrap();

            if outcome == "X" {
                if *opponent_score > 1 {
                    opponent_score - 1
                } else {
                    3
                }
            } else if outcome == "Y" {
                opponent_score + 3
            } else if *opponent_score < 3 {
                opponent_score + 7
            } else {
                7
            }
        })
        .map(i32::from)
        .sum();

    println!("{}", val);
}
