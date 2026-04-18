def add_medical(u):
    illness = input("Illness: ")
    allergy = input("Allergy: ")
    surgery = input("Surgery: ")
    prescription = input("Prescription: ")
    df = pd.DataFrame([[u, illness, allergy, surgery, prescription]],
                      columns=["User","Illness","Allergy","Surgery","Prescription"])
    try:
        old = pd.read_csv("medical.csv")
        df = pd.concat([old, df])
    except:
        pass
    df.to_csv("medical.csv", index=False)
    print("Medical history saved!")