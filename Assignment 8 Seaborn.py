import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

# ------------------------------------------------------------
# GLOBAL AESTHETIC SETTINGS
# This sets a consistent visual style for every chart in the script.
# whitegrid adds light reference lines, talk makes text larger, and Set2
# gives the plots softer colors that are easier to read.
# ------------------------------------------------------------
sns.set_theme(style="whitegrid", context="talk", palette="Set2")

# Store all saved charts inside a separate folder in the assignment directory.
# This keeps the images organized and makes them easy to submit or review later.
OUTPUT_DIR = Path(__file__).resolve().parent / "charts"
OUTPUT_DIR.mkdir(exist_ok=True)


def save_figure(fig, filename):
    # Save each figure at high resolution so it looks clear in the folder.
    fig.savefig(OUTPUT_DIR / filename, dpi=300, bbox_inches="tight")

# ------------------------------------------------------------
# LOAD DATA
# The exercise data comes from the CSV file given by the assignment.
# The planets data is one of Seaborn's built-in datasets.
# ------------------------------------------------------------
exercise = pd.read_csv("Exercise_Data.csv")
planets = sns.load_dataset("planets")

# Use only the most common discovery methods so the legends stay readable.
top_methods = planets["method"].value_counts().head(5).index.tolist()

# ------------------------------------------------------------
# PART 1 — EXERCISE DATA VISUALS
# ------------------------------------------------------------

# Heatmap of pulse measurements
# A heatmap is useful here because it shows how pulse changes across the
# three time points for every student in a compact table-like view.
pulse_data = exercise[["1 min", "15 min", "30 min"]]

plt.figure(figsize=(9, 6))
sns.heatmap(
    pulse_data,
    cmap="YlOrRd",
    linewidths=0.5,
    linecolor="white",
    cbar_kws={"label": "Pulse Rate (BPM)"},
)
# The title and axis labels explain what the rows and columns mean.
plt.title("Heatmap of Student Pulse Measurements")
plt.xlabel("Time After Start of Activity")
plt.ylabel("Student Record")
plt.tight_layout()
# Save before showing so the file is written even if the display window closes.
save_figure(plt.gcf(), "01_exercise_heatmap.png")
plt.show()

# Categorical plot: pulse by diet
# A box plot is a good categorical plot because it shows the median,
# spread, and possible outliers for each diet group.
diet_plot = sns.catplot(
    data=exercise,
    x="diet",
    y="30 min",
    hue="diet",
    kind="box",
    height=6,
    aspect=1.25,
    palette="Set3",
)
# These labels make the comparison between diet groups easy to understand.
diet_plot.set_axis_labels("Diet Type", "Pulse at 30 Minutes (BPM)")
diet_plot.figure.suptitle("Pulse at 30 Minutes by Diet Type", y=1.03)
diet_plot.figure.tight_layout()
save_figure(diet_plot.figure, "02_exercise_diet_catplot.png")
plt.show()

# Categorical plot: pulse by exercise type
# A violin plot shows the distribution shape, so it is helpful for seeing
# how pulse values are spread across the three exercise categories.
exercise_plot = sns.catplot(
    data=exercise,
    x="kind",
    y="30 min",
    hue="kind",
    kind="violin",
    inner="quartile",
    height=6,
    aspect=1.25,
    palette="Pastel1",
)
exercise_plot.set_axis_labels("Exercise Type", "Pulse at 30 Minutes (BPM)")
exercise_plot.figure.suptitle("Pulse at 30 Minutes by Exercise Type", y=1.03)
exercise_plot.figure.tight_layout()
save_figure(exercise_plot.figure, "03_exercise_kind_catplot.png")
plt.show()

# ------------------------------------------------------------
# PART 1 — BRIEF CONCLUSIONS FOR ELEMENTARY STUDENTS
# These summary statistics turn the visual patterns into simple conclusions.
# ------------------------------------------------------------
means_by_kind = exercise.groupby("kind")["30 min"].mean().sort_values()
means_by_diet = exercise.groupby("diet")["30 min"].mean().sort_values()
avg_change = (exercise["30 min"] - exercise["1 min"]).mean()

print("\nExercise Dataset Conclusions:")
# The goal is to explain the chart in simple language.
print("- Pulse usually goes up from 1 minute to 30 minutes after activity.")
print(
    f"- {means_by_kind.index[-1].title()} gave the highest average pulse at 30 minutes "
    f"({means_by_kind.iloc[-1]:.1f} BPM), while {means_by_kind.index[0].title()} was lowest "
    f"({means_by_kind.iloc[0]:.1f} BPM)."
)
print(
    f"- Diet groups were closer together ({means_by_diet.iloc[0]:.1f} to {means_by_diet.iloc[-1]:.1f} BPM), "
    "so exercise type seems to affect pulse more in this class data."
)
print(f"- Average pulse change from 1 min to 30 min was {avg_change:.1f} BPM.")

# ------------------------------------------------------------
# PART 2 — PLANETS DATA VISUALS
# ------------------------------------------------------------

# Clean subsets for plotting
# Missing values are removed because Seaborn cannot plot them reliably in
# all graph types, especially when comparing two numeric axes.
rel_mass = planets.dropna(subset=["distance", "mass", "method"])
rel_mass = rel_mass[rel_mass["method"].isin(top_methods)]

rel_orbit = planets.dropna(subset=["distance", "orbital_period", "method"])
rel_orbit = rel_orbit[rel_orbit["method"].isin(top_methods)]

