#!/usr/bin/python3

import sys

def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split(" ")
    if len(parts) >= 9:
        return int(parts[-1])
    return 0

def update_status_codes(status_codes, line):
    parts = line.split(" ")
    if len(parts) >= 9 and parts[-2].isnumeric():
        code = int(parts[-2])
        status_codes[code] = status_codes.get(code, 0) + 1

def main():
    try:
        total_size = 0
        status_codes = {}
        line_count = 0

        for line in sys.stdin:
            line_count += 1
            total_size += parse_line(line)
            update_status_codes(status_codes, line)

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
