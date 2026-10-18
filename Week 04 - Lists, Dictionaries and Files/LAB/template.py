"""
RECORD CHECK  -  my version
===========================

Name  : Al Maseera Jahangir
Lane  :  AI       (delete two)
Date  :18/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Calculates the difference, percentage, and status of a record."""
    difference = limit - value
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, difference, percent, status):
    """Prints the report for one record."""
    print(f"{label}: {status}")
    print(f"Difference: {difference}")
    print(f"Percent: {percent:.1f}%")

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

 
def load_records(path):
    records = []

    try:
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")

                rec = {
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                }

                records.append(rec)

    except FileNotFoundError:
        print(f"{path} not found")
        return []

    return records


records = load_records("records_sample.txt")


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_count = 0

with open("results.txt", "w") as f:
    for rec in records:
        difference, percent, status = check_record(
            rec["value"], rec["limit"]
        )

        print_report(
            rec["label"], difference, percent, status
        )

        if status == "OVER LIMIT":
            over_count += 1

        f.write(rec["label"] + "," + status + "\n")

print(f"{over_count} of {len(records)} were over limit")


with open("results.txt") as f:
    print(f.read())

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
