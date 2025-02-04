import pandas as pd
import matplotlib.pyplot as plt

csv_file = "final_results.csv"

df = pd.read_csv(csv_file)

# Print column names to verify they match
print("Columns:", df.columns)

# Convert to numeric, force errors to NaN
df["generation"] = pd.to_numeric(df["generation"], errors="coerce")
df["average_score"] = pd.to_numeric(df["average_score"], errors="coerce")
df["lowest_score"] = pd.to_numeric(df["lowest_score"], errors="coerce")
df["highest_score"] = pd.to_numeric(df["highest_score"], errors="coerce")

# Drop missing values
df.dropna(subset=["generation", "highest_score", "average_score","lowest_score","total_wins","total_losses","total_draws","highest_defection_rate","average_defection_rate","lowest_defection_rate"], inplace=True)

# Convert to NumPy arrays
x = df["generation"].to_numpy()
y = df["average_score"].to_numpy()
y_low = df["lowest_score"].to_numpy()
y_high = df["highest_score"].to_numpy()

# Plot Average Score with range
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Average Score", color="blue")
plt.fill_between(x, y_low, y_high, color="blue", alpha=0.2, label="Score Range")
plt.xlabel("Generation")
plt.ylabel("Score")
plt.title("Change in Average Score Over Generations (with Range)")
plt.legend()
plt.grid()
plt.show()


# Convert to NumPy arrays
x = df["generation"].to_numpy()
y = df["average_defection_rate"].to_numpy()
y_low = df["lowest_defection_rate"].to_numpy()
y_high = df["highest_defection_rate"].to_numpy()

# Plot Average Defection with range
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Average Defection Rate", color="blue")
plt.fill_between(x, y_low, y_high, color="blue", alpha=0.2, label="Defection Rate Range")
plt.xlabel("Generation")
plt.ylabel("Defection Rate")
plt.title("Change in Average Defection Rate Over Generations (with Range)")
plt.legend()
plt.grid()
plt.show()

# Convert to NumPy arrays
x = df["generation"].to_numpy()
total_games = (df["total_wins"] + df["total_losses"] + df["total_draws"]).to_numpy()
decisive_percentage = ((df["total_wins"] + df["total_losses"]) / total_games * 100).to_numpy()
non_decisive_percentage = ((df["total_draws"] / total_games) * 100).to_numpy()

# Plot percentages of decisive and non-decisive games
plt.figure(figsize=(10, 5))
plt.plot(x, decisive_percentage, label="Decisive Games (%)", color="blue")
plt.plot(x, non_decisive_percentage, label="Non-Decisive Games (%)", color="grey")
plt.xlabel("Generation")
plt.ylabel("Percentage of Games")
plt.title("Decisive vs Non-Decisive Game Percentages Over Generations")
plt.legend()
plt.grid()
plt.show()

