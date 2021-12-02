from helper import readStdin
commands = [line.split() for line in readStdin()]

#part 1
depth = horizontal = 0
for c in commands:
    if c[0] == 'forward': horizontal += int(c[1])
    else: depth += int(c[1]) if c[0] == 'down' else -int(c[1])
print(horizontal * depth)

#part 2
aim = depth = horizontal = 0
for c in commands:
    if c[0] == 'forward':
        horizontal += int(c[1])
        depth += aim*int(c[1])
    else: aim += int(c[1]) if c[0] == 'down' else -int(c[1])
print(horizontal * depth)
