import string
items = list(string.ascii_lowercase + string.ascii_uppercase)
priorities = list(range(1,53))
sum = 0
#Read each line. Split line in half
input = open('Day3/input.txt')
for line in input:
    n = len(line)
    comp1 = str(line[0:n//2])
    comp2 = str(line[n//2:])
    match = str((set(comp1).intersection(comp2)))
    match = match.rstrip("'}")
    match = match.lstrip("{'")
    index = (items.index(match))
    sum = sum + priorities[index]
print('Part 1 - The sum of the priorities is:',sum)