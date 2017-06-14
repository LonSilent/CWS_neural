data_path = '../very_small.txt'

with open(data_path) as f:
    for line in f:
        line = line.strip()
        line = [x for x in line if x != ' ']
        print(line)