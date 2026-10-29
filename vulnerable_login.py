# Demonstraion of an insecure login system.

USERNAME = "admin"
PASSWORD = "admin123"

def login(username, password):
    if username == USERNAME and password == PASSWORD:
        return "Login successful"
    return "Invalid username or password"

print(login("admin", "admin123"))
print(login("admin", "wrongpassword"))
