import sqlite3
import datetime

# Step 1: Create database and table
conn = sqlite3.connect("incidents.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        message TEXT,
        severity TEXT
    )
""")
conn.commit()

# Step 2: Create fake log file
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
# Step 3: Read log file
with open("system_logs.txt", "r") as f:
    logs = [line.strip() for line in f.readlines()]
    
# Step 4: Save errors to database
today = str(datetime.date.today())
saved = 0

for line in logs:
    if "ERROR" in line:
        cursor.execute("""
            INSERT INTO incidents (date, message, severity)
            VALUES (?, ?, ?)
        """, (today, line, "ERROR"))
        saved += 1
    elif "WARNING" in line:
        cursor.execute("""
            INSERT INTO incidents (date, message, severity)
            VALUES (?, ?, ?)
        """, (today, line, "WARNING"))
        saved += 1
conn.commit()
print(f"Saved {saved} incidents to database!")

# Step 5: Read back from database
print("")
print("=== Incidents in Database ===")
cursor.execute("SELECT id, date, severity, message FROM incidents")
rows = cursor.fetchall()

for row in rows:
    print(f"ID:{row[0]} | {row[1]} | {row[2]} | {row[3]}")

conn.close()