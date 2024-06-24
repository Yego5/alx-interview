#!/usr/bin/python3
import sys
import signal
import re

# Global variables to keep track of the total file size and status code counts
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to match the input format
log_regex = re.compile(r'^\d+\.\d+\.\d+\.\d+ - \[\d+-\d+-\d+ \d+:\d+:\d+\.\d+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

def print_statistics():
    """Prints the statistics of the log parsing."""
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_regex.match(line.strip())
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics()
except Exception as e:
    sys.stderr.write(f"Error: {e}\n")
finally:
    print_statistics()
#!/usr/bin/python3
import sys
import signal
import re

# Global variables to keep track of the total file size and status code counts
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to match the input format
log_regex = re.compile(r'^\d+\.\d+\.\d+\.\d+ - \[\d+-\d+-\d+ \d+:\d+:\d+\.\d+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

def print_statistics():
    """Prints the statistics of the log parsing."""
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_regex.match(line.strip())
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics()
except Exception as e:
    sys.stderr.write(f"Error: {e}\n")
finally:
    print_statistics()
