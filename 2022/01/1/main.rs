fn main() {
    let val = std::fs::read_to_string("input.txt")
        .unwrap()
        .split("\n\n")
        .map(|s| {
            s.split("\n")
                .map(|s| s.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .max()
        .unwrap();
    println!("{}", val);
}
