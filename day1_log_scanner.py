import datetime

# A list of log messages (like a real system would generate)
logs = [
    "INFO: Server started successfully",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "ERROR: File not found - config.json",
    "WARNING: Memory usage at 85%",
    "ERROR: Timeout after 30 seconds"
]

# Function that checks if a line is an error
def is_error(log_line):
    if "ERROR" in log_line:
        return True
    else:
        return False

# Function that scans all logs and returns only errors
def find_errors(log_list):
    errors = []
    for line in log_list:
        if is_error(line):
            errors.append(line)
    return errors

# Run it
today = datetime.date.today()
found = find_errors(logs)

print("=== Log Scan Report ===")
print("Date:", today)
print("Total logs scanned:", len(logs))
print("Errors found:", len(found))
print("")
print("--- Error Details ---")
for error in found:
    print(">>", error)
    # Count by type
def count_by_type(log_list):
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    for line in log_list:
        for key in counts:
            if key in line:
                counts[key] += 1
    return counts

summary = count_by_type(logs)
print("")
print("=== Summary ===")
for type_name, count in summary.items():
    print(f"{type_name}: {count} messages")``