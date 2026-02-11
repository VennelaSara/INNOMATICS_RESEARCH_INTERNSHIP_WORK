"""
Data Science Internship – February 2026
Logic Building Task – 1

NOTE:
Below each task you will find:
✔ Possible Inputs
✔ Expected Outputs
written clearly as comments for evaluation reference.
"""


# ============================================================
# 1️⃣ USER LOGIN CHECK
# ============================================================

def check_login(username, password):

    stored_username = "admin"
    stored_password = "1234"

    print("\n========== USER LOGIN CHECK ==========")

    if username == stored_username and password == stored_password:
        print("Login Successful")
    else:
        print("Invalid Credentials")


# ---------------- POSSIBLE INPUTS & OUTPUTS ----------------
# Input: username="admin", password="1234"
# Output:
# Login Successful
#
# Input: username="admin", password="0000"
# Output:
# Invalid Credentials
#
# Input: username="user", password="1234"
# Output:
# Invalid Credentials
#
# Input: username="user", password="pass"
# Output:
# Invalid Credentials
# -----------------------------------------------------------



# ============================================================
# 2️⃣ PASS / FAIL ANALYZER
# ============================================================

def analyze_results(marks):

    pass_students = 0
    fail_students = 0

    print("\n========== PASS / FAIL ANALYZER ==========")

    for score in marks:
        if score >= 50:
            pass_students += 1
        else:
            fail_students += 1

    print("Total Students Passed :", pass_students)
    print("Total Students Failed :", fail_students)


# ---------------- POSSIBLE INPUTS & OUTPUTS ----------------
# Input: [45, 78, 90, 33, 60]
# Output:
# Total Students Passed : 3
# Total Students Failed : 2
#
# Input: [10, 20, 30]
# Output:
# Total Students Passed : 0
# Total Students Failed : 3
#
# Input: [50, 50, 50]
# Output:
# Total Students Passed : 3
# Total Students Failed : 0
#
# Input: []
# Output:
# Total Students Passed : 0
# Total Students Failed : 0
# -----------------------------------------------------------



# ============================================================
# 3️⃣ SIMPLE DATA CLEANER
# ============================================================

def clean_user_names(names):

    cleaned_names = []

    print("\n========== SIMPLE DATA CLEANER ==========")

    for name in names:
        processed_name = name.strip().lower()
        cleaned_names.append(processed_name)

    print("Cleaned Names List :", cleaned_names)


# ---------------- POSSIBLE INPUTS & OUTPUTS ----------------
# Input: [" Alice ", "bob", " CHARLIE "]
# Output:
# Cleaned Names List : ['alice', 'bob', 'charlie']
#
# Input: ["  RAM  ", "  SITA"]
# Output:
# Cleaned Names List : ['ram', 'sita']
#
# Input: ["john"]
# Output:
# Cleaned Names List : ['john']
#
# Input: []
# Output:
# Cleaned Names List : []
# -----------------------------------------------------------



# ============================================================
# 4️⃣ MESSAGE LENGTH ANALYZER
# ============================================================

def analyze_messages(messages):

    print("\n========== MESSAGE LENGTH ANALYZER ==========")

    for message in messages:
        msg_length = len(message)

        print(f"Message: '{message}'")
        print(f"Length : {msg_length}")

        if msg_length > 10:
            print("Flag: Message longer than 10 characters")

        print("-" * 30)


# ---------------- POSSIBLE INPUTS & OUTPUTS ----------------
# Input: ["Hi", "Welcome to the platform", "OK"]
# Output:
# Message: 'Hi'
# Length : 2
#
# Message: 'Welcome to the platform'
# Length : 23
# Flag: Message longer than 10 characters
#
# Message: 'OK'
# Length : 2
#
#
# Input: ["HelloWorld!"]
# Output:
# Message: 'HelloWorld!'
# Length : 11
# Flag: Message longer than 10 characters
#
# Input: []
# Output:
# (No messages printed)
# -----------------------------------------------------------



# ============================================================
# 5️⃣ ERROR MESSAGE DETECTOR
# ============================================================

def detect_errors(logs):

    error_count = 0

    print("\n========== ERROR MESSAGE DETECTOR ==========")

    for entry in logs:
        if entry == "ERROR":
            error_count += 1

    print("Total ERROR entries found :", error_count)


# ---------------- POSSIBLE INPUTS & OUTPUTS ----------------
# Input: ["INFO", "ERROR", "WARNING", "ERROR"]
# Output:
# Total ERROR entries found : 2
#
# Input: ["INFO", "WARNING"]
# Output:
# Total ERROR entries found : 0
#
# Input: ["ERROR", "ERROR", "ERROR"]
# Output:
# Total ERROR entries found : 3
#
# Input: []
# Output:
# Total ERROR entries found : 0
# -----------------------------------------------------------



# ============================================================
# 🚀 MAIN EXECUTION
# ============================================================

if __name__ == "__main__":

    check_login("admin", "1234")

    marks = [45, 78, 90, 33, 60]
    analyze_results(marks)

    names = [" Alice ", "bob", " CHARLIE "]
    clean_user_names(names)

    messages = ["Hi", "Welcome to the platform", "OK"]
    analyze_messages(messages)

    logs = ["INFO", "ERROR", "WARNING", "ERROR"]
    detect_errors(logs)
