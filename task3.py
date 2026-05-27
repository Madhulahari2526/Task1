import re

try:
    # Open and read the input file
    with open("input.txt", "r") as file:
        content = file.read()

    # Email pattern
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Find emails
    emails = re.findall(email_pattern, content)

    # Save emails to another file
    with open("emails.txt", "w") as output_file:
        for email in emails:
            output_file.write(email + "\n")

    print("✅ Email addresses extracted successfully!")
    print("\n📧 Found Emails:")

    for email in emails:
        print(email)

except FileNotFoundError:
    print("❌ input.txt file not found!")
    print("Please create input.txt in the same folder as your Python script.")
    