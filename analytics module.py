import numpy as np
import matplotlib.pyplot as plt

def analyze(u):
    try:
        df = pd.read_csv("health.csv")
        data = df[df["User"] == u]
        if data.empty:
            print("No data!")
            return
        avg_bmi = np.mean(data["BMI"])
        avg_sugar = np.mean(data["Sugar"])
        print("Average BMI:", round(avg_bmi,2))
        print("Average Sugar:", round(avg_sugar,2))
        if avg_bmi > 25:
            print("⚠ Overweight")
        if avg_sugar > 180:
            print("⚠ High Sugar")
        data[["Weight","BMI"]].plot()
        plt.title("Health Trends")
        plt.show()
    except:
        print("Error!")