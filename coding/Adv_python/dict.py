# List of users
users = [
    {"name": "Alice", "email": "alice@example.com", "active": True},
    {"name": "Bob", "email": "bob@example.com", "active": False},
    {"name": "Charlie", "email": "charlie@example.com", "active": True}
]

# Get the email addresses of active users
active_email = [x['email'] for x in users if x['active']]

# Print the result
print(active_email)
