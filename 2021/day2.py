from helper import readStdin
commands = [line.split() for line in readStdin()]

#part 1
horizontal = 0
depth = 0
for c in commands:
    if c[0] == 'forward': horizontal += int(c[1])
    elif c[0] == 'down': depth +=  int(c[1])
    elif c[0] == 'up': depth -= int(c[1])
print(horizontal * depth)

#part 2
horizontal = 0
depth = 0
aim = 0
for c in commands:
    if c[0] == 'forward':
        horizontal += int(c[1])
        depth += aim*int(c[1])
    elif c[0] == 'down': aim +=  int(c[1])
    elif c[0] == 'up': aim -= int(c[1])
print(horizontal * depth)
