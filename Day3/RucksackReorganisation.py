
input = open('Day3/input.txt')
for line in input:
    n = len(line)
    comp1 = line[0:n//2]
    comp2 = line[n//2:]
    print(set(comp1).intersection(comp2))