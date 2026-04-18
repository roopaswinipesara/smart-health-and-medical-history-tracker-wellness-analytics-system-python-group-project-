def add_appointment(u):
    doctor = input("Doctor: ")
    date = input("Date: ")
    df = pd.DataFrame([[u, doctor, date]],
                      columns=["User","Doctor","Date"])
    try:
        old = pd.read_csv("appointment.csv")
        df = pd.concat([old, df])
    except:
        pass
    df.to_csv("appointment.csv", index=False)
    print("Appointment saved!")