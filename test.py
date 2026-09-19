import os

# 1. Get your logged-in username
print(f"User: {os.getlogin()}")

# 2. Get all Environment Variables (like PATH)
# This returns a dictionary of system settings
print(os.environ.get('PATH'))

# 3. Check if a specific file exists before you try to open it
if os.path.exists("test.txt"):
    print("File found!")
else:
    print("File not found.")