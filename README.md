# Assignment 8 - Seaborn Visual Analytics

## Project Purpose
This project applies Seaborn visualization techniques from Lecture 13 to two datasets:
1. `Exercise_Data.csv` to study how diet and exercise affect pulse.
2. Seaborn's built-in `planets` dataset to compare relational, distributional, and categorical patterns.

The script uses a lecture-style, top-to-bottom workflow (load data, create plots, print conclusions).

## Implementation Design
The implementation is procedural (not class-based) to match the Lecture 13 notes style.

### Script Sections
1. Global aesthetic settings
2. Data loading
3. Exercise data visualizations
4. Exercise conclusions
5. Planets data visualizations
6. Planets conclusions

### Core Variables
- `exercise`: DataFrame from `Exercise_Data.csv`
- `planets`: DataFrame from `sns.load_dataset("planets")`
- `top_methods`: Five most frequent discovery methods (used to keep legends readable)
- `OUTPUT_DIR`: Folder path for saved chart images

### Helper Function
- `save_figure(fig, filename)`
  - Saves each chart as a high-resolution PNG in the `charts` folder.

## Charts Produced

### Exercise Data
1. Heatmap of pulse values (`1 min`, `15 min`, `30 min`)
2. Categorical box plot of pulse by diet
3. Categorical violin plot of pulse by exercise type

### Planets Data
Relational (2):
1. Planet mass vs distance
2. Orbital period vs distance

Distributional (2):
1. Histogram of mass by method
2. KDE of orbital period by method

Categorical (2):
1. Count by discovery method and system type
2. Box plot of mass by discovery method and system type

## Output Files
When the script runs, it saves charts to:
- `charts/01_exercise_heatmap.png`
- `charts/02_exercise_diet_catplot.png`
- `charts/03_exercise_kind_catplot.png`
- `charts/04_planets_relational_mass_distance.png`
- `charts/05_planets_relational_orbital_distance.png`
- `charts/06_planets_distribution_mass_hist.png`
- `charts/07_planets_distribution_orbital_kde.png`
- `charts/08_planets_categorical_method_counts.png`
- `charts/09_planets_categorical_mass_box.png`

## Brief Conclusions

### Exercise Data (student-friendly)
- Pulse generally increases after activity.
- Running tends to produce the highest pulse values, while rest tends to be lowest.
- In this sample, exercise type appears to affect pulse more strongly than diet.

### Planets Data
- Planets farther from their stars tend to have longer orbital periods.
- Discovery methods are unevenly represented across records.
- The orbital period vs distance relational plot best highlights a notable trend.

## Limitations
- Exercise dataset size is small, so findings are descriptive.
- Missing values in `planets` require filtering.
- Some category labels can still be crowded due to many discovery methods.
- No formal statistical hypothesis tests are included.

## How to Run
From the assignment folder, run:

```bash
python "Assignment 8 Seaborn.py"
```

The script displays each chart and also saves PNG files in the `charts` folder.

## Results 
Exercise Dataset Conclusions:
- Pulse usually goes up from 1 minute to 30 minutes after activity.
- Running gave the highest average pulse at 30 minutes (126.0 BPM), while Rest was lowest (91.4 BPM).
- Diet groups were closer together (98.8 to 110.1 BPM), so exercise type seems to affect pulse more in this class data.
- Average pulse change from 1 min to 30 min was 11.3 BPM.

Planets Dataset Conclusions:
- The most notable graph is the relational plot of orbital period vs distance, which shows that planets farther from stars usually take longer to orbit.
- This is supported by a positive distance-orbital period correlation (r = -0.03).
- Discovery methods are not evenly represented; top methods are Radial Velocity (553), Transit (397), Imaging (38). 

