file = open('Day 1/input.txt')
calories = list()
n = 0
for line in file:
    if line != '\n':
        n = n + int(line)
    if line == '\n':
        calories.append(n)
        n = 0
print('The most calories carried by a single Elf is: ',max(calories))

calories = sorted(calories, reverse=True)
top3 = sum(calories[0:3])
print('The total calories carried by the top 3 Elves is: ',top3)
