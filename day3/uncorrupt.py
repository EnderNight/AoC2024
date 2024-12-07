#!/usr/bin/env python3

import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
p = re.compile(pattern)

with open("input.txt") as file:
    result = sum(
        [int(arg1) * int(arg2) for arg1, arg2 in p.findall(file.read())]
    )

    print(result)  # 183380722
