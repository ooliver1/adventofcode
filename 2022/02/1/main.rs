use phf::phf_map;

// i8 so the use below can subtract.
static ITEMS: phf::Map<&str, i8> = phf_map! {
    "A" => 1,
    "B" => 2,
    "C" => 3,

    "X" => 1,
    "Y" => 2,
    "Z" => 3,
};

fn main() {
    let val: i32 = std::fs::read_to_string("input.txt")
        .unwrap()
        .split('\n')
        .map(|r| {
            let (opponent, me) = r.split_once(' ').unwrap();
            let opponent_score = ITEMS.get(opponent).unwrap();
            let my_score = ITEMS.get(me).unwrap();
            if my_score == opponent_score {
                my_score + 3
            } else if *my_score == opponent_score + 1 || *my_score == opponent_score - 2 {
                my_score + 6
            } else {
                *my_score
            }
        })
        .map(i32::from)
        .sum();

    println!("{}", val);
}
