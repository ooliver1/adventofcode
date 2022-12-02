# fmt: off
print((lambda nums: sum(1 for i, n in enumerate(nums) if i != 0 and i < len(nums) - 2 and (n + int(nums[i + 1]) + int(nums[i + 2])) > (int(nums[i - 1]) + n + int(nums[i + 1]))))([int(x) for x in open("input.txt").readlines()]))
