import pandas as pd

def add_profile(u):
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    df = pd.DataFrame([[u, name, age, gender]],
                      columns=["User","Name","Age","Gender"])
    try:
        old = pd.read_csv("profile.csv")
        df = pd.concat([old, df])
    except:
        pass
    df.to_csv("profile.csv", index=False)
    print("Profile saved!")