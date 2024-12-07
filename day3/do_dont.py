#!/usr/bin/env python3

import re


pattern = r"(do\(\))|(don't\(\))|mul\((?P<arg1>\d{1,3}),(?P<arg2>\d{1,3})\)"
p = re.compile(pattern)


with open("input.txt") as file:
    matches = p.findall(file.read())

    enabled = True
    result = 0

    for match in matches:
        if match[0] != "":
            enabled = True
        elif match[1] != "":
            enabled = False
        elif enabled:
            result += int(match[2]) * int(match[3])

    print(result)  # 82733683
