import bcrypt

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    return bcrypt.checkpw(password_bytes, hashed_password.encode("utf-8"))


def main() -> None:
    password = input("Enter password : ").strip()
    hashed_password = hash_password(password)

    print("\nOriginal Password :", password)
    print("\nHashed Password :")
    print(hashed_password)

    user_pass = input("enter password again :").strip()

    if verify_password(user_pass, hashed_password):
        print("Login Success")
    else:
        print("wrong password")


if __name__ == "__main__":
    main()