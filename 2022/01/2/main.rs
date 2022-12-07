fn main() {
    let mut data: Vec<u32> = std::fs::read_to_string("2022/01/input.txt")
        .unwrap()
        .split("\n\n")
        .map(|s| s.split('\n').map(|s| s.parse::<u32>().unwrap()).sum())
        .collect();

    data.sort_unstable();
    data.reverse();

    let val = data[..3].iter().sum::<u32>();
    println!("{}", val);
}
