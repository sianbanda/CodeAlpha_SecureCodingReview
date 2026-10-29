import bcrypt

def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

def verify_login(username, password, stored_username, stored_hash):
    if username != stored_username:
        return False
    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash
    )

#demonstration only
demo_username = "student"
demo_password_hash = hash_password("demo-password")
print(
    "Correct password:",
    verify_login(
        "student", "demo-password",
        demo_username, demo_password_hash
    )
)
print(
    "Wrong password:",
    verify_login(
        "student", "wrong-password",
        demo_username, demo_password_hash
    )
)
