#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_counts = {}

# Read stdin line by line
try:
    for i, line in enumerate(sys.stdin, start=1):
        # Parse the line using regex
        parts = line.split()
        if len(parts) < 7:
            continue

        ip_address = parts[0]
        date = parts[1][1:]
        status_code = parts[5]
        file_size = int(parts[6])

        # Update total file size
        total_size += file_size

        # Update status code counts
        if status_code.isdigit():
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

        # Print statistics every 10 lines
        if i % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys(), key=int):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print(f"\nTotal file size: {total_size}")
    for code in sorted(status_counts.keys(), key=int):
        print(f"{code}: {status_counts[code]}")

