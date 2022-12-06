fn main() {
    let mut data = std::fs::read_to_string("input.txt")
        .unwrap()
        .split("\n\n")
        .map(|s| {
            s.split("\n")
                .map(|s| s.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect::<Vec<_>>();
    data.sort_unstable();
    data.reverse();

    let val = data[..3].iter().sum::<u32>();
    println!("{}", val);
}
