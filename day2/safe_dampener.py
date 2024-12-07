#!/usr/bin/env python3


def is_sorted(li: list) -> bool:
    return all(li[i] <= li[i + 1] for i in range(len(li) - 1))


def is_safe(line: [int]) -> bool:
    if not is_sorted(line):
        if not is_sorted(list(reversed(line))):
            return False

    diffs = [abs(line[i] - line[i + 1]) for i in range(len(line) - 1)]

    return all([level >= 1 and level <= 3 for level in diffs])


with open("input.txt") as file:
    safe_reports = 0

    for line in file:
        report = [int(level) for level in line.split()]

        if is_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                trunkated_report = report.copy()
                trunkated_report.pop(i)
                if is_safe(trunkated_report):
                    safe_reports += 1
                    break

    print(safe_reports)  # 381
