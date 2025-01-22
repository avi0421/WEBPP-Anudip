# Q2: Extract the domain part (after '@') from each email address.

# List of email addresses
emails = [
    "alice@example.com",
    "bob@eg.org",
    "charlie@secure.com"
]

# Extract the domain part of each email
domains = [email.split('@')[1] for email in emails]

# Print the result
print(domains)
