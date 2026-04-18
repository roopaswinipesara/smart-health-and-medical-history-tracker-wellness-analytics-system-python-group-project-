current_user = None
role = None

while True:
    print("\n--- HEALTH SYSTEM ---")
    print("1.Register")
    print("2.Login")
    print("3.Profile")
    print("4.Medical History")
    print("5.Medication")
    print("6.Appointment")
    print("7.Health Data")
    print("8.Analysis")
    print("9.Exit")

    ch = input("Choice: ")

    if ch == "1":
        register()

    elif ch == "2":
        current_user, role = login()

    elif ch == "3" and current_user:
        add_profile(current_user)

    elif ch == "4" and current_user:
        add_medical(current_user)

    elif ch == "5" and current_user:
        add_medication(current_user)

    elif ch == "6" and current_user:
        add_appointment(current_user)

    elif ch == "7" and current_user:
        p = Patient(current_user)
        p.add_health()

    elif ch == "8" and current_user:
        analyze(current_user)

    elif ch == "9":
        break

    else:
        print("Login first!")