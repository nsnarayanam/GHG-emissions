import matplotlib.pyplot as plt

def generate_report(data):
    plt.bar(data.keys(), data.values())
    plt.title("Weekly Emissions Summary")
    plt.xlabel("Gas")
    plt.ylabel("Emissions (tons)")
    plt.savefig("weekly_summary.png")
    print("Report generated.")

sample_data = {"CH4": 120, "CO2": 340, "NO2": 150}
generate_report(sample_data)
