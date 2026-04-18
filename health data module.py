class Person:
    def __init__(self, username):
        self.username = username

class Patient(Person):
    def add_health(self):
        try:
            weight = float(input("Weight: "))
            height = float(input("Height: "))
            sugar = int(input("Sugar: "))
            bmi = round(weight/(height*height),2)
            df = pd.DataFrame([[self.username, weight, bmi, sugar]],
                              columns=["User","Weight","BMI","Sugar"])
            try:
                old = pd.read_csv("health.csv")
                df = pd.concat([old, df])
            except:
                pass
            df.to_csv("health.csv", index=False)
            print("Health data saved!")
        except:
            print("Invalid input!")