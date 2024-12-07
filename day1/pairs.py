#!/usr/bin/env python3

with open("input.txt", "r") as file:
    group1 = []
    group2 = []

    for line in file:
        ids = line.split()

        group1.append(int(ids[0]))
        group2.append(int(ids[1]))

    group1.sort()
    group2.sort()

    distances = [abs(id1 - id2) for id1, id2 in zip(group1, group2)]

    total_dist = sum(distances)

    print(total_dist)  # 2086478
