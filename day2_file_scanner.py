import datetime

# Step 1: Create the log file
with open("system_logs.txt", "w") as f:
    f.write("INFO: Server started successfully\n")
    f.write("ERROR: Database connection failed\n")
    f.write("INFO: User logged in\n")
    f.write("ERROR: File not found - config.json\n")
    f.write("WARNING: Memory usage at 85%\n")
    f.write("ERROR: Timeout after 30 seconds\n")
    f.write("INFO: Backup completed\n")
    f.write("WARNING: Disk space below 20%\n")
    f.write("ERROR: Authentication failed for user admin\n")
    f.write("INFO: Scheduled task completed\n")

# Step 2: Read the file
with open("system_logs.txt", "r") as f:
    logs = f.readlines()

# Step 3: Clean each line (remove \n at end)
logs = [line.strip() for line in logs]

# Step 4: Scan for errors
def find_errors(log_list):
    errors = []
    for line in log_list:
        if "ERROR" in line:
            errors.append(line)
    return errors

# Step 5: Count by type
def count_by_type(log_list):
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    for line in log_list:
        for key in counts:
            if key in line:
                counts[key] += 1
    return counts

# Step 6: Print report
today = datetime.date.today()
errors = find_errors(logs)
summary = count_by_type(logs)

print("=== Automated Log Scan Report ===")
print("Date:", today)
print("File: system_logs.txt")
print("Total lines scanned:", len(logs))
print("")
print("--- Summary ---")
for type_name, count in summary.items():
    print(f"{type_name}: {count}")
print("")
print("--- Errors Found ---")
for error in errors:
    print(">>", error)