def add_medication(u):
    med = input("Medicine Name: ")
    dose = input("Dosage: ")
    df = pd.DataFrame([[u, med, dose]],
                      columns=["User","Medicine","Dosage"])
    try:
        old = pd.read_csv("medicine.csv")
        df = pd.concat([old, df])
    except:
        pass
    df.to_csv("medicine.csv", index=False)
    print("Medication added!")