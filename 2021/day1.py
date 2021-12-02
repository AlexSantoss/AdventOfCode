from helper import readStdin
depths = list(map(int, readStdin()))

#part 1
increased = [i for i, j in zip(depths, depths[1:]) if j > i]
print(len(increased))

#part 2
three_window = [sum(x) for x in zip(depths, depths[1:], depths[2:])]
increased = [i for i, j in zip(three_window, three_window[1:]) if j > i]
print(len(increased))
