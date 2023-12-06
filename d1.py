

total = 0
with open("d1.input") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("zero", "zero0zero")
        line = line.replace("one", "one1one")
        line = line.replace("two", "two2two")
        line = line.replace("three", "three3three")
        line = line.replace("four", "four4three")
        line = line.replace("five", "five5five")
        line = line.replace("six", "six6six")
        line = line.replace("seven", "seven7seven")
        line = line.replace("eight", "eight8eight")
        line = line.replace("nine", "nine9nine")

        nums = (list(filter(lambda x: x in "0123456789", line)))
        total += int(nums[0]) * 10 + int(nums[-1])

print(total)
