import bcrypt

def get_hashed_password(password: str) -> bytes:
    pwd = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd, salt)

    print(salt)
    print(hashed.decode("utf-8"))
    return hashed


password1 = get_hashed_password("Lyceum1")
password2 = get_hashed_password("Lyceum1")
check_password = bytes("Lyceum1", "utf-8")

print(bcrypt.checkpw(check_password, password1))
print(bcrypt.checkpw(check_password, password2))