dist_data = planets.dropna(subset=["mass", "orbital_period", "method"])
dist_data = dist_data[dist_data["method"].isin(top_methods)]

# The system_type column gives an extra categorical grouping for the
# categorical plots, which helps show whether a planet was found alone or
# in a multi-planet system.
cat_data = planets[planets["method"].isin(top_methods)].copy()
cat_data["system_type"] = cat_data["number"].apply(
    lambda value: "Multi-planet" if value > 1 else "Single-planet"
)

# ---------------- RELATIONAL PLOTS (2) ----------------
# Relational plots show the connection between two numeric variables.
rel_1 = sns.relplot(
    data=rel_mass,
    x="distance",
    y="mass",
    hue="method",
    style="method",
    kind="scatter",
    height=6,
    aspect=1.3,
    alpha=0.75,
    palette="tab10",
)
# Hue and style both use method so the categories are easy to distinguish.
rel_1.set_axis_labels("Distance from Star (AU)", "Planet Mass (Jupiter Masses)")
rel_1.figure.suptitle("Relational Plot 1: Planet Mass vs Distance", y=1.03)
rel_1.figure.tight_layout()
save_figure(rel_1.figure, "04_planets_relational_mass_distance.png")
plt.show()

# This second relational plot focuses on orbital period instead of mass.
rel_2 = sns.relplot(
    data=rel_orbit,
    x="distance",
    y="orbital_period",
    hue="method",
    kind="scatter",
    height=6,
    aspect=1.3,
    alpha=0.7,
    palette="Dark2",
)
rel_2.set_axis_labels("Distance from Star (AU)", "Orbital Period (Days)")
rel_2.figure.suptitle("Relational Plot 2: Orbital Period vs Distance", y=1.03)
rel_2.figure.tight_layout()
save_figure(rel_2.figure, "05_planets_relational_orbital_distance.png")
plt.show()

# ---------------- DISTRIBUTIONAL PLOTS (2) ----------------
# Distribution plots show how values are spread across the dataset.
dist_1 = sns.displot(
    data=dist_data,
    x="mass",
    hue="method",
    kind="hist",
    bins=30,
    element="step",
    stat="density",
    common_norm=False,
    height=6,
    aspect=1.3,
    palette="tab10",
)
# A histogram shows the frequency of planet masses in bins.
dist_1.set_axis_labels("Planet Mass (Jupiter Masses)", "Density")
dist_1.figure.suptitle("Distributional Plot 1: Mass Distribution by Method", y=1.03)
dist_1.figure.tight_layout()
save_figure(dist_1.figure, "06_planets_distribution_mass_hist.png")
plt.show()

# A KDE plot smooths the distribution so overall shape is easier to see.
dist_2 = sns.displot(
    data=dist_data,
    x="orbital_period",
    hue="method",
    kind="kde",
    fill=True,
    common_norm=False,
    height=6,
    aspect=1.3,
    palette="Set1",
)
dist_2.set_axis_labels("Orbital Period (Days)", "Density")
dist_2.figure.suptitle("Distributional Plot 2: KDE of Orbital Period", y=1.03)
dist_2.figure.tight_layout()
save_figure(dist_2.figure, "07_planets_distribution_orbital_kde.png")
plt.show()

# ---------------- CATEGORICAL PLOTS (2) ----------------
# Categorical plots compare values across named groups.
cat_1 = sns.catplot(
    data=cat_data,
    x="method",
    hue="system_type",
    kind="count",
    height=6,
    aspect=1.6,
    palette="Set2",
)
cat_1.set_axis_labels("Discovery Method", "Number of Planets")
cat_1.figure.suptitle("Categorical Plot 1: Counts by Method and System Type", y=1.03)
# Rotating labels makes the method names easier to read.
cat_1.ax.tick_params(axis="x", labelrotation=25)
cat_1.figure.tight_layout()
save_figure(cat_1.figure, "08_planets_categorical_method_counts.png")
plt.show()

# A box plot is useful here because it shows the distribution of mass
# for each discovery method and system type.
mass_data = cat_data.dropna(subset=["mass"])
cat_2 = sns.catplot(
    data=mass_data,
    x="method",
    y="mass",
    hue="system_type",
    kind="box",
    height=6,
    aspect=1.6,
    palette="Paired",
)
cat_2.set_axis_labels("Discovery Method", "Planet Mass (Jupiter Masses)")
cat_2.figure.suptitle("Categorical Plot 2: Planet Mass by Method and System Type", y=1.03)
cat_2.ax.tick_params(axis="x", labelrotation=25)
cat_2.figure.tight_layout()
save_figure(cat_2.figure, "09_planets_categorical_mass_box.png")
plt.show()

# ------------------------------------------------------------
# PART 2 — BRIEF INTERPRETATION OF NOTABLE RESULTS
# These calculations summarize the visual pattern that stands out most clearly.
# ------------------------------------------------------------
clean = planets.dropna(subset=["distance", "orbital_period", "method"])
corr = clean["distance"].corr(clean["orbital_period"])
method_counts = planets["method"].value_counts().head(3)

print("\nPlanets Dataset Conclusions:")
# The relational plot of distance vs orbital period is the clearest
# because it shows the strongest visible trend in the dataset.
print(
    "- The most notable graph is the relational plot of orbital period vs distance, "
    "which shows that planets farther from stars usually take longer to orbit."
)
print(f"- This is supported by a positive distance-orbital period correlation (r = {corr:.2f}).")
print(
    "- Discovery methods are not evenly represented; top methods are "
    + ", ".join([f"{name} ({count})" for name, count in method_counts.items()])
    + "."
)
