def register():
    u = input("Username: ")
    p = input("Password: ")
    role = input("Role (admin/patient): ")
    users[u] = (encrypt(p), role)
    print("Registered successfully!")

def login():
    u = input("Username: ")
    p = input("Password: ")
    if u in users and users[u][0] == encrypt(p):
        print("Login successful!")
        return u, users[u][1]
    else:
        print("Login failed!")
        return None, None