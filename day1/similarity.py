#!/usr/bin/env python3

with open("input.txt", "r") as file:
    group1 = []
    group2 = []

    for line in file:
        ids = line.split()

        group1.append(int(ids[0]))
        group2.append(int(ids[1]))

    histo = {}

    for id in group2:
        if id not in histo:
            histo[id] = 1
        else:
            histo[id] += 1

    mults = [id * (histo[id] if id in histo else 0) for id in group1]

    score = sum(mults)

    print(score)  # 24941624
