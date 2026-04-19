# Sensor Plots — synthetic sensor visualization

This repository contains a small script that generates synthetic temperature sensor data and produces publication-quality visualizations (scatter, histogram, box plot).

## Installation

1. Activate the course environment:

   conda activate ece105

2. Install required packages (using conda or mamba):

   conda install numpy matplotlib

   or

   mamba install numpy matplotlib

(Alternatively, in a plain Python environment: pip install numpy matplotlib.)

## Usage

Run the script from the repository root with the ece105 environment active:

    python generate_plots.py

This will generate and save a combined figure as `sensor_analysis.png` in the current directory.

## Example output

The script creates a single 1×3 figure (saved as sensor_analysis.png) containing:

- Scatter plot: temperature (°C) vs. time (s) with Sensor A in blue and Sensor B in orange, including axis labels, title, and legend.
- Histogram: overlaid histograms for both sensors (30 bins) with dashed vertical lines marking each sensor mean.
- Box plot: side-by-side box plots for Sensor A and Sensor B with mean markers and a horizontal dashed line at the overall mean.

## AI tools used and disclosure

Placeholder: describe any AI assistance, prompts, or tools used to create or modify the code and documentation. Replace this paragraph with a tailored disclosure.
