#!/usr/bin/python3

"""
Reads stdin line by line and computes metrics
"""

import sys


def parse_line(line):
    """
    Parses a line in the specified format and extraxcts relevant info

    Returns:
        Tuple (status_code, file_size) or None if the line format is invalid.
    """
    try:
        _, _, request, status_code, file_size = line.split()
        if request != '"GET /projects/260 HTTP/1.1"':
            return None
        return int(status_code), int(file_size)
    except ValueError:
        return None


def print_metrics(total_size, status_counts):
    """
    Prints the computed metrics
    """
    print("File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
    print()


def main():
    """
    Main function to compute metrics from stdin
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 402: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed = parse_line(line)
            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_metrics(total_size, status_counts)
        sys.exit(0)
    except BrokenPipeError:
        sys.stderr.write("Broken pipe error. Exiting gracefully.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
