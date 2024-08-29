Here's a brief README for your log parsing script:

---

# Log Parsing Script

## Description

This Python script reads log data from standard input (`sys.stdin`), processes it to extract HTTP status codes and file sizes, and outputs the cumulative statistics. It is designed to display the total file size and the count of specific HTTP status codes every 10 lines of input and at the end of the input.

## Usage

To run the script, use the following command in a Unix-based environment (Linux, macOS, etc.) where logs are piped into the script:

```bash
cat your_log_file.log | ./log_parsing.py
```

Alternatively, you can run it directly in interactive mode and manually input log entries, finishing with `Ctrl+D` to signal the end of input.

## Output

The script outputs:
- The cumulative file size of all processed log entries.
- The count of HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).

The output is displayed after every 10 lines of input and once more when all input has been processed.

## Dependencies

- Python 3

## Notes

- Ensure the script is executable by running `chmod +x log_parsing.py`.
- The script assumes log entries are formatted with specific HTTP request details and timestamps. Modify the regular expression in the script if the log format differs.

##Example Log Format

A valid log entry should look like this:

```
123.45.67.89 - [2024-08-29 12:34:56.789] "GET /projects/260 HTTP/1.1" 200 1234
```

This script will correctly parse and tally the status code (`200`) and file size (`1234`) from such entries.


This README provides an overview of how to use the script, what it outputs, its dependencies, and other essential details.
